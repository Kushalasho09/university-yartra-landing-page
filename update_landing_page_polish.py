import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Hero trust section to match Image 5
old_hero_trust = '''          <div class="hero-trust">
            <span><i class="fa-solid fa-circle-check"></i> 100% Free Guidance</span>
            <span><i class="fa-solid fa-circle-check"></i> Top Global Universities</span>
            <span class="stamp-badge"><i class="fa-solid fa-stamp"></i> VISA APPROVED 2026</span>
          </div>'''

new_hero_trust = '''          <div class="hero-trust">
            <span><i class="fa-solid fa-circle-check" style="color:var(--blue)"></i> 100% Free Guidance</span>
            <span><i class="fa-solid fa-circle-check" style="color:var(--blue)"></i> Top Global Universities</span>
            <span><i class="fa-solid fa-circle-check" style="color:var(--blue)"></i> Fast-Track Credit Transfer</span>
          </div>'''

if old_hero_trust in html:
    html = html.replace(old_hero_trust, new_hero_trust)

# Replace Fast Track card to match Image 1
fast_track_pattern = re.compile(
    r'<div class="path fast">.*?</div>\s*</div>\s*</div>\s*</section>',
    re.DOTALL
)

new_fast_track_section = '''<div class="path fast">
            <span class="sticker sun">BUDGET-SMART PATHWAY</span>
            <span class="eyebrow" style="color:var(--lime);font-size:0.8rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px;display:block;">SMART CREDIT TRANSFER</span>
            <h3>FAST TRACK STUDY ABROAD</h3>
            <p style="font-weight:700;margin-bottom:6px;color:#fff;">Complete the Initial Study Phase in India. Continue Abroad.</p>
            <p style="color:#fff;opacity:0.95;margin-bottom:16px;">Start selected programmes online in India for approximately 8–12 months, then continue your degree at a partner university abroad, subject to eligibility and credit-transfer approval.</p>
            <ul>
              <li>Begin your selected programme online in India.</li>
              <li>Complete the required academic phase.</li>
              <li>Transfer eligible credits and continue abroad.</li>
            </ul>
            <p class="best">
              <strong>Best if:</strong> you want to save up to 45% on overall expenses, build your academic profile, or need a flexible start.
            </p>
            <a href="#calculator" class="btn btn-lime">View Fast Track Programmes</a>
            <p class="fine">*Credit-transfer terms and eligibility vary by programme and partner university.</p>
          </div>
        </div>
      </div>
    </section>'''

html = fast_track_pattern.sub(new_fast_track_section, html)

# Replace Direct card to be clean and aligned
direct_card_pattern = re.compile(
    r'<div class="path">\s*<div class="path-header">.*?</div>\s*<h3>DIRECT STUDY ABROAD</h3>',
    re.DOTALL
)
new_direct_head = '''<div class="path">
            <span class="eyebrow" style="color:var(--blue);font-size:0.8rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px;display:block;">ON-CAMPUS OVERSEAS</span>
            <h3>DIRECT STUDY ABROAD</h3>'''
html = direct_card_pattern.sub(new_direct_head, html)

# Replace Calculator section with unified Image 3, 4, 7 experience
calc_section_pattern = re.compile(
    r'<section class="calc-sec" id="calculator">.*?</section>',
    re.DOTALL
)

