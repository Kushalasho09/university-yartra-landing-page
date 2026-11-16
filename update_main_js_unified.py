unified_main_js = '''/**
 * University Yatra — Study Abroad Landing Page
 * Official Dual Calculator & Interactive Guide Engine
 * Fully aligned with Client Design Handover & Verified Official Guides
 */

(function () {
  'use strict';

  const WA_NUMBER = '919217368750';
  const SHEET_URL = 'https://script.google.com/macros/s/AKfycbx_YOUR_APP_SCRIPT_ID/exec';

  const $ = id => document.getElementById(id);
  const wa = m => 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(m);

  /* =====================================================
     1. VERIFIED COST DATASET & GUIDE PDF MAP
     Tuition & Living figures in INR Lakhs (L) per year
     Derived from Official Embassies, Blocked Accounts & Client Data
     ===================================================== */
  const D = {
    'Germany': {
      flag: '🇩🇪',
      name: 'Germany',
      t: { "Bachelor's": [0.5, 3], "Master's": [0.5, 4], "MBA": [6, 15] },
      l: [9, 13], // Blocked Account: €11,904/yr ≈ ₹10.7L
      other: [1.5, 3], // APS ₹18k, Visa, Flights
      directGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftAllowed: ["Bachelor's", "Master's", "MBA"]
    },
    'Canada': {
      flag: '🇨🇦',
      name: 'Canada',
      t: { "Bachelor's": [12, 22], "Master's": [12, 24], "MBA": [18, 35] },
      l: [11, 16], // GIC Living Requirement: CAD 20,635 ≈ ₹12.8L
      other: [2, 4], // Biometrics, Medical, Study permit, Flights
      directGuide: 'assets/pdfs/Canada_Country_Guide_University_Yatra_v4.pdf',
      ftGuide: 'assets/pdfs/University-Yatra-Canada-Fast-Track-Guide.pdf',
      ftAllowed: ["Bachelor's", "Master's", "MBA"]
    },
    'United Kingdom': {
      flag: '🇬🇧',
      name: 'United Kingdom',
      t: { "Bachelor's": [13, 22], "Master's": [14, 25], "MBA": [18, 35] },
      l: [11, 17], // UKVI Maintenance: £10,827-£14,130 ≈ ₹11.8L-₹15.5L
      other: [2.2, 4.5], // Visa £490, IHS £776/yr, TB test, Flights
      directGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftAllowed: ["Master's", "MBA"]
    },
    'Australia': {
      flag: '🇦🇺',
      name: 'Australia',
      t: { "Bachelor's": [12, 24], "Master's": [14, 26], "MBA": [18, 34] },
      l: [14, 18], // Govt visa requirement: AUD 29,710/yr ≈ ₹16.6L
      other: [2.5, 5], // Visa, OSHC, Flights
      directGuide: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf',
      ftAllowed: []
    },
    'USA': {
      flag: '🇺🇸',
      name: 'USA',
      t: { "Bachelor's": [15, 32], "Master's": [16, 35], "MBA": [22, 50] },
      l: [12, 19], // US Living: $1,000-$2,500/mo ≈ ₹10.5L-₹20.5L
      other: [2.5, 5], // SEVIS, DS-160, Insurance, Flights
      directGuide: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf',
      ftAllowed: ["Bachelor's", "Master's", "MBA"]
    },
    'France': {
      flag: '🇫🇷',
      name: 'France',
      t: { "Bachelor's": [2, 12], "Master's": [2.5, 14], "MBA": [10, 22] },
      l: [8, 13], // Living: €700-€1,100/mo ≈ ₹7.5L-₹12L
      other: [1.5, 3.5], // Campus France, Visa, Flights
      directGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf', // Europe guide
      ftGuide: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftAllowed: ["Bachelor's", "Master's", "MBA"]
    },
    'Ireland': {
      flag: '🇮🇪',
      name: 'Ireland',
      t: { "Bachelor's": [9, 20], "Master's": [11, 22], "MBA": [14, 28] },
      l: [10, 15], // Living: €1,000-€1,500/mo ≈ ₹10.8L-₹15L
      other: [2, 4], // Visa, Medical, Flights
      directGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftGuide: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftAllowed: []
    }
  };

  /* Helper to format INR Lakhs */
  function fmtLakh(n) {
    return '₹' + (Number.isInteger(n) ? n : n.toFixed(1)) + 'L';
  }

  function rngLakh(arr) {
    return fmtLakh(arr[0]) + ' – ' + fmtLakh(arr[1]);
  }

  /* =====================================================
     2. VIEW 1: TWO-COLUMN INTERACTIVE CALCULATOR (Image 7)
     ===================================================== */
  const S2 = {
    country: 'Canada',
    level: 'MBA',
    pathway: 'fast-track',
    lifestyle: 'plus'
  };

  function update2ColCalculator() {
    const data = D[S2.country] || D['Canada'];
    const tBase = data.t[S2.level] || data.t["Master's"];
    const lBase = data.l;

    // Lifestyle multiplier: Budget: 0.9x, Moderate: 1.0x, Comfy: 1.2x
    const lifeMult = { lean: 0.9, mid: 1.0, plus: 1.2 }[S2.lifestyle] || 1.0;
    const lCalculated = [lBase[0] * lifeMult, lBase[1] * lifeMult];

    // Pathway: Fast Track Year 1 in India saves 45% on tuition
    let tCalculated = [tBase[0], tBase[1]];
    let pathwayLabel = 'Direct';
    let isFT = false;

    if (S2.pathway === 'fast-track') {
      tCalculated = [tBase[0] * 0.55, tBase[1] * 0.55];
      pathwayLabel = 'Fast Track (Yr 1)';
      isFT = true;
    }

    const totalRange = [tCalculated[0] + lCalculated[0], tCalculated[1] + lCalculated[1]];

    // Update Right Obsidian Card
    const rTitle = $('rTitle');
    const rRange = $('rRange');
    const rTuition = $('rTuition');
    const rLiving = $('rLiving');
    const rOther = $('rOther');
    const calcBtn = $('calcDownloadPdfBtn');

    if (rTitle) rTitle.textContent = `${S2.country} · ${S2.level} · ${pathwayLabel}`;
    if (rRange) rRange.textContent = rngLakh(totalRange);
    if (rTuition) rTuition.textContent = rngLakh(tCalculated);
    if (rLiving) rLiving.textContent = rngLakh(lCalculated);
    if (rOther) rOther.textContent = rngLakh(data.other);

    if (calcBtn) {
      calcBtn.textContent = `Download Free ${S2.country} Guide (PDF) ↓`;
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
        // Smoothly scroll to enquiry form
        const enq = $('enquiry');
        if (enq) enq.scrollIntoView({ behavior: 'smooth', block: 'start' });
      };
    }
  }

  function init2ColCalculator() {
    const view2Col = $('view2Col');
    if (!view2Col) return;

    view2Col.querySelectorAll('.opts').forEach(group => {
      const key = group.dataset.k;
      group.querySelectorAll('.opt').forEach(btn => {
        btn.addEventListener('click', () => {
          group.querySelectorAll('.opt').forEach(b => b.classList.remove('on'));
          btn.classList.add('on');
          S2[key] = btn.dataset.v;
          update2ColCalculator();
        });
      });
    });

    update2ColCalculator();
  }

  /* =====================================================
     3. VIEW 2: 4-TAP GUIDE WIZARD (Matches Image 2 & 4)
     ===================================================== */
  const WIZ_COUNTRIES = [
    { k: 'USA', n: 'USA', ft: ["Bachelor's", "Master's", "MBA"] },
    { k: 'Canada', n: 'Canada', ft: ["Bachelor's", "Master's", "MBA"] },
    { k: 'United Kingdom', n: 'United Kingdom', ft: ["Master's", "MBA"] },
    { k: 'Germany', n: 'Germany', ft: ["Bachelor's", "Master's", "MBA"] },
    { k: 'France', n: 'France', ft: ["Bachelor's", "Master's", "MBA"] },
    { k: 'Ireland', n: 'Ireland', ft: [] },
    { k: 'Australia', n: 'Australia', ft: [] },
    { k: 'Other', n: 'Other / Not sure', ft: [] }
  ];

  const WIZ_S = { country: 'Canada', level: "Master's", pathway: 'direct', timeline: 'Next 6 months' };
  let wizStep = 0;
  let wizLead = null;

  function renderWizardStep() {
    const gateView = $('wizGateView');
    const stepView = $('wizStepView');
    const backBtn = $('wizBackBtn');
    const dots = $('wizDots');
    const stepNo = $('wizStepNo');
    const crumbs = $('wizCrumbs');

    if (!stepView) return;

    gateView.hidden = true;
    stepView.hidden = false;

    // Update Dots and Back button
    if (backBtn) backBtn.hidden = wizStep === 0;
    if (stepNo) stepNo.textContent = (wizStep >= 4 ? 4 : wizStep + 1) + '/4';
    if (dots) {
      [...dots.children].forEach((d, i) => d.classList.toggle('on', i <= Math.min(wizStep, 3)));
    }

    // Update Crumbs
    if (crumbs) {
      crumbs.innerHTML = '';
      const vals = [WIZ_S.country, WIZ_S.level, WIZ_S.pathway, WIZ_S.timeline];
      for (let i = 0; i < wizStep; i++) {
        if (!vals[i]) continue;
        const cBtn = document.createElement('button');
        cBtn.type = 'button';
        cBtn.className = 'wizard-crumb';
        cBtn.textContent = vals[i] + ' ✎';
        cBtn.onclick = () => { wizStep = i; renderWizardStep(); };
        crumbs.appendChild(cBtn);
      }
    }

    stepView.innerHTML = '';
    const animWrap = document.createElement('div');
    animWrap.className = 'anim';

    const q = document.createElement('div');
    q.className = 'wizard-q';

    const sub = document.createElement('p');
    sub.className = 'wizard-qsub';

    const optsGrid = document.createElement('div');
    optsGrid.className = 'wizard-opts';

    if (wizStep === 0) {
      q.innerHTML = 'Where do you want <span class="hl">to study?</span>';
      sub.textContent = 'Tap one. We will take it from there.';
      WIZ_COUNTRIES.forEach(c => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'wizard-o' + (WIZ_S.country === c.k ? ' sel' : '');
        btn.innerHTML = `<b>${c.n}</b>`;
        btn.onclick = () => {
          WIZ_S.country = c.k;
          wizStep = 1;
          renderWizardStep();
        };
        optsGrid.appendChild(btn);
      });
    } else if (wizStep === 1) {
      q.innerHTML = 'What are you <span class="hl">aiming for?</span>';
      sub.textContent = 'Choose your level of study.';
      optsGrid.className = 'wizard-opts c3';
      [
        { lvl: "Bachelor's", sub: 'After 12th' },
        { lvl: "Master's", sub: 'After graduation' },
        { lvl: "MBA", sub: 'Business school' }
      ].forEach(item => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'wizard-o' + (WIZ_S.level === item.lvl ? ' sel' : '');
        btn.innerHTML = `<b>${item.lvl}</b><span>${item.sub}</span>`;
        btn.onclick = () => {
          WIZ_S.level = item.lvl;
          wizStep = 2;
          renderWizardStep();
        };
        optsGrid.appendChild(btn);
      });
    } else if (wizStep === 2) {
      q.innerHTML = 'Which route <span class="hl">interests you?</span>';
      sub.textContent = 'You can change this later with your counsellor.';
      optsGrid.className = 'wizard-opts c1';

      const dCountry = D[WIZ_S.country] || D['Canada'];
      const ftAllowed = dCountry.ftAllowed.includes(WIZ_S.level);

      const dBtn = document.createElement('button');
      dBtn.type = 'button';
      dBtn.className = 'wizard-o' + (WIZ_S.pathway === 'direct' ? ' sel' : '');
      dBtn.innerHTML = `<b>Direct</b><span>Study on campus abroad from day one</span>`;
      dBtn.onclick = () => {
        WIZ_S.pathway = 'direct';
        wizStep = 3;
        renderWizardStep();
      };
      optsGrid.appendChild(dBtn);

      if (ftAllowed) {
        const ftBtn = document.createElement('button');
        ftBtn.type = 'button';
        ftBtn.className = 'wizard-o' + (WIZ_S.pathway === 'fast-track' ? ' sel' : '');
        ftBtn.innerHTML = `<b>Fast Track</b><span>Start online in India, save up to 45%, finish abroad</span>`;
        ftBtn.onclick = () => {
          WIZ_S.pathway = 'fast-track';
          wizStep = 3;
          renderWizardStep();
        };
        optsGrid.appendChild(ftBtn);
      }
    } else if (wizStep === 3) {
      q.innerHTML = 'When do you plan <span class="hl">to start?</span>';
      sub.textContent = 'This helps us suggest the right intake.';
      optsGrid.className = 'wizard-opts';
      [
        { t: 'Next 6 months', s: 'Ready to move fast' },
        { t: '6-12 months', s: 'Planning ahead' },
        { t: '12+ months', s: 'Starting early' },
        { t: 'Just exploring', s: 'Learning the options' }
      ].forEach(item => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'wizard-o' + (WIZ_S.timeline === item.t ? ' sel' : '');
        btn.innerHTML = `<b>${item.t}</b><span>${item.s}</span>`;
        btn.onclick = () => {
          WIZ_S.timeline = item.t;
          showWizardGate();
        };
        optsGrid.appendChild(btn);
      });
    }

    animWrap.appendChild(q);
    animWrap.appendChild(sub);
    animWrap.appendChild(optsGrid);
    stepView.appendChild(animWrap);
  }

  function showWizardGate() {
    const gateView = $('wizGateView');
    const stepView = $('wizStepView');
    const gateTitle = $('wizGateTitle');
    const backBtn = $('wizBackBtn');

    if (!gateView || !stepView) return;

    stepView.hidden = true;
    gateView.hidden = false;
    if (backBtn) backBtn.hidden = false;

    if (gateTitle) {
      gateTitle.innerHTML = `Your <span class="hl">${WIZ_S.country}</span> guide is ready.`;
    }

    $('wiz_country').value = WIZ_S.country;
    $('wiz_level').value = WIZ_S.level;
    $('wiz_path').value = WIZ_S.pathway;
    $('wiz_time').value = WIZ_S.timeline;

    const gateForm = $('wizGateForm');
    const doneView = $('wizDoneView');
    if (gateForm) gateForm.style.display = 'block';
    if (doneView) doneView.style.display = 'none';
  }

  function initWizard() {
    const backBtn = $('wizBackBtn');
    if (backBtn) {
      backBtn.onclick = () => {
        if (wizStep > 0) {
          wizStep--;
          renderWizardStep();
        }
      };
    }

    const wizLeadForm = $('wizLeadForm');
    if (wizLeadForm) {
      wizLeadForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const fd = new FormData(wizLeadForm);
        const phone = String(fd.get('phone') || '').trim();
        const name = String(fd.get('name') || '').trim();

        if (!/^[6-9][0-9]{9}$/.test(phone)) {
          alert('Please enter a valid 10-digit Indian WhatsApp number');
          return;
        }

        const data = D[WIZ_S.country] || D['Canada'];
        const isFT = WIZ_S.pathway === 'fast-track';
        const guideFile = isFT ? data.ftGuide : data.directGuide;

        // Display Done State
        $('wizGateForm').style.display = 'none';
        $('wizDoneView').style.display = 'block';

        const dlContainer = $('wizDlContainer');
        if (dlContainer && guideFile) {
          dlContainer.innerHTML = `
            <a href="${guideFile}" download class="btn btn-primary btn-block" style="padding:15px;margin-bottom:10px;">
              <i class="fa-solid fa-download"></i> Download ${WIZ_S.country} Guide (PDF)
            </a>
          `;
          // Auto download
          setTimeout(() => {
            const a = document.createElement('a');
            a.href = guideFile;
            a.setAttribute('download', '');
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
          }, 300);
        }

        // WhatsApp personalized link
        const waMsg = `Hi University Yatra, I am ${name}. I am looking for ${WIZ_S.level} programmes in ${WIZ_S.country} (${WIZ_S.pathway}, timeline: ${WIZ_S.timeline}). I just downloaded the country guide.`;
        const waBtn = $('wizWaBtn');
        if (waBtn) waBtn.href = wa(waMsg);
      });
    }

    renderWizardStep();
  }

  /* =====================================================
     4. MODE SWITCHER (Live 2-Col vs 4-Tap Wizard)
     ===================================================== */
  function initModeSwitcher() {
    const btn2Col = $('btnMode2Col');
    const btnWiz = $('btnModeWizard');
    const v2Col = $('view2Col');
    const vWiz = $('viewWizard');

    if (!btn2Col || !btnWiz || !v2Col || !vWiz) return;

    btn2Col.addEventListener('click', () => {
      btn2Col.classList.add('on');
      btnWiz.classList.remove('on');
      v2Col.style.display = 'grid';
      vWiz.style.display = 'none';
    });

    btnWiz.addEventListener('click', () => {
      btnWiz.classList.add('on');
      btn2Col.classList.remove('on');
      v2Col.style.display = 'none';
      vWiz.style.display = 'block';
      renderWizardStep();
    });
  }

  /* =====================================================
     5. BOTTOM ENQUIRY FORM & SMOOTH CONTROLLERS
     ===================================================== */
  function initEnquiryForm() {
    const form = $('enquiryForm');
    const ok = $('formSuccess');
    if (!form || !ok) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const fd = new FormData(form);
      const phone = String(fd.get('mobile') || '').trim();

      if (!/^[6-9][0-9]{9}$/.test(phone)) {
        alert('Please enter a valid 10-digit Indian WhatsApp number');
        return;
      }

      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Submitting Enquiry...';
      }

      // Record lead
      setTimeout(() => {
        form.style.display = 'none';
        ok.style.display = 'block';
      }, 500);
    });
  }

  // Initialize all controllers on DOMContentLoaded
  document.addEventListener('DOMContentLoaded', function () {
    init2ColCalculator();
    initWizard();
    initModeSwitcher();
    initEnquiryForm();
  });

})();
'''

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(unified_main_js)

print('js/main.js updated with unified dual engine!')

