import re

# ==============================================================================
# 1. UPDATE INDEX.HTML
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Sticky Mobile Bottom Bar: ONLY WHATSAPP BUTTON (Remove Get Free Guide)
old_mbar_pattern = re.compile(r'<div class="mbar">.*?</div>', re.DOTALL)
new_mbar = '''<div class="mbar">
    <a class="btn btn-wa btn-block" href="https://wa.me/919217368750?text=Hi%20University%20Yatra%2C%20I%20want%20to%20know%20more%20about%20study%20abroad%20programmes." target="_blank" rel="noopener">
      <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp with Counsellor
    </a>
  </div>'''
html = old_mbar_pattern.sub(new_mbar, html)

# Replace Calculator Section with the Step-by-Step Card having Previous and Continue buttons
calc_pattern = re.compile(r'<section class="calc-sec" id="calculator">.*?</section>', re.DOTALL)

new_calc_section = '''<section class="calc-sec" id="calculator">
      <div class="container" style="max-width:820px;padding:0 16px;">
        <!-- Clean, straight, aligned header -->
        <div class="sec-head" style="margin-bottom: 24px;text-align:center;margin-inline:auto;">
          <span class="sticker white">⚡ 30-Second Estimate · Free Country Handbook</span>
          <h2>Calculate Your Study Abroad Cost &amp; <span class="box">Get Free Guide</span></h2>
          <p class="lead" style="margin-inline:auto;">Select your destination, study level, and route to calculate your tuition, living expenses, and download the official 2026 country handbook.</p>
        </div>

        <!-- Step-by-Step Wizard Card -->
        <div class="calc-wizard-card" id="calcWizardCard">
          <!-- Wizard Header with Progress Bar -->
          <div class="wiz-header">
            <div class="wiz-progress-bar">
              <div class="wiz-progress-fill" id="wizProgressFill" style="width: 25%;"></div>
            </div>
            <div class="wiz-header-meta">
              <span class="wiz-step-indicator" id="wizStepIndicator">Step 1 of 4</span>
              <span class="badge" style="position:static;padding:3px 12px;font-size:0.75rem;">Takes 30 sec</span>
            </div>
          </div>

          <!-- STEP 1: DESTINATION -->
          <div class="wiz-step-pane" id="wizStep1">
            <div class="wiz-step-title">
              <span class="step-num">1</span>
              <div>
                <h3>Where do you want to study?</h3>
                <p>Select your target country to see real costs &amp; official handbook.</p>
              </div>
            </div>
            <div class="wiz-grid-countries">
              <button class="wiz-opt on" type="button" data-k="country" data-v="Canada">
                <span class="flag">🇨🇦</span>
                <span class="c-name">Canada</span>
                <span class="c-sub">PR &amp; Work Route</span>
              </button>
              <button class="wiz-opt" type="button" data-k="country" data-v="Germany">
                <span class="flag">🇩🇪</span>
                <span class="c-name">Germany</span>
                <span class="c-sub">Low Tuition &amp; ROI</span>
              </button>
              <button class="wiz-opt" type="button" data-k="country" data-v="United Kingdom">
                <span class="flag">🇬🇧</span>
                <span class="c-name">United Kingdom</span>
                <span class="c-sub">1-Year Master's</span>
              </button>
              <button class="wiz-opt" type="button" data-k="country" data-v="Australia">
                <span class="flag">🇦🇺</span>
                <span class="c-name">Australia</span>
                <span class="c-sub">Top Universities</span>
              </button>
              <button class="wiz-opt" type="button" data-k="country" data-v="USA">
                <span class="flag">🇺🇸</span>
                <span class="c-name">United States</span>
                <span class="c-sub">Global Campuses</span>
              </button>
              <button class="wiz-opt" type="button" data-k="country" data-v="France">
                <span class="flag">🇫🇷</span>
                <span class="c-name">France</span>
                <span class="c-sub">Affordable Degrees</span>
              </button>
              <button class="wiz-opt" type="button" data-k="country" data-v="Ireland">
                <span class="flag">🇮🇪</span>
                <span class="c-name">Ireland</span>
                <span class="c-sub">Tech Hub &amp; PSW</span>
              </button>
            </div>
          </div>

          <!-- STEP 2: STUDY LEVEL -->
          <div class="wiz-step-pane" id="wizStep2" style="display:none;">
            <div class="wiz-step-title">
              <span class="step-num">2</span>
              <div>
                <h3>What degree are you aiming for?</h3>
                <p>Select your intended qualification level.</p>
              </div>
            </div>
            <div class="wiz-grid-cards">
              <button class="wiz-opt on" type="button" data-k="level" data-v="Master's">
                <div class="opt-icon">📜</div>
                <div class="opt-body">
                  <strong>Master's Degree</strong>
                  <span>Postgraduate programmes for university graduates</span>
                </div>
              </button>
              <button class="wiz-opt" type="button" data-k="level" data-v="Bachelor's">
                <div class="opt-icon">🎓</div>
                <div class="opt-body">
                  <strong>Bachelor's Degree</strong>
                  <span>Undergraduate programmes after 12th standard</span>
                </div>
              </button>
              <button class="wiz-opt" type="button" data-k="level" data-v="MBA">
                <div class="opt-icon">💼</div>
                <div class="opt-body">
                  <strong>Global MBA</strong>
                  <span>Business management &amp; executive programmes</span>
                </div>
              </button>
            </div>
          </div>

          <!-- STEP 3: PATHWAY -->
          <div class="wiz-step-pane" id="wizStep3" style="display:none;">
            <div class="wiz-step-title">
              <span class="step-num">3</span>
              <div>
                <h3>Which study pathway fits your budget?</h3>
                <p>Compare full on-campus vs budget-smart credit transfer.</p>
              </div>
            </div>
            <div class="wiz-grid-cards">
              <button class="wiz-opt on" type="button" data-k="pathway" data-v="fast-track">
                <div class="opt-icon">⚡</div>
                <div class="opt-body">
                  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;">
                    <strong>Fast Track Pathway</strong>
                    <span class="badge-mini">SAVE UP TO 45%</span>
                  </div>
                  <span>Start Year 1 online in India, complete your degree at partner university abroad.</span>
                </div>
              </button>
              <button class="wiz-opt" type="button" data-k="pathway" data-v="direct">
                <div class="opt-icon">🏛️</div>
                <div class="opt-body">
                  <strong>Direct Study Abroad</strong>
                  <span>Apply directly and study on-campus overseas from semester one.</span>
                </div>
              </button>
            </div>
          </div>

          <!-- STEP 4: LIFESTYLE -->
          <div class="wiz-step-pane" id="wizStep4" style="display:none;">
            <div class="wiz-step-title">
              <span class="step-num">4</span>
              <div>
                <h3>What is your living style?</h3>
                <p>Choose your expected living and accommodation standard.</p>
              </div>
            </div>
            <div class="wiz-grid-cards">
              <button class="wiz-opt on" type="button" data-k="lifestyle" data-v="mid">
                <div class="opt-icon">😌</div>
                <div class="opt-body">
                  <strong>Moderate (Standard)</strong>
                  <span>Shared student housing, hostel, balanced groceries (1.0x living)</span>
                </div>
              </button>
              <button class="wiz-opt" type="button" data-k="lifestyle" data-v="lean">
                <div class="opt-icon">🥺</div>
                <div class="opt-body">
                  <strong>Budget / Lean</strong>
                  <span>Shared flat, home-cooked food, transit pass (0.9x living)</span>
                </div>
              </button>
              <button class="wiz-opt" type="button" data-k="lifestyle" data-v="plus">
                <div class="opt-icon">😎</div>
                <div class="opt-body">
                  <strong>Comfortable / Plus</strong>
                  <span>Private studio, prime central location, flexible living (1.2x living)</span>
                </div>
              </button>
            </div>
          </div>

          <!-- STEP 5: CALCULATED RESULT & GUIDE GATE -->
          <div class="wiz-step-pane" id="wizStepResult" style="display:none;">
            <div class="wiz-result-box">
              <div class="wiz-result-header">
                <span class="result-tag" id="rTag">Estimated Yearly Budget</span>
                <h3 id="rTitle" class="r-title" style="color:var(--lime);font-size:1.25rem;font-weight:800;margin:4px 0 10px;">🇨🇦 Canada · Master's · Fast Track (Yr 1)</h3>
              </div>

              <div class="result-total">
                <div id="rRange" class="big" style="color:#fff;font-size:clamp(2.2rem,5vw,3.2rem);font-weight:800;line-height:1;margin:6px 0 4px;">₹17.6L – ₹29.2L</div>
                <div class="per" style="color:#B6C3E6;font-size:0.88rem;margin-bottom:14px;">Estimated tuition + living per year (indicative)</div>
              </div>

              <div id="ftSavingsBadge" class="ft-savings-callout" style="display:flex;">
                <i class="fa-solid fa-bolt"></i> Fast Track saves approx. <strong>₹5.4L – ₹10.8L</strong> on Year 1 tuition!
              </div>

              <div class="break" style="border-top:1px dashed rgba(255,255,255,0.25);padding-top:12px;margin-bottom:16px;">
                <div style="display:flex;justify-content:space-between;padding:5px 0;color:#DCE5FA;font-size:0.92rem;">
                  <span>Tuition Fees (Year 1)</span>
                  <span id="rTuition" class="val" style="font-weight:700;color:#fff;">₹6.6L – ₹13.2L</span>
                </div>
                <div style="display:flex;justify-content:space-between;padding:5px 0;color:#DCE5FA;font-size:0.92rem;">
                  <span>Living &amp; Accommodation</span>
                  <span id="rLiving" class="val" style="font-weight:700;color:#fff;">₹11.0L – ₹16.0L</span>
                </div>
                <div style="display:flex;justify-content:space-between;padding:5px 0;color:#DCE5FA;font-size:0.92rem;">
                  <span>Visa, Insurance &amp; Travel (One-time)</span>
                  <span id="rOther" class="val" style="font-weight:700;color:#fff;">₹2.0L – ₹4.0L</span>
                </div>
              </div>

              <!-- Instant Free PDF Download Action -->
              <button class="btn btn-lime btn-block" id="calcDownloadPdfBtn" type="button" style="margin:12px 0 16px;font-size:1.02rem;">
                <i class="fa-solid fa-file-arrow-down"></i> Download Free Canada Guide (PDF) ↓
              </button>

              <!-- In-Card Lead Form (3 Fields ONLY: Name, Mobile, Email) -->
              <div class="calc-lead-gate" style="margin-top:16px;padding-top:16px;border-top:1px dashed rgba(255,255,255,0.25);">
                <p style="font-size:0.88rem;color:#DCE5FA;margin-bottom:12px;font-weight:600;">
                  Want this personalized cost sheet &amp; admission checklist sent to WhatsApp?
                </p>
                <form id="calcQuickLeadForm" class="form" style="display:grid;gap:10px;">
                  <input class="fi" name="name" id="calc_name" placeholder="Full Name" required autocomplete="name" style="background:rgba(255,255,255,0.08);color:#fff;border-color:rgba(255,255,255,0.3);" />
                  <div class="ph">
                    <span style="background:var(--lime);color:var(--ink);font-weight:800;border:var(--b);border-right:0;">+91</span>
                    <input class="fi" name="phone" id="calc_phone" type="tel" inputmode="numeric" pattern="[0-9]{10}" maxlength="10" placeholder="10-digit Mobile Number" required style="background:rgba(255,255,255,0.08);color:#fff;border-color:rgba(255,255,255,0.3);border-radius:0 14px 14px 0;" />
                  </div>
                  <input class="fi" name="email" id="calc_email" type="email" placeholder="Email Address" required autocomplete="email" style="background:rgba(255,255,255,0.08);color:#fff;border-color:rgba(255,255,255,0.3);" />
                  <button class="btn btn-primary btn-block" type="submit" id="calcQuickSubmitBtn" style="padding:14px;">
                    Send Guide to WhatsApp <i class="fa-solid fa-paper-plane"></i>
                  </button>
                </form>
                <div id="calcQuickSuccess" style="display:none;background:rgba(200,255,62,0.15);border:2px solid var(--lime);border-radius:14px;padding:14px;text-align:center;margin-top:10px;">
                  <strong style="color:var(--lime);display:block;margin-bottom:4px;">✓ Guide Sent &amp; Downloaded!</strong>
                  <p style="font-size:0.82rem;color:#DCE5FA;margin:0;">A senior counsellor will connect with you on WhatsApp shortly.</p>
                </div>
              </div>

              <p class="disc" style="margin-top:14px;font-size:0.75rem;color:#9FB0D8;line-height:1.4;">
                *Indicative planning ranges in ₹ (L = lakh). Actual expenses depend on university, course, city and foreign exchange rates.
              </p>
            </div>
          </div>

          <!-- Wizard Navigation Footer (Previous and Continue Buttons) -->
          <div class="wiz-nav-footer">
            <button class="btn wiz-prev-btn" id="wizPrevBtn" type="button" style="visibility:hidden;">
              <i class="fa-solid fa-arrow-left"></i> Previous
            </button>
            <button class="btn btn-primary wiz-next-btn" id="wizNextBtn" type="button">
              Continue <i class="fa-solid fa-arrow-right"></i>
            </button>
          </div>
        </div>
      </div>
    </section>'''

