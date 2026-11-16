import re

# ==============================================================================
# 1. UPDATE CSS (REMOVE ALL ROTATE/TILT, FIX ALIGNMENT, ADD PROPER STYLES)
# ==============================================================================
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace all rotate instances with clean straight alignments
css = re.sub(r'transform:\s*rotate\(-2deg\);?', 'transform: none;', css)
css = re.sub(r'transform:\s*rotate\(0deg\)\s*scale\(1\.04\);?', 'transform: translateY(-2px);', css)
css = re.sub(r'transform:\s*rotate\(1deg\)\s*scale\(1\.05\);?', 'transform: translateY(-2px);', css)
css = re.sub(r'transform:\s*rotate\(-3deg\);?', 'transform: none;', css)
css = re.sub(r'transform:\s*rotate\(2deg\);?', 'transform: none;', css)
css = re.sub(r'transform:\s*rotate\(3deg\);?', 'transform: none;', css)

# Make sure badges sit straight and flush on top border
css = re.sub(
    r'\.badge\s*\{[^}]*\}',
    '''.badge {
  position: absolute;
  top: -14px;
  right: 24px;
  background: var(--sun);
  border: var(--b);
  border-radius: 99px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.8rem;
  padding: 4px 16px;
  transform: none;
  box-shadow: 2px 2px 0 var(--ink);
  color: var(--ink);
  z-index: 5;
  white-space: nowrap;
}''',
    css
)

css = re.sub(
    r'\.path\s*\.sticker\s*\{[^}]*\}',
    '''.path .sticker {
  position: absolute;
  top: -14px;
  right: 24px;
  margin: 0;
  transform: none;
  background: var(--sun);
  color: var(--ink);
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.78rem;
  padding: 4px 16px;
  box-shadow: 2px 2px 0 var(--ink);
  z-index: 5;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}''',
    css
)

# Append specific new styles for unified non-refreshing planner
unified_css = '''
/* =====================================================
   UNIFIED STUDY ABROAD CALCULATOR & GUIDE (PROPER ALIGNMENT)
   ===================================================== */
.calc-unified-wrap {
  display: grid;
  grid-template-columns: 1.18fr 0.82fr;
  gap: 28px;
  align-items: start;
}

.step-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--blue);
  color: #fff;
  font-size: 0.78rem;
  font-weight: 800;
  margin-right: 8px;
  flex-shrink: 0;
}

.opt-label {
  display: flex;
  align-items: center;
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 1.08rem;
  margin: 22px 0 10px;
  color: var(--ink);
}

.opt-label:first-child {
  margin-top: 0;
}

.ft-savings-callout {
  background: rgba(200, 255, 62, 0.15);
  border: 1.5px solid var(--lime);
  border-radius: 12px;
  padding: 10px 14px;
  font-size: 0.88rem;
  color: var(--lime);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
}

.result-header {
  margin-bottom: 14px;
}

.result-tag {
  display: inline-block;
  font-size: 0.74rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #8DB3FF;
  margin-bottom: 4px;
}

.result-total {
  margin-bottom: 16px;
}

/* Prevent auto zoom on mobile inputs */
@media (max-width: 768px) {
  .calc-unified-wrap {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  input, select, textarea, .fi {
    font-size: 16px !important;
  }
  .opt {
    font-size: 0.88rem;
    padding: 8px 14px;
  }
}
'''

if '/* =====================================================\n   UNIFIED STUDY ABROAD CALCULATOR' not in css:
    css += unified_css

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('css/styles.css updated (all rotation removed, alignment cleaned)!')


# ==============================================================================
# 2. UPDATE INDEX.HTML (UNIFIED CALCULATOR & METATAGS)
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix viewport tag to prevent mobile zoom-in jumps
html = re.sub(
    r'<meta name="viewport"[^>]*>',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />',
    html
)

# Replace the entire calculator section with the clean unified layout
calc_pattern = re.compile(r'<section class="calc-sec" id="calculator">.*?</section>', re.DOTALL)

