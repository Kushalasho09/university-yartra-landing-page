import re

# ==============================================================================
# 1. UPDATE CSS (REDUCE UNUSED SPACES, FIX SECTION COLLAPSE, PERFECT ALIGNMENT)
# ==============================================================================
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Reduce unused spaces across the web
# General section padding
css = re.sub(
    r'section\s*\{\s*padding:\s*\d+px\s*0;\s*\}',
    '''section {
  padding: 52px 0;
}
@media (max-width: 768px) {
  section {
    padding: 32px 0;
  }
}''',
    css
)

# Calc section padding (was 80px, reduce dead yellow void)
css = re.sub(
    r'\.calc-sec\s*\{[^}]*\}',
    '''.calc-sec {
  background: var(--sun);
  border-block: var(--b);
  padding: 44px 0 52px;
  position: relative;
}
@media (max-width: 768px) {
  .calc-sec {
    padding: 26px 0 34px;
  }
}''',
    css
)

# Sec-head margin-bottom (reduce dead space)
css = re.sub(
    r'\.sec-head\s*\{[^}]*\}',
    '''.sec-head {
  max-width: 760px;
  margin-bottom: 24px;
}
@media (max-width: 768px) {
  .sec-head {
    margin-bottom: 16px;
  }
  .sec-head h2 {
    font-size: 1.75rem;
    line-height: 1.15;
  }
  .sec-head p.lead {
    font-size: 0.95rem;
    margin-top: 8px;
  }
}''',
    css
)

# Add custom styles for the 5 fixes
additions = '''
/* =====================================================
   FIXES FOR THE 5 USER REPORTED ISSUES
   ===================================================== */

/* 1. Badge-mini contrast fix (Image 3) */
.badge-mini {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.78rem;
  background: var(--lime);
  color: #0A1230;
  padding: 3px 9px;
  border-radius: 99px;
  border: 1.5px solid #0A1230;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  flex-shrink: 0;
}

/* 2. Fast Track Savings Box Contrast & Legibility Fix (Image 4) */
.ft-savings-callout {
  background: var(--lime);
  color: #0A1230;
  border: 2px solid #0A1230;
  border-radius: 12px;
  padding: 10px 14px;
  font-size: 0.9rem;
  font-weight: 800;
  line-height: 1.35;
  margin-bottom: 14px;
  box-shadow: 2px 2px 0 #0A1230;
  display: block;
  text-align: left;
}
.ft-savings-callout strong {
  text-decoration: underline;
}

/* 3. Breakdown table alignment fix (Image 4 - No more 2-line wrapped numbers) */
.wiz-break-table {
  border-top: 1px dashed rgba(255, 255, 255, 0.25);
  padding-top: 12px;
  margin-bottom: 14px;
}

.wiz-break-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
  padding: 6px 0;
  font-size: 0.92rem;
}

.wiz-break-label {
  flex: 1;
  color: #DCE5FA;
  line-height: 1.35;
}

.wiz-break-val {
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.98rem;
  color: #fff;
  white-space: nowrap;
  flex-shrink: 0;
  text-align: right;
}

/* 4. Perfect In-Card Form Field Alignments & Country Dropdowns (Image 5) */
.field-wrap {
  display: flex;
  flex-direction: column;
  gap: 4px;
  text-align: left;
}

.field-label {
  font-size: 0.76rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #B6C3E6;
}

.phone-group {
  display: flex;
  align-items: stretch;
  border: 2px solid rgba(255, 255, 255, 0.25);
  border-radius: 12px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.08);
  height: 50px;
  box-sizing: border-box;
}

.phone-group:focus-within {
  border-color: var(--lime);
  background: rgba(255, 255, 255, 0.12);
}

.phone-code-select {
  border: none;
  border-right: 2px solid rgba(255, 255, 255, 0.25);
  background: var(--lime);
  color: #0A1230;
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.9rem;
  padding: 0 10px;
  cursor: pointer;
  height: 100%;
  border-radius: 0;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%230A1230'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 8px center;
  padding-right: 22px;
}

.fi-phone {
  border: none !important;
  background: transparent !important;
  color: #fff !important;
  font-size: 16px !important;
  padding: 0 14px !important;
  width: 100% !important;
  height: 100% !important;
  outline: none !important;
}

.fi-dark {
  height: 50px !important;
  border: 2px solid rgba(255, 255, 255, 0.25) !important;
  border-radius: 12px !important;
  background: rgba(255, 255, 255, 0.08) !important;
  color: #fff !important;
  font-size: 16px !important;
  padding: 0 14px !important;
  box-sizing: border-box !important;
  width: 100% !important;
  outline: none !important;
}

.fi-dark:focus {
  border-color: var(--lime) !important;
  background: rgba(255, 255, 255, 0.12) !important;
}

.fi-select-dark {
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M0 0l6 8 6-8z' fill='%23C8FF3E'/%3E%3C/svg%3E") !important;
  background-repeat: no-repeat !important;
  background-position: right 14px center !important;
  padding-right: 36px !important;
  cursor: pointer;
}

.fi-select-dark option {
  background: #0A1230;
  color: #fff;
}
'''

