import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure .calc-box and .path have position: relative
new_rules = '''
/* =====================================================
   OVERLAPPING BADGES & POLISH (Matches User Screenshots)
   ===================================================== */
.badge {
  position: absolute;
  top: -16px;
  right: 22px;
  background: var(--sun);
  border: var(--b);
  border-radius: 99px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.8rem;
  padding: 5px 16px;
  transform: rotate(3deg);
  box-shadow: 3px 3px 0 var(--ink);
  color: var(--ink);
  z-index: 5;
  white-space: nowrap;
}

.calc-box {
  position: relative;
}

.path .sticker {
  position: absolute;
  top: -16px;
  right: 22px;
  margin: 0;
  transform: rotate(3deg);
  background: var(--sun);
  color: var(--ink);
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.78rem;
  padding: 5px 16px;
  box-shadow: 3px 3px 0 var(--ink);
  z-index: 5;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* Mode Switcher between 2-Column and 4-Tap Wizard */
.calc-mode-switcher {
  display: inline-flex;
  gap: 8px;
  background: #fff;
  border: var(--b);
  border-radius: 99px;
  padding: 5px;
  box-shadow: var(--sh-s);
}

.mode-btn {
  font-family: 'DM Sans', sans-serif;
  font-weight: 700;
  font-size: 0.88rem;
  padding: 9px 18px;
  border-radius: 99px;
  border: none;
  background: transparent;
  cursor: pointer;
  transition: 0.15s;
  color: var(--ink);
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.mode-btn.on {
  background: var(--blue);
  color: #fff;
  box-shadow: 2px 2px 0 var(--ink);
}

/* 4-Tap Wizard (Matches Image 2 & Image 4) */
.wizard-box {
  position: relative;
  background: #fff;
  border: var(--b);
  border-radius: 28px;
  padding: 30px;
  box-shadow: 8px 8px 0 var(--blue);
  min-height: 480px;
  display: flex;
  flex-direction: column;
}

.wizard-top {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.wizard-back {
  width: 38px;
  height: 38px;
  border: var(--b);
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.1rem;
  background: #fff;
  flex: none;
  cursor: pointer;
  transition: 0.15s;
}

.wizard-back:hover {
  background: var(--lime);
}

.wizard-back[hidden] {
  display: none;
}

.wizard-dots {
  display: flex;
  gap: 8px;
  flex: 1;
}

.wizard-dots i {
  flex: 1;
  height: 8px;
  border: 2px solid var(--ink);
  border-radius: 9px;
  background: #fff;
  transition: 0.3s;
}

.wizard-dots i.on {
  background: var(--blue);
}

.wizard-stepno {
  font-weight: 800;
  font-size: 0.88rem;
  min-width: 32px;
  text-align: right;
  color: var(--ink);
}

.wizard-crumbs {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  min-height: 32px;
  margin-bottom: 10px;
}

.wizard-crumb {
  font-size: 0.78rem;
  font-weight: 700;
  background: var(--sky);
  border: 2px solid var(--ink);
  padding: 4px 12px;
  border-radius: 99px;
  cursor: pointer;
  transition: 0.15s;
}

.wizard-crumb:hover {
  background: var(--lime);
}

.wizard-q {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: clamp(1.8rem, 4.4vw, 2.6rem);
  line-height: 1.05;
  letter-spacing: -0.03em;
  margin-bottom: 6px;
  color: var(--ink);
}

.wizard-qsub {
  color: var(--muted);
  margin-bottom: 20px;
  font-size: 0.98rem;
}

.wizard-opts {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.wizard-opts.c3 {
  grid-template-columns: repeat(3, 1fr);
}

.wizard-opts.c1 {
  grid-template-columns: 1fr;
}

.wizard-o {
  text-align: left;
  border: var(--b);
  border-radius: 18px;
  padding: 16px 18px;
  background: #fff;
  box-shadow: var(--sh-s);
  transition: transform 0.12s, box-shadow 0.12s, background 0.12s;
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-height: 64px;
  justify-content: center;
  cursor: pointer;
}

.wizard-o b {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--ink);
}

.wizard-o span {
  font-size: 0.84rem;
  color: var(--muted);
  line-height: 1.3;
}

.wizard-o:hover {
  transform: translate(-2px, -2px);
  box-shadow: 5px 5px 0 var(--ink);
}

.wizard-o.sel {
  background: var(--lime);
}

@media (max-width: 600px) {
  .wizard-opts,
  .wizard-opts.c3 {
    grid-template-columns: 1fr;
  }
  .wizard-box {
    padding: 20px;
    border-radius: 24px;
    box-shadow: 6px 6px 0 var(--blue);
  }
}
'''

if '/* =====================================================\n   OVERLAPPING BADGES' not in css:
    css += new_rules
    with open('css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print('styles.css updated with badge and wizard styles!')
else:
    print('styles already contained the rules')