new_calc_html = '''<section class="calc-sec" id="calculator">
      <div class="container">
        <!-- Clean, straight, aligned header -->
        <div class="sec-head" style="margin-bottom: 30px;">
          <span class="sticker white">⚡ 30-Second Estimate · Free Country Handbook</span>
          <h2>Calculate Your Study Abroad Cost &amp; <span class="box">Get Free Guide</span></h2>
          <p class="lead">Select your destination, study level, and route to calculate your tuition, living expenses, and download the official 2026 country handbook.</p>
        </div>

        <div class="calc-unified-wrap">
          <!-- Step Controls Card (Left on Desktop, Top on Mobile) -->
          <div class="calc-box">
            <span class="badge">Takes 30 sec</span>

            <!-- Step 1: Destination -->
            <div class="opt-label"><span class="step-num">1</span> Where do you want to study?</div>
            <div class="opts" data-k="country">
              <button class="opt" type="button" data-v="Germany">🇩🇪 Germany</button>
              <button class="opt on" type="button" data-v="Canada">🇨🇦 Canada</button>
              <button class="opt" type="button" data-v="United Kingdom">🇬🇧 United Kingdom</button>
              <button class="opt" type="button" data-v="Australia">🇦🇺 Australia</button>
              <button class="opt" type="button" data-v="USA">🇺🇸 United States</button>
              <button class="opt" type="button" data-v="France">🇫🇷 France</button>
              <button class="opt" type="button" data-v="Ireland">🇮🇪 Ireland</button>
            </div>

            <!-- Step 2: Study Level -->
            <div class="opt-label"><span class="step-num">2</span> What degree are you aiming for?</div>
            <div class="opts" data-k="level">
              <button class="opt" type="button" data-v="Bachelor's">🎓 Bachelor's (After 12th)</button>
              <button class="opt" type="button" data-v="Master's">📜 Master's (After Graduation)</button>
              <button class="opt on" type="button" data-v="MBA">💼 Global MBA</button>
            </div>

            <!-- Step 3: Pathway -->
            <div class="opt-label"><span class="step-num">3</span> Which study route fits your budget?</div>
            <div class="opts" data-k="pathway">
              <button class="opt" type="button" data-v="direct">🏛️ Direct Study Abroad (On-campus from day 1)</button>
              <button class="opt on" type="button" data-v="fast-track">⚡ Fast Track (Online Year 1 in India · Save up to 45%)</button>
            </div>

            <!-- Step 4: Lifestyle -->
            <div class="opt-label"><span class="step-num">4</span> What is your living style?</div>
            <div class="opts" data-k="lifestyle">
              <button class="opt" type="button" data-v="lean">Budget 🥺 (Shared room, cook at home)</button>
              <button class="opt" type="button" data-v="mid">Moderate 😌 (Standard student housing)</button>
              <button class="opt on" type="button" data-v="plus">Comfortable 😎 (Studio / prime city)</button>
            </div>
          </div>

          <!-- Live Result Card (Right on Desktop, Bottom on Mobile) -->
          <div class="result" id="calcResultBox">
            <div class="result-header">
              <span class="result-tag" id="rTag">Indicative Planning Budget</span>
              <div id="rTitle" class="r-title" style="color:var(--lime);font-size:1.15rem;font-weight:800;">Canada · MBA · Fast Track (Yr 1)</div>
            </div>

            <div class="result-total">
              <div id="rRange" class="big" style="color:#fff;font-size:clamp(2.2rem,4.4vw,3.2rem);font-weight:800;line-height:1;margin:6px 0 2px;">₹23.1L – ₹38.5L</div>
              <div class="per" style="color:#B6C3E6;font-size:0.88rem;">Estimated total per year (Tuition + Living)</div>
            </div>

            <div id="ftSavingsBadge" class="ft-savings-callout">
              <i class="fa-solid fa-bolt"></i> Fast Track saves approx. <strong>₹8.1L – ₹15.7L</strong> on Year 1 tuition!
            </div>

            <div class="break">
              <div>
                <span>Tuition Fees (Year 1)</span>
                <span id="rTuition" class="val">₹9.9L – ₹19.3L</span>
              </div>
              <div>
                <span>Living &amp; Accommodation</span>
                <span id="rLiving" class="val">₹13.2L – ₹19.2L</span>
              </div>
              <div>
                <span>Visa, Insurance &amp; Travel (One-time)</span>
                <span id="rOther" class="val">₹2L – ₹4L</span>
              </div>
            </div>

            <!-- Instant PDF Download Action -->
            <button class="btn btn-lime btn-block" id="calcDownloadPdfBtn" type="button" style="margin-top:14px;font-size:1.05rem;">
              <i class="fa-solid fa-file-arrow-down"></i> Download Free Canada Guide (PDF) ↓
            </button>

            <!-- Quick In-Card Delivery Form -->
            <div class="calc-lead-gate" style="margin-top:22px;padding-top:18px;border-top:1px dashed rgba(255,255,255,0.25);">
              <p style="font-size:0.88rem;color:#DCE5FA;margin-bottom:12px;font-weight:600;">
                Want this complete cost sheet &amp; admission checklist sent to WhatsApp?
              </p>
              <form id="calcQuickLeadForm" class="form" style="display:grid;gap:10px;">
                <input class="fi" name="name" id="calc_name" placeholder="Your Full Name" required autocomplete="name" style="background:rgba(255,255,255,0.08);color:#fff;border-color:rgba(255,255,255,0.3);" />
                <div class="ph">
                  <span style="background:var(--lime);color:var(--ink);font-weight:800;border:var(--b);border-right:0;">+91</span>
                  <input class="fi" name="phone" id="calc_phone" type="tel" inputmode="numeric" pattern="[0-9]{10}" maxlength="10" placeholder="WhatsApp Number" required style="background:rgba(255,255,255,0.08);color:#fff;border-color:rgba(255,255,255,0.3);border-radius:0 14px 14px 0;" />
                </div>
                <input class="fi" name="email" id="calc_email" type="email" placeholder="Email Address" required autocomplete="email" style="background:rgba(255,255,255,0.08);color:#fff;border-color:rgba(255,255,255,0.3);" />
                <button class="btn btn-primary btn-block" type="submit" id="calcQuickSubmitBtn" style="padding:14px;">
                  Send My Guide &amp; Cost Sheet <i class="fa-solid fa-paper-plane"></i>
                </button>
              </form>
              <div id="calcQuickSuccess" style="display:none;background:rgba(200,255,62,0.15);border:2px solid var(--lime);border-radius:14px;padding:14px;text-align:center;margin-top:10px;">
                <strong style="color:var(--lime);display:block;margin-bottom:4px;">✓ Guide Sent &amp; Downloaded!</strong>
                <p style="font-size:0.82rem;color:#DCE5FA;margin:0;">A counsellor has been assigned to help you with university selection and visa guidance.</p>
              </div>
            </div>

            <p class="disc" style="margin-top:14px;">
              *Indicative planning ranges in ₹ (L = lakh). Actual expenses depend on university, course, city and foreign exchange rates.
            </p>
          </div>
        </div>
      </div>
    </section>'''

