/**
 * UNIVERSITY YATRA - GOOGLE APPS SCRIPT WEBHOOK
 * 
 * Deployment Instructions:
 * 1. Open your target Google Sheet.
 * 2. Click Extensions > Apps Script.
 * 3. Replace any code with this entire file.
 * 4. Click Deploy > New deployment.
 * 5. Select type: "Web app".
 * 6. Set "Execute as": "Me".
 * 7. Set "Who has access": "Anyone".
 * 8. Click Deploy, authorize permissions, and copy the Web App URL.
 * 9. Paste the Web App URL into SHEET_URL in js/main.js and POPSHEET_URL in index.html.
 */

const SHEETS = {
  calculator: {
    name: 'Calculator Leads',
    headers: ['Time', 'Name', 'Mobile', 'Qualification', 'Country', 'Pathway',
              'Course', 'Budget', 'Tuition', 'Living', 'Total', 'Page'],
    row: function(d) {
      return [d.name, d.mobile, d.qualification, d.country, d.pathway,
              d.course, d.budget, d.tuition, d.living, d.total, d.page];
    }
  },
  enquiry: {
    name: 'Enquiry Leads',
    headers: ['Time', 'Name', 'Mobile', 'Email', 'Qualification', 'Destination',
              'Course', 'Page'],
    row: function(d) {
      return [d.name, d.mobile, d.email, d.qualification, d.destination,
              d.course, d.page];
    }
  },
  popup: {
    name: 'Popup Leads',
    headers: ['Time', 'Name', 'Mobile', 'Email', 'Country', 'Page'],
    row: function(d) {
      return [d.name, d.mobile, d.email, d.country, d.page];
    }
  }
};

function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(10000);

    let data = {};
    if (e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (err) {
        // Parse urlencoded if not JSON
        data = e.parameter || {};
      }
    } else {
      data = e.parameter || {};
    }

    const type = data.type || (data.country && !data.qualification ? 'popup' : (data.tuition ? 'calculator' : 'enquiry'));
    const cfg = SHEETS[type] || SHEETS.enquiry;

    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(cfg.name);
    if (!sheet) {
      sheet = ss.insertSheet(cfg.name);
      sheet.appendRow(cfg.headers);
      sheet.setFrozenRows(1);
    }

    const time = Utilities.formatDate(new Date(), 'Asia/Kolkata', 'dd MMM yyyy, hh:mm a');
    sheet.appendRow([time].concat(cfg.row(data).map(function(v) { return v == null ? '' : String(v); })));

    return ContentService.createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

