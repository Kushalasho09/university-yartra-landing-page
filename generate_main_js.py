import re

js_code = """/**
 * University Yatra — Study Abroad Landing Page
 * Client Design Engine & Calculator Controller
 */

(function () {
  'use strict';

  // CONFIGURATION & CONSTANTS
  const WA_NUMBER = '919217368750';
  const SHEET_URL = 'https://script.google.com/macros/s/AKfycbx_YOUR_APP_SCRIPT_ID/exec'; // Replace with deployed Apps Script Web App URL

  // Real PDF paths available in repository
  const GUIDES = {
    'germany': 'assets/pdfs/direct/germany.pdf',
    'germany-ft': 'assets/pdfs/fast-track/germany.pdf',
    'canada': 'assets/pdfs/direct/canada.pdf',
    'canada-ft': 'assets/pdfs/fast-track/canada.pdf'
  };

  const COUNTRIES = [
    { k: 'germany', n: 'Germany', ft: ['12th', 'bachelor', 'master'], currency: 'EUR', symbol: '€' },
    { k: 'canada', n: 'Canada', ft: ['12th', 'bachelor', 'master'], currency: 'CAD', symbol: 'CAD' },
    { k: 'uk', n: 'United Kingdom', ft: ['master'], currency: 'GBP', symbol: '£' },
    { k: 'australia', n: 'Australia', ft: [], currency: 'AUD', symbol: 'AUD' },
    { k: 'usa', n: 'United States', ft: ['bachelor', 'master'], currency: 'USD', symbol: '$' },
    { k: 'other', n: 'Other / Not Sure', ft: [], currency: 'USD', symbol: '$' }
  ];

  const C = {};
  COUNTRIES.forEach(c => { C[c.k] = c; });

  const LEVELS = {
    '12th': "After 12th (Bachelor's)",
    'bachelor': "After Graduation (Master's)",
    'master': "Postgraduate / Master's",
    'mba': "MBA / Business School"
  };

  const PATH_LABELS = {
    'direct': 'Direct Study Abroad',
    'ft': 'Fast Track Study Abroad',
    'both': 'Direct + Fast Track'
  };

  const TIMELINES = [
    { k: 'Next 6 months', s: 'Ready to move fast' },
    { k: '6-12 months', s: 'Planning ahead' },
    { k: '12+ months', s: 'Starting early' },
    { k: 'Just exploring', s: 'Learning the options' }
  ];

  // CALCULATOR STATE
  const S = {
    country: null,
    level: null,
    path: null,
    time: null
  };
  const KEYS = ['country', 'level', 'path', 'time'];
  let step = 0;
  let lead = null;

  const $ = id => document.getElementById(id);
  const wa = m => 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(m);

  function guideFor(k, path) {
    if (path === 'ft' && GUIDES[k + '-ft']) return GUIDES[k + '-ft'];
    return GUIDES[k] || '';
  }

  function ftOK(k, l) {
    if (!C[k] || !C[k].ft) return false;
    return C[k].ft.includes(l);
  }

  function crumbText(i) {
    if (i === 0) return C[S.country] ? C[S.country].n : '';
    if (i === 1) return LEVELS[S.level] || '';
    if (i === 2) return PATH_LABELS[S.path] || '';
    if (i === 3) return S.time || '';
    return '';
  }

  function drawCrumbs() {
    const box = $('crumbs');
    if (!box) return;
    box.innerHTML = '';
    for (let i = 0; i < Math.min(step, 4); i++) {
      if (!S[KEYS[i]]) continue;
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'crumb';
      btn.textContent = crumbText(i) + ' ✎';
      btn.onclick = () => goToStep(i);
      box.appendChild(btn);
    }
  }

  function drawProgress() {
    const dots = $('dots');
    const stepNo = $('stepNo');
    const backBtn = $('backBtn');
    if (!dots || !stepNo || !backBtn) return;

    const n = Math.min(step, 3);
    Array.from(dots.children).forEach((d, i) => {
      d.classList.toggle('on', i <= n || step >= 4);
    });
    stepNo.textContent = (step >= 4 ? 4 : step + 1) + '/4';
    backBtn.hidden = (step === 0);
  }

  function updateCover() {
    const cvTitle = $('cvTitle');
    if (!cvTitle) return;
    if (S.country && S.country !== 'other' && C[S.country]) {
      cvTitle.innerHTML = 'Study in<br><em>' + C[S.country].n + '.</em>';
    } else {
      cvTitle.innerHTML = 'Your Country <em>Guide.</em>';
    }
  }

  function createOpt(title, sub, val, isSelected) {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'o' + (isSelected ? ' sel' : '');
    b.dataset.v = val;
    b.innerHTML = '<b>' + title + '</b>' + (sub ? '<span>' + sub + '</span>' : '');
    return b;
  }

  function renderStep() {
    const gateView = $('gateView');
    const stepView = $('stepView');
    if (!gateView || !stepView) return;

    gateView.hidden = true;
    stepView.hidden = false;

    drawCrumbs();
    drawProgress();
    updateCover();

    stepView.innerHTML = '';
    const wrap = document.createElement('div');
    wrap.className = 'anim';

    const q = document.createElement('div');
    q.className = 'q';

    const sub = document.createElement('p');
    sub.className = 'qsub';

    const grid = document.createElement('div');
    grid.className = 'opts';

    let note = null;

    if (step === 0) {
      q.innerHTML = 'Where do you want <span class="hl">to study?</span>';
      sub.textContent = 'Select your preferred country to begin your evaluation.';
      COUNTRIES.forEach(c => {
        grid.appendChild(createOpt(c.n, '', c.k, S.country === c.k));
      });
    } else if (step === 1) {
      q.innerHTML = 'What is your <span class="hl">current qualification?</span>';
      sub.textContent = 'Choose the level of degree you are pursuing abroad.';
      grid.classList.add('c3');
      [
        ['12th', "Class 12th", 'Looking for Bachelor degrees'],
        ['bachelor', "Graduation", 'Looking for Master degrees'],
        ['master', "Postgraduate", 'Master / Specialisation'],
        ['mba', "MBA", 'Business School']
      ].forEach(l => {
        grid.appendChild(createOpt(l[1], l[2], l[0], S.level === l[0]));
      });
    } else if (step === 2) {
      q.innerHTML = 'Which route <span class="hl">interests you?</span>';
      sub.textContent = 'Compare Direct study abroad vs Fast Track credit transfer.';
      grid.classList.add('c1');

      const isEligible = ftOK(S.country, S.level);
      if (!isEligible && S.path && S.path !== 'direct') S.path = null;

      grid.appendChild(createOpt('Direct Study Abroad', 'Apply directly and study on campus abroad from day one', 'direct', S.path === 'direct'));

      if (isEligible) {
        grid.appendChild(createOpt('Fast Track Study Abroad', 'Start online in India (8-12 mo), then finish on campus abroad', 'ft', S.path === 'ft'));
        grid.appendChild(createOpt('Compare Both Routes', 'See fee, eligibility and duration comparison side-by-side', 'both', S.path === 'both'));
      } else {
        note = document.createElement('p');
        note.className = 'note';
        const cName = C[S.country] ? C[S.country].n : 'this country';
        note.innerHTML = '<strong>Note:</strong> Fast Track credit transfer is currently available for select programmes in Germany, Canada, and the UK. Your counsellor will suggest eligible direct options.';
      }
    } else {
      q.innerHTML = 'When do you plan <span class="hl">to start?</span>';
      sub.textContent = 'This helps us match upcoming intake deadlines and visa slots.';
      TIMELINES.forEach(t => {
        grid.appendChild(createOpt(t.k, t.s, t.k, S.time === t.k));
      });
    }

    wrap.appendChild(q);
    wrap.appendChild(sub);
    wrap.appendChild(grid);
    if (note) wrap.appendChild(note);
    stepView.appendChild(wrap);

    grid.addEventListener('click', e => {
      const btn = e.target.closest('.o');
      if (!btn) return;
      grid.querySelectorAll('.o').forEach(x => x.classList.remove('sel'));
      btn.classList.add('sel');
      S[KEYS[step]] = btn.dataset.v;

      setTimeout(() => {
        step++;
        if (step >= 4) {
          showGate();
        } else {
          renderStep();
        }
      }, 200);
    });
  }

  function goToStep(i) {
    step = i;
    for (let j = i; j < 4; j++) {
      S[KEYS[j]] = null;
    }
    renderStep();
  }

  function showGate() {
    const c = C[S.country] || { n: 'Study Abroad' };
    const stepView = $('stepView');
    const gateView = $('gateView');
    const gateTitle = $('gateTitle');
    const gateSub = $('gateSub');
    const gateBtn = $('gateBtn');
    const backBtn = $('backBtn');

    if (!stepView || !gateView) return;

    stepView.hidden = true;
    gateView.hidden = false;

    drawCrumbs();
    drawProgress();
    updateCover();
    if (backBtn) backBtn.hidden = false;

    if (gateTitle) {
      gateTitle.innerHTML = 'Your ' + (S.country === 'other' ? '' : '<span class="hl">' + c.n + '</span> ') + 'Guide & Estimate is Ready.';
    }
    if (gateSub) {
      gateSub.textContent = 'Enter your name and WhatsApp number to download it free.';
    }

    if ($('h_country')) $('h_country').value = c.n;
    if ($('h_level')) $('h_level').value = LEVELS[S.level] || S.level;
    if ($('h_path')) $('h_path').value = PATH_LABELS[S.path] || S.path;
    if ($('h_time')) $('h_time').value = S.time;

    if (gateBtn) {
      gateBtn.disabled = false;
      gateBtn.textContent = 'Download Free PDF Guide ↓';
    }

    if (lead) {
      finish(false);
    } else {
      const gf = $('gateForm');
      const dv = $('doneView');
      if (gf) gf.style.display = '';
      if (dv) dv.style.display = 'none';
    }

    const calcEl = $('calc');
    if (calcEl) {
      const rect = calcEl.getBoundingClientRect();
      if (rect.top < 0 || rect.top > 140) {
        calcEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  }

  // BACK BUTTON
  const backBtn = $('backBtn');
  if (backBtn) {
    backBtn.onclick = () => {
      if (step >= 4) {
        step = 3;
        renderStep();
      } else if (step > 0) {
        step--;
        renderStep();
      }
    };
  }

  // DYNAMIC PDF GENERATOR (Fallback for countries without pre-made PDFs)
  async function generateCustomGuidePdf(countryName, levelName, pathName, timeline, studentName) {
    if (typeof PDFLib === 'undefined') {
      console.warn('PDFLib not loaded, skipping custom PDF generation.');
      return null;
    }
    try {
      const { PDFDocument, rgb, StandardFonts } = PDFLib;
      const pdfDoc = await PDFDocument.create();
      const page = pdfDoc.addPage([595.28, 841.89]); // A4
      const font = await pdfDoc.embedFont(StandardFonts.Helvetica);
      const fontBold = await pdfDoc.embedFont(StandardFonts.HelveticaBold);

      // Colors
      const blue = rgb(0.09, 0.40, 0.96); // #1765F5
      const ink = rgb(0.04, 0.07, 0.19);   // #0A1230
      const lime = rgb(0.78, 1.0, 0.24);   // #C8FF3E
      const gray = rgb(0.30, 0.35, 0.47);  // #4D5878
      const lightBg = rgb(0.96, 0.97, 1.0);// #F4F7FF

      // Top banner
      page.drawRectangle({
        x: 0,
        y: 750,
        width: 595.28,
        height: 92,
        color: blue
      });

      page.drawText('UNIVERSITY YATRA', {
        x: 40,
        y: 795,
        size: 20,
        font: fontBold,
        color: rgb(1, 1, 1)
      });
      page.drawText('Study Abroad Country & Cost Guide 2026', {
        x: 40,
        y: 775,
        size: 11,
        font: font,
        color: lime
      });

      // Greeting
      page.drawText(`Prepared for: ${studentName || 'Student'}`, {
        x: 40,
        y: 715,
        size: 14,
        font: fontBold,
        color: ink
      });
      page.drawText(`Target Destination: ${countryName}  |  Level: ${levelName}  |  Route: ${pathName}`, {
        x: 40,
        y: 695,
        size: 10,
        font: font,
        color: gray
      });

      // Section 1: Overview
      page.drawRectangle({
        x: 40,
        y: 575,
        width: 515,
        height: 100,
        color: lightBg,
        borderColor: ink,
        borderWidth: 1.5
      });

      page.drawText('01. Destination Overview & Academic Intake', {
        x: 55,
        y: 650,
        size: 12,
        font: fontBold,
        color: blue
      });
      page.drawText(`Selected Target: ${countryName} (${pathName})`, {
        x: 55,
        y: 630,
        size: 10,
        font: fontBold,
        color: ink
      });
      page.drawText(`Expected Intake: ${timeline}  |  Credit Eligibility: Direct & Fast Track pathways evaluated.`, {
        x: 55,
        y: 612,
        size: 9,
        font: font,
        color: gray
      });
      page.drawText('Our team coordinates end-to-end documentation, university shortlisting, and SOP drafting.', {
        x: 55,
        y: 595,
        size: 9,
        font: font,
        color: ink
      });

      // Section 2: Budget Breakdown
      page.drawRectangle({
        x: 40,
        y: 380,
        width: 515,
        height: 175,
        color: rgb(1, 1, 1),
        borderColor: ink,
        borderWidth: 1.5
      });

      page.drawText('02. Indicative Annual Expenses & Cost Breakdown', {
        x: 55,
        y: 530,
        size: 12,
        font: fontBold,
        color: blue
      });

      const items = [
        ['Tuition Fees (Indicative Range)', 'INR 9,00,000 - 18,00,000 / year (varies by course)'],
        ['Living Expenses & Accommodation', 'INR 6,00,000 - 10,00,000 / year (includes housing & food)'],
        ['Health Insurance & Visa Processing', 'INR 60,000 - 1,20,000 (one-time embassy & medical)'],
        ['Flight & Initial Relocation', 'INR 50,000 - 80,000 (pre-departure tickets)']
      ];

      items.forEach((item, idx) => {
        const y = 495 - idx * 26;
        page.drawText(`• ${item[0]}:`, { x: 55, y, size: 9, font: fontBold, color: ink });
        page.drawText(item[1], { x: 260, y, size: 9, font: font, color: gray });
      });

      // Section 3: Next Steps
      page.drawRectangle({
        x: 40,
        y: 200,
        width: 515,
        height: 160,
        color: lightBg,
        borderColor: ink,
        borderWidth: 1.5
      });

      page.drawText('03. 360° Admission & Student Visa Checklist', {
        x: 55,
        y: 335,
        size: 12,
        font: fontBold,
        color: blue
      });

      const steps = [
        '1. Academic Profile Review & University Shortlisting with Senior Counsellor',
        '2. English Proficiency Readiness (IELTS / TOEFL / PTE / Duolingo or Waiver)',
        '3. Statement of Purpose (SOP) & Letter of Recommendation (LOR) Drafting',
        '4. Education Loan Sanction Letter / Blocked Account Setup',
        '5. Embassy Visa Filing & Pre-Departure Briefing'
      ];

      steps.forEach((st, idx) => {
        page.drawText(st, { x: 55, y: 310 - idx * 22, size: 9, font: font, color: ink });
      });

      // Footer
      page.drawText('University Yatra | Future Yatra Pvt Ltd | Helpline: +91 92173 68750 | Email: info@universityyatra.com', {
        x: 40,
        y: 40,
        size: 8,
        font: font,
        color: gray
      });
      page.drawText('Admissions and visa approval depend on university criteria and government immigration regulations.', {
        x: 40,
        y: 28,
        size: 7,
        font: font,
        color: gray
      });

      const pdfBytes = await pdfDoc.save();
      return pdfBytes;
    } catch (err) {
      console.error('Error generating PDF:', err);
      return null;
    }
  }

  function downloadBlob(bytes, filename) {
    const blob = new Blob([bytes], { type: 'application/pdf' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(() => URL.revokeObjectURL(url), 4000);
  }

  async function finish(autoDownload) {
    const c = C[S.country] || { n: 'Study Abroad' };
    const preMadeFile = guideFor(S.country, S.path);
    const gf = $('gateForm');
    const dv = $('doneView');
    const dl = $('dl');
    const doneTitle = $('doneTitle');
    const doneSub = $('doneSub');
    const waNext = $('waNext');

    if (gf) gf.style.display = 'none';
    if (dv) dv.style.display = 'block';
    if (dl) dl.innerHTML = '';

    const studentName = lead ? lead.name : 'Student';
    const msgBase = `Hi University Yatra, I'm ${studentName}. I'm interested in ${LEVELS[S.level] || S.level} in ${c.n} (${PATH_LABELS[S.path] || S.path}, planning ${S.time}). `;

    if (preMadeFile) {
      if (doneTitle) doneTitle.textContent = 'Done! Check your downloads.';
      if (doneSub) doneSub.textContent = `Your ${c.n} guide should download automatically. If not, tap below.`;

      const btn = document.createElement('a');
      btn.href = preMadeFile;
      btn.setAttribute('download', `${c.n}_Guide_University_Yatra.pdf`);
      btn.className = 'btn btn-primary btn-block';
      btn.innerHTML = `<i class="fa-solid fa-file-pdf"></i> Download ${c.n} Guide (PDF) ↓`;
      dl.appendChild(btn);

      if (autoDownload) {
        setTimeout(() => btn.click(), 300);
      }
      if (waNext) {
        waNext.href = wa(msgBase + 'I downloaded the country guide and would like to speak with a counsellor.');
      }
    } else {
      // Dynamic PDF generation fallback
      if (doneTitle) doneTitle.textContent = 'Done! Generating your guide...';
      if (doneSub) doneSub.textContent = `Preparing custom ${c.n} cost estimate and roadmap for ${studentName}.`;

      const pdfBytes = await generateCustomGuidePdf(
        c.n,
        LEVELS[S.level] || S.level || 'Study Abroad',
        PATH_LABELS[S.path] || S.path || 'Direct',
        S.time || 'Upcoming Intake',
        studentName
      );

      if (pdfBytes) {
        if (doneTitle) doneTitle.textContent = 'Done! Check your downloads.';
        if (doneSub) doneSub.textContent = `Your ${c.n} guide has been prepared. If download didn't start, click below.`;

        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'btn btn-primary btn-block';
        btn.innerHTML = `<i class="fa-solid fa-file-pdf"></i> Download ${c.n} Guide (PDF) ↓`;
        btn.onclick = () => downloadBlob(pdfBytes, `${c.n}_Guide_University_Yatra.pdf`);
        dl.appendChild(btn);

        if (autoDownload) {
          downloadBlob(pdfBytes, `${c.n}_Guide_University_Yatra.pdf`);
        }
      } else {
        if (doneTitle) doneTitle.textContent = 'Thank you! Guide on its way.';
        if (doneSub) doneSub.textContent = `We will share your ${c.n} guide directly on WhatsApp shortly. A senior counsellor will also call you.`;
      }

      if (waNext) {
        waNext.href = wa(msgBase + 'Please share the country guide and call me.');
      }
    }

    if (autoDownload && dv) {
      setTimeout(() => dv.scrollIntoView({ behavior: 'smooth', block: 'center' }), 200);
    }
  }

  // LEAD FORM SUBMISSION
  const leadForm = $('leadForm');
  if (leadForm) {
    leadForm.addEventListener('submit', async e => {
      e.preventDefault();
      const name = ($('f_name') ? $('f_name').value : '').trim();
      const phone = ($('f_phone') ? $('f_phone').value : '').trim();
      const email = ($('f_email') ? $('f_email').value : '').trim();

      if (!name) {
        alert('Please enter your name.');
        return;
      }
      if (!/^[6-9][0-9]{9}$/.test(phone)) {
        alert('Please enter a valid 10-digit mobile number.');
        return;
      }
      if (!email || !email.includes('@')) {
        alert('Please enter a valid email address.');
        return;
      }

      const gateBtn = $('gateBtn');
      if (gateBtn) {
        gateBtn.disabled = true;
        gateBtn.textContent = 'Preparing your guide...';
      }

      lead = { name, phone, email };

      // Send lead to webhook
      try {
        const payload = new URLSearchParams({
          type: 'calculator_lead',
          name,
          phone,
          email,
          country: C[S.country] ? C[S.country].n : 'Not Selected',
          level: LEVELS[S.level] || S.level || '',
          pathway: PATH_LABELS[S.path] || S.path || '',
          timeline: S.time || '',
          timestamp: new Date().toISOString()
        });

        fetch(SHEET_URL, {
          method: 'POST',
          mode: 'no-cors',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: payload.toString()
        }).catch(err => console.warn('Sheet submission note:', err));
      } catch (err) {
        console.warn('Payload err:', err);
      }

      finish(true);
    });
  }

  // DESTINATION SECTION QUICK START
  window.startCountryGuide = function (countryKey) {
    if (!C[countryKey]) countryKey = 'other';
    S.country = countryKey;
    S.level = null;
    S.path = null;
    S.time = null;
    step = 1;
    renderStep();

    const calcEl = $('calculator');
    if (calcEl) {
      calcEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  // COUNTRY FILTER PILLS
  const cgrid = $('cgrid');
  if (cgrid) {
    COUNTRIES.forEach(c => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'ct';
      b.textContent = c.n;
      b.onclick = () => window.startCountryGuide(c.k);
      cgrid.appendChild(b);
    });
  }

  // FINAL ENQUIRY FORM SUBMISSION
  const enquiryForm = $('enquiryForm');
  if (enquiryForm) {
    enquiryForm.addEventListener('submit', async e => {
      e.preventDefault();
      const name = ($('eq_name') ? $('eq_name').value : '').trim();
      const mobile = ($('eq_mobile') ? $('eq_mobile').value : '').trim();
      const email = ($('eq_email') ? $('eq_email').value : '').trim();

      if (!name) {
        alert('Please enter your full name.');
        return;
      }
      if (!/^[6-9][0-9]{9}$/.test(mobile)) {
        alert('Please enter a valid 10-digit mobile number.');
        return;
      }
      if (!email || !email.includes('@')) {
        alert('Please enter a valid email address.');
        return;
      }

      const submitBtn = $('enquirySubmitBtn');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Sending details...';
      }

      try {
        const payload = new URLSearchParams({
          type: 'enquiry_lead',
          name,
          phone: mobile,
          email,
          timestamp: new Date().toISOString()
        });

        fetch(SHEET_URL, {
          method: 'POST',
          mode: 'no-cors',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: payload.toString()
        }).catch(err => console.warn('Sheet err:', err));
      } catch (err) {
        console.warn('Enquiry dispatch err:', err);
      }

      enquiryForm.style.display = 'none';
      const successEl = $('enquirySuccess');
      if (successEl) {
        successEl.style.display = 'block';
        successEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  }

  // AUTO-UPDATE CURRENT YEAR
  const yr = $('yearVal');
  if (yr) {
    yr.textContent = new Date().getFullYear();
  }

  // INITIALIZE CALCULATOR
  renderStep();

})();
"""

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Generated js/main.js successfully! Length:", len(js_code))