html = calc_pattern.sub(new_calc_section, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html: step-by-step wizard card & single WhatsApp sticky button!')


# ==============================================================================
# 2. UPDATE CSS/STYLES.CSS (FIX OVERFLOW, RESPONSIVE WIZARD, CLEAN ALIGNMENT)
# ==============================================================================
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add complete clean styles for the step-by-step wizard
wizard_css_rules = '''
/* =====================================================
   STEP-BY-STEP WIZARD CALCULATOR (RESPONSIVE & MOBILE-FIRST)
   ===================================================== */
.calc-wizard-card {
  background: #fff;
  border: var(--b);
  border-radius: 24px;
  box-shadow: var(--sh);
  padding: 28px;
  max-width: 720px;
  margin: 0 auto;
  box-sizing: border-box;
  width: 100%;
}

.wiz-header {
  margin-bottom: 20px;
}

.wiz-progress-bar {
  width: 100%;
  height: 8px;
  background: #E8EEFB;
  border-radius: 99px;
  overflow: hidden;
  border: 1.5px solid var(--ink);
  margin-bottom: 10px;
}

.wiz-progress-fill {
  height: 100%;
  background: var(--blue);
  border-radius: 99px;
  transition: width 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.wiz-header-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.wiz-step-indicator {
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.84rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.wiz-step-pane {
  animation: fadeIn 0.25s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.wiz-step-title {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 18px;
}

.wiz-step-title h3 {
  font-size: 1.25rem;
  line-height: 1.2;
  margin-bottom: 4px;
  color: var(--ink);
}

.wiz-step-title p {
  font-size: 0.88rem;
  color: var(--muted);
  line-height: 1.4;
}

.wiz-grid-countries {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-bottom: 20px;
}

.wiz-opt {
  border: var(--b);
  border-radius: 14px;
  background: #fff;
  padding: 12px 14px;
  box-shadow: 2px 2px 0 var(--ink);
  cursor: pointer;
  transition: all 0.15s ease;
  text-align: left;
  display: flex;
  flex-direction: column;
  gap: 2px;
  box-sizing: border-box;
  width: 100%;
  color: var(--ink);
}

.wiz-opt:hover {
  background: var(--cream);
  transform: translateY(-2px);
  box-shadow: 4px 4px 0 var(--ink);
}

.wiz-opt:active {
  transform: translateY(1px);
  box-shadow: 1px 1px 0 var(--ink);
}

.wiz-opt.on {
  background: var(--blue);
  color: #fff;
  box-shadow: 3px 3px 0 var(--ink);
  border-color: var(--ink);
}

.wiz-opt.on .c-sub,
.wiz-opt.on span,
.wiz-opt.on .opt-body span {
  color: #DCE8FF;
}

.wiz-opt .flag {
  font-size: 1.4rem;
  line-height: 1;
  margin-bottom: 4px;
}

.wiz-opt .c-name {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 1.05rem;
  line-height: 1.2;
}

.wiz-opt .c-sub {
  font-size: 0.74rem;
  color: var(--muted);
  line-height: 1.3;
}

.wiz-grid-cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  margin-bottom: 20px;
}

.wiz-grid-cards .wiz-opt {
  flex-direction: row;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
}

.opt-icon {
  font-size: 1.6rem;
  line-height: 1;
  flex-shrink: 0;
}

.opt-body {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.opt-body strong {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.05rem;
  font-weight: 800;
}

.opt-body span {
  font-size: 0.82rem;
  color: var(--muted);
  line-height: 1.35;
}

.badge-mini {
  display: inline-block;
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.68rem;
  background: var(--lime);
  color: var(--ink);
  padding: 2px 7px;
  border-radius: 99px;
  border: 1.5px solid var(--ink);
}

.wiz-result-box {
  background: var(--ink);
  color: #fff;
  border-radius: 18px;
  padding: 22px;
  box-shadow: 4px 4px 0 var(--ink);
  margin-bottom: 20px;
}

.wiz-nav-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-top: 16px;
  border-top: 1.5px solid rgba(10, 18, 48, 0.12);
}

.wiz-prev-btn {
  font-size: 0.92rem;
  padding: 11px 18px;
  background: #fff;
  color: var(--ink);
}

.wiz-next-btn {
  font-size: 0.95rem;
  padding: 12px 24px;
  margin-left: auto;
}

/* Mobile responsive constraints */
@media (max-width: 600px) {
  .calc-wizard-card {
    padding: 18px 14px;
    border-radius: 18px;
    box-shadow: 4px 4px 0 var(--ink);
  }
  .wiz-grid-countries {
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
  }
  .wiz-opt {
    padding: 10px 10px;
  }
  .wiz-opt .c-name {
    font-size: 0.95rem;
  }
  .wiz-opt .c-sub {
    font-size: 0.7rem;
  }
  .wiz-grid-cards .wiz-opt {
    padding: 12px 14px;
    gap: 10px;
  }
  .opt-body strong {
    font-size: 0.96rem;
  }
  .opt-body span {
    font-size: 0.78rem;
  }
  .wiz-result-box {
    padding: 16px 12px;
  }
  .wiz-prev-btn {
    padding: 10px 14px;
    font-size: 0.86rem;
  }
  .wiz-next-btn {
    padding: 11px 18px;
    font-size: 0.88rem;
  }
  .mbar {
    padding: 10px 14px;
  }
  .mbar .btn-wa {
    font-size: 0.95rem;
    padding: 14px 18px;
  }
}
'''

if '/* =====================================================\n   STEP-BY-STEP WIZARD CALCULATOR' not in css:
    css += wizard_css_rules
else:
    css = re.sub(r'/\* =====================================================\n   STEP-BY-STEP WIZARD CALCULATOR.*', wizard_css_rules, css, flags=re.DOTALL)

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated css/styles.css with mobile-first step-by-step styles!')


# ==============================================================================
# 3. UPDATE JS/MAIN.JS (STEP-BY-STEP PREV / CONTINUE CONTROLLER)
# ==============================================================================
wizard_js = '''/**
 * University Yatra — Study Abroad Landing Page
 * Step-by-Step Calculator & Official Country Guide Controller
 * Features Prev/Continue navigation, zero UI jump, authentic costs & PDF downloads
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
  const totalSteps = 4;

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
      if (stepIndicator) stepIndicator.textContent = 'Results Ready';
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

    if (rTitle) rTitle.textContent = `${data.flag} ${S.country} · ${S.level} · ${pathwayLabel}`;
    if (rRange) rRange.textContent = rngLakh(totalRange);
    if (rTuition) rTuition.textContent = rngLakh(tCalc);
    if (rLiving) rLiving.textContent = rngLakh(lCalc);
    if (rOther) rOther.textContent = rngLakh(data.other);

    // Fast Track Savings Badge
    if (ftBadge) {
      if (isFT) {
        const savedMin = tBase[0] * 0.45;
        const savedMax = tBase[1] * 0.45;
        ftBadge.style.display = 'flex';
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
        if (key && val) S[key] = val;
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

        if (!/^[6-9][0-9]{9}$/.test(phone)) {
          alert('Please enter a valid 10-digit Indian WhatsApp number');
          return;
        }

        const btn = $('calcQuickSubmitBtn');
        if (btn) {
          btn.disabled = true;
          btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending Guide...';
        }

        const data = D[S.country] || D['Canada'];
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
    f.write(wizard_js)

print('Updated js/main.js with step-by-step navigation controller!')