if '/* =====================================================\n   FIXES FOR THE 5 USER REPORTED ISSUES' not in css:
    css += additions
else:
    css = re.sub(
        r'/\* =====================================================\n   FIXES FOR THE 5 USER REPORTED ISSUES.*',
        additions,
        css,
        flags=re.DOTALL
    )

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated css/styles.css successfully with spacing and alignment fixes!')


# ==============================================================================
# 2. UPDATE INDEX.HTML (REMOVE PADDING-TOP:0 COLLAPSE, FIX FORM & WIZARD)
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 2: Remove collapsing 'style="padding-top:0"' from all sections
html = re.sub(r'<section class="section" id="post-study" style="padding-top:0">', '<section class="section" id="post-study">', html)
html = re.sub(r'<section class="section" id="destinations" style="padding-top:0">', '<section class="section" id="destinations">', html)
html = re.sub(r'<section class="section" id="support" style="padding-top:0">', '<section class="section" id="support">', html)
html = re.sub(r'<section class="section" id="testimonials" style="padding-top:0">', '<section class="section" id="testimonials">', html)
html = re.sub(r'<section class="section" id="faqs" style="padding-top:0">', '<section class="section" id="faqs">', html)

# Fix 3, 4, 5: Update the Calculator Section HTML with the improved, clean Step 3, Step 4, Step 5 result, country dropdown, and form
calc_pattern = re.compile(r'<section class="calc-sec" id="calculator">.*?</section>', re.DOTALL)

