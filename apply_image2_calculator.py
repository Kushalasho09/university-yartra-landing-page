import re

# 1. Update Section 4 in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_calc_html = """    <!-- SECTION 4 — STUDY ABROAD COST CALCULATOR (IMAGE 2 UI) -->
    <section class="calc-sec" id="calculator">
      <div class="container">
        <div class="sec-head">
          <span class="sticker pink">Instant · No Sign-Up</span>
          <h2>How much will it <mark>actually</mark> cost?</h2>
          <p>Tap your options, see an approximate yearly budget. Want the detailed guide? Download it instantly below.</p>
        </div>

        <div class="calc-two-col">
          <!-- Left Options Box -->
          <div class="calc-box">
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
            <div class="opts" data-k="path">
              <button class="opt" type="button" data-v="Direct">Direct</button>
              <button class="opt on" type="button" data-v="Fast Track">Fast Track</button>
            </div>

            <div class="opt-label">4. Lifestyle</div>
            <div class="opts" data-k="life">
              <button class="opt" type="button" data-v="lean">Budget 🥺</button>
              <button class="opt" type="button" data-v="mid">Moderate 🙂</button>
              <button class="opt on" type="button" data-v="plus">Comfy 😎</button>
            </div>
          </div>

          <!-- Right Result Card (Obsidian Dark with Lime & White) -->
          <div class="result" aria-live="polite">
            <h3 id="rTitle">Canada · MBA · Fast Track (Yr 1)</h3>
            <div class="big" id="rRange">₹23.1L – ₹38.5L</div>
            <div class="per">per year · tuition + living · indicative</div>

            <div class="break">
              <div><span>Tuition</span><b id="rTuition">₹9.9L – ₹19.3L</b></div>
              <div><span>Living &amp; stay</span><b id="rLiving">₹13.2L – ₹19.2L</b></div>
              <div><span>Visa, insurance, travel (one-time)</span><b id="rOther">₹2L – ₹4L</b></div>
            </div>

            <button type="button" id="calcDownloadPdfBtn" class="btn btn-lime btn-block">
              <i class="fa-solid fa-file-pdf"></i> Download Free <span id="rBtnCountry">Canada</span> Guide (PDF) ↓
            </button>
            <a href="#enquiry" id="calcCta" class="btn btn-block" style="background:#fff;margin-top:10px;">
              Get Personalized Cost Plan →
            </a>

            <p class="disc">
              Indicative ranges in ₹ (L = lakh) for planning only. Actual costs vary by university, course, city and exchange rate. Your counsellor shares a verified breakdown.
            </p>
          </div>
        </div>
      </div>
    </section>"""

# Replace existing Section 4 in index.html
html = re.sub(
    r'<section class=\"calc-sec\" id=\"calculator\">[\s\S]*?</section>',
    new_calc_html,
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html Section 4 with Image 2 calculator!")

# 2. Update css/styles.css with exact Image 2 styling
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

calc_css = """
/* =====================================================
   IMAGE 2 CALCULATOR STYLES (SUNNY YELLOW BG & CRISP TILES)
   ===================================================== */
.calc-sec {
  background: var(--sun);
  border-block: var(--b);
  padding: 80px 0;
  position: relative;
}

.calc-two-col {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 28px;
  align-items: start;
}

.calc-box {
  background: #fff;
  border: var(--b);
  border-radius: var(--r);
  padding: 32px;
  box-shadow: var(--sh);
}

.opt-label {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 1.12rem;
  margin: 20px 0 10px;
  color: var(--ink);
}

.opt-label:first-child {
  margin-top: 0;
}

.opts {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.opt {
  font-family: 'DM Sans', sans-serif;
  font-weight: 700;
  font-size: 0.94rem;
  padding: 10px 18px;
  border: var(--b);
  border-radius: 99px;
  background: #fff;
  cursor: pointer;
  transition: transform 0.12s, box-shadow 0.12s, background 0.12s;
  color: var(--ink);
  white-space: nowrap;
}

.opt:hover {
  background: var(--cream);
  transform: translateY(-2px);
  box-shadow: 3px 3px 0 var(--ink);
}

.opt.on {
  background: var(--blue) !important;
  color: #fff !important;
  box-shadow: 3px 3px 0 var(--ink);
}

.result {
  background: var(--ink);
  color: #fff;
  border: var(--b);
  border-radius: var(--r);
  padding: 32px;
  box-shadow: var(--sh);
}

.result h3 {
  color: var(--lime);
  font-size: 1.08rem;
  margin-bottom: 6px;
  letter-spacing: -0.01em;
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
}

.result .big {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: clamp(2.3rem, 4.6vw, 3.4rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #fff;
  margin: 10px 0 4px;
  line-height: 1;
}

.result .per {
  color: #B6C3E6;
  font-size: 0.92rem;
  margin-bottom: 20px;
}

.break {
  border-top: 2px dashed rgba(255, 255, 255, 0.3);
  padding-top: 16px;
  margin-bottom: 22px;
}

.break div {
  display: flex;
  justify-content: space-between;
  font-size: 0.95rem;
  padding: 6px 0;
  color: #DCE5FA;
}

.break div b {
  color: #fff;
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.05rem;
}

.disc {
  font-size: 0.78rem;
  color: #9FB0D8;
  margin-top: 16px;
  line-height: 1.45;
}

@media (max-width: 860px) {
  .calc-two-col {
    grid-template-columns: 1fr;
  }
}
"""

css += calc_css

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/styles.css with Image 2 calculator styles!")
