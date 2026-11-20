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

  /* 100% Verified Logic Sheet Data extracted directly from official DOCX files */
  const DOCX_DATA = {
    'Canada': {
      flag: '🇨🇦',
      name: 'Canada',
      currency: 'CAD',
      fx: 'CAD 1 = ₹65',
      levels: {
        "Bachelor's": { directTotal: '≈ ₹91.5 Lakhs', ftAvailable: true, ftTotal: '≈ ₹66.3 Lakhs', ftSavings: '≈ ₹25.2 Lakhs' },
        "Master's": { directTotal: '≈ ₹65.2 Lakhs', ftAvailable: true, ftTotal: '≈ ₹55.0 Lakhs', ftSavings: '≈ ₹10.2 Lakhs' },
        "MBA": { directTotal: '≈ ₹70.4 Lakhs', ftAvailable: true, ftTotal: '≈ ₹58.0 Lakhs', ftSavings: '≈ ₹12.4 Lakhs' }
      },
      intake: 'September 2027 (Main) · May 2027 (Secondary)',
      guidePdf: 'assets/pdfs/Canada_Country_Guide_University_Yatra_v4.pdf',
      ftGuidePdf: 'assets/pdfs/University-Yatra-Canada-Fast-Track-Guide.pdf'
    },
    'Germany': {
      flag: '🇩🇪',
      name: 'Germany',
      currency: 'EUR',
      fx: 'EUR 1 = ₹100',
      levels: {
        "Bachelor's": { directTotal: '≈ ₹85.6 Lakhs', ftAvailable: true, ftTotal: '≈ ₹62.3 Lakhs', ftSavings: '≈ ₹23.3 Lakhs' },
        "Master's": { directTotal: '≈ ₹45.7 Lakhs', ftAvailable: true, ftTotal: '≈ ₹34.1 Lakhs', ftSavings: '≈ ₹11.6 Lakhs' },
        "MBA": { directTotal: '≈ ₹49.0 Lakhs', ftAvailable: true, ftTotal: '≈ ₹37.0 Lakhs', ftSavings: '≈ ₹12.0 Lakhs' }
      },
      intake: 'Winter Semester (Oct 2027) · Summer (Apr 2028)',
      guidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    },
    'United Kingdom': {
      flag: '🇬🇧',
      name: 'United Kingdom',
      currency: 'GBP',
      fx: 'GBP 1 = ₹110',
      levels: {
        "Bachelor's": { directTotal: '≈ ₹1.32 Cr', ftAvailable: true, ftTotal: '≈ ₹93.4 Lakhs', ftSavings: '≈ ₹38.6 Lakhs' },
        "Master's": { directTotal: '≈ ₹69.5 Lakhs', ftAvailable: true, ftTotal: '≈ ₹41.0 Lakhs', ftSavings: '≈ ₹28.5 Lakhs' },
        "MBA": { directTotal: '≈ ₹69.5 Lakhs', ftAvailable: true, ftTotal: '≈ ₹41.0 Lakhs', ftSavings: '≈ ₹28.5 Lakhs' }
      },
      intake: 'September 2027 (Main) · January 2028 (Secondary)',
      guidePdf: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftGuidePdf: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf'
    },
    'Australia': {
      flag: '🇦🇺',
      name: 'Australia',
      currency: 'AUD',
      fx: 'AUD 1 = ₹58',
      levels: {
        "Bachelor's": { directTotal: '≈ ₹1.16 Cr', ftAvailable: true, ftTotal: '≈ ₹82.8 Lakhs', ftSavings: '≈ ₹32.9 Lakhs' },
        "Master's": { directTotal: '≈ ₹72.0 Lakhs', ftAvailable: false, ftTotal: 'Direct Study Only', ftSavings: 'Direct Study Only' },
        "MBA": { directTotal: '≈ ₹77.8 Lakhs', ftAvailable: false, ftTotal: 'Direct Study Only', ftSavings: 'Direct Study Only' }
      },
      intake: 'July 2027 (Main) · February 2028 (Secondary)',
      guidePdf: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf',
      ftGuidePdf: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf'
    },
    'USA': {
      flag: '🇺🇸',
      name: 'USA',
      currency: 'USD',
      fx: 'USD 1 = ₹92',
      levels: {
        "Bachelor's": { directTotal: '≈ ₹1.56 Cr', ftAvailable: true, ftTotal: '≈ ₹1.23 Cr', ftSavings: '≈ ₹33.6 Lakhs' },
        "Master's": { directTotal: '≈ ₹82.6 Lakhs', ftAvailable: true, ftTotal: '≈ ₹47.1 Lakhs', ftSavings: '≈ ₹35.5 Lakhs' },
        "MBA": { directTotal: '≈ ₹86.3 Lakhs', ftAvailable: true, ftTotal: '≈ ₹49.0 Lakhs', ftSavings: '≈ ₹37.3 Lakhs' }
      },
      intake: 'Fall 2027 (Aug/Sept) · Spring 2028 (Jan)',
      guidePdf: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf',
      ftGuidePdf: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf'
    },
    'France': {
      flag: '🇫🇷',
      name: 'France',
      currency: 'EUR',
      fx: 'EUR 1 = ₹100',
      levels: {
        "Bachelor's": { directTotal: '≈ ₹73.1 Lakhs', ftAvailable: true, ftTotal: '≈ ₹54.0 Lakhs', ftSavings: '≈ ₹19.1 Lakhs' },
        "Master's": { directTotal: '≈ ₹55.0 Lakhs', ftAvailable: true, ftTotal: '≈ ₹32.9 Lakhs', ftSavings: '≈ ₹22.1 Lakhs' },
        "MBA": { directTotal: '≈ ₹61.0 Lakhs', ftAvailable: false, ftTotal: 'Direct Study Only', ftSavings: 'Direct Study Only' }
      },
      intake: 'September 2027 (Main) · January 2028 (Secondary)',
      guidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    },
    'Finland': {
      flag: '🇫🇮',
      name: 'Finland',
      currency: 'EUR',
      fx: 'EUR 1 = ₹100',
      levels: {
        "Bachelor's": { directTotal: '≈ ₹77.6 Lakhs', ftAvailable: true, ftTotal: '≈ ₹57.1 Lakhs', ftSavings: '≈ ₹20.5 Lakhs' },
        "Master's": { directTotal: '≈ ₹49.1 Lakhs', ftAvailable: true, ftTotal: '≈ ₹29.6 Lakhs', ftSavings: '≈ ₹19.5 Lakhs' },
        "MBA": { directTotal: '≈ ₹53.1 Lakhs', ftAvailable: true, ftTotal: '≈ ₹31.6 Lakhs', ftSavings: '≈ ₹21.5 Lakhs' }
      },
      intake: 'Autumn 2027 (Aug/Sept) · Spring 2028 (Jan)',
      guidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    }
  };

  const FLAG_SVGS = {
    'Canada': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 0H8V32H0Z" fill="#D80027"/><path d="M24 0H32V32H24Z" fill="#D80027"/><path d="M16 6L17.5 11L21 10L19 13.5L22 15.5L17.5 18L17 22H15L14.5 18L10 15.5L13 13.5L11 10L14.5 11L16 6Z" fill="#D80027"/></svg>',
    'Germany': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H32V11H0Z" fill="#0A1230"/><path d="M0 11H32V21H0Z" fill="#DE0000"/><path d="M0 21H32V32H0Z" fill="#FFCE00"/></svg>',
    'United Kingdom': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#012169"/><path d="M0 0L32 32M32 0L0 32" stroke="#fff" stroke-width="4"/><path d="M0 0L32 32M32 0L0 32" stroke="#C8102E" stroke-width="2.2"/><path d="M16 0V32M0 16H32" stroke="#fff" stroke-width="6"/><path d="M16 0V32M0 16H32" stroke="#C8102E" stroke-width="3.6"/></svg>',
    'Australia': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#00008B"/><path d="M0 0H16V16H0Z" fill="#012169"/><path d="M0 0L16 16M16 0L0 16" stroke="#fff" stroke-width="2"/><path d="M0 0L16 16M16 0L0 16" stroke="#C8102E" stroke-width="1.2"/><path d="M8 0V16M0 8H16" stroke="#fff" stroke-width="3"/><path d="M8 0V16M0 8H16" stroke="#C8102E" stroke-width="1.8"/><circle cx="24" cy="8" r="1.5" fill="#fff"/><circle cx="27" cy="14" r="1.5" fill="#fff"/><circle cx="22" cy="20" r="1.5" fill="#fff"/><circle cx="25" cy="25" r="1.5" fill="#fff"/><circle cx="8" cy="24" r="2.5" fill="#fff"/></svg>',
    'USA': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 3H32M0 8H32M0 13H32M0 18H32M0 23H32M0 28H32" stroke="#B22234" stroke-width="2.6"/><rect width="15" height="16" fill="#3C3B6E"/><circle cx="4" cy="4" r="1" fill="#fff"/><circle cx="11" cy="4" r="1" fill="#fff"/><circle cx="7.5" cy="8" r="1" fill="#fff"/><circle cx="4" cy="12" r="1" fill="#fff"/><circle cx="11" cy="12" r="1" fill="#fff"/></svg>',
    'France': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H11V32H0Z" fill="#002654"/><path d="M11 0H21V32H11Z" fill="#FFFFFF"/><path d="M21 0H32V32H21Z" fill="#ED2939"/></svg>',
    'Finland': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 13H32V19H0Z" fill="#003580"/><path d="M10 0H16V32H10Z" fill="#003580"/></svg>'
  };

  /* Current Active State */
  const S = {
    pathway: 'fast-track',
    level: "Master's",
    country: 'Canada',
    timeline: 'fall-2027'
  };

  let currentStep = 1;

  function resetResultGate() {
    const costsTable = $('lockedCostsTable');
    if (costsTable) costsTable.classList.remove('unlocked');
    const quickForm = $('calcQuickLeadForm');
    if (quickForm) {
      quickForm.style.display = '';
      quickForm.reset();
    }
    const quickSuccess = $('calcQuickSuccess');
    if (quickSuccess) quickSuccess.style.display = 'none';
    const btn = $('calcQuickSubmitBtn');
    if (btn) {
      btn.disabled = false;
      const cName = S.country || 'Canada';
      btn.innerHTML = `<i class="fa-solid fa-lock-open"></i> <span>Download Free ${cName} Cost Guide</span>`;
    }
  }

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
      // Clear unlocked / downloaded state when going back to previous steps
      resetResultGate();

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
      if (stepIndicator) stepIndicator.textContent = '';
      if (prevBtn) {
        prevBtn.style.visibility = 'visible';
        prevBtn.innerHTML = '<i class="fa-solid fa-arrow-left"></i> Edit Choices';
      }
      if (nextBtn) {
        nextBtn.style.display = 'none'; // Replaced by in-card lead form
      }
      calculateResults();
    }
  }

  function calculateResults() {
    const cData = DOCX_DATA[S.country] || DOCX_DATA['Canada'];
    const lvlData = cData.levels[S.level] || cData.levels["Master's"];

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

    // Exact Verified Figures (Blurred Behind Padlock until Lead submit)
    const blurDirect = $('blurDirectTotal');
    const blurFt = $('blurFtTotal');
    const blurSav = $('blurSavings');

    if (blurDirect) blurDirect.textContent = lvlData.directTotal;
    if (blurFt) blurFt.textContent = lvlData.ftTotal;
    if (blurSav) blurSav.textContent = lvlData.ftSavings;
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
        }
      });
    });

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
        const country = S.country || 'Canada';

        if (phone.length < 7 || phone.length > 12) {
          alert('Please enter a valid mobile number');
          return;
        }

        const btn = $('calcQuickSubmitBtn');
        if (btn) {
          btn.disabled = true;
          btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> <span>Preparing ${country} Cost Guide...</span>`;
        }

        const cData = DOCX_DATA[country] || DOCX_DATA['Canada'];
        const isFT = S.pathway === 'fast-track';
        const guidePdf = isFT ? cData.ftGuidePdf : cData.guidePdf;

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
          const msg = `Hi University Yatra, my name is ${name}. I am looking for ${S.level} programmes in ${country} (Route: ${S.pathway}, Target Intake: ${S.timeline}). I just unlocked the official ${country} cost guide${emailNote}. Please connect with me at ${phoneCode} ${phone}.`;
          window.open(wa(msg), '_blank');
        }, 400);
      });
    }

    // Reset button inside success view
    const resetBtn = $('calcResetBtn');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        currentStep = 1;
        updateStepView();
        const calcEl = $('calculator');
        if (calcEl) calcEl.scrollIntoView({ behavior: 'smooth' });
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
      'finland': 'Finland'
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

    // 8. Seamless Dual-Buffer Video Looper (Eliminates flicker & loop pause)
    initSeamlessFooterVideo();
  }

  /* ========================================================
     STEALTH AMBIENT FOOTER VIDEO — SEAMLESS DUAL BUFFER LOOP
     Eliminates native browser loop-stall & black-frame flicker
     ======================================================== */
  function initSeamlessFooterVideo() {
    const vidA = document.getElementById('ssfVideoA');
    const vidB = document.getElementById('ssfVideoB');
    if (!vidA || !vidB) return;

    let isAActive = true;
    let isTransitioning = false;
    const CROSSFADE_OFFSET = 0.6; // Start crossfade 0.6s before video ends

    // Start playback safely with user gesture fallback for mobile
    const startPlay = () => {
      vidA.play().catch(() => {});
    };
    startPlay();
    document.addEventListener('touchstart', startPlay, { once: true, passive: true });
    document.addEventListener('click', startPlay, { once: true });

    // Monitor time of currently active video
    function checkCrossfade(activeVid, incomingVid) {
      if (isTransitioning) return;
      if (!activeVid.duration || isNaN(activeVid.duration)) return;

      const timeLeft = activeVid.duration - activeVid.currentTime;
      if (timeLeft <= CROSSFADE_OFFSET && timeLeft > 0) {
        isTransitioning = true;

        // Cue and play incoming video
        incomingVid.currentTime = 0;
        incomingVid.play().then(() => {
          incomingVid.classList.add('is-active');
          activeVid.classList.remove('is-active');

          setTimeout(() => {
            isAActive = !isAActive;
            isTransitioning = false;
          }, 650);
        }).catch(() => {
          isTransitioning = false;
        });
      }
    }

    vidA.addEventListener('timeupdate', () => {
      if (isAActive) checkCrossfade(vidA, vidB);
    });

    vidB.addEventListener('timeupdate', () => {
      if (!isAActive) checkCrossfade(vidB, vidA);
    });

    // Battery & CPU optimization: pause when off-screen
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            if (isAActive) vidA.play().catch(() => {});
            else vidB.play().catch(() => {});
          } else {
            vidA.pause();
            vidB.pause();
          }
        });
      }, { threshold: 0.1 });
      const footer = document.querySelector('.ssf');
      if (footer) observer.observe(footer);
    }
  }

  /* ========================================================
     SECTION 2 — STUDY PATHWAYS MOBILE CAROUSEL & AUTO-SWIPE
     ======================================================== */
  function initPathwaysSlider() {
    const grid = document.getElementById('pathwaysGrid');
    const sliderWrap = document.querySelector('.path-slider-wrap');
    const tabs = document.querySelectorAll('.path-tab-btn');
    const dots = document.querySelectorAll('.path-dot');
    const slides = document.querySelectorAll('.path-slide');
    if (!grid || slides.length < 2) return;

    let currentIndex = 0;
    let autoTimer = null;
    const INTERVAL_MS = 5000; // 5 seconds loop

    function goToSlide(index, restartTimer = true) {
      if (window.innerWidth > 768) {
        grid.style.transform = '';
        return;
      }

      currentIndex = (index + slides.length) % slides.length;
      grid.style.transform = 'translateX(-' + (currentIndex * 50) + '%)';

      // Update Tab Buttons
      tabs.forEach((tab, i) => {
        const isActive = i === currentIndex;
        tab.classList.toggle('is-active', isActive);
        tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
      });

      // Update Indicator Dots
      dots.forEach((dot, i) => {
        dot.classList.toggle('is-active', i === currentIndex);
      });

      // Update Slide State
      slides.forEach((slide, i) => {
        slide.classList.toggle('is-active', i === currentIndex);
      });

      if (restartTimer) {
        startTimer();
      }
    }

    function nextSlide() {
      goToSlide(currentIndex + 1, false);
    }

    function startTimer() {
      stopTimer();
      if (window.innerWidth <= 768) {
        autoTimer = setInterval(nextSlide, INTERVAL_MS);
      }
    }

    function stopTimer() {
      if (autoTimer) {
        clearInterval(autoTimer);
        autoTimer = null;
      }
    }

    // Tab Button Clicks
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const idx = parseInt(tab.getAttribute('data-index'), 10) || 0;
        goToSlide(idx);
      });
    });

    // Dot Button Clicks
    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const idx = parseInt(dot.getAttribute('data-index'), 10) || 0;
        goToSlide(idx);
      });
    });

    // Touch Swipe Support
    let touchStartX = 0;
    let touchStartY = 0;
    let touchEndX = 0;
    let touchEndY = 0;

    const gestureTarget = sliderWrap || grid;

    gestureTarget.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
      touchStartY = e.changedTouches[0].screenY;
      stopTimer();
    }, { passive: true });

    gestureTarget.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      touchEndY = e.changedTouches[0].screenY;
      const diffX = touchEndX - touchStartX;
      const diffY = touchEndY - touchStartY;

      if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 35) {
        if (diffX < 0) {
          goToSlide(currentIndex + 1);
        } else {
          goToSlide(currentIndex - 1);
        }
      } else {
        startTimer();
      }
    }, { passive: true });

    // Handle screen resize
    window.addEventListener('resize', () => {
      if (window.innerWidth > 768) {
        stopTimer();
        grid.style.transform = '';
      } else {
        goToSlide(currentIndex, true);
      }
    });

    // Initial setup on load
    if (window.innerWidth <= 768) {
      goToSlide(0, true);
    }
  }

  /* ==========================================================================
     TESTIMONIALS INTERACTIVE STUDENT JOURNEYS CONTROLLER
     ========================================================================== */
  function initTestimonialsStories() {
    const stories = {
      unnati: [
        {k:'Starting point',t:'Could studying in Canada be financially possible?',d:'Unnati wanted to pursue a Master’s in Canada, but funding was a major concern. We reviewed her academic profile, finances and goals to understand the options.',s:'✦',img:'assets/images/consultation-unnati.jpg',alt:'Unnati Parekh online counselling consultation with University Yatra'},
        {k:'Education loan',t:'Her education loan was approved in 24 hours.',d:'We identified a suitable financing option and guided her application. The loan was approved within 24 hours with basic documentation; no additional supporting documents were required in her case.',s:'₹',img:'assets/images/unnati-milestone-02-loan.jpg?v=clean_hd1',alt:'3D clay diorama of fast 24-hour education loan approval with golden coins and certificate'},
        {k:'University admission',t:'She secured admission to Trent University.',d:'Unnati received an offer for the Master’s in Instrumental Chemical Analysis at Trent University, Ontario.',s:'⌂',img:'assets/images/unnati-milestone-03-admission.jpg?v=clean_hd1',alt:'3D clay diorama of Canadian university campus and admission acceptance offer'},
        {k:'Scholarship',t:'A university scholarship followed.',d:'After securing admission, Unnati also received a scholarship from Trent University, adding financial support to her studies.',s:'★',img:'assets/images/unnati-milestone-04-scholarship.jpg?v=clean_hd1',alt:'3D clay diorama of university scholarship golden trophy and merit award'},
        {k:'Co-op selection',t:'Selected for a Health Canada co-op.',d:'Unnati was selected for a co-op opportunity at Health Canada, Government of Canada, giving her the opportunity to gain professional exposure in her field.',s:'＋',img:'assets/images/unnati-milestone-05-coop.jpg?v=clean_hd1',alt:'3D clay diorama of chemistry and health science laboratory research workbench'}
      ],
      tauheed: [
        {k:'Academic eligibility',t:'Could a three-year degree lead to a Master’s?',d:'Tauheed wanted to study in Canada, but his three-year Bachelor’s degree made university selection more complex. We reviewed his qualification and researched suitable pathways.',s:'◎',img:'assets/images/consultation-tauheed.jpg',alt:'Tauheed Khan online academic counselling consultation with University Yatra'},
        {k:'University selection',t:'We identified a pathway at Algoma University.',d:'After evaluating his academic background, we found a Master’s pathway where his existing qualification could be considered for admission.',s:'⌂',img:'assets/images/tauheed-milestone-02-pathway.jpg?v=clean_hd1',alt:'3D clay diorama of Algoma University collegiate campus and winding academic pathway'},
        {k:'Education loan',t:'₹45 lakh sanctioned without a property mortgage.',d:'We assessed Tauheed’s financial profile and guided the loan application. His ₹45 lakh education loan was sanctioned without property mortgage collateral.',s:'₹',img:'assets/images/tauheed-milestone-03-loan.jpg?v=clean_hd1',alt:'3D clay diorama of ₹45 lakh education loan sanction document without mortgage'},
        {k:'Location planning',t:'The university location was part of the decision.',d:'Alongside academic fit, we considered Sault Ste. Marie’s regional context, local economic conditions and potential PNP pathways before finalising Algoma University.',s:'⌖',img:'assets/images/tauheed-milestone-04-location.jpg?v=clean_hd1',alt:'3D clay diorama of Sault Ste. Marie regional Ontario landscape with suspension bridge and compass'},
        {k:'Next step',t:'His admission and financing were in place.',d:'With a suitable Master’s admission and his education loan sanctioned, Tauheed was able to begin his academic journey in Canada.',s:'✓',img:'assets/images/tauheed-milestone-05-journey.jpg?v=clean_hd1',alt:'3D clay diorama of Canadian student arrival, passport, flight and Toronto city skyline'}
      ]
    };

    const section = document.querySelector('#testimonials, #uy-testimonials');
    if (!section) return;

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    section.querySelectorAll('[data-story]').forEach(card => {
      const key = card.dataset.story, steps = stories[key];
      if (!steps) return;
      let index = 0, timer = null;
      const image = card.querySelector('[data-image]'),
            title = card.querySelector('[data-title]'),
            desc = card.querySelector('[data-description]'),
            kicker = card.querySelector('[data-kicker]'),
            symbol = card.querySelector('[data-symbol]'),
            count = card.querySelector('[data-count]'),
            dots = card.querySelector('[data-dots]');

      if (dots && dots.children.length === 0) {
        steps.forEach((step, i) => {
          const b = document.createElement('button');
          b.type = 'button';
          b.className = 'uy-dot';
          b.setAttribute('aria-label', `Go to milestone ${i + 1}`);
          b.addEventListener('click', () => { show(i); restart(); });
          dots.appendChild(b);
        });
      }

      function show(next) {
        index = (next + steps.length) % steps.length;
        const s = steps[index];
        if (image) { image.src = s.img; image.alt = s.alt; }
        if (title) title.textContent = s.t;
        if (desc) desc.textContent = s.d;
        if (kicker) kicker.textContent = `${String(index + 1).padStart(2, '0')} · ${s.k}`;
        if (symbol) symbol.textContent = s.s;
        if (count) count.textContent = `${String(index + 1).padStart(2, '0')} / ${String(steps.length).padStart(2, '0')}`;
        if (dots) {
          [...dots.children].forEach((dot, i) => dot.setAttribute('aria-current', String(i === index)));
        }
      }

      function stop() {
        if (timer) {
          window.clearInterval(timer);
          timer = null;
        }
      }

      function start() {
        if (reduceMotion || document.hidden || card.matches(':hover') || card.contains(document.activeElement)) return;
        stop();
        timer = window.setInterval(() => show(index + 1), 5600);
      }

      function restart() {
        stop();
        start();
      }

      const prevBtn = card.querySelector('[data-prev]');
      const nextBtn = card.querySelector('[data-next]');
      if (prevBtn) prevBtn.addEventListener('click', () => { show(index - 1); restart(); });
      if (nextBtn) nextBtn.addEventListener('click', () => { show(index + 1); restart(); });

      card.addEventListener('mouseenter', stop);
      card.addEventListener('mouseleave', start);
      card.addEventListener('focusin', stop);
      card.addEventListener('focusout', e => {
        if (!card.contains(e.relatedTarget)) start();
      });

      document.addEventListener('visibilitychange', () => document.hidden ? stop() : start());
      show(0);
      start();
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initWizardController();
    initBottomEnquiry();
    initStickerSlapFooter();
    initPathwaysSlider();
    initTestimonialsStories();
  });

})();
