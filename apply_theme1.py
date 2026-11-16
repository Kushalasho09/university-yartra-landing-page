import re

# Read current css
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add / update Theme 1 Neo-Brutalist enhancements
theme1_styles = """
/* =====================================================
   THEME 1 — ELEVATED NEO-BRUTALISM / NEO-POP ENHANCEMENTS
   ===================================================== */

/* Playful Tilted Stickers */
.sticker {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.82rem;
  padding: 6px 16px;
  border: var(--b);
  border-radius: 99px;
  background: var(--lime);
  box-shadow: var(--sh-s);
  transform: rotate(-2deg);
  margin-bottom: 16px;
  color: var(--ink);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  transition: transform 0.2s ease;
}

.sticker:hover {
  transform: rotate(0deg) scale(1.04);
}

.sticker.pink { background: var(--pink); }
.sticker.sun  { background: var(--sun); }
.sticker.sky  { background: var(--sky); }

/* Fancy Tilted Boxed Headline Word */
.hero h1 .box {
  background: var(--blue);
  color: #fff;
  padding: 0 0.22em;
  border-radius: 0.22em;
  display: inline-block;
  transform: rotate(-2deg);
  border: var(--b);
  box-shadow: 4px 4px 0 var(--ink);
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.hero h1 .box:hover {
  transform: rotate(1deg) scale(1.05);
}

/* Passport Stamp & Starburst Badges */
.stamp-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 0.78rem;
  padding: 4px 12px;
  border: 2px dashed var(--ink);
  border-radius: 8px;
  background: #fff;
  color: var(--blue);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  transform: rotate(-3deg);
  box-shadow: 2px 2px 0 var(--ink);
}

.starburst-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: var(--lime);
  color: var(--ink);
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 0.76rem;
  padding: 4px 10px;
  border: 2px solid var(--ink);
  border-radius: 99px;
  transform: rotate(2deg);
  box-shadow: 2px 2px 0 var(--ink);
}

/* Tactile 3D Buttons */
.btn {
  box-shadow: 4px 4px 0 var(--ink);
}

.btn:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 var(--ink);
}

.btn:active {
  transform: translate(2px, 2px);
  box-shadow: 0 0 0 var(--ink);
}

/* Fast Track Card Starburst highlight */
.path.fast .starburst-badge {
  background: var(--sun);
  color: var(--ink);
}

/* Hero Compact on Mobile */
@media (max-width: 768px) {
  .hero {
    padding: 24px 0 16px;
  }
  .hero h1 {
    font-size: clamp(2rem, 6.8vw, 3.2rem);
    margin-bottom: 12px;
  }
  .hero p.lead {
    font-size: 1rem;
    margin-bottom: 18px;
  }
  .hero-card {
    display: none; /* Keep hero compact on mobile so calculator is near top */
  }
}
"""

with open('css/styles.css', 'a', encoding='utf-8') as f:
    f.write(theme1_styles)

print("Appended Theme 1 enhancements to css/styles.css")
