import os, sys

css_code = """/* =====================================================
   UNIVERSITY YATRA — CLIENT DESIGN SYSTEM
   Bricolage Grotesque + DM Sans · High Contrast · Tactile
   ===================================================== */
:root {
  --blue: #1765F5;
  --blue-d: #0F4FCC;
  --ink: #0A1230;
  --cream: #F4F7FF;
  --white: #ffffff;
  --lime: #C8FF3E;
  --pink: #FF8AD0;
  --sun: #FFD84A;
  --sky: #BFD6FF;
  --muted: #4D5878;
  --border-color: #0A1230;
  --b: 2.5px solid var(--ink);
  --sh: 5px 5px 0 var(--ink);
  --sh-s: 3px 3px 0 var(--ink);
  --sh-lg: 8px 8px 0 var(--ink);
  --r: 24px;
  --r-sm: 16px;
  --r-lg: 32px;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 84px;
}

body {
  font-family: 'DM Sans', system-ui, -apple-system, sans-serif;
  color: var(--ink);
  background: var(--cream);
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  font: inherit;
  color: inherit;
  cursor: pointer;
  background: none;
  border: 0;
}

h1, h2, h3, .disp {
  font-family: 'Bricolage Grotesque', 'DM Sans', sans-serif;
  line-height: 1.08;
  letter-spacing: -0.03em;
  color: var(--ink);
}

.container {
  max-width: 1140px;
  margin: 0 auto;
  padding: 0 20px;
}

section {
  padding: 76px 0;
}

h2 {
  font-size: clamp(1.9rem, 4.5vw, 3.1rem);
  font-weight: 800;
}

.sec-head {
  max-width: 760px;
  margin-bottom: 36px;
}

.sec-head.center {
  text-align: center;
  margin-inline: auto;
}

.sec-head p {
  color: var(--muted);
  font-size: 1.08rem;
  margin-top: 12px;
  line-height: 1.5;
}

/* STICKERS / BADGES */
.sticker {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 700;
  font-size: 0.82rem;
  padding: 6px 14px;
  border: var(--b);
  border-radius: 99px;
  background: var(--lime);
  box-shadow: var(--sh-s);
  transform: rotate(-1.5deg);
  margin-bottom: 16px;
  color: var(--ink);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.sticker.pink { background: var(--pink); }
.sticker.sun  { background: var(--sun); }
.sticker.sky  { background: var(--sky); }
.sticker.white { background: #fff; }

.hl {
  color: var(--blue);
}

mark {
  background: var(--lime);
  padding: 0 0.15em;
  border-radius: 0.2em;
  color: var(--ink);
}

/* BUTTONS */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 700;
  font-size: 1rem;
  padding: 13px 26px;
  border: var(--b);
  border-radius: 99px;
  box-shadow: var(--sh-s);
  transition: transform 0.12s ease, box-shadow 0.12s ease, background 0.12s ease;
  background: #fff;
  color: var(--ink);
  white-space: nowrap;
  cursor: pointer;
  text-decoration: none;
}

.btn:hover {
  transform: translate(-2px, -2px);
  box-shadow: 5px 5px 0 var(--ink);
}

.btn:active {
  transform: translate(2px, 2px);
  box-shadow: 0 0 0 var(--ink);
}

.btn:disabled {
  opacity: 0.6;
  pointer-events: none;
}

.btn-primary {
  background: var(--blue);
  color: #fff;
}

.btn-lime {
  background: var(--lime);
  color: var(--ink);
}

.btn-sun {
  background: var(--sun);
  color: var(--ink);
}

.btn-wa {
  background: #25D366;
  color: #fff;
}

.btn-block {
  width: 100%;
}

.btn-sm {
  padding: 9px 18px;
  font-size: 0.88rem;
}

/* HEADER & NAVBAR */
header {
  position: sticky;
  top: 0;
  z-index: 900;
  background: #fff;
  border-bottom: var(--b);
}

.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 1.3rem;
  letter-spacing: -0.03em;
  color: var(--ink);
}

.logo i {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: var(--blue);
  display: grid;
  place-items: center;
  border: 2px solid var(--ink);
  box-shadow: 2px 2px 0 var(--ink);
}

.logo b {
  color: var(--blue);
}

.nav-links {
  display: flex;
  gap: 22px;
  font-weight: 700;
  font-size: 0.92rem;
}

.nav-links a {
  transition: color 0.15s;
}

.nav-links a:hover {
  color: var(--blue);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

@media (max-width: 890px) {
  .nav-links { display: none; }
}

/* HERO SECTION */
.hero {
  padding: 42px 0 24px;
  position: relative;
  background: var(--cream);
}

.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: radial-gradient(var(--sky) 1.5px, transparent 1.5px);
  background-size: 26px 26px;
  opacity: 0.7;
  pointer-events: none;
}

.hero .container {
  position: relative;
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 36px;
  align-items: center;
}

.hero-content {
  max-width: 640px;
}

.hero h1 {
  font-size: clamp(2.3rem, 5.8vw, 4.2rem);
  font-weight: 800;
  margin-bottom: 16px;
  line-height: 1.05;
}

.hero h1 .box {
  background: var(--blue);
  color: #fff;
  padding: 0 0.18em;
  border-radius: 0.22em;
  display: inline-block;
  transform: rotate(-1.5deg);
  border: var(--b);
  box-shadow: var(--sh-s);
}

.hero p.lead {
  font-size: 1.12rem;
  color: var(--muted);
  line-height: 1.55;
  margin-bottom: 24px;
}

.hero-actions {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 28px;
}

.hero-trust {
  display: flex;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
  padding-top: 16px;
  border-top: 1px dashed rgba(10, 18, 48, 0.2);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--ink);
}

.hero-trust span {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.hero-trust i {
  color: var(--blue);
}

.hero-card {
  border: var(--b);
  border-radius: var(--r);
  background: #fff;
  box-shadow: var(--sh-lg);
  padding: 16px;
  position: relative;
}

.hero-card img {
  width: 100%;
  height: auto;
  border-radius: calc(var(--r) - 8px);
  display: block;
  border: 2px solid var(--ink);
  aspect-ratio: 4/3;
  object-fit: cover;
}

.hero-card-badge {
  position: absolute;
  bottom: 28px;
  left: 30px;
  background: var(--lime);
  border: var(--b);
  box-shadow: var(--sh-s);
  padding: 8px 16px;
  border-radius: 99px;
  font-weight: 800;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 8px;
}

@media (max-width: 900px) {
  .hero .container {
    grid-template-columns: 1fr;
    gap: 28px;
  }
  .hero-card {
    max-width: 520px;
  }
}

/* SECTION 2 — STUDY PATHWAYS */
.path-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.path {
  position: relative;
  border: var(--b);
  border-radius: var(--r);
  padding: 32px;
  box-shadow: var(--sh);
  background: #fff;
  display: flex;
  flex-direction: column;
}

.path.fast {
  background: var(--blue);
  color: #fff;
  box-shadow: 8px 8px 0 var(--ink);
}

.path.fast h3,
.path.fast > p,
.path.fast li {
  color: #fff;
}

.path .eyebrow {
  font-size: 0.76rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--blue);
  margin-bottom: 6px;
}

.path.fast .eyebrow {
  color: var(--lime);
}

.path h3 {
  font-size: 2rem;
  margin-bottom: 8px;
  line-height: 1.1;
}

.path > p {
  margin-bottom: 18px;
  color: var(--muted);
  font-size: 0.98rem;
  line-height: 1.45;
}

.path ul {
  list-style: none;
  margin-bottom: 20px;
}

.path li {
  padding: 6px 0 6px 28px;
  position: relative;
  font-weight: 600;
  font-size: 0.94rem;
}

.path li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: var(--blue);
  font-weight: 900;
}

.path.fast li::before {
  color: var(--lime);
}

.best {
  font-size: 0.88rem;
  padding: 12px 16px;
  border: 2px dashed currentColor;
  border-radius: 14px;
  margin-bottom: 20px;
  line-height: 1.45;
}

.path .sticker {
  position: absolute;
  top: -16px;
  right: 20px;
  margin: 0;
  transform: rotate(3deg);
  color: var(--ink);
}

.fine {
  font-size: 0.78rem;
  margin-top: 14px;
  opacity: 0.85;
}

.path .btn {
  margin-top: auto;
}

@media (max-width: 800px) {
  .path-grid { grid-template-columns: 1fr; }
}

/* SECTION 3 — POST-STUDY OPPORTUNITIES */
.inside {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 18px;
}

.ic {
  border: var(--b);
  border-radius: var(--r);
  padding: 24px;
  box-shadow: var(--sh-s);
  background: #fff;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.ic:hover {
  transform: translate(-2px, -2px);
  box-shadow: 5px 5px 0 var(--ink);
}

.ic:nth-child(5n+1) { background: var(--sky); }
.ic:nth-child(5n+2) { background: var(--lime); }
.ic:nth-child(5n+3) { background: var(--pink); }
.ic:nth-child(5n+4) { background: var(--sun); }
.ic:nth-child(5n+5) { background: #fff; }

.ic .n {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 2.2rem;
  line-height: 1;
  margin-bottom: 10px;
}

.ic h3 {
  font-size: 1.25rem;
  margin-bottom: 6px;
  line-height: 1.2;
}

.ic p {
  font-size: 0.92rem;
  opacity: 0.9;
  line-height: 1.4;
}

.sec-cta-wrap {
  margin-top: 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  padding: 18px 24px;
  background: #fff;
  border: var(--b);
  border-radius: var(--r);
  box-shadow: var(--sh-s);
}

.sec-cta-wrap p {
  font-size: 0.85rem;
  color: var(--muted);
  max-width: 600px;
}

/* SECTION 4 — CALCULATOR & COUNTRY GUIDE */
.calc-sec {
  padding: 40px 0 80px;
  position: relative;
}

.calc-wrap {
  display: grid;
  grid-template-columns: 1.45fr 0.55fr;
  gap: 24px;
  align-items: stretch;
}

.calc {
  background: #fff;
  border: var(--b);
  border-radius: 28px;
  padding: 32px;
  box-shadow: 8px 8px 0 var(--blue);
  min-height: 480px;
  display: flex;
  flex-direction: column;
  position: relative;
}

.calc .badge {
  position: absolute;
  top: -15px;
  right: 24px;
  background: var(--sun);
  border: var(--b);
  border-radius: 99px;
  font-weight: 800;
  font-size: 0.8rem;
  padding: 4px 14px;
  transform: rotate(3deg);
  box-shadow: 2px 2px 0 var(--ink);
}

.calc .top {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 18px;
}

.calc .back {
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
  transition: background 0.15s;
}

.calc .back:hover {
  background: var(--lime);
}

.calc .back[hidden] {
  display: none;
}

.dots {
  display: flex;
  gap: 7px;
  flex: 1;
}

.dots i {
  flex: 1;
  height: 9px;
  border: 2px solid var(--ink);
  border-radius: 9px;
  background: #fff;
  transition: background 0.25s;
}

.dots i.on {
  background: var(--blue);
}

.stepno {
  font-weight: 800;
  font-size: 0.88rem;
  font-family: 'Bricolage Grotesque', sans-serif;
}

.crumbs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  min-height: 32px;
  margin-bottom: 12px;
}

.crumb {
  font-size: 0.8rem;
  font-weight: 700;
  background: var(--sky);
  border: 2px solid var(--ink);
  padding: 4px 12px;
  border-radius: 99px;
  cursor: pointer;
  transition: background 0.15s;
}

.crumb:hover {
  background: var(--lime);
}

.q {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: clamp(1.8rem, 4.4vw, 2.6rem);
  line-height: 1.05;
  letter-spacing: -0.03em;
  margin-bottom: 6px;
}

.qsub {
  color: var(--muted);
  margin-bottom: 20px;
  font-size: 0.98rem;
}

.opts {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.opts.c3 { grid-template-columns: repeat(3, 1fr); }
.opts.c1 { grid-template-columns: 1fr; }

.o {
  text-align: left;
  border: var(--b);
  border-radius: 18px;
  padding: 16px 18px;
  background: #fff;
  box-shadow: var(--sh-s);
  transition: transform 0.12s, box-shadow 0.12s, background 0.12s;
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-height: 64px;
  justify-content: center;
  cursor: pointer;
}

.o b {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.o span {
  font-size: 0.84rem;
  color: var(--muted);
  line-height: 1.3;
}

.o:hover {
  transform: translate(-2px, -2px);
  box-shadow: 5px 5px 0 var(--ink);
}

.o:active {
  transform: translate(2px, 2px);
  box-shadow: 0 0 0 var(--ink);
}

.o.sel {
  background: var(--lime);
}

.o.dis {
  opacity: 0.4;
  pointer-events: none;
}

.note {
  margin-top: 14px;
  font-size: 0.86rem;
  background: var(--cream);
  border: 2px dashed var(--ink);
  border-radius: 14px;
  padding: 12px 14px;
}

.anim {
  animation: calcIn 0.3s cubic-bezier(0.2, 0.7, 0.2, 1);
}

@keyframes calcIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 580px) {
  .opts.c3 { grid-template-columns: 1fr 1fr; }
  .calc { padding: 22px 18px; border-radius: 22px; box-shadow: 6px 6px 0 var(--blue); }
}

/* GATE VIEW */
.gate .tick {
  display: inline-grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--lime);
  border: var(--b);
  font-weight: 800;
  font-size: 1.2rem;
  margin-bottom: 12px;
  box-shadow: 2px 2px 0 var(--ink);
}

.form {
  display: grid;
  gap: 12px;
  margin-top: 12px;
}

.fi {
  width: 100%;
  font: inherit;
  font-size: 1rem;
  padding: 14px 16px;
  border: var(--b);
  border-radius: 14px;
  background: #fff;
  color: var(--ink);
  outline: none;
  transition: background 0.15s, box-shadow 0.15s;
}

.fi:focus {
  background: #F2F7FF;
  box-shadow: 3px 3px 0 var(--blue);
}

.ph {
  display: flex;
}

.ph span {
  display: grid;
  place-items: center;
  padding: 0 16px;
  border: var(--b);
  border-right: 0;
  border-radius: 14px 0 0 14px;
  background: var(--lime);
  font-weight: 800;
  font-size: 0.95rem;
}

.ph .fi {
  border-radius: 0 14px 14px 0;
}

.r2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

@media (max-width: 580px) {
  .r2 { grid-template-columns: 1fr; }
}

.cons {
  font-size: 0.76rem;
  color: var(--muted);
  line-height: 1.45;
}

.cons a {
  text-decoration: underline;
  color: var(--blue);
}

.done {
  display: none;
}

.dl {
  display: grid;
  gap: 12px;
  margin: 16px 0;
}

/* GUIDE COVER ASIDE */
.cover {
  background: var(--ink);
  color: #fff;
  border: var(--b);
  border-radius: 28px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  box-shadow: var(--sh);
}

.cover::after {
  content: "";
  position: absolute;
  right: -70px;
  bottom: -90px;
  width: 280px;
  height: 280px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(23, 101, 245, 0.95), transparent 66%);
  pointer-events: none;
}

.cover > * {
  position: relative;
  z-index: 1;
}

.cv-t {
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  font-weight: 700;
  color: #9AA4BE;
}

.cv-h {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: clamp(2rem, 3.2vw, 2.7rem);
  line-height: 1;
  letter-spacing: -0.03em;
  margin: 14px 0 20px;
  color: #fff;
}

.cv-h em {
  font-style: normal;
  color: var(--lime);
}

.cv-l {
  list-style: none;
  margin-top: auto;
}

.cv-l li {
  padding: 10px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.18);
  font-size: 0.9rem;
  display: flex;
  gap: 12px;
  align-items: center;
}

.cv-l li b {
  color: var(--lime);
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.1rem;
}

@media (max-width: 960px) {
  .calc-wrap { grid-template-columns: 1fr; }
  .cover { display: none; }
}

/* SECTION 5 — DESTINATIONS & STUDY OPTIONS */
.cgrid {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 32px;
}

.ct {
  border: var(--b);
  border-radius: 99px;
  padding: 12px 22px;
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 700;
  font-size: 1.15rem;
  background: #fff;
  box-shadow: var(--sh-s);
  transition: transform 0.12s, box-shadow 0.12s;
  cursor: pointer;
}

.ct:nth-child(4n+1) { background: var(--sky); }
.ct:nth-child(4n+2) { background: var(--lime); }
.ct:nth-child(4n+3) { background: var(--pink); }
.ct:nth-child(4n+4) { background: var(--sun); }

.ct:hover {
  transform: translate(-2px, -2px) rotate(-1deg);
  box-shadow: 5px 5px 0 var(--ink);
}

.dest-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 22px;
}

.dest-card {
  border: var(--b);
  border-radius: var(--r);
  background: #fff;
  overflow: hidden;
  box-shadow: var(--sh);
  display: flex;
  flex-direction: column;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.dest-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 7px 7px 0 var(--ink);
}

.dest-img-wrap {
  position: relative;
  height: 200px;
  border-bottom: var(--b);
  overflow: hidden;
}

.dest-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.dest-badge {
  position: absolute;
  top: 14px;
  right: 14px;
  background: #fff;
  border: 2px solid var(--ink);
  box-shadow: 2px 2px 0 var(--ink);
  padding: 4px 12px;
  border-radius: 99px;
  font-weight: 800;
  font-size: 0.78rem;
  text-transform: uppercase;
}

.dest-body {
  padding: 24px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.dest-body h3 {
  font-size: 1.6rem;
  margin-bottom: 6px;
}

.dest-body p {
  color: var(--muted);
  font-size: 0.92rem;
  line-height: 1.45;
  margin-bottom: 18px;
}

.dest-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  padding: 12px;
  border: 2px dashed rgba(10, 18, 48, 0.2);
  border-radius: 14px;
  margin-bottom: 20px;
  background: var(--cream);
  font-size: 0.82rem;
}

.dest-stats b {
  display: block;
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1rem;
  color: var(--ink);
}

.dest-stats span {
  color: var(--muted);
  font-size: 0.76rem;
}

.dest-body .btn {
  margin-top: auto;
}

/* SECTION 6 — 360° SUPPORT */
.support-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 18px;
}

.sc {
  border: var(--b);
  border-radius: var(--r);
  padding: 24px;
  background: #fff;
  box-shadow: var(--sh-s);
  position: relative;
  transition: transform 0.12s ease, box-shadow 0.12s ease;
}

.sc:hover {
  transform: translate(-2px, -2px);
  box-shadow: 5px 5px 0 var(--ink);
}

.sc-num {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 1.8rem;
  color: var(--blue);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sc-num i {
  font-size: 1.2rem;
  color: var(--ink);
}

.sc h3 {
  font-size: 1.18rem;
  margin-bottom: 6px;
  line-height: 1.25;
}

.sc p {
  font-size: 0.9rem;
  color: var(--muted);
  line-height: 1.45;
}

/* SECTION 7 — TESTIMONIALS (2 HIGH IMPACT CARDS) */
.testi-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.testi-card {
  border: var(--b);
  border-radius: var(--r);
  background: #fff;
  box-shadow: var(--sh);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.testi-media {
  position: relative;
  height: 240px;
  border-bottom: var(--b);
  background: var(--ink);
}

.testi-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.92;
}

.testi-tag {
  position: absolute;
  top: 14px;
  left: 14px;
  background: var(--lime);
  border: 2px solid var(--ink);
  box-shadow: 2px 2px 0 var(--ink);
  padding: 4px 12px;
  border-radius: 99px;
  font-weight: 800;
  font-size: 0.78rem;
  display: flex;
  align-items: center;
  gap: 6px;
}

.testi-tag.sun { background: var(--sun); }

.testi-body {
  padding: 26px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.testi-quote {
  font-size: 1.05rem;
  font-weight: 600;
  line-height: 1.5;
  color: var(--ink);
  margin-bottom: 16px;
}

.testi-author {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: auto;
  padding-top: 14px;
  border-top: 1px dashed rgba(10, 18, 48, 0.2);
}

.testi-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--sky);
  border: 2px solid var(--ink);
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.1rem;
}

.testi-meta b {
  display: block;
  font-size: 0.96rem;
}

.testi-meta span {
  font-size: 0.8rem;
  color: var(--muted);
}

@media (max-width: 800px) {
  .testi-grid { grid-template-columns: 1fr; }
}

/* SECTION 8 — FAQs */
.faq {
  max-width: 840px;
  margin: 0 auto;
}

details {
  border: var(--b);
  border-radius: 18px;
  padding: 0 22px;
  margin-bottom: 12px;
  background: #fff;
  box-shadow: var(--sh-s);
  transition: background 0.15s ease;
}

details[open] {
  background: var(--lime);
}

summary {
  cursor: pointer;
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 700;
  font-size: 1.12rem;
  padding: 18px 0;
  list-style: none;
  display: flex;
  justify-content: space-between;
  gap: 14px;
  align-items: center;
}

summary::-webkit-details-marker {
  display: none;
}

summary::after {
  content: "+";
  font-size: 1.7rem;
  line-height: 1;
  font-weight: 700;
}

details[open] summary::after {
  content: "×";
}

details p {
  padding: 0 0 18px;
  font-size: 0.96rem;
  line-height: 1.5;
}

/* FINAL ENQUIRY & CTA SECTION */
.enquiry-wrap {
  margin-top: 60px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
  align-items: stretch;
}

.cta-box {
  background: var(--blue);
  color: #fff;
  border: var(--b);
  border-radius: 32px;
  padding: 44px 32px;
  box-shadow: 8px 8px 0 var(--ink);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cta-box h2 {
  color: #fff;
  font-size: clamp(2rem, 3.8vw, 2.7rem);
  margin-bottom: 14px;
}

.cta-box p {
  color: #DCE8FF;
  font-size: 1.05rem;
  line-height: 1.5;
  margin-bottom: 24px;
}

.cta-perks {
  list-style: none;
  margin-bottom: 28px;
}

.cta-perks li {
  padding: 6px 0;
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 600;
  font-size: 0.94rem;
}

.cta-perks li i {
  color: var(--lime);
}

.cta-box-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.enquiry-card {
  background: #fff;
  border: var(--b);
  border-radius: 32px;
  padding: 40px 32px;
  box-shadow: 8px 8px 0 var(--ink);
  display: flex;
  flex-direction: column;
}

.enquiry-card h3 {
  font-size: 1.8rem;
  margin-bottom: 6px;
}

.enquiry-card p.sub {
  color: var(--muted);
  font-size: 0.94rem;
  margin-bottom: 20px;
}

.enquiry-card .form {
  gap: 14px;
}

.enquiry-success {
  display: none;
  background: var(--lime);
  border: var(--b);
  border-radius: 20px;
  padding: 24px;
  text-align: center;
  box-shadow: var(--sh-s);
  margin-top: 10px;
}

.enquiry-success h4 {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.4rem;
  margin-bottom: 6px;
}

.contact-trio {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 16px;
  margin-top: 40px;
}

.cc {
  border: var(--b);
  border-radius: 20px;
  background: #fff;
  padding: 22px;
  box-shadow: var(--sh-s);
}

.cc small {
  display: block;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-weight: 800;
  color: var(--blue);
  margin-bottom: 6px;
}

.cc a {
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--ink);
}

@media (max-width: 860px) {
  .enquiry-wrap { grid-template-columns: 1fr; }
}

/* FOOTER */
footer {
  background: #fff;
  border-top: var(--b);
  padding: 38px 0 110px;
}

.ft {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
  align-items: center;
}

.ftl {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  font-size: 0.92rem;
  font-weight: 700;
}

.ftl a:hover {
  color: var(--blue);
}

.copy {
  margin-top: 18px;
  font-size: 0.8rem;
  color: var(--muted);
  max-width: 960px;
  line-height: 1.5;
}

/* MOBILE BOTTOM BAR (.mbar) */
.mbar {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 950;
  display: none;
  background: #fff;
  border-top: var(--b);
  padding: 10px 16px;
  padding-bottom: max(10px, env(safe-area-inset-bottom));
  gap: 10px;
  box-shadow: 0 -4px 16px rgba(10, 18, 48, 0.1);
}

.mbar .btn {
  flex: 1;
  padding: 12px 14px;
  font-size: 0.92rem;
}

@media (max-width: 768px) {
  .mbar { display: flex; }
  section { padding: 56px 0; }
}
"""

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css_code)

print("Wrote css/styles.css successfully! Length:", len(css_code))
