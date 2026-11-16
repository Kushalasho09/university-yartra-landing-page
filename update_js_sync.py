js_code = '''/**
 * University Yatra — Study Abroad Landing Page
 * Step-by-Step Calculator & Official Country Guide Controller
 * Features Prev/Continue navigation, country dropdown two-way sync, authentic costs & PDF downloads
 */

(function () {
  'use strict';

  const WA_NUMBER = '919217368750';
  const $ = id => document.getElementById(id);
  const wa = m => 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(m);

  /* Verified Official Cost Data (INR Lakhs/yr) */
  const D = {
    'Germany': {
      flag: '🇩🇪',
      name: 'Germany',
      t: { "Bachelor's": [0.5, 3], "Master's": [0.5, 4], "MBA": [6, 15] },
      l: [9, 13], // Blocked Account: €11,904/yr ≈ ₹10.7L
      other: [1.5, 3], // APS ₹18k, Visa, Flights
      directGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    },
    'Canada': {
      flag: '🇨🇦',
      name: 'Canada',
      t: { "Bachelor's": [12, 22], "Master's": [12, 24], "MBA": [18, 35] },
      l: [11, 16], // GIC Requirement: CAD 20,635 ≈ ₹12.8L
      other: [2, 4], // Biometrics, Medical, Study permit, Flights
      directGuide: 'assets/pdfs/Canada_Country_Guide_University_Yatra_v4.pdf',
      ftGuide: 'assets/pdfs/University-Yatra-Canada-Fast-Track-Guide.pdf'
    },
    'United Kingdom': {
      flag: '🇬🇧',
      name: 'United Kingdom',
      t: { "Bachelor's": [13, 22], "Master's": [14, 25], "MBA": [18, 35] },
      l: [11, 17], // UKVI Maintenance: £10,827-£14,130 ≈ ₹11.8L-₹15.5L
      other: [2.2, 4.5], // Visa £490, IHS £776/yr, TB, Flights
      directGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf'
    },
    'Australia': {
      flag: '🇦🇺',
      name: 'Australia',
      t: { "Bachelor's": [12, 24], "Master's": [14, 26], "MBA": [18, 34] },
      l: [14, 18], // Govt Visa Benchmark: AUD 29,710 ≈ ₹16.6L
      other: [2.5, 5], // Visa, OSHC, Flights
      directGuide: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf'
    },
    'USA': {
      flag: '🇺🇸',
      name: 'USA',
      t: { "Bachelor's": [15, 32], "Master's": [16, 35], "MBA": [22, 50] },
      l: [12, 19], // Living: $1,000-$2,500/mo ≈ ₹10.5L-₹20.5L
      other: [2.5, 5], // SEVIS, DS-160, Insurance, Flights
      directGuide: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf'
    },
    'France': {
      flag: '🇫🇷',
      name: 'France',
      t: { "Bachelor's": [2, 12], "Master's": [2.5, 14], "MBA": [10, 22] },
      l: [8, 13], // Living: €700-€1,100/mo ≈ ₹7.5L-₹12L
      other: [1.5, 3.5], // Campus France, Visa, Flights
      directGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    },
    'Ireland': {
      flag: '🇮🇪',
      name: 'Ireland',
      t: { "Bachelor's": [9, 20], "Master's": [11, 22], "MBA": [14, 28] },
      l: [10, 15], // Living: €1,000-€1,500/mo ≈ ₹10.8L-₹15L
      other: [2, 4], // Visa, Flights
      directGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf'
    }
  };

  function fmtLakh(n) {
    return '₹' + (Number.isInteger(n) ? n : n.toFixed(1)) + 'L';
  }

  function rngLakh(arr) {
    return fmtLakh(arr[0]) + ' – ' + fmtLakh(arr[1]);
  }

  /* Current Active State */
  const S = {
    country: 'Canada',
    level: "Master's",
    pathway: 'fast-track',
    lifestyle: 'mid'
  };

  let currentStep = 1;

  function updateStepView() {
    // Show/hide panes
    for (let i = 1; i <= 4; i++) {
      const pane = $('wizStep' + i);
      if (pane) pane.style.display = (currentStep === i) ? 'block' : 'none';
    }
    const resultPane = $('wizStepResult');
    if (resultPane) resultPane.style.display = (currentStep === 5) ? 'block' : 'none';

    // Update Progress Bar & Indicator
    const progressFill = $('wizProgressFill');
    const stepIndicator = $('wizStepIndicator');
    const prevBtn = $('wizPrevBtn');
    const nextBtn = $('wizNextBtn');

    if (currentStep <= 4) {
      if (progressFill) progressFill.style.width = (currentStep * 25) + '%';
      if (stepIndicator) stepIndicator.textContent = 'Step ' + currentStep + ' of 4';
      if (prevBtn) prevBtn.style.visibility = (currentStep === 1) ? 'hidden' : 'visible';
      if (nextBtn) {
        nextBtn.style.display = 'inline-flex';
        nextBtn.innerHTML = (currentStep === 4) ? 'Calculate Cost <i class="fa-solid fa-calculator"></i>' : 'Continue <i class="fa-solid fa-arrow-right"></i>';
      }
    } else {
      // Step 5: Result View
      if (progressFill) progressFill.style.width = '100%';
      if (stepIndicator) stepIndicator.textContent = 'Estimated Budget Ready';
      if (prevBtn) {
        prevBtn.style.visibility = 'visible';
        prevBtn.innerHTML = '<i class="fa-solid fa-arrow-left"></i> Edit Choices';
      }
      if (nextBtn) {
        nextBtn.style.display = 'none'; // Replaced by in-card actions
      }
      calculateResults();
    }
  }

  function calculateResults() {
    const data = D[S.country] || D['Canada'];
    const tBase = data.t[S.level] || data.t["Master's"];
    const lBase = data.l;

    // Lifestyle multiplier
    const lifeMult = { lean: 0.9, mid: 1.0, plus: 1.2 }[S.lifestyle] || 1.0;
    const lCalc = [lBase[0] * lifeMult, lBase[1] * lifeMult];

    // Pathway factor
    let tCalc = [tBase[0], tBase[1]];
    let pathwayLabel = 'Direct';
    let isFT = false;

    if (S.pathway === 'fast-track') {
      tCalc = [tBase[0] * 0.55, tBase[1] * 0.55];
      pathwayLabel = 'Fast Track (Yr 1)';
      isFT = true;
    }

    const totalRange = [tCalc[0] + lCalc[0], tCalc[1] + lCalc[1]];

    // DOM Updates
    const rTitle = $('rTitle');
    const rRange = $('rRange');
    const rTuition = $('rTuition');
    const rLiving = $('rLiving');
    const rOther = $('rOther');
    const ftBadge = $('ftSavingsBadge');
    const calcBtn = $('calcDownloadPdfBtn');
    const countrySelect = $('calc_country_select');

    if (rTitle) rTitle.textContent = `${data.flag} ${S.country} · ${S.level} · ${pathwayLabel}`;
    if (rRange) rRange.textContent = rngLakh(totalRange);
    if (rTuition) rTuition.textContent = rngLakh(tCalc);
    if (rLiving) rLiving.textContent = rngLakh(lCalc);
    if (rOther) rOther.textContent = rngLakh(data.other);

    // Sync Country Dropdown in form
    if (countrySelect && countrySelect.value !== S.country) {
      countrySelect.value = S.country;
    }

    // Fast Track Savings Badge
    if (ftBadge) {
      if (isFT) {
        const savedMin = tBase[0] * 0.45;
        const savedMax = tBase[1] * 0.45;
        ftBadge.style.display = 'block';
        ftBadge.innerHTML = `<i class="fa-solid fa-bolt"></i> Fast Track saves approx. <strong>${fmtLakh(savedMin)} – ${fmtLakh(savedMax)}</strong> on Year 1 tuition!`;
      } else {
        ftBadge.style.display = 'none';
      }
    }

    // PDF Download Button
    if (calcBtn) {
      calcBtn.innerHTML = `<i class="fa-solid fa-file-arrow-down"></i> Download Free ${S.country} Guide (PDF) ↓`;
      calcBtn.onclick = function () {
        const guidePdf = isFT ? data.ftGuide : data.directGuide;
        if (guidePdf) {
          const a = document.createElement('a');
          a.href = guidePdf;
          a.setAttribute('download', '');
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        }
      };
    }
  }

  function initWizardController() {
    const card = $('calcWizardCard');
    if (!card) return;

    // Option item selection
    card.querySelectorAll('.wiz-opt').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const parentGrid = btn.parentElement;
        parentGrid.querySelectorAll('.wiz-opt').forEach(b => b.classList.remove('on'));
        btn.classList.add('on');

        const key = btn.dataset.k;
        const val = btn.dataset.v;
        if (key && val) {
          S[key] = val;
          // If country changed in step 1, sync with dropdown
          if (key === 'country') {
            const countrySelect = $('calc_country_select');
            if (countrySelect) countrySelect.value = val;
          }
        }
      });
    });

    // Country Dropdown in Form (Two-way sync!)
    const countrySelect = $('calc_country_select');
    if (countrySelect) {
      countrySelect.addEventListener('change', function () {
        S.country = this.value;
        // Update Step 1 country buttons
        const step1Grid = $('wizStep1');
        if (step1Grid) {
          step1Grid.querySelectorAll('.wiz-opt').forEach(b => {
            b.classList.toggle('on', b.dataset.v === S.country);
          });
        }
        calculateResults();
      });
    }

    // Previous Button
    const prevBtn = $('wizPrevBtn');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (currentStep > 1) {
          currentStep--;
          updateStepView();
        }
      });
    }

    // Continue / Next Button
    const nextBtn = $('wizNextBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (currentStep < 5) {
          currentStep++;
          updateStepView();
        }
      });
    }

    // In-Card Delivery Form
    const quickForm = $('calcQuickLeadForm');
    const quickSuccess = $('calcQuickSuccess');
    if (quickForm && quickSuccess) {
      quickForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const fd = new FormData(quickForm);
        const phone = String(fd.get('phone') || '').trim();
        const phoneCode = String(fd.get('phone_code') || '+91').trim();
        const name = String(fd.get('name') || '').trim();
        const country = String(fd.get('country') || S.country).trim();

        if (phone.length < 7 || phone.length > 12) {
          alert('Please enter a valid mobile number');
          return;
        }

        const btn = $('calcQuickSubmitBtn');
        if (btn) {
          btn.disabled = true;
          btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Preparing Handbook...';
        }

        const data = D[country] || D['Canada'];
        const isFT = S.pathway === 'fast-track';
        const guidePdf = isFT ? data.ftGuide : data.directGuide;

        setTimeout(() => {
          quickForm.style.display = 'none';
          quickSuccess.style.display = 'block';

          // Trigger PDF download
          if (guidePdf) {
            const a = document.createElement('a');
            a.href = guidePdf;
            a.setAttribute('download', '');
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
          }

          // Open WhatsApp with detailed message
          const msg = `Hi University Yatra, my name is ${name}. I am looking for ${S.level} programmes in ${country} (${S.pathway}). I just downloaded the country guide. Please connect with me at ${phoneCode} ${phone}.`;
          window.open(wa(msg), '_blank');
        }, 400);
      });
    }

    updateStepView();
  }

  /* Bottom Enquiry Form (3 Fields ONLY: Name, Mobile, Email) */
  function initBottomEnquiry() {
    const form = $('enquiryForm');
    const ok = $('enquirySuccess');
    if (!form || !ok) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const fd = new FormData(form);
      const phone = String(fd.get('mobile') || '').trim();

      if (!/^[6-9][0-9]{9}$/.test(phone)) {
        alert('Please enter a valid 10-digit Indian WhatsApp number');
        return;
      }

      const btn = $('enquirySubmitBtn');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Submitting Enquiry...';
      }

      setTimeout(() => {
        form.style.display = 'none';
        ok.style.display = 'block';
      }, 500);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initWizardController();
    initBottomEnquiry();
  });

})();
'''

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print('Updated js/main.js successfully with country dropdown sync & clean WhatsApp connection!')

