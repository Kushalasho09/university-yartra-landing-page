import re

js_code = """/**
 * University Yatra — Study Abroad Landing Page
 * Official Calculator Engine & Interactive Controller
 */

(function () {
  'use strict';

  const WA_NUMBER = '919217368750';
  const SHEET_URL = 'https://script.google.com/macros/s/AKfycbx_YOUR_APP_SCRIPT_ID/exec';

  const $ = id => document.getElementById(id);
  const wa = m => 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(m);

  /* =====================================================
     LEGIT COST DATA & PDF GUIDE REPOSITORY MAPPING
     Tuition & Living figures in INR Lakhs (L) per year
     ===================================================== */
  const D = {
    'Germany': {
      flag: '🇩🇪',
      t: { "Bachelor's": [0.5, 3], "Master's": [0.5, 4], "MBA": [6, 15] },
      l: [9, 13], // Blocked Account: €11,208/yr ≈ ₹10.2L
      other: [1.5, 3], // APS, Visa, Health Insurance, Flight
      directGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    },
    'Canada': {
      flag: '🇨🇦',
      t: { "Bachelor's": [12, 22], "Master's": [12, 24], "MBA": [18, 35] },
      l: [11, 16], // GIC Living Requirement: CAD 20,635/yr ≈ ₹12.8L
      other: [2, 4], // Biometrics, Medical, Visa, Flight
      directGuide: 'assets/pdfs/Canada_Country_Guide_University_Yatra_v4.pdf',
      ftGuide: 'assets/pdfs/University-Yatra-Canada-Fast-Track-Guide.pdf'
    },
    'United Kingdom': {
      flag: '🇬🇧',
      t: { "Bachelor's": [14, 24], "Master's": [14, 26], "MBA": [18, 35] },
      l: [11, 16], // UKVI Living Funds: £1,023 - £1,334/mo × 12 ≈ ₹11L - ₹16L
      other: [2.5, 4.5], // IHS Surcharge, Student Visa, Flight
      directGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf'
    },
    'Australia': {
      flag: '🇦🇺',
      t: { "Bachelor's": [16, 28], "Master's": [16, 30], "MBA": [20, 40] },
      l: [14, 20], // Dept of Home Affairs Funds: AUD 24,505/yr ≈ ₹13.8L
      other: [2.5, 4.5], // OSHC, Visa Subclass 500, Biometrics
      directGuide: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf'
    },
    'USA': {
      flag: '🇺🇸',
      t: { "Bachelor's": [18, 35], "Master's": [20, 40], "MBA": [25, 50] },
      l: [12, 18], // $14,000 - $22,000 / year
      other: [3, 5], // SEVIS I-901, DS-160 Visa, Health Insurance, Flight
      directGuide: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf'
    },
    'France': {
      flag: '🇫🇷',
      t: { "Bachelor's": [1, 6], "Master's": [1.5, 8], "MBA": [8, 22] },
      l: [9, 14], // €615 - €850/mo × 12 ≈ ₹7L - ₹11L (Campus France requirement)
      other: [1.5, 3], // Campus France fee, VFS Visa, Travel
      directGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    },
    'Ireland': {
      flag: '🇮🇪',
      t: { "Bachelor's": [12, 20], "Master's": [12, 22], "MBA": [16, 30] },
      l: [10, 15], // INIS Proof of Funds: €10,000/yr
      other: [2, 4], // Visa, Medical, Flight
      directGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf'
    }
  };

  const mult = {
    lean: 0.9, // Budget lifestyle
    mid: 1.0,  // Moderate lifestyle
    plus: 1.2  // Comfy lifestyle
  };

  // Default state matching Image 2
  const S = {
    country: 'Canada',
    level: 'MBA',
    path: 'Fast Track',
    life: 'plus'
  };

  function fmtLakh(n) {
    return '₹' + (Math.round(n * 10) / 10).toString().replace(/\\.0$/, '') + 'L';
  }

  function rngLakh(a) {
    return fmtLakh(a[0]) + ' – ' + fmtLakh(a[1]);
  }

  function updateCalculator() {
    const d = D[S.country] || D['Canada'];
    let t = (d.t[S.level] || d.t["Bachelor's"]).slice();
    let l = d.l.slice();
    const o = d.other;
    const m = mult[S.life] || 1.0;

    // Lifestyle multiplier on living & accommodation
    l = [l[0] * m, l[1] * m];

    // Fast Track discount on Year 1 tuition (45% savings, so 0.55x)
    if (S.path === 'Fast Track') {
      t = [t[0] * 0.55, t[1] * 0.55];
    }

    const totalRange = [t[0] + l[0], t[1] + l[1]];

    const rTitle = $('rTitle');
    const rRange = $('rRange');
    const rTuition = $('rTuition');
    const rLiving = $('rLiving');
    const rOther = $('rOther');
    const rBtnCountry = $('rBtnCountry');

    if (rTitle) {
      rTitle.textContent = `${S.country} · ${S.level}${S.path === 'Fast Track' ? ' · Fast Track (Yr 1)' : ''}`;
    }
    if (rRange) rRange.textContent = rngLakh(totalRange);
    if (rTuition) rTuition.textContent = rngLakh(t);
    if (rLiving) rLiving.textContent = rngLakh(l);
    if (rOther) rOther.textContent = rngLakh(o);
    if (rBtnCountry) rBtnCountry.textContent = S.country;
  }

  // OPTION TILE SELECTION HANDLER
  document.querySelectorAll('.opts').forEach(group => {
    group.addEventListener('click', e => {
      const btn = e.target.closest('.opt');
      if (!btn) return;
      group.querySelectorAll('.opt').forEach(x => x.classList.remove('on'));
      btn.classList.add('on');
      S[group.dataset.k] = btn.dataset.v;
      updateCalculator();
    });
  });

  // DOWNLOAD REAL PDF BUTTON
  const calcDownloadPdfBtn = $('calcDownloadPdfBtn');
  if (calcDownloadPdfBtn) {
    calcDownloadPdfBtn.addEventListener('click', () => {
      const d = D[S.country] || D['Canada'];
      const pdfPath = (S.path === 'Fast Track' && d.ftGuide) ? d.ftGuide : d.directGuide;
      const fileName = `${S.country}_${S.path.replace(/\\s+/g, '_')}_Country_Guide_University_Yatra.pdf`;

      const a = document.createElement('a');
      a.href = pdfPath;
      a.download = fileName;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    });
  }

  // QUICK START FROM DESTINATIONS SECTION
  window.startCountryGuide = function (countryKey) {
    const keyMap = {
      'germany': 'Germany',
      'canada': 'Canada',
      'uk': 'United Kingdom',
      'australia': 'Australia',
      'usa': 'USA',
      'france': 'France',
      'ireland': 'Ireland'
    };
    const cName = keyMap[countryKey.toLowerCase()] || 'Canada';
    S.country = cName;

    // Highlight the button in UI
    const countryGroup = document.querySelector('.opts[data-k="country"]');
    if (countryGroup) {
      countryGroup.querySelectorAll('.opt').forEach(btn => {
        btn.classList.toggle('on', btn.dataset.v === cName);
      });
    }

    updateCalculator();

    const calcEl = $('calculator');
    if (calcEl) {
      calcEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  // ENQUIRY FORM SUBMISSION (NAME, NUMBER, EMAIL ONLY)
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
        submitBtn.innerHTML = 'Submitting...';
      }

      try {
        const payload = new URLSearchParams({
          type: 'enquiry_lead',
          name,
          phone: mobile,
          email,
          country: S.country,
          level: S.level,
          pathway: S.path,
          timestamp: new Date().toISOString()
        });

        fetch(SHEET_URL, {
          method: 'POST',
          mode: 'no-cors',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: payload.toString()
        }).catch(err => console.warn('Sheet webhook note:', err));
      } catch (err) {
        console.warn('Enquiry dispatch note:', err);
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

  // INITIALIZE CALCULATOR WITH IMAGE 2 VALUES
  updateCalculator();

})();
"""

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Updated js/main.js successfully with Image 2 calculator engine!")