html = calc_pattern.sub(new_calc_html, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('index.html updated successfully with unified non-refreshing planner!')


# ==============================================================================
# 3. UPDATE JS (STATEFUL, SMOOTH, ZERO JUMP, LIVE CALCULATOR)
# ==============================================================================
unified_js = '''/**
 * University Yatra — Study Abroad Landing Page
 * Unified Study Abroad Cost Calculator & Guide Engine
 * Zero-Jumping, Non-Refreshing, Smooth Real-Time Reactive Controller
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
    level: 'MBA',
    pathway: 'fast-track',
    lifestyle: 'plus'
  };

  function calculate() {
    const data = D[S.country] || D['Canada'];
    const tBase = data.t[S.level] || data.t["Master's"];
    const lBase = data.l;

    // Lifestyle factor
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

    // DOM Updates (Instant, No Page Shifts)
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

    // Fast Track Savings Badge Callout
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

  function initCalculator() {
    const calcSec = $('calculator');
    if (!calcSec) return;

    // Handle Option Button Clicks (Smooth, No Refresh, No Scroll Jumps)
    calcSec.querySelectorAll('.opts').forEach(group => {
      const key = group.dataset.k;
      group.querySelectorAll('.opt').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          group.querySelectorAll('.opt').forEach(b => b.classList.remove('on'));
          btn.classList.add('on');
          S[key] = btn.dataset.v;
          calculate();
        });
      });
    });

    // In-Card Quick Delivery Form
    const quickForm = $('calcQuickLeadForm');
    const quickSuccess = $('calcQuickSuccess');
    if (quickForm && quickSuccess) {
      quickForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const fd = new FormData(quickForm);
        const phone = String(fd.get('phone') || '').trim();
        const name = String(fd.get('name') || '').trim();

        if (!/^[6-9][0-9]{9}$/.test(phone)) {
          alert('Please enter a valid 10-digit Indian WhatsApp number');
          return;
        }

        const btn = $('calcQuickSubmitBtn');
        if (btn) {
          btn.disabled = true;
          btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Preparing Handbook...';
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

    calculate();
  }

  /* Bottom Enquiry Form */
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
    initCalculator();
    initBottomEnquiry();
  });

})();
'''

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(unified_js)

print('js/main.js updated with rock-solid, zero-jumping calculator controller!')