new_calc_section = '''<section class="calc-sec" id="calculator">
      <div class="container">
        <!-- Section Heading matching Image 3 & Image 4 -->
        <div class="sec-head" style="margin-bottom: 24px;">
          <span class="sticker">Free country guide · 4 quick taps</span>
          <h2>Know your study cost. <span class="box">Download</span> your free guide.</h2>
          <p class="lead">Tap your country and course. Get a free guide with real costs, the full admission flow, exams, visa and life abroad.</p>
        </div>

        <!-- Mode Switcher -->
        <div style="display:flex;justify-content:center;margin-bottom:28px;">
          <div class="calc-mode-switcher">
            <button type="button" class="mode-btn on" id="btnMode2Col"><i class="fa-solid fa-sliders"></i> Interactive Cost Estimator</button>
            <button type="button" class="mode-btn" id="btnModeWizard"><i class="fa-solid fa-list-check"></i> 4-Tap Guide Wizard</button>
          </div>
        </div>

        <!-- VIEW 1: Two-Column Live Calculator (Matches Image 7) -->
        <div class="calc-two-col" id="view2Col">
          <!-- Left Options Box -->
          <div class="calc-box">
            <span class="badge">Takes 30 sec</span>

            <div class="opt-label">1. Where to?</div>
            <div class="opts" data-k="country">
              <button class="opt" type="button" data-v="Germany">🇩🇪 Germany</button>
              <button class="opt" type="button" data-v="France">🇫🇷 France</button>
              <button class="opt" type="button" data-v="United Kingdom">🇬🇧 UK</button>
              <button class="opt" type="button" data-v="Ireland">🇮🇪 Ireland</button>
              <button class="opt" type="button" data-v="Australia">🇦🇺 Australia</button>
              <button class="opt on" type="button" data-v="Canada">🇨🇦 Canada</button>
              <button class="opt" type="button" data-v="USA">🇺🇸 USA</button>
            </div>

            <div class="opt-label">2. Level</div>
            <div class="opts" data-k="level">
              <button class="opt" type="button" data-v="Bachelor's">Bachelor's</button>
              <button class="opt" type="button" data-v="Master's">Master's</button>
              <button class="opt on" type="button" data-v="MBA">MBA</button>
            </div>

            <div class="opt-label">3. Pathway</div>
            <div class="opts" data-k="pathway">
              <button class="opt" type="button" data-v="direct">Direct</button>
              <button class="opt on" type="button" data-v="fast-track">Fast Track</button>
            </div>

            <div class="opt-label">4. Lifestyle</div>
            <div class="opts" data-k="lifestyle">
              <button class="opt" type="button" data-v="lean">Budget 🥺</button>
              <button class="opt" type="button" data-v="mid">Moderate 😌</button>
              <button class="opt on" type="button" data-v="plus">Comfy 😎</button>
            </div>
          </div>

          <!-- Right Result Box -->
          <div class="result">
            <div id="rTitle" class="r-title">Canada · MBA · Fast Track (Yr 1)</div>
            <div id="rRange" class="big">₹23.1L – ₹38.5L</div>
            <div class="per">per year · tuition + living · indicative</div>

            <div class="break">
              <div>
                <span>Tuition</span>
                <span id="rTuition" class="val">₹9.9L – ₹19.3L</span>
              </div>
              <div>
                <span>Living &amp; stay</span>
                <span id="rLiving" class="val">₹13.2L – ₹19.2L</span>
              </div>
              <div>
                <span>Visa, insurance, travel (one-time)</span>
                <span id="rOther" class="val">₹2L – ₹4L</span>
              </div>
            </div>

            <button class="btn btn-lime btn-block" id="calcDownloadPdfBtn" type="button" style="margin-top:14px;font-size:1.05rem;">
              Get my detailed cost guide →
            </button>

            <p class="disc">
              Indicative ranges in ₹ (L = lakh) for planning only. Actual costs vary by university, course, city and exchange rate. Your counsellor shares a verified breakdown.
            </p>
          </div>
        </div>

        <!-- VIEW 2: 4-Tap Wizard (Matches Image 2 & Image 4) -->
        <div class="wizard-wrap" id="viewWizard" style="display:none;max-width:760px;margin:0 auto;">
          <div class="wizard-box" id="wizardBox">
            <span class="badge">Takes 30 sec</span>
            <div class="wizard-top">
              <button class="wizard-back" id="wizBackBtn" type="button" aria-label="Go back" hidden>←</button>
              <div class="wizard-dots" id="wizDots"><i class="on"></i><i></i><i></i><i></i></div>
              <span class="wizard-stepno" id="wizStepNo">1/4</span>
            </div>
            <div class="wizard-crumbs" id="wizCrumbs"></div>
            <div id="wizStepView"></div>

            <div class="wizard-gate" id="wizGateView" hidden>
              <div id="wizGateForm">
                <span class="tick" style="display:inline-grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--lime);border:var(--b);font-weight:800;margin-bottom:12px;">✓</span>
                <div class="wizard-q" id="wizGateTitle">Your guide is ready.</div>
                <p class="wizard-qsub" id="wizGateSub">Enter your details to download it free.</p>
                <form class="form" id="wizLeadForm" style="display:grid;gap:12px;margin-top:10px;">
                  <input type="hidden" name="country" id="wiz_country">
                  <input type="hidden" name="level" id="wiz_level">
                  <input type="hidden" name="pathway" id="wiz_path">
                  <input type="hidden" name="timeline" id="wiz_time">
                  <input class="fi" name="name" id="wiz_name" placeholder="Your name" required autocomplete="name">
                  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;" class="wiz-r2">
                    <div class="phone" style="display:flex;">
                      <span style="padding:12px 14px;border:var(--b);border-right:0;border-radius:14px 0 0 14px;background:var(--lime);font-weight:800;display:grid;place-items:center;">+91</span>
                      <input class="fi" name="phone" id="wiz_phone" type="tel" inputmode="numeric" pattern="[0-9]{10}" maxlength="10" placeholder="WhatsApp number" required style="border-radius:0 14px 14px 0;">
                    </div>
                    <input class="fi" name="email" id="wiz_email" type="email" placeholder="Email address" required autocomplete="email">
                  </div>
                  <button class="btn btn-primary btn-block" type="submit" id="wizGateBtn" style="padding:15px;margin-top:4px;">Download free PDF guide ↓</button>
                  <p style="font-size:0.75rem;color:var(--muted);line-height:1.45;margin-top:4px;">
                    By continuing you agree to be contacted by University Yatra via call, SMS, email and WhatsApp. We never sell your data. <a href="#" style="text-decoration:underline;color:var(--blue);">Privacy Policy</a>
                  </p>
                </form>
              </div>

              <div class="wizard-done" id="wizDoneView" style="display:none;text-align:center;padding:12px 0;">
                <span class="tick" style="display:inline-grid;place-items:center;width:48px;height:48px;border-radius:50%;background:var(--lime);border:var(--b);font-weight:800;margin:0 auto 12px;font-size:1.4rem;">✓</span>
                <div class="wizard-q" id="wizDoneTitle">Done! Check your downloads.</div>
                <p class="wizard-qsub" id="wizDoneSub">Your guide should download automatically. If not, tap below.</p>
                <div id="wizDlContainer" style="margin:16px 0;"></div>
                <a id="wizWaBtn" class="btn btn-wa btn-block" href="https://wa.me/919217368750" target="_blank" rel="noopener">
                  <i class="fa-brands fa-whatsapp"></i> Talk to a counsellor on WhatsApp
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''

html = calc_section_pattern.sub(new_calc_section, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('index.html updated successfully!')

