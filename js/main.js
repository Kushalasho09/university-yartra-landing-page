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
        "Master's": { directTotal: '≈ ₹72.0 Lakhs', ftAvailable: false, ftTotal: 'Regular Admission Only', ftSavings: 'Regular Admission Only' },
        "MBA": { directTotal: '≈ ₹77.8 Lakhs', ftAvailable: false, ftTotal: 'Regular Admission Only', ftSavings: 'Regular Admission Only' }
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
        "MBA": { directTotal: '≈ ₹61.0 Lakhs', ftAvailable: false, ftTotal: 'Regular Admission Only', ftSavings: 'Regular Admission Only' }
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
    },
    'Other': {
      flag: '🌐',
      name: 'Other',
      currency: 'USD',
      fx: 'Flexible Global FX',
      levels: {
        "Bachelor's": { directTotal: 'Custom Estimate', ftAvailable: true, ftTotal: 'Custom Fast Track', ftSavings: 'Save up to 50%*' },
        "Master's": { directTotal: 'Custom Estimate', ftAvailable: true, ftTotal: 'Custom Fast Track', ftSavings: 'Save up to 50%*' },
        "MBA": { directTotal: 'Custom Estimate', ftAvailable: true, ftTotal: 'Custom Fast Track', ftSavings: 'Save up to 50%*' }
      },
      intake: 'Flexible Intakes across Europe, Asia & Overseas',
      guidePdf: 'assets/pdfs/Canada_Country_Guide_University_Yatra_v4.pdf',
      ftGuidePdf: 'assets/pdfs/University-Yatra-Canada-Fast-Track-Guide.pdf'
    }
  };

  const INTAKE_TABLE = {
    'Germany': '<strong>Germany Intakes:</strong> Main: Winter (September/October) &bull; Additional: Summer (March/April)',
    'Canada': '<strong>Canada Intakes:</strong> Main: Fall (September) &bull; Additional: Winter (January), Summer (May)',
    'USA': '<strong>USA Intakes:</strong> Main: Fall (August/September) &bull; Additional: Spring (January), Summer (May/June)',
    'United Kingdom': '<strong>UK Intakes:</strong> Main: September/October &bull; Additional: January, May',
    'France': '<strong>France Intakes:</strong> Main: September/October &bull; Additional: January/February (selected programs)',
    'Australia': '<strong>Australia Intakes:</strong> Main: February/March, July &bull; Additional: November (selected universities)',
    'Finland': '<strong>Finland Intakes:</strong> Main: Autumn (August/September) &bull; Additional: Spring (January)',
    'Other': '<strong>Other Destinations:</strong> Multiple flexible intakes across Europe, Asia & overseas'
  };

  const FLAG_SVGS = {
    'Canada': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 0H8V32H0Z" fill="#D80027"/><path d="M24 0H32V32H24Z" fill="#D80027"/><path d="M16 6L17.5 11L21 10L19 13.5L22 15.5L17.5 18L17 22H15L14.5 18L10 15.5L13 13.5L11 10L14.5 11L16 6Z" fill="#D80027"/></svg>',
    'Germany': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H32V11H0Z" fill="#0A1230"/><path d="M0 11H32V21H0Z" fill="#DE0000"/><path d="M0 21H32V32H0Z" fill="#FFCE00"/></svg>',
    'United Kingdom': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#012169"/><path d="M0 0L32 32M32 0L0 32" stroke="#fff" stroke-width="4"/><path d="M0 0L32 32M32 0L0 32" stroke="#C8102E" stroke-width="2.2"/><path d="M16 0V32M0 16H32" stroke="#fff" stroke-width="6"/><path d="M16 0V32M0 16H32" stroke="#C8102E" stroke-width="3.6"/></svg>',
    'Australia': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#00008B"/><path d="M0 0H16V16H0Z" fill="#012169"/><path d="M0 0L16 16M16 0L0 16" stroke="#fff" stroke-width="2"/><path d="M0 0L16 16M16 0L0 16" stroke="#C8102E" stroke-width="1.2"/><path d="M8 0V16M0 8H16" stroke="#fff" stroke-width="3"/><path d="M8 0V16M0 8H16" stroke="#C8102E" stroke-width="1.8"/><circle cx="24" cy="8" r="1.5" fill="#fff"/><circle cx="27" cy="14" r="1.5" fill="#fff"/><circle cx="22" cy="20" r="1.5" fill="#fff"/><circle cx="25" cy="25" r="1.5" fill="#fff"/><circle cx="8" cy="24" r="2.5" fill="#fff"/></svg>',
    'USA': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 3H32M0 8H32M0 13H32M0 18H32M0 23H32M0 28H32" stroke="#B22234" stroke-width="2.6"/><rect width="15" height="16" fill="#3C3B6E"/><circle cx="4" cy="4" r="1" fill="#fff"/><circle cx="11" cy="4" r="1" fill="#fff"/><circle cx="7.5" cy="8" r="1" fill="#fff"/><circle cx="4" cy="12" r="1" fill="#fff"/><circle cx="11" cy="12" r="1" fill="#fff"/></svg>',
    'France': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H11V32H0Z" fill="#002654"/><path d="M11 0H21V32H11Z" fill="#FFFFFF"/><path d="M21 0H32V32H21Z" fill="#ED2939"/></svg>',
    'Finland': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 13H32V19H0Z" fill="#003580"/><path d="M10 0H16V32H10Z" fill="#003580"/></svg>',
    'Other': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><circle cx="16" cy="16" r="15" fill="#1856F3" stroke="#0A1230" stroke-width="1.8"/><ellipse cx="16" cy="16" rx="7" ry="14.5" fill="none" stroke="#C8FF3E" stroke-width="1.6"/><line x1="1.5" y1="16" x2="30.5" y2="16" stroke="#C8FF3E" stroke-width="1.6"/><line x1="3.5" y1="10" x2="28.5" y2="10" stroke="#FFFDF5" stroke-width="1.4"/><line x1="3.5" y1="22" x2="28.5" y2="22" stroke="#FFFDF5" stroke-width="1.4"/></svg>'
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
      quickForm.classList.remove('is-hidden');
      quickForm.style.setProperty('display', 'flex');
      quickForm.reset();
    }
    const quickSuccess = $('calcQuickSuccess');
    if (quickSuccess) {
      quickSuccess.classList.remove('is-active');
      quickSuccess.style.setProperty('display', 'none');
    }
    const btn = $('calcQuickSubmitBtn');
    if (btn) {
      btn.disabled = false;
      const cName = S.country || 'Canada';
      btn.innerHTML = `<i class="fa-solid fa-lock-open"></i> <span>Download Free ${cName} Cost Guide</span>`;
    }
    try {
      sessionStorage.removeItem('uy_calc_unlocked');
    } catch (e) {}
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

      // Update dynamic intake schedule banner for chosen country
      const intakeTextEl = $('countryIntakeText');
      if (intakeTextEl) {
        intakeTextEl.innerHTML = INTAKE_TABLE[S.country] || INTAKE_TABLE['Canada'];
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

    // Calculator smooth scroll alignment on step transition
    const cardEl = $('calcWizardCard');
    if (cardEl) {
      const rect = cardEl.getBoundingClientRect();
      if (rect.top < 50 || rect.top > 160) {
        cardEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  }

  function calculateResults() {
    const isOther = (S.country === 'Other');
    const cData = DOCX_DATA[S.country] || DOCX_DATA['Canada'];
    const lvlData = cData.levels[S.level] || cData.levels["Master's"];

    // DOM Updates
    const flagEl = $('rCountryFlag');
    const titleText = $('rTitleText');
    const lockedDocName = $('lockedCountryDocName');
    const otherBlock = $('otherCountryBlock');
    const lockedCard = document.querySelector('.locked-report-card');
    const quickForm = $('calcQuickLeadForm');
    const quickSuccess = $('calcQuickSuccess');
    const discEl = document.querySelector('.wiz-result-box .disc');

    if (otherBlock) otherBlock.style.display = isOther ? 'block' : 'none';
    if (lockedCard) lockedCard.style.display = isOther ? 'none' : 'block';

    // In 'Others', hide lead form and 'Download Free Global Study Guide' button completely as requested
    if (quickForm) {
      if (isOther) {
        quickForm.classList.add('is-hidden');
        quickForm.style.setProperty('display', 'none', 'important');
      } else {
        quickForm.classList.remove('is-hidden');
        quickForm.style.setProperty('display', 'flex');
      }
    }
    if (quickSuccess && isOther) {
      quickSuccess.classList.remove('is-active');
      quickSuccess.style.setProperty('display', 'none', 'important');
    }
    if (discEl) {
      discEl.style.display = isOther ? 'none' : 'block';
    }

    if (flagEl) flagEl.innerHTML = FLAG_SVGS[S.country] || FLAG_SVGS['Canada'];
    if (titleText) titleText.textContent = isOther ? `Other Destinations · ${S.level} Programme` : `${S.country} · ${S.level} Programme`;
    if (lockedDocName) lockedDocName.textContent = `${S.country} Complete Cost Guide`;

    // Exact Verified Figures (Blurred Behind Padlock until Lead submit)
    const blurDirect = $('blurDirectTotal');
    const blurFt = $('blurFtTotal');
    const blurSav = $('blurSavings');

    if (blurDirect) blurDirect.textContent = lvlData.directTotal;
    if (blurFt) blurFt.textContent = lvlData.ftTotal;
    if (blurSav) blurSav.textContent = lvlData.ftSavings;

    if (!isOther) {
      // Check if user already unlocked this destination in current session
      try {
        const unlockedCountry = sessionStorage.getItem('uy_calc_unlocked');
        if (unlockedCountry && unlockedCountry === S.country) {
          const costsTable = $('lockedCostsTable');
          if (costsTable) costsTable.classList.add('unlocked');
          if (quickForm) {
            quickForm.classList.add('is-hidden');
            quickForm.style.setProperty('display', 'none', 'important');
          }
          if (quickSuccess) {
            quickSuccess.classList.add('is-active');
            quickSuccess.style.setProperty('display', 'block', 'important');
            const scName = $('successCountryName');
            if (scName) scName.textContent = S.country;
          }
        }
      } catch (e) {}
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
        const isOther = (country === 'Other');

        if (phone.length < 7 || phone.length > 12) {
          alert('Please enter a valid mobile number');
          return;
        }

        const btn = $('calcQuickSubmitBtn');
        if (btn) {
          btn.disabled = true;
          btn.innerHTML = isOther ?
            `<i class="fa-solid fa-spinner fa-spin"></i> <span>Preparing Global Study Guide...</span>` :
            `<i class="fa-solid fa-spinner fa-spin"></i> <span>Preparing ${country} Cost Guide...</span>`;
        }

        const cData = DOCX_DATA[country] || DOCX_DATA['Canada'];
        const isFT = S.pathway === 'fast-track';
        const guidePdf = isOther ? 'assets/pdfs/Canada_Country_Guide_University_Yatra_v4.pdf' : (isFT ? cData.ftGuidePdf : cData.guidePdf);

        setTimeout(() => {
          // Reset the submit button state so it is never permanently stuck on spinner
          if (btn) {
            btn.disabled = false;
            btn.innerHTML = isOther ?
              `<i class="fa-solid fa-lock-open"></i> <span>Download Free Global Study Guide</span>` :
              `<i class="fa-solid fa-lock-open"></i> <span>Download Free ${country} Cost Guide</span>`;
          }

          // Unblur and reveal the personalized figures upon unlock!
          const costsTable = $('lockedCostsTable');
          if (costsTable) costsTable.classList.add('unlocked');

          // Cleanly hide lead form (both class and inline !important)
          quickForm.classList.add('is-hidden');
          quickForm.style.setProperty('display', 'none', 'important');

          // Update country name on success banner and cleanly show it
          const scName = $('successCountryName');
          if (scName) scName.textContent = isOther ? 'Global Study Abroad' : country;
          quickSuccess.classList.add('is-active');
          quickSuccess.style.setProperty('display', 'block', 'important');

          // Save unlocked state to sessionStorage
          try {
            sessionStorage.setItem('uy_calc_unlocked', country);
          } catch (e) {}

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
          const msg = isOther ?
            `Hi University Yatra, my name is ${name}. I am looking for ${S.level} programmes in other international destinations (Europe, Asia or elsewhere - Target Intake: ${S.timeline}). Please connect with me to give me a clearer idea of what to expect${emailNote}. Contact me at ${phoneCode} ${phone}.` :
            `Hi University Yatra, my name is ${name}. I am looking for ${S.level} programmes in ${country} (Route: ${S.pathway}, Target Intake: ${S.timeline}). I just unlocked the official ${country} cost guide${emailNote}. Please connect with me at ${phoneCode} ${phone}.`;
          window.open(wa(msg), '_blank');
        }, 400);
      });
    }

    // Download Again button inside success view
    const downloadAgainBtn = $('calcDownloadAgainBtn');
    if (downloadAgainBtn) {
      downloadAgainBtn.addEventListener('click', () => {
        const country = S.country || 'Canada';
        const cData = DOCX_DATA[country] || DOCX_DATA['Canada'];
        const isFT = S.pathway === 'fast-track';
        const guidePdf = isFT ? cData.ftGuidePdf : cData.guidePdf;
        if (guidePdf) {
          const a = document.createElement('a');
          a.href = guidePdf;
          a.setAttribute('download', '');
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        }
      });
    }

    // Reset button inside success view
    const resetBtn = $('calcResetBtn');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        resetResultGate();
        currentStep = 1;
        updateStepView();
        const calcEl = $('calculator');
        if (calcEl) calcEl.scrollIntoView({ behavior: 'smooth' });
      });
    }

    // Prevent stuck disabled/loading buttons when returning from another tab or BFCache
    window.addEventListener('pageshow', () => {
      const btn = $('calcQuickSubmitBtn');
      if (btn && btn.disabled) {
        btn.disabled = false;
        const cName = S.country || 'Canada';
        btn.innerHTML = `<i class="fa-solid fa-lock-open"></i> <span>Download Free ${cName} Cost Guide</span>`;
      }
    });

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
      'finland': 'Finland',
      'other': 'Other'
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

      const countryCode = String(fd.get('country_code') || '+91').trim();

      if (countryCode === '+91') {
        if (!/^[6-9][0-9]{9}$/.test(phone)) {
          alert('Please enter a valid 10-digit Indian WhatsApp number');
          return;
        }
      } else {
        if (!/^[0-9]{7,15}$/.test(phone)) {
          alert('Please enter a valid phone number');
          return;
        }
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
          sub.innerHTML = `Your enquiry has been received. Our team will contact you at <strong>${countryCode} ${phone}</strong> shortly.`;
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
    const INTERVAL_MS = 2800; // Set transition delay to under 3 seconds (2.8s auto-scroll)

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
     REEL-STYLE STUDENT JOURNEY MODAL CONTROLLER (OPTION 1)
     ========================================================================== */
  function initStudentJourneyReelModal() {
    const modal = document.getElementById('uyReelModal');
    if (!modal) return;

    const backdrop = document.getElementById('uyReelBackdrop');
    const outerClose = document.getElementById('uyReelCloseBtn');
    const innerClose = document.getElementById('uyReelInnerClose');
    const intro = document.getElementById('uyReelIntro');
    const introTitle = document.getElementById('uyReelIntroTitle');
    const loaderBar = document.getElementById('uyReelLoaderBar');
    const video = document.getElementById('uyReelVideo');
    const centerPlay = document.getElementById('uyReelCenterPlay');
    const playPauseBtn = document.getElementById('uyReelPlayPause');
    const muteBtn = document.getElementById('uyReelMute');
    const track = document.getElementById('uyReelTrack');
    const trackFill = document.getElementById('uyReelTrackFill');
    const trackKnob = document.getElementById('uyReelTrackKnob');
    const timeText = document.getElementById('uyReelTime');
    const tag = document.getElementById('uyReelTag');

    const cards = document.querySelectorAll('.uy-card[data-story-video]');
    let introTimer = null;

    function formatTime(secs) {
      if (isNaN(secs) || secs < 0) return '0:00';
      const m = Math.floor(secs / 60);
      const s = Math.floor(secs % 60);
      return `${m}:${s < 10 ? '0' : ''}${s}`;
    }

    function openModal(name, videoSrc) {
      // 1. Set titles and video source
      if (introTitle) {
        introTitle.innerHTML = `${name}'s Story<br><span>Begins Like This...</span>`;
      }
      if (tag) {
        tag.innerHTML = `<i class="fa-solid fa-circle-play"></i> ${name}'s Journey`;
      }

      if (video) {
        video.src = videoSrc;
        video.load();
      }

      // 2. Reset intro state
      if (intro) {
        intro.classList.remove('is-hidden');
        intro.classList.add('is-animating');
      }
      if (loaderBar) {
        loaderBar.style.animation = 'none';
        void loaderBar.offsetHeight;
        loaderBar.style.animation = '';
      }

      // 3. Reset video controls state
      updatePlayPauseState(false);
      if (trackFill) trackFill.style.width = '0%';
      if (trackKnob) trackKnob.style.left = '0%';
      if (timeText) timeText.textContent = '0:00 / 0:00';

      // 4. Open modal
      modal.classList.add('is-active');
      modal.setAttribute('aria-hidden', 'false');
      document.body.classList.add('uy-modal-open');

      if (introTimer) clearTimeout(introTimer);

      // 5. After intro animation (~1.4s), transition to video playback
      introTimer = setTimeout(() => {
        if (intro) {
          intro.classList.add('is-hidden');
          intro.classList.remove('is-animating');
        }
        if (video) {
          video.play().then(() => {
            updatePlayPauseState(true);
          }).catch(err => {
            console.warn('Auto-play prevented:', err);
            updatePlayPauseState(false);
            if (centerPlay) centerPlay.classList.add('is-visible');
          });
        }
      }, 1450);
    }

    function closeModal() {
      if (introTimer) clearTimeout(introTimer);
      if (video) {
        video.pause();
        video.currentTime = 0;
        video.src = '';
      }
      modal.classList.remove('is-active');
      modal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('uy-modal-open');
      if (intro) {
        intro.classList.remove('is-hidden', 'is-animating');
      }
      updatePlayPauseState(false);
    }

    function updatePlayPauseState(isPlaying) {
      if (playPauseBtn) {
        const icon = playPauseBtn.querySelector('i');
        if (icon) {
          icon.className = isPlaying ? 'fa-solid fa-pause' : 'fa-solid fa-play';
        }
      }
      if (centerPlay) {
        const centerIcon = centerPlay.querySelector('i');
        if (isPlaying) {
          centerPlay.classList.remove('is-visible');
          if (centerIcon) centerIcon.className = 'fa-solid fa-pause';
        } else {
          centerPlay.classList.add('is-visible');
          if (centerIcon) centerIcon.className = 'fa-solid fa-play';
        }
      }
    }

    function togglePlayPause() {
      if (!video) return;
      if (video.paused || video.ended) {
        if (video.ended) video.currentTime = 0;
        video.play().then(() => updatePlayPauseState(true)).catch(err => console.warn(err));
      } else {
        video.pause();
        updatePlayPauseState(false);
      }
    }

    // Attach click triggers to cards
    cards.forEach(card => {
      const visual = card.querySelector('.uy-visual');
      const name = card.dataset.storyName || 'Student';
      const videoSrc = card.dataset.storyVideo || '';

      function handleClick(e) {
        e.preventDefault();
        openModal(name, videoSrc);
      }

      if (visual) {
        visual.addEventListener('click', handleClick);
        visual.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            handleClick(e);
          }
        });
      }
    });

    // Close triggers
    if (backdrop) backdrop.addEventListener('click', closeModal);
    if (outerClose) outerClose.addEventListener('click', closeModal);
    if (innerClose) innerClose.addEventListener('click', closeModal);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('is-active')) {
        closeModal();
      }
    });

    // Play/Pause controls
    if (playPauseBtn) {
      playPauseBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        togglePlayPause();
      });
    }
    if (centerPlay) {
      centerPlay.addEventListener('click', (e) => {
        e.stopPropagation();
        togglePlayPause();
      });
    }
    if (video) {
      video.addEventListener('click', (e) => {
        e.stopPropagation();
        togglePlayPause();
      });
      video.addEventListener('timeupdate', () => {
        if (!video.duration) return;
        const pct = Math.min(100, Math.max(0, (video.currentTime / video.duration) * 100));
        if (trackFill) trackFill.style.width = `${pct}%`;
        if (trackKnob) trackKnob.style.left = `${pct}%`;
        if (track) track.setAttribute('aria-valuenow', Math.round(pct));
        if (timeText) {
          timeText.textContent = `${formatTime(video.currentTime)} / ${formatTime(video.duration)}`;
        }
      });
      video.addEventListener('loadedmetadata', () => {
        if (timeText) {
          timeText.textContent = `0:00 / ${formatTime(video.duration)}`;
        }
      });
      video.addEventListener('ended', () => {
        updatePlayPauseState(false);
        if (centerPlay) {
          centerPlay.classList.add('is-visible');
          const centerIcon = centerPlay.querySelector('i');
          if (centerIcon) centerIcon.className = 'fa-solid fa-rotate-right';
        }
      });
      video.addEventListener('play', () => updatePlayPauseState(true));
      video.addEventListener('pause', () => updatePlayPauseState(false));
    }

    // Time scrubber
    if (track) {
      track.addEventListener('click', (e) => {
        e.stopPropagation();
        const rect = track.getBoundingClientRect();
        const clientX = e.clientX || (e.touches && e.touches[0] ? e.touches[0].clientX : 0);
        const pos = Math.min(Math.max(0, clientX - rect.left), rect.width);
        const fraction = pos / rect.width;
        if (video && video.duration) {
          video.currentTime = fraction * video.duration;
        }
      });
    }

    // Mute toggle
    if (muteBtn && video) {
      muteBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        video.muted = !video.muted;
        const icon = muteBtn.querySelector('i');
        if (icon) {
          icon.className = video.muted ? 'fa-solid fa-volume-xmark' : 'fa-solid fa-volume-high';
        }
      });
    }
  }

  // Alias
  function initTestimonialsStories() {
    initStudentJourneyReelModal();
  }

  /* =====================================================
     HERO 3-FRIENDS CHAT CONTROLLER
     Infinite loop conversational speech bubbles directly above speakers
     ===================================================== */
  function initHeroDialogue() {
    const stage = document.getElementById('heroDialogueStage');
    if (!stage) return;

    const bubble3 = document.getElementById('bubbleSpeaker3');
    const bubble1 = document.getElementById('bubbleSpeaker1');
    const bubble2 = document.getElementById('bubbleSpeaker2');

    const text3 = document.getElementById('bubbleText3');
    const text1 = document.getElementById('bubbleText1');
    const text2 = document.getElementById('bubbleText2');

    if (!bubble3 || !bubble1 || !bubble2) return;

    // The 9 dialogue lines requested by the user:
    // Speaker 1: Middle girl (purple sweater)
    // Speaker 2: Right boy (green jacket)
    // Speaker 3: Left boy (glasses & headphones - guide)
    const DIALOGUE = [
      { speaker: 1, text: 'Fast Track abroad?', duration: 2400 },
      { speaker: 2, text: 'How does it work?', duration: 2400 },
      { speaker: 3, text: 'Start online in India.', duration: 2600 },
      { speaker: 1, text: 'For 8–12 months?', duration: 2400 },
      { speaker: 3, text: 'Then transfer abroad.', duration: 2600 },
      { speaker: 2, text: 'Lower study costs?', duration: 2400 },
      { speaker: 3, text: 'Save up to 50%*.', duration: 2600 },
      { speaker: 1, text: 'Who can guide us?', duration: 2400 },
      { speaker: 3, text: 'University Yatra', duration: 3400, isHighlight: true }
    ];

    let currentIndex = 0;
    let timer = null;
    let isPaused = false;

    function renderStep(index) {
      const item = DIALOGUE[index];

      // Deactivate all bubbles first
      bubble1.classList.remove('is-active');
      bubble2.classList.remove('is-active');
      bubble3.classList.remove('is-active', 'is-brand-highlight');

      requestAnimationFrame(() => {
        if (item.speaker === 1) {
          if (text1) text1.textContent = item.text;
          bubble1.classList.add('is-active');
        } else if (item.speaker === 2) {
          if (text2) text2.textContent = item.text;
          bubble2.classList.add('is-active');
        } else if (item.speaker === 3) {
          if (text3) text3.textContent = item.text;
          if (item.isHighlight) {
            bubble3.classList.add('is-brand-highlight');
          }
          bubble3.classList.add('is-active');
        }
      });
    }

    function scheduleNext() {
      if (timer) clearTimeout(timer);
      const currentItem = DIALOGUE[currentIndex];
      const duration = currentItem.duration || 2400;

      timer = setTimeout(() => {
        if (isPaused) return;
        currentIndex++;
        if (currentIndex >= DIALOGUE.length) {
          // Loop reset: fade out last message, pause gently, then start from beginning
          bubble1.classList.remove('is-active');
          bubble2.classList.remove('is-active');
          bubble3.classList.remove('is-active', 'is-brand-highlight');

          currentIndex = 0;
          timer = setTimeout(() => {
            if (!isPaused) {
              renderStep(currentIndex);
              scheduleNext();
            }
          }, 450);
        } else {
          renderStep(currentIndex);
          scheduleNext();
        }
      }, duration);
    }

    // Tap/click anywhere on stage to advance conversation immediately
    stage.addEventListener('click', () => {
      if (timer) clearTimeout(timer);
      currentIndex = (currentIndex + 1) % DIALOGUE.length;
      renderStep(currentIndex);
      scheduleNext();
    });

    // Handle tab visibility to avoid queuing animations
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        isPaused = true;
        if (timer) clearTimeout(timer);
      } else {
        isPaused = false;
        renderStep(currentIndex);
        scheduleNext();
      }
    });

    // Initial trigger
    renderStep(0);
    scheduleNext();
  }

  /* =====================================================
     SCROLL DIRECTION CONTROLLER
     Scroll DOWN -> Hide header (University Yatra) & Bottom Bar (Chat on WhatsApp)
     Scroll UP   -> Reveal header & Bottom Bar smoothly
     ===================================================== */
  function initScrollDirectionBars() {
    let lastScrollY = window.pageYOffset || document.documentElement.scrollTop || 0;
    let ticking = false;
    const threshold = 6;

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const currentScrollY = window.pageYOffset || document.documentElement.scrollTop || 0;
          const diff = currentScrollY - lastScrollY;

          if (currentScrollY <= 20) {
            // At top of page
            document.body.classList.remove('scroll-down');
          } else if (diff > threshold) {
            // User is scrolling DOWN
            document.body.classList.add('scroll-down');
          } else if (diff < -threshold) {
            // User is scrolling UP
            document.body.classList.remove('scroll-down');
          }

          lastScrollY = currentScrollY;
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  function initFooterLegalToggle() {
    const btn = document.getElementById('footerSeeMoreBtn');
    const disclaimer = document.getElementById('footerLegalDisclaimer');
    if (!btn || !disclaimer) return;

    const label = btn.querySelector('.footer-seemore-label');
    btn.addEventListener('click', () => {
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';
      const nextState = !isExpanded;
      btn.setAttribute('aria-expanded', String(nextState));
      disclaimer.hidden = !nextState;
      if (label) {
        label.textContent = nextState ? '( see less )' : '( see more )';
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initWizardController();
    initBottomEnquiry();
    initStickerSlapFooter();
    initPathwaysSlider();
    initTestimonialsStories();
    initHeroDialogue();
    initScrollDirectionBars();
    initFooterLegalToggle();
  });

})();
