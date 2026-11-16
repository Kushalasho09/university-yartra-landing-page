/**
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

  const FLAG_SVGS = {
    'Canada': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 0H8V32H0Z" fill="#D80027"/><path d="M24 0H32V32H24Z" fill="#D80027"/><path d="M16 6L17.5 11L21 10L19 13.5L22 15.5L17.5 18L17 22H15L14.5 18L10 15.5L13 13.5L11 10L14.5 11L16 6Z" fill="#D80027"/></svg>',
    'Germany': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H32V11H0Z" fill="#0A1230"/><path d="M0 11H32V21H0Z" fill="#DE0000"/><path d="M0 21H32V32H0Z" fill="#FFCE00"/></svg>',
    'United Kingdom': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#012169"/><path d="M0 0L32 32M32 0L0 32" stroke="#fff" stroke-width="4"/><path d="M0 0L32 32M32 0L0 32" stroke="#C8102E" stroke-width="2.2"/><path d="M16 0V32M0 16H32" stroke="#fff" stroke-width="6"/><path d="M16 0V32M0 16H32" stroke="#C8102E" stroke-width="3.6"/></svg>',
    'Australia': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#00008B"/><path d="M0 0H16V16H0Z" fill="#012169"/><path d="M0 0L16 16M16 0L0 16" stroke="#fff" stroke-width="2"/><path d="M0 0L16 16M16 0L0 16" stroke="#C8102E" stroke-width="1.2"/><path d="M8 0V16M0 8H16" stroke="#fff" stroke-width="3"/><path d="M8 0V16M0 8H16" stroke="#C8102E" stroke-width="1.8"/><circle cx="24" cy="8" r="1.5" fill="#fff"/><circle cx="27" cy="14" r="1.5" fill="#fff"/><circle cx="22" cy="20" r="1.5" fill="#fff"/><circle cx="25" cy="25" r="1.5" fill="#fff"/><circle cx="8" cy="24" r="2.5" fill="#fff"/></svg>',
    'USA': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 3H32M0 8H32M0 13H32M0 18H32M0 23H32M0 28H32" stroke="#B22234" stroke-width="2.6"/><rect width="15" height="16" fill="#3C3B6E"/><circle cx="4" cy="4" r="1" fill="#fff"/><circle cx="11" cy="4" r="1" fill="#fff"/><circle cx="7.5" cy="8" r="1" fill="#fff"/><circle cx="4" cy="12" r="1" fill="#fff"/><circle cx="11" cy="12" r="1" fill="#fff"/></svg>',
    'France': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H11V32H0Z" fill="#002654"/><path d="M11 0H21V32H11Z" fill="#FFFFFF"/><path d="M21 0H32V32H21Z" fill="#ED2939"/></svg>',
    'Ireland': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H11V32H0Z" fill="#169B62"/><path d="M11 0H21V32H11Z" fill="#FFFFFF"/><path d="M21 0H32V32H21Z" fill="#FF883E"/></svg>'
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
    const flagEl = $('rCountryFlag');
    const titleText = $('rTitleText');
    const lockedDocName = $('lockedCountryDocName');
    const quickSubmitBtn = $('calcQuickSubmitBtn');

    if (flagEl) flagEl.innerHTML = FLAG_SVGS[S.country] || FLAG_SVGS['Canada'];
    if (titleText) titleText.textContent = `${S.country} · ${S.level} Programme`;
    if (lockedDocName) lockedDocName.textContent = `${S.country} Complete Cost Guide`;
    if (quickSubmitBtn) {
      quickSubmitBtn.innerHTML = `<i class="fa-solid fa-lock-open"></i> <span>Download Free ${S.country} Cost Guide</span>`;
    }

    // Actual Calculated Figures (Blurred Behind Padlock)
    const blurTuition = $('blurTuition');
    const blurLiving = $('blurLiving');
    const blurOther = $('blurOther');

    if (blurTuition) blurTuition.textContent = rngLakh(tCalc);
    if (blurLiving) blurLiving.textContent = rngLakh(lCalc);
    if (blurOther) blurOther.textContent = rngLakh(data.other);

    // Safely update legacy elements if present in DOM
    const rRange = $('rRange');
    const rTuition = $('rTuition');
    const rLiving = $('rLiving');
    const rOther = $('rOther');
    const ftBadge = $('ftSavingsBadge');
    const calcBtn = $('calcDownloadPdfBtn');
    const countrySelect = $('calc_country_select');

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
        const email = String(fd.get('email') || '').trim();
        const country = S.country || String(fd.get('country') || 'Canada').trim();

        if (phone.length < 7 || phone.length > 12) {
          alert('Please enter a valid mobile number');
          return;
        }

        const btn = $('calcQuickSubmitBtn');
        if (btn) {
          btn.disabled = true;
          btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> <span>Preparing ${country} Cost Guide...</span>`;
        }

        const data = D[country] || D['Canada'];
        const isFT = S.pathway === 'fast-track';
        const guidePdf = isFT ? data.ftGuide : data.directGuide;

        setTimeout(() => {
          // Unblur and reveal the personalized figures upon unlock!
          const costsTable = $('lockedCostsTable');
          if (costsTable) costsTable.classList.add('unlocked');

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
          const emailNote = email ? ` (Email: ${email})` : '';
          const msg = `Hi University Yatra, my name is ${name}. I am looking for ${S.level} programmes in ${country} (${S.pathway}). I just unlocked the official cost guide${emailNote}. Please connect with me at ${phoneCode} ${phone}.`;
          window.open(wa(msg), '_blank');
        }, 400);
      });
    }

    updateStepView();
  }

  // Country Quick Shortcut for Destination Cards
  window.startCountryGuide = function(cKey) {
    const map = {
      'germany': 'Germany',
      'canada': 'Canada',
      'uk': 'United Kingdom',
      'australia': 'Australia',
      'usa': 'USA',
      'france': 'France',
      'ireland': 'Ireland'
    };
    const cName = map[String(cKey).toLowerCase()] || 'Canada';
    const btn = document.querySelector(`.wiz-opt[data-k="country"][data-v="${cName}"]`);
    if (btn) btn.click();
    const calcEl = document.getElementById('calculator');
    if (calcEl) calcEl.scrollIntoView({ behavior: 'smooth' });
  };

  /* Bottom Enquiry Form (Name, Mobile, Email, Qualification, Destination, Course) */
  function initBottomEnquiry() {
    const form = $('enquiryForm');
    const ok = $('enquirySuccess');
    if (!form || !ok) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const fd = new FormData(form);
      const name = String(fd.get('name') || '').trim();
      const phone = String(fd.get('mobile') || '').trim();
      const email = String(fd.get('email') || '').trim();
      const qual = String(fd.get('qualification') || '').trim();
      const country = String(fd.get('country') || '').trim();
      const course = String(fd.get('course') || '').trim();

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
        const sub = ok.querySelector('p');
        if (sub) {
          sub.innerHTML = `Your enquiry has been received. Our team will contact you at <strong>+91 ${phone}</strong> shortly.`;
        }
      }, 500);
    });
  }

  /* ==========================================================================
     UNIVERSITY YATRA — STICKER SLAP FOOTER CONTROLLER
     Interactive Neo-Brutalist Studio Footer with Draggable Physics & SVG Marker
     ========================================================================== */
  function initStickerSlapFooter() {
    const footer = document.querySelector('.ssf');
    if (!footer) return;

    // 1. Stamp real path lengths for smooth SVG draw-in animation
    function stampLengths() {
      footer.querySelectorAll('path[data-draw]').forEach(p => {
        try {
          const l = Math.ceil(p.getTotalLength()) + 1;
          p.style.setProperty('--l', l + 'px');
        } catch (e) {}
      });
    }
    stampLengths();

    // 2. Intersection Observer to trigger storyboard on enter
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver(entries => {
        if (entries.some(e => e.isIntersecting)) {
          footer.classList.add('is-in');
          io.disconnect();
        }
      }, { threshold: 0.15 });
      io.observe(footer);
    } else {
      footer.classList.add('is-in');
    }

    // 3. Parallax tilt on mousemove
    footer.addEventListener('pointermove', e => {
      if (e.pointerType !== 'mouse') return;
      const r = footer.getBoundingClientRect();
      if (!r.width || !r.height) return;
      footer.style.setProperty('--ssf-px', (((e.clientX - r.left) / r.width - 0.5) * 2).toFixed(3));
      footer.style.setProperty('--ssf-py', (((e.clientY - r.top) / r.height - 0.5) * 2).toFixed(3));
    });
    footer.addEventListener('pointerleave', () => {
      footer.style.setProperty('--ssf-px', '0');
      footer.style.setProperty('--ssf-py', '0');
    });

    // 4. Interactive Draggable Stickers with Throw-Tilt & Slap Physics
    const stage = footer.querySelector('.ssf-stage-in');
    const stickers = footer.querySelectorAll('.ssf-st');
    let highestZ = 10;

    stickers.forEach((st) => {
      const btn = st.querySelector('.ssf-st-btn');
      const lift = st.querySelector('.ssf-st-lift');
      if (!btn) return;

      const homeX = parseFloat(st.dataset.homeX || st.style.left);
      const homeY = parseFloat(st.dataset.homeY || st.style.top);
      st.dataset.homeX = homeX;
      st.dataset.homeY = homeY;

      let drag = null;

      btn.addEventListener('pointerdown', e => {
        if (e.button !== 0 || !stage) return;
        const r = stage.getBoundingClientRect();
        btn.setPointerCapture(e.pointerId);
        highestZ++;
        st.style.zIndex = highestZ;

        drag = {
          id: e.pointerId,
          sx: parseFloat(st.style.left),
          sy: parseFloat(st.style.top),
          px: e.clientX,
          py: e.clientY,
          lx: e.clientX,
          t: performance.now(),
          tilt: 0,
          w: r.width,
          h: r.height,
          went: false
        };
      });

      btn.addEventListener('pointermove', e => {
        if (!drag || drag.id !== e.pointerId) return;
        const dx = e.clientX - drag.px;
        const dy = e.clientY - drag.py;
        if (!drag.went && Math.hypot(dx, dy) < 4) return;

        if (!drag.went) st.classList.add('is-drag');
        drag.went = true;

        const x = Math.min(99, Math.max(1, drag.sx + (dx / drag.w) * 100));
        const y = Math.min(96, Math.max(-70, drag.sy + (dy / drag.h) * 100));
        st.style.left = x + '%';
        st.style.top = y + '%';

        const now = performance.now();
        const v = (e.clientX - drag.lx) / Math.max(1, now - drag.t);
        drag.tilt = drag.tilt * 0.75 + Math.min(24, Math.max(-24, v * 22)) * 0.25;
        drag.lx = e.clientX;
        drag.t = now;
        st.style.setProperty('--tilt', drag.tilt.toFixed(2) + 'deg');
      });

      const onUp = e => {
        if (!drag || drag.id !== e.pointerId) return;
        drag = null;
        st.classList.remove('is-drag');
        st.style.setProperty('--tilt', '0deg');
        if (lift && lift.animate) {
          lift.animate([
            { transform: 'scale(1.14)' },
            { transform: 'scale(.93, 1.04)', offset: 0.4 },
            { transform: 'scale(1.02, .98)', offset: 0.7 },
            { transform: 'none' }
          ], { duration: 420, easing: 'cubic-bezier(.3, 1.4, .4, 1)' });
        }
      };

      btn.addEventListener('pointerup', onUp);
      btn.addEventListener('pointercancel', onUp);

      // Double-click returns sticker back to home position
      btn.addEventListener('dblclick', () => {
        st.style.left = homeX + '%';
        st.style.top = homeY + '%';
        if (lift && lift.animate) {
          lift.animate([
            { transform: 'scale(1.18)' },
            { transform: 'scale(.92, 1.05)', offset: 0.4 },
            { transform: 'none' }
          ], { duration: 420, easing: 'cubic-bezier(.3, 1.4, .4, 1)' });
        }
      });
    });

    // 5. Click wordmark to replay writing animation and send stickers home
    const wmBtn = footer.querySelector('.ssf-wm-btn');
    if (wmBtn) {
      wmBtn.addEventListener('click', () => {
        stickers.forEach(st => {
          st.style.left = st.dataset.homeX + '%';
          st.style.top = st.dataset.homeY + '%';
        });
        footer.classList.remove('is-in');
        void footer.offsetWidth; // force reflow
        stampLengths();
        footer.classList.add('is-in');
      });
    }

    // 6. Copy email on click
    const copyBtn = footer.querySelector('.ssf-copy');
    if (copyBtn) {
      copyBtn.addEventListener('click', async () => {
        const email = copyBtn.querySelector('.ssf-addr')?.textContent?.trim() || 'info@universityyatra.com';
        try {
          await navigator.clipboard.writeText(email);
          copyBtn.classList.add('is-copied');
          setTimeout(() => copyBtn.classList.remove('is-copied'), 2200);
        } catch (err) {
          window.location.href = 'mailto:' + email;
        }
      });
    }

    // 7. Credits popover toggle
    const creditsPill = footer.querySelector('.ssf-pill');
    const creditsPop = footer.querySelector('.ssf-pop');
    if (creditsPill && creditsPop) {
      creditsPill.addEventListener('click', e => {
        e.stopPropagation();
        creditsPop.style.display = creditsPop.style.display === 'block' ? 'none' : 'block';
      });
      document.addEventListener('pointerdown', e => {
        if (!creditsPop.contains(e.target) && e.target !== creditsPill) {
          creditsPop.style.display = 'none';
        }
      });
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    initWizardController();
    initBottomEnquiry();
    initStickerSlapFooter();
  });

})();