new_calc_section = '''<section class="calc-sec" id="calculator">
      <div class="container" style="max-width:820px;padding:0 16px;">
        <!-- Clean, straight, well-spaced header -->
        <div class="sec-head" style="text-align:center;margin-inline:auto;">
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
                  <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:4px;">
                    <strong style="font-size:1.06rem;">Fast Track Pathway</strong>
                    <span class="badge-mini">⚡ SAVE UP TO 45%</span>
                  </div>
                  <span>Start Year 1 online in India, complete remaining degree at partner university abroad.</span>
                </div>
              </button>
              <button class="wiz-opt" type="button" data-k="pathway" data-v="direct">
                <div class="opt-icon">🏛️</div>
                <div class="opt-body">
                  <strong style="font-size:1.06rem;margin-bottom:4px;display:block;">Direct Study Abroad</strong>
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

          <!-- STEP 5: CALCULATED RESULT & GUIDE GATE (Clean alignment, high contrast) -->
          <div class="wiz-step-pane" id="wizStepResult" style="display:none;">
            <div class="wiz-result-box">
              <div class="wiz-result-header" style="margin-bottom:10px;">
                <span class="result-tag" id="rTag" style="display:inline-block;font-size:0.75rem;font-weight:800;letter-spacing:0.08em;text-transform:uppercase;color:#8DB3FF;margin-bottom:4px;">Estimated Yearly Budget</span>
                <h3 id="rTitle" class="r-title" style="color:var(--lime);font-size:1.25rem;font-weight:800;margin:0 0 6px;">🇨🇦 Canada · Master's · Fast Track (Yr 1)</h3>
              </div>

              <div class="result-total" style="margin-bottom:12px;">
                <div id="rRange" class="big" style="color:#fff;font-size:clamp(2.2rem,5vw,3.2rem);font-weight:800;line-height:1;margin:4px 0 2px;">₹17.6L – ₹29.2L</div>
                <div class="per" style="color:#B6C3E6;font-size:0.86rem;">Estimated tuition + living per year (indicative)</div>
              </div>

              <!-- High Contrast, Legible Savings Callout (Fix 3 & 4) -->
              <div id="ftSavingsBadge" class="ft-savings-callout">
                <i class="fa-solid fa-bolt"></i> Fast Track saves approx. <strong>₹5.4L – ₹10.8L</strong> on Year 1 tuition!
              </div>

              <!-- Clean Breakdown Table with Non-Wrapping Figures (Fix 4) -->
              <div class="wiz-break-table">
                <div class="wiz-break-row">
                  <span class="wiz-break-label">Tuition Fees (Year 1)</span>
                  <span id="rTuition" class="wiz-break-val">₹6.6L – ₹13.2L</span>
                </div>
                <div class="wiz-break-row">
                  <span class="wiz-break-label">Living &amp; Accommodation</span>
                  <span id="rLiving" class="wiz-break-val">₹11.0L – ₹16.0L</span>
                </div>
                <div class="wiz-break-row">
                  <span class="wiz-break-label">Visa, Insurance &amp; Travel (One-time)</span>
                  <span id="rOther" class="wiz-break-val">₹2.0L – ₹4.0L</span>
                </div>
              </div>

              <!-- Instant Free PDF Download Button -->
              <button class="btn btn-lime btn-block" id="calcDownloadPdfBtn" type="button" style="margin:10px 0 16px;padding:14px;font-size:1rem;font-weight:800;">
                <i class="fa-solid fa-file-arrow-down"></i> Download Free Canada Guide (PDF) ↓
              </button>

              <!-- In-Card Lead Form (Fix 5: Functional Country Dropdown + Phone Code Dropdown + Unified Alignments) -->
              <div class="calc-lead-gate" style="margin-top:14px;padding-top:14px;border-top:1px dashed rgba(255,255,255,0.25);">
                <p style="font-size:0.88rem;color:#DCE5FA;margin-bottom:12px;font-weight:600;">
                  Want this personalized cost sheet &amp; admission checklist sent to WhatsApp?
                </p>
                <form id="calcQuickLeadForm" class="form" style="display:grid;gap:10px;">
                  <div class="field-wrap">
                    <label class="field-label" for="calc_name">Full Name</label>
                    <input class="fi-dark" name="name" id="calc_name" placeholder="Enter your full name" required autocomplete="name" />
                  </div>

                  <div class="field-wrap">
                    <label class="field-label" for="calc_country_select">Preferred Study Country</label>
                    <select class="fi-dark fi-select-dark" name="country" id="calc_country_select" required>
                      <option value="Canada" selected>🇨🇦 Canada</option>
                      <option value="Germany">🇩🇪 Germany</option>
                      <option value="United Kingdom">🇬🇧 United Kingdom</option>
                      <option value="Australia">🇦🇺 Australia</option>
                      <option value="USA">🇺🇸 United States</option>
                      <option value="France">🇫🇷 France</option>
                      <option value="Ireland">🇮🇪 Ireland</option>
                    </select>
                  </div>

                  <div class="field-wrap">
                    <label class="field-label" for="calc_phone">WhatsApp Mobile Number</label>
                    <div class="phone-group">
                      <select class="phone-code-select" id="calc_phone_code" name="phone_code" aria-label="Country Code">
                        <option value="+91" selected>🇮🇳 +91</option>
                        <option value="+1">🇺🇸 +1</option>
                        <option value="+44">🇬🇧 +44</option>
                        <option value="+61">🇦🇺 +61</option>
                        <option value="+49">🇩🇪 +49</option>
                        <option value="+971">🇦🇪 +971</option>
                        <option value="+65">🇸🇬 +65</option>
                      </select>
                      <input class="fi-phone" name="phone" id="calc_phone" type="tel" inputmode="numeric" pattern="[0-9]{7,12}" maxlength="10" placeholder="10-digit mobile number" required />
                    </div>
                  </div>

                  <div class="field-wrap">
                    <label class="field-label" for="calc_email">Email Address</label>
                    <input class="fi-dark" name="email" id="calc_email" type="email" placeholder="name@example.com" required autocomplete="email" />
                  </div>

                  <button class="btn btn-primary btn-block" type="submit" id="calcQuickSubmitBtn" style="padding:14px;margin-top:4px;font-size:0.98rem;">
                    Send Guide to WhatsApp <i class="fa-solid fa-paper-plane"></i>
                  </button>
                </form>

                <div id="calcQuickSuccess" style="display:none;background:rgba(200,255,62,0.15);border:2px solid var(--lime);border-radius:12px;padding:12px;text-align:center;margin-top:10px;">
                  <strong style="color:var(--lime);display:block;margin-bottom:4px;">✓ Guide Sent &amp; Downloaded!</strong>
                  <p style="font-size:0.82rem;color:#DCE5FA;margin:0;">A senior counsellor will connect with you on WhatsApp shortly.</p>
                </div>
              </div>

              <p class="disc" style="margin-top:12px;font-size:0.75rem;color:#9FB0D8;line-height:1.4;">
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

print('Updated index.html: section padding collapse fixed, form alignment & country dropdown added!')

