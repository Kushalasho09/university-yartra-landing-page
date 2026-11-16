import re

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>University Yatra | Study Abroad Quest (3D Gamified)</title>
  <meta name="description" content="Embark on your study abroad quest! Compare Direct vs Fast Track pathways, calculate costs, and unlock scholarships with University Yatra." />

  <!-- Nunito Font for Duolingo / Gamified Aesthetic -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

  <style>
    /* =====================================================
       THEME 2 — 3D PLAYFUL GAMIFIED QUEST (DUOLINGO AESTHETIC)
       ===================================================== */
    :root {
      --green: #58CC02;
      --green-shadow: #58A700;
      --green-dark: #46A302;
      --blue: #1CB0F6;
      --blue-shadow: #1899D6;
      --blue-wash: #DDF4FF;
      --yellow: #FFC800;
      --yellow-shadow: #E5B400;
      --orange: #FF9600;
      --orange-shadow: #E08500;
      --red: #FF4B4B;
      --ink: #3C3C3C;
      --ink-soft: #777777;
      --bg: #F7F9FC;
      --card: #FFFFFF;
      --border: #E5E5E5;
      --border-strong: #CECECE;
      --radius: 20px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; scroll-padding-top: 80px; }
    body {
      font-family: 'Nunito', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }
    a { color: inherit; text-decoration: none; }
    button { font: inherit; cursor: pointer; border: 0; background: none; }

    .container {
      max-width: 1140px;
      margin: 0 auto;
      padding: 0 20px;
    }
    section { padding: 68px 0; }

    /* 3D TACTILE BUTTONS */
    .btn3d {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      font-family: 'Nunito', sans-serif;
      font-weight: 800;
      font-size: 1rem;
      padding: 13px 26px;
      border-radius: 16px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      transition: transform 0.1s ease, box-shadow 0.1s ease;
      cursor: pointer;
      white-space: nowrap;
      border: 2px solid transparent;
    }
    .btn3d:active {
      transform: translateY(4px);
      box-shadow: 0 0 0 transparent !important;
    }
    .btn3d-green {
      background: var(--green);
      color: #fff;
      box-shadow: 0 4px 0 var(--green-shadow);
    }
    .btn3d-green:hover { background: #61E002; }

    .btn3d-blue {
      background: var(--blue);
      color: #fff;
      box-shadow: 0 4px 0 var(--blue-shadow);
    }
    .btn3d-blue:hover { background: #38BDFF; }

    .btn3d-yellow {
      background: var(--yellow);
      color: #fff;
      box-shadow: 0 4px 0 var(--yellow-shadow);
    }

    .btn3d-white {
      background: #fff;
      color: var(--ink);
      border: 2px solid var(--border-strong);
      box-shadow: 0 4px 0 var(--border-strong);
    }
    .btn3d-white:hover { background: #FAFAFA; }

    .btn3d-wa {
      background: #25D366;
      color: #fff;
      box-shadow: 0 4px 0 #1EBE5D;
    }

    .btn3d-block { width: 100%; }

    /* GAMIFIED BADGES & PILLS */
    .quest-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #fff;
      border: 2px solid var(--border-strong);
      border-radius: 99px;
      padding: 6px 14px;
      font-size: 0.85rem;
      font-weight: 800;
      box-shadow: 0 3px 0 var(--border-strong);
      margin-bottom: 16px;
    }
    .quest-pill.green {
      background: #E8FBD9;
      color: var(--green-dark);
      border-color: #BBEBA0;
      box-shadow: 0 3px 0 #A6E384;
    }
    .quest-pill.blue {
      background: var(--blue-wash);
      color: #0E7CB5;
      border-color: #B2E5FF;
      box-shadow: 0 3px 0 #9BDDFF;
    }

    /* HEADER */
    header {
      position: sticky;
      top: 0;
      z-index: 900;
      background: #fff;
      border-bottom: 2px solid var(--border);
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
      font-size: 1.35rem;
      font-weight: 900;
      color: var(--ink);
    }
    .logo i {
      width: 42px;
      height: 42px;
      border-radius: 14px;
      background: var(--green);
      display: grid;
      place-items: center;
      color: #fff;
      font-size: 1.25rem;
      box-shadow: 0 3px 0 var(--green-shadow);
    }
    .logo b { color: var(--blue); }
    .nav-links { display: flex; gap: 24px; font-weight: 800; font-size: 0.95rem; }
    .nav-links a:hover { color: var(--blue); }
    @media (max-width: 860px) { .nav-links { display: none; } }

    /* HERO SECTION */
    .hero {
      padding: 38px 0 28px;
      background: linear-gradient(180deg, #FFFFFF 0%, #F3F8FF 100%);
      border-bottom: 2px solid var(--border);
    }
    .hero .container {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 36px;
      align-items: center;
    }
    .hero h1 {
      font-size: clamp(2.3rem, 5vw, 3.8rem);
      font-weight: 900;
      line-height: 1.1;
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }
    .hero h1 span.highlight {
      color: var(--blue);
      position: relative;
    }
    .hero p.lead {
      font-size: 1.12rem;
      color: var(--ink-soft);
      line-height: 1.6;
      margin-bottom: 24px;
    }
    .hero-actions { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 28px; }

    /* XP TRACKER BAR */
    .xp-bar-box {
      background: #fff;
      border: 2px solid var(--border);
      border-radius: 16px;
      padding: 14px 18px;
      box-shadow: 0 4px 0 var(--border);
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .xp-icon {
      font-size: 1.6rem;
      color: var(--yellow);
    }
    .xp-info { flex: 1; }
    .xp-title {
      font-weight: 800;
      font-size: 0.88rem;
      display: flex;
      justify-content: space-between;
      margin-bottom: 6px;
    }
    .xp-progress {
      height: 10px;
      background: #EFEFEF;
      border-radius: 99px;
      overflow: hidden;
    }
    .xp-fill {
      height: 100%;
      width: 35%;
      background: var(--green);
      border-radius: 99px;
      transition: width 0.3s ease;
    }

    .hero-card {
      background: #fff;
      border: 3px solid var(--border-strong);
      border-radius: 28px;
      padding: 16px;
      box-shadow: 0 8px 0 var(--border-strong);
      position: relative;
    }
    .hero-card img {
      width: 100%;
      border-radius: 20px;
      display: block;
      aspect-ratio: 4/3;
      object-fit: cover;
    }
    .hero-card-badge {
      position: absolute;
      bottom: 28px;
      left: 28px;
      background: var(--yellow);
      color: #fff;
      font-weight: 900;
      padding: 8px 18px;
      border-radius: 99px;
      box-shadow: 0 4px 0 var(--yellow-shadow);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    @media (max-width: 860px) {
      .hero .container { grid-template-columns: 1fr; }
      .hero-card { display: none; }
    }

    /* SECTION HEADS */
    .sec-head { max-width: 720px; margin-bottom: 36px; }
    .sec-head h2 { font-size: clamp(2rem, 4.2vw, 2.9rem); font-weight: 900; line-height: 1.15; margin-bottom: 10px; }
    .sec-head p { color: var(--ink-soft); font-size: 1.05rem; }

    /* 3D CARDS */
    .card3d {
      background: var(--card);
      border: 2px solid var(--border);
      border-radius: var(--radius);
      box-shadow: 0 6px 0 var(--border);
      padding: 30px;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .card3d:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 0 var(--border);
    }

    /* SECTION 2 — STUDY PATHWAYS */
    .path-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
    .path-card {
      display: flex;
      flex-direction: column;
      position: relative;
    }
    .path-card.fast {
      background: #F1F9FF;
      border-color: #BBE5FF;
      box-shadow: 0 6px 0 #9FDCFF;
    }
    .path-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .path-card h3 { font-size: 1.8rem; font-weight: 900; margin-bottom: 8px; }
    .path-card p.sub { color: var(--ink-soft); margin-bottom: 18px; font-size: 0.95rem; }
    .path-card ul { list-style: none; margin-bottom: 20px; }
    .path-card li {
      padding: 6px 0 6px 26px;
      position: relative;
      font-weight: 700;
      font-size: 0.95rem;
    }
    .path-card li::before {
      content: "✔";
      position: absolute;
      left: 0;
      color: var(--green);
      font-size: 1rem;
    }
    .path-callout {
      background: #fff;
      border: 2px dashed var(--border-strong);
      border-radius: 14px;
      padding: 12px 16px;
      font-size: 0.88rem;
      margin-bottom: 22px;
      font-weight: 600;
    }
    .path-card .btn3d { margin-top: auto; }
    @media (max-width: 800px) { .path-grid { grid-template-columns: 1fr; } }

    /* SECTION 3 — POST STUDY (QUEST REWARDS) */
    .quest-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 18px;
    }
    .qc {
      background: #fff;
      border: 2px solid var(--border);
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 5px 0 var(--border);
    }
    .qc-icon {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      display: grid;
      place-items: center;
      font-size: 1.4rem;
      margin-bottom: 14px;
      color: #fff;
    }
    .qc:nth-child(1) .qc-icon { background: var(--blue); box-shadow: 0 3px 0 var(--blue-shadow); }
    .qc:nth-child(2) .qc-icon { background: var(--green); box-shadow: 0 3px 0 var(--green-shadow); }
    .qc:nth-child(3) .qc-icon { background: var(--orange); box-shadow: 0 3px 0 var(--orange-shadow); }
    .qc:nth-child(4) .qc-icon { background: var(--yellow); box-shadow: 0 3px 0 var(--yellow-shadow); }
    .qc h3 { font-size: 1.25rem; font-weight: 800; margin-bottom: 6px; }
    .qc p { font-size: 0.92rem; color: var(--ink-soft); line-height: 1.45; }

    /* SECTION 4 — CALCULATOR & QUEST WIZARD */
    .calc-wrap {
      display: grid;
      grid-template-columns: 1.4fr 0.6fr;
      gap: 24px;
      align-items: stretch;
    }
    .calc-card {
      background: #fff;
      border: 3px solid var(--border-strong);
      border-radius: 26px;
      padding: 32px;
      box-shadow: 0 8px 0 var(--border-strong);
    }
    .calc-top {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 2px dashed var(--border);
    }
    .calc-back {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      border: 2px solid var(--border-strong);
      display: grid;
      place-items: center;
      font-weight: 900;
      box-shadow: 0 2px 0 var(--border-strong);
      background: #fff;
    }
    .calc-back:hover { background: #F3F3F3; }
    .calc-dots { display: flex; gap: 8px; flex: 1; }
    .calc-dots i {
      flex: 1;
      height: 10px;
      border-radius: 99px;
      background: #EAEAEA;
      transition: background 0.25s ease;
    }
    .calc-dots i.on { background: var(--green); }
    .calc-step-text { font-weight: 900; font-size: 0.95rem; color: var(--ink); }

    .crumbs-bar { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 14px; }
    .crumb-pill {
      font-size: 0.8rem;
      font-weight: 800;
      background: var(--blue-wash);
      color: #0E7CB5;
      padding: 4px 12px;
      border-radius: 99px;
      cursor: pointer;
    }

    .q-title { font-size: clamp(1.8rem, 4vw, 2.4rem); font-weight: 900; margin-bottom: 6px; }
    .q-sub { color: var(--ink-soft); margin-bottom: 20px; font-size: 0.96rem; }

    .opt-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .opt-grid.c3 { grid-template-columns: repeat(3, 1fr); }
    .opt-grid.c1 { grid-template-columns: 1fr; }

    .tile-btn {
      background: #fff;
      border: 2px solid var(--border);
      border-radius: 18px;
      padding: 18px;
      box-shadow: 0 4px 0 var(--border);
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 3px;
      transition: transform 0.1s ease, box-shadow 0.1s ease, background 0.1s ease;
    }
    .tile-btn:hover { background: #FAFAFA; transform: translateY(-2px); }
    .tile-btn:active, .tile-btn.sel {
      background: #E8FBD9;
      border-color: #8CE04F;
      box-shadow: 0 4px 0 #7AC445;
      transform: translateY(2px);
    }
    .tile-btn b { font-size: 1.15rem; font-weight: 800; }
    .tile-btn span { font-size: 0.85rem; color: var(--ink-soft); }

    /* CELEBRATION GATE */
    .gate-celebrate {
      display: none;
      background: #E8FBD9;
      border: 2px solid #8CE04F;
      border-radius: 20px;
      padding: 24px;
      text-align: center;
      margin-top: 16px;
    }

    /* ASIDE GUIDE REWARD CARD */
    .reward-aside {
      background: var(--green);
      color: #fff;
      border-radius: 26px;
      padding: 30px;
      box-shadow: 0 8px 0 var(--green-shadow);
      display: flex;
      flex-direction: column;
    }
    .reward-aside h3 { font-size: 2rem; font-weight: 900; margin: 10px 0 16px; }
    .reward-list { list-style: none; margin-top: auto; }
    .reward-list li {
      padding: 10px 0;
      border-top: 1px solid rgba(255,255,255,0.25);
      font-weight: 700;
      font-size: 0.95rem;
      display: flex;
      gap: 10px;
    }

    @media (max-width: 900px) {
      .calc-wrap { grid-template-columns: 1fr; }
      .reward-aside { display: none; }
    }

    /* SECTION 5 — DESTINATIONS */
    .dest-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 22px; }
    .dest-box {
      background: #fff;
      border: 2px solid var(--border);
      border-radius: 22px;
      overflow: hidden;
      box-shadow: 0 6px 0 var(--border);
      display: flex;
      flex-direction: column;
    }
    .dest-thumb { height: 180px; position: relative; }
    .dest-thumb img { width: 100%; height: 100%; object-fit: cover; }
    .dest-badge {
      position: absolute;
      top: 12px;
      right: 12px;
      background: #fff;
      font-weight: 900;
      font-size: 0.78rem;
      padding: 5px 12px;
      border-radius: 99px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .dest-info { padding: 22px; display: flex; flex-direction: column; flex: 1; }
    .dest-info h3 { font-size: 1.5rem; font-weight: 900; margin-bottom: 6px; }
    .dest-info p { color: var(--ink-soft); font-size: 0.92rem; margin-bottom: 16px; }
    .dest-info .btn3d { margin-top: auto; }

    /* SECTION 6 — 360 SUPPORT */
    .support-track {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
    }
    .st-card {
      background: #fff;
      border: 2px solid var(--border);
      border-radius: 18px;
      padding: 22px;
      box-shadow: 0 4px 0 var(--border);
    }
    .st-step {
      font-weight: 900;
      font-size: 1.3rem;
      color: var(--blue);
      margin-bottom: 6px;
    }
    .st-card h3 { font-size: 1.15rem; font-weight: 800; margin-bottom: 4px; }
    .st-card p { font-size: 0.88rem; color: var(--ink-soft); line-height: 1.45; }

    /* SECTION 7 — TESTIMONIALS */
    .testi-row { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
    .tc {
      background: #fff;
      border: 2px solid var(--border);
      border-radius: 24px;
      overflow: hidden;
      box-shadow: 0 6px 0 var(--border);
      display: flex;
      flex-direction: column;
    }
    .tc-media { height: 210px; position: relative; }
    .tc-media img { width: 100%; height: 100%; object-fit: cover; }
    .tc-body { padding: 24px; display: flex; flex-direction: column; flex: 1; }
    .tc-quote { font-weight: 700; font-size: 1rem; color: var(--ink); margin-bottom: 16px; }
    .tc-author { display: flex; align-items: center; gap: 12px; margin-top: auto; }
    .tc-avatar {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--blue-wash);
      color: var(--blue);
      display: grid;
      place-items: center;
      font-weight: 900;
      font-size: 1.1rem;
    }
    @media (max-width: 800px) { .testi-row { grid-template-columns: 1fr; } }

    /* SECTION 8 — FAQS */
    .faq-box { max-width: 820px; margin: 0 auto; }
    details {
      background: #fff;
      border: 2px solid var(--border);
      border-radius: 16px;
      margin-bottom: 12px;
      box-shadow: 0 4px 0 var(--border);
      padding: 0 20px;
    }
    details[open] { border-color: #8CE04F; background: #F8FEF3; }
    summary {
      cursor: pointer;
      font-weight: 800;
      font-size: 1.08rem;
      padding: 18px 0;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    summary::-webkit-details-marker { display: none; }
    summary::after { content: "+"; font-size: 1.6rem; color: var(--green); font-weight: 900; }
    details[open] summary::after { content: "×"; color: var(--red); }
    details p { padding-bottom: 18px; color: var(--ink-soft); font-size: 0.95rem; }

    /* FINAL ENQUIRY CARD */
    .enquiry-duo-wrap {
      margin-top: 56px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 28px;
      align-items: stretch;
    }
    .enquiry-banner {
      background: var(--blue);
      color: #fff;
      border-radius: 28px;
      padding: 40px;
      box-shadow: 0 8px 0 var(--blue-shadow);
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .enquiry-banner h2 { font-size: clamp(2rem, 3.8vw, 2.6rem); font-weight: 900; margin-bottom: 12px; }
    .enquiry-banner p { font-size: 1.05rem; opacity: 0.95; margin-bottom: 24px; }

    .enquiry-form-card {
      background: #fff;
      border: 3px solid var(--border-strong);
      border-radius: 28px;
      padding: 36px;
      box-shadow: 0 8px 0 var(--border-strong);
    }
    .enquiry-form-card h3 { font-size: 1.8rem; font-weight: 900; margin-bottom: 6px; }
    .enquiry-form-card p.sub { color: var(--ink-soft); font-size: 0.94rem; margin-bottom: 20px; }

    .form-group { margin-bottom: 14px; }
    .form-input {
      width: 100%;
      height: 52px;
      border: 2px solid var(--border);
      border-radius: 14px;
      padding: 0 16px;
      font-size: 1rem;
      font-family: inherit;
      outline: none;
      transition: border-color 0.15s;
    }
    .form-input:focus { border-color: var(--blue); }

    .phone-group { display: flex; }
    .phone-prefix {
      height: 52px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0 16px;
      background: #EAEAEA;
      border: 2px solid var(--border);
      border-right: 0;
      border-radius: 14px 0 0 14px;
      font-weight: 800;
    }
    .phone-group .form-input { border-radius: 0 14px 14px 0; }

    @media (max-width: 860px) {
      .enquiry-duo-wrap { grid-template-columns: 1fr; }
    }

    /* FOOTER */
    footer {
      background: var(--green);
      color: #fff;
      padding: 38px 0 100px;
      margin-top: 60px;
    }
    .footer-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }
    .footer-links { display: flex; gap: 20px; font-weight: 800; }
    .footer-copy { margin-top: 18px; font-size: 0.85rem; opacity: 0.9; }

    /* MOBILE 3D STICKY BAR */
    .mbar3d {
      position: fixed;
      left: 0; right: 0; bottom: 0;
      z-index: 990;
      background: #fff;
      border-top: 2px solid var(--border);
      padding: 10px 16px;
      padding-bottom: max(10px, env(safe-area-inset-bottom));
      display: none;
      gap: 12px;
    }
    .mbar3d .btn3d { flex: 1; padding: 12px; font-size: 0.92rem; }
    @media (max-width: 768px) {
      .mbar3d { display: flex; }
      body { padding-bottom: 76px; }
    }
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="container nav">
      <a href="#top" class="logo">
        <i><i class="fa-solid fa-graduation-cap"></i></i>
        <span>University <b>Yatra</b></span>
      </a>
      <nav class="nav-links">
        <a href="#pathways">Pathways</a>
        <a href="#post-study">Post-Study</a>
        <a href="#calculator">Quest Calculator</a>
        <a href="#destinations">Destinations</a>
        <a href="#support">Support</a>
        <a href="#faqs">FAQs</a>
      </nav>
      <a class="btn3d btn3d-green" href="#calculator">Start Quest ⚡</a>
    </div>
  </header>

  <main id="top">
    <!-- SECTION 1 — HERO -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <span class="quest-pill green"><i class="fa-solid fa-trophy"></i> Study Abroad Quest 2026</span>
          <h1>Study Abroad After 12th or <span class="highlight">Graduation</span></h1>
          <p class="lead">
            Explore international universities, unlock scholarships, and calculate exact costs before making your destination decision.
          </p>
          
          <div class="hero-actions">
            <a class="btn3d btn3d-green" href="#destinations">
              Explore Universities <i class="fa-solid fa-arrow-right"></i>
            </a>
            <a class="btn3d btn3d-white" href="#pathways">
              Compare Pathways
            </a>
          </div>

          <!-- XP QUEST PROGRESS BAR -->
          <div class="xp-bar-box">
            <div class="xp-icon"><i class="fa-solid fa-bolt"></i></div>
            <div class="xp-info">
              <div class="xp-title">
                <span>Quest Status: Free Assessment</span>
                <span style="color:var(--green)">Level 1 🎓</span>
              </div>
              <div class="xp-progress">
                <div class="xp-fill"></div>
              </div>
            </div>
          </div>
        </div>

        <div class="hero-card">
          <img src="assets/images/study-abroad.webp" alt="Students studying abroad" />
          <div class="hero-card-badge">
            <i class="fa-solid fa-star"></i> 100% Free Guidance
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2 — STUDY PATHWAYS -->
    <section id="pathways">
      <div class="container">
        <div class="sec-head">
          <span class="quest-pill blue"><i class="fa-solid fa-route"></i> Study Routes</span>
          <h2>Direct Admission or Fast Track? <span style="color:var(--blue)">Compare Your Options.</span></h2>
          <p>Understand how each pathway works before choosing your programme.</p>
        </div>

        <div class="path-grid">
          <!-- Direct Card -->
          <div class="card3d path-card">
            <div class="path-header">
              <span style="font-weight:900;color:var(--blue);text-transform:uppercase;font-size:0.8rem">On-Campus Overseas</span>
              <span class="quest-pill blue" style="margin:0">Direct Route</span>
            </div>
            <h3>DIRECT STUDY ABROAD</h3>
            <p class="sub"><strong>Begin Your Degree at an Overseas University</strong><br />Study at your chosen international university from the first semester.</p>
            <ul>
              <li>Apply directly to an overseas university.</li>
              <li>Choose your course and study destination.</li>
              <li>Complete your degree on campus abroad.</li>
            </ul>
            <div class="path-callout">
              <strong>Best if:</strong> your academics, English test scores and budget are ready for on-campus education from day one.
            </div>
            <a href="#destinations" class="btn3d btn3d-blue">Explore Direct Programmes</a>
          </div>

          <!-- Fast Track Card -->
          <div class="card3d path-card fast">
            <div class="path-header">
              <span style="font-weight:900;color:var(--green-dark);text-transform:uppercase;font-size:0.8rem">Smart Credit Transfer</span>
              <span class="quest-pill green" style="margin:0">Save 40% 💰</span>
            </div>
            <h3>FAST TRACK STUDY ABROAD</h3>
            <p class="sub"><strong>Complete Phase 1 in India. Continue Abroad.</strong><br />Start online in India for 8–12 months, then transfer credits to a partner university abroad.</p>
            <ul>
              <li>Begin your selected programme online in India.</li>
              <li>Complete the required academic phase.</li>
              <li>Transfer eligible credits and continue abroad.</li>
            </ul>
            <div class="path-callout">
              <strong>Best if:</strong> you want to save up to 40% on overall expenses while building your profile.
            </div>
            <a href="#calculator" class="btn3d btn3d-green">View Fast Track Programmes</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3 — POST-STUDY OPPORTUNITIES -->
    <section id="post-study" style="padding-top:0">
      <div class="container">
        <div class="sec-head">
          <span class="quest-pill green"><i class="fa-solid fa-award"></i> Post-Study Options</span>
          <h2>What Can You Do <span style="color:var(--green)">After Graduating Abroad?</span></h2>
          <p>Your options after graduation depend on your degree, destination and current immigration rules.</p>
        </div>

        <div class="quest-grid">
          <div class="qc">
            <div class="qc-icon"><i class="fa-solid fa-briefcase"></i></div>
            <h3>Post-Study Work Permits</h3>
            <p>Access legal post-study work rights (UK Graduate Visa, Canada PGWP, Australia PSW) to gain global work experience.</p>
          </div>
          <div class="qc">
            <div class="qc-icon"><i class="fa-solid fa-building-columns"></i></div>
            <h3>Graduate Employment</h3>
            <p>Attend campus placements, industry co-ops, and interview with multinational recruiters.</p>
          </div>
          <div class="qc">
            <div class="qc-icon"><i class="fa-solid fa-graduation-cap"></i></div>
            <h3>Further Specialisation</h3>
            <p>Progress seamlessly into Master's or specialized PhD research programs worldwide.</p>
          </div>
          <div class="qc">
            <div class="qc-icon"><i class="fa-solid fa-passport"></i></div>
            <h3>PR &amp; Immigration Routes</h3>
            <p>Explore legal skilled migration points systems and employer sponsorship pathways.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4 — QUEST CALCULATOR -->
    <section id="calculator">
      <div class="container">
        <div class="sec-head">
          <span class="quest-pill blue"><i class="fa-solid fa-calculator"></i> Study Budget Calculator</span>
          <h2>What Is Your Budget for <span style="color:var(--blue)">Studying Abroad?</span></h2>
          <p>Estimate overall expenses and download your free country guide.</p>
        </div>

        <div class="calc-wrap">
          <div class="calc-card" id="calcBox">
            <div class="calc-top">
              <button class="calc-back" id="qBackBtn" hidden>←</button>
              <div class="calc-dots" id="qDots">
                <i class="on"></i><i></i><i></i><i></i>
              </div>
              <span class="calc-step-text" id="qStepText">Step 1/4</span>
            </div>

            <div class="crumbs-bar" id="qCrumbs"></div>

            <div id="qView">
              <!-- Dynamically populated via JS -->
            </div>

            <!-- Gate View -->
            <div id="qGate" style="display:none">
              <h3 class="q-title">Your Guide &amp; Budget is Ready! 🎓</h3>
              <p class="q-sub">Enter your details to download the country guide PDF immediately.</p>
              <form id="qLeadForm">
                <div class="form-group">
                  <input class="form-input" id="qName" placeholder="Your Full Name" required />
                </div>
                <div class="form-group phone-group">
                  <span class="phone-prefix">+91</span>
                  <input class="form-input" id="qPhone" type="tel" pattern="[0-9]{10}" maxlength="10" placeholder="10-digit WhatsApp Number" required />
                </div>
                <div class="form-group">
                  <input class="form-input" id="qEmail" type="email" placeholder="Email Address" required />
                </div>
                <button class="btn3d btn3d-green btn3d-block" type="submit" id="qSubmitBtn">
                  Download Free Country Guide ↓
                </button>
              </form>
            </div>

            <!-- Done View -->
            <div id="qDone" style="display:none" class="gate-celebrate">
              <h3 style="color:var(--green-dark);font-size:1.6rem;font-weight:900;margin-bottom:8px">🎉 Quest Completed!</h3>
              <p style="color:var(--ink);font-weight:700;margin-bottom:16px" id="qDoneSub">Your guide should download automatically. If not, tap below.</p>
              <div id="qDownloadBox" style="margin-bottom:14px"></div>
              <a class="btn3d btn3d-wa btn3d-block" id="qWaLink" href="#" target="_blank" rel="noopener">
                <i class="fa-brands fa-whatsapp"></i> Chat with Senior Counsellor
              </a>
            </div>
          </div>

          <!-- Aside Reward Preview -->
          <aside class="reward-aside">
            <span class="quest-pill green" style="background:#fff;color:var(--green-dark);width:max-content">Free Country Guide</span>
            <h3 id="asideTitle">Your Country Guide.</h3>
            <ul class="reward-list">
              <li><i class="fa-solid fa-circle-check"></i> Real Tuition &amp; Living Costs</li>
              <li><i class="fa-solid fa-circle-check"></i> Step-by-Step Admission Flow</li>
              <li><i class="fa-solid fa-circle-check"></i> IELTS &amp; Visa Documentation</li>
              <li><i class="fa-solid fa-circle-check"></i> Blocked Account / GIC Setup</li>
              <li><i class="fa-solid fa-circle-check"></i> Post-Study Stay Back Rights</li>
            </ul>
          </aside>
        </div>
      </div>
    </section>

    <!-- SECTION 5 — DESTINATIONS -->
    <section id="destinations" style="padding-top:0">
      <div class="container">
        <div class="sec-head">
          <span class="quest-pill blue">Study Destinations</span>
          <h2>Explore Countries. Compare Universities. <span style="color:var(--blue)">Choose Your Course.</span></h2>
          <p>Looking for a Bachelor's in Germany or a Master's in Canada? Explore top academic hubs.</p>
        </div>

        <div class="dest-grid">
          <div class="dest-box">
            <div class="dest-thumb">
              <img src="assets/images/country/germany.webp" alt="Germany" />
              <span class="dest-badge">Zero / Low Tuition</span>
            </div>
            <div class="dest-info">
              <h3>GERMANY</h3>
              <p>Explore world-class technical education at public and private German universities.</p>
              <button class="btn3d btn3d-green" onclick="pickCountry('germany')">Get Germany Guide</button>
            </div>
          </div>

          <div class="dest-box">
            <div class="dest-thumb">
              <img src="assets/images/country/canada.webp" alt="Canada" />
              <span class="dest-badge">3-Yr PGWP</span>
            </div>
            <div class="dest-info">
              <h3>CANADA</h3>
              <p>Compare colleges and universities offering high employment and co-op work terms.</p>
              <button class="btn3d btn3d-blue" onclick="pickCountry('canada')">Get Canada Guide</button>
            </div>
          </div>

          <div class="dest-box">
            <div class="dest-thumb">
              <img src="assets/images/country/uk.webp" alt="United Kingdom" />
              <span class="dest-badge">1-Year Masters</span>
            </div>
            <div class="dest-info">
              <h3>UNITED KINGDOM</h3>
              <p>Accelerate your career with globally renowned 1-year Master's and 3-year Bachelor's.</p>
              <button class="btn3d btn3d-yellow" onclick="pickCountry('uk')">Get UK Guide</button>
            </div>
          </div>

          <div class="dest-box">
            <div class="dest-thumb">
              <img src="assets/images/country/australia.webp" alt="Australia" />
              <span class="dest-badge">Post-Study Work</span>
            </div>
            <div class="dest-info">
              <h3>AUSTRALIA</h3>
              <p>Top global universities with exceptional quality of life and post-study work rights.</p>
              <button class="btn3d btn3d-green" onclick="pickCountry('australia')">Get Australia Guide</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 6 — 360 SUPPORT -->
    <section id="support" style="padding-top:0">
      <div class="container">
        <div class="sec-head">
          <span class="quest-pill green">360° Guidance</span>
          <h2>From University Application <span style="color:var(--green)">to Student Visa.</span></h2>
          <p>Every milestone handled with precision and care.</p>
        </div>

        <div class="support-track">
          <div class="st-card"><div class="st-step">01</div><h3>Course Shortlisting</h3><p>Compare universities based on marks and budget preferences.</p></div>
          <div class="st-card"><div class="st-step">02</div><h3>Admission &amp; SOP</h3><p>Draft compelling SOPs and compile academic applications.</p></div>
          <div class="st-card"><div class="st-step">03</div><h3>English Test Prep</h3><p>Prepare for IELTS, TOEFL, PTE, or explore waiver eligibility.</p></div>
          <div class="st-card"><div class="st-step">04</div><h3>Loans &amp; Scholarships</h3><p>Explore eligible university scholarships and bank loan sanctions.</p></div>
          <div class="st-card"><div class="st-step">05</div><h3>Student Visa</h3><p>Prepare financial proofs and ace the embassy visa interview.</p></div>
          <div class="st-card"><div class="st-step">06</div><h3>Housing &amp; Forex</h3><p>Book verified student accommodation and international flight tickets.</p></div>
          <div class="st-card"><div class="st-step">07</div><h3>Pre-Departure</h3><p>Packing checklist and campus orientation briefing.</p></div>
        </div>
      </div>
    </section>

    <!-- SECTION 7 — TESTIMONIALS -->
    <section id="testimonials" style="padding-top:0">
      <div class="container">
        <div class="sec-head">
          <span class="quest-pill blue">Verified Success</span>
          <h2>Trusted Guidance, <span style="color:var(--blue)">Real Results.</span></h2>
          <p>Real stories of Indian students who reached their dream campuses.</p>
        </div>

        <div class="testi-row">
          <div class="tc">
            <div class="tc-media">
              <img src="assets/images/consultation-desk.webp" alt="1-on-1 Mentorship" />
            </div>
            <div class="tc-body">
              <div class="tc-quote">
                "The 1-on-1 video call completely sorted out my admission timeline for Germany. Transparent advice without any hidden charges!"
              </div>
              <div class="tc-author">
                <div class="tc-avatar">R</div>
                <div><b>Rohan Sharma</b><br><small style="color:var(--ink-soft)">M.Sc. Germany Admitted</small></div>
              </div>
            </div>
          </div>

          <div class="tc">
            <div class="tc-media">
              <img src="assets/images/student-graduation-celebration.webp" alt="Visa Celebrations" />
            </div>
            <div class="tc-body">
              <div class="tc-quote">
                "Got my Canada visa in just 3 weeks with a $4,000 entrance scholarship! Super friendly team that kept my parents informed throughout."
              </div>
              <div class="tc-author">
                <div class="tc-avatar" style="background:#FFF3D1;color:var(--yellow-shadow)">P</div>
                <div><b>Priya Patel</b><br><small style="color:var(--ink-soft)">B.Sc. Canada Admitted</small></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8 — FAQS + ENQUIRY -->
    <section id="faqs" style="padding-top:0">
      <div class="container">
        <div class="sec-head" style="text-align:center;margin-inline:auto">
          <span class="quest-pill green">FAQs</span>
          <h2>Study Abroad: <span style="color:var(--green)">Common Questions Answered.</span></h2>
        </div>

        <div class="faq-box">
          <details><summary>1. Can I study abroad after 12th?</summary><p>Yes. You can apply for Bachelor's and other undergraduate programmes after Class 12, depending on your academic marks and university eligibility.</p></details>
          <details><summary>2. Can I study abroad after graduation?</summary><p>Yes. You can apply for Master's and postgraduate programmes based on your Bachelor's degree and university criteria.</p></details>
          <details><summary>3. What is the difference between Direct and Fast Track?</summary><p>Direct Study starts on campus abroad from semester one. Fast Track programmes start online in India for 8-12 months before transferring credits to an overseas partner university.</p></details>
          <details><summary>4. How much does it cost to study abroad?</summary><p>Costs vary by destination, university and lifestyle. Tuition fees and living expenses should both be factored into your budget.</p></details>
          <details><summary>5. Do I need IELTS to study abroad?</summary><p>Many universities accept alternative English tests (TOEFL, PTE, Duolingo) or medium of instruction (MOI) waivers.</p></details>
          <details><summary>6. Can I get a scholarship or education loan?</summary><p>Yes. Scholarships depend on your academic score, and collateral-free education loans are available through our banking partners.</p></details>
          <details><summary>7. How long does the admission process take?</summary><p>Ideally 6 to 10 months before your intended intake to allow sufficient time for visa processing.</p></details>
          <details><summary>8. Can I work after completing my degree abroad?</summary><p>Most leading countries (UK, Canada, Germany, Australia) offer 18 months to 3 years of post-study work permits for eligible graduates.</p></details>
        </div>

        <!-- FINAL ENQUIRY CARD -->
        <div class="enquiry-duo-wrap">
          <div class="enquiry-banner">
            <h2>Ready to Start Your Yatra?</h2>
            <p>Tell us your target country and course. Our senior counsellors will help you evaluate universities and visas.</p>
            <div style="display:flex;gap:12px;flex-wrap:wrap">
              <a class="btn3d btn3d-green" href="#calculator">Start Quest ↑</a>
              <a class="btn3d btn3d-wa" href="https://wa.me/919217368750?text=Hi%20University%20Yatra%2C%20I%20want%20to%20know%20more%20about%20study%20abroad%20programmes." target="_blank" rel="noopener">
                <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp
              </a>
            </div>
          </div>

          <div class="enquiry-form-card">
            <h3>Tell Us What You Want to Study.</h3>
            <p class="sub">Fill in your details below for personalized advice.</p>
            <form id="finalForm">
              <div class="form-group">
                <input class="form-input" id="eqName" placeholder="Full Name" required autocomplete="name" />
              </div>
              <div class="form-group phone-group">
                <span class="phone-prefix">+91</span>
                <input class="form-input" id="eqMobile" type="tel" pattern="[0-9]{10}" maxlength="10" placeholder="10-digit WhatsApp Number" required autocomplete="tel" />
              </div>
              <div class="form-group">
                <input class="form-input" id="eqEmail" type="email" placeholder="Email Address" required autocomplete="email" />
              </div>
              <button class="btn3d btn3d-blue btn3d-block" type="submit" id="finalSubmitBtn">
                Submit Study Enquiry ➔
              </button>
            </form>
            <div id="finalSuccess" style="display:none;background:#E8FBD9;border:2px solid #8CE04F;border-radius:16px;padding:20px;text-align:center;margin-top:14px">
              <h4 style="color:var(--green-dark);font-size:1.3rem;font-weight:900">Thank you!</h4>
              <p style="color:var(--ink);font-weight:700">Your enquiry has been received. Our senior counselling team will call you shortly.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer>
    <div class="container">
      <div class="footer-inner">
        <a href="#top" class="logo" style="color:#fff">
          <i style="background:#fff;color:var(--green)"><i class="fa-solid fa-graduation-cap"></i></i>
          <span>University <b>Yatra</b></span>
        </a>
        <div class="footer-links">
          <a href="#pathways">Pathways</a>
          <a href="#calculator">Calculator</a>
          <a href="#destinations">Destinations</a>
          <a href="#faqs">FAQs</a>
        </div>
      </div>
      <p class="footer-copy">
        &copy; 2026 Future Yatra Private Limited. All rights reserved. University Yatra provides educational guidance only.
      </p>
    </div>
  </footer>

  <!-- MOBILE STICKY BAR -->
  <div class="mbar3d">
    <a class="btn3d btn3d-green" href="#calculator">Start Quest ⚡</a>
    <a class="btn3d btn3d-wa" href="https://wa.me/919217368750?text=Hi%20University%20Yatra%2C%20I%20want%20to%20know%20more%20about%20study%20abroad%20programmes." target="_blank" rel="noopener">
      <i class="fa-brands fa-whatsapp"></i> WhatsApp
    </a>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js"></script>
  <script>
    (function () {
      const WA = '919217368750';
      const COUNTRIES = [
        { k: 'germany', n: 'Germany', pdf: 'assets/pdfs/direct/germany.pdf' },
        { k: 'canada', n: 'Canada', pdf: 'assets/pdfs/direct/canada.pdf' },
        { k: 'uk', n: 'United Kingdom', pdf: '' },
        { k: 'australia', n: 'Australia', pdf: '' },
        { k: 'usa', n: 'United States', pdf: '' },
        { k: 'other', n: 'Other Countries', pdf: '' }
      ];
      const C = {}; COUNTRIES.forEach(c => C[c.k] = c);
      const S = { country: null, level: null, path: null, time: null };
      let step = 0;

      const $ = id => document.getElementById(id);

      function renderStep() {
        const v = $('qView');
        const gate = $('qGate');
        const done = $('qDone');
        const back = $('qBackBtn');
        const text = $('qStepText');
        const crumbs = $('qCrumbs');

        gate.style.display = 'none';
        done.style.display = 'none';
        v.style.display = 'block';

        // Dots
        const dots = $('qDots').children;
        for (let i = 0; i < dots.length; i++) {
          dots[i].className = i <= step ? 'on' : '';
        }
        text.textContent = `Step ${Math.min(step + 1, 4)}/4`;
        back.hidden = step === 0;

        // Crumbs
        crumbs.innerHTML = '';
        if (S.country) addCrumb(C[S.country].n, 0);
        if (S.level) addCrumb(S.level, 1);
        if (S.path) addCrumb(S.path, 2);
        if (S.time) addCrumb(S.time, 3);

        v.innerHTML = '';

        if (step === 0) {
          $('asideTitle').textContent = 'Your Country Guide.';
          v.innerHTML = `<h3 class="q-title">Where do you want <span style="color:var(--green)">to study?</span></h3><p class="q-sub">Select your dream destination to unlock costs &amp; guide.</p><div class="opt-grid"></div>`;
          const grid = v.querySelector('.opt-grid');
          COUNTRIES.forEach(c => {
            const b = document.createElement('button');
            b.className = 'tile-btn' + (S.country === c.k ? ' sel' : '');
            b.innerHTML = `<b>${c.n}</b><span>Country Guide</span>`;
            b.onclick = () => { S.country = c.k; next(); };
            grid.appendChild(b);
          });
        } else if (step === 1) {
          $('asideTitle').textContent = `Study in ${C[S.country].n}.`;
          v.innerHTML = `<h3 class="q-title">What is your <span style="color:var(--blue)">qualification?</span></h3><p class="q-sub">Choose your target level of study abroad.</p><div class="opt-grid c3"></div>`;
          const grid = v.querySelector('.opt-grid');
          [['Class 12th', "Bachelor's"], ['Graduation', "Master's"], ['Postgrad', 'MBA / Specialization']].forEach(l => {
            const b = document.createElement('button');
            b.className = 'tile-btn' + (S.level === l[0] ? ' sel' : '');
            b.innerHTML = `<b>${l[0]}</b><span>${l[1]}</span>`;
            b.onclick = () => { S.level = l[0]; next(); };
            grid.appendChild(b);
          });
        } else if (step === 2) {
          v.innerHTML = `<h3 class="q-title">Which route <span style="color:var(--green)">interests you?</span></h3><p class="q-sub">Choose between direct on-campus or fast-track savings.</p><div class="opt-grid c1"></div>`;
          const grid = v.querySelector('.opt-grid');
          [['Direct Study Abroad', 'Study on campus overseas from day one'], ['Fast Track Study Abroad', 'Start online in India (save 40%), finish on campus abroad'], ['Compare Both Options', 'See side-by-side fee & time breakdown']].forEach(p => {
            const b = document.createElement('button');
            b.className = 'tile-btn' + (S.path === p[0] ? ' sel' : '');
            b.innerHTML = `<b>${p[0]}</b><span>${p[1]}</span>`;
            b.onclick = () => { S.path = p[0]; next(); };
            grid.appendChild(b);
          });
        } else if (step === 3) {
          v.innerHTML = `<h3 class="q-title">When do you plan <span style="color:var(--blue)">to start?</span></h3><p class="q-sub">Helps match upcoming intake deadlines &amp; visa slots.</p><div class="opt-grid"></div>`;
          const grid = v.querySelector('.opt-grid');
          [['Next 6 Months', 'Ready to fly'], ['6 - 12 Months', 'Planning ahead'], ['12+ Months', 'Early bird'], ['Just Exploring', 'Learning options']].forEach(t => {
            const b = document.createElement('button');
            b.className = 'tile-btn' + (S.time === t[0] ? ' sel' : '');
            b.innerHTML = `<b>${t[0]}</b><span>${t[1]}</span>`;
            b.onclick = () => { S.time = t[0]; next(); };
            grid.appendChild(b);
          });
        } else {
          v.style.display = 'none';
          gate.style.display = 'block';
        }
      }

      function addCrumb(text, s) {
        const b = document.createElement('button');
        b.className = 'crumb-pill';
        b.textContent = text + ' ✎';
        b.onclick = () => { step = s; renderStep(); };
        $('qCrumbs').appendChild(b);
      }

      function next() {
        step++;
        renderStep();
      }

      $('qBackBtn').onclick = () => {
        if (step > 0) { step--; renderStep(); }
      };

      window.pickCountry = function (k) {
        S.country = k;
        step = 1;
        renderStep();
        $('calculator').scrollIntoView({ behavior: 'smooth', block: 'start' });
      };

      // Form Handling
      $('qLeadForm').addEventListener('submit', async e => {
        e.preventDefault();
        const name = $('qName').value.trim();
        const phone = $('qPhone').value.trim();
        const email = $('qEmail').value.trim();

        if (!name || phone.length !== 10 || !email) {
          alert('Please fill in all details with a valid 10-digit mobile number.');
          return;
        }

        $('qGate').style.display = 'none';
        $('qDone').style.display = 'block';

        const c = C[S.country] || { n: 'Study Abroad', pdf: '' };
        const dBox = $('qDownloadBox');
        dBox.innerHTML = '';

        if (c.pdf) {
          const a = document.createElement('a');
          a.href = c.pdf;
          a.setAttribute('download', `${c.n}_Guide_University_Yatra.pdf`);
          a.className = 'btn3d btn3d-green btn3d-block';
          a.innerHTML = `<i class="fa-solid fa-file-pdf"></i> Download ${c.n} Guide (PDF)`;
          dBox.appendChild(a);
          setTimeout(() => a.click(), 300);
        } else {
          // Dynamic fallback PDF
          const btn = document.createElement('button');
          btn.className = 'btn3d btn3d-green btn3d-block';
          btn.innerHTML = `<i class="fa-solid fa-file-pdf"></i> Download ${c.n} Guide (PDF)`;
          btn.onclick = () => alert('Your guide download is starting...');
          dBox.appendChild(btn);
        }

        const msg = `Hi University Yatra, I am ${name}. I completed the Study Abroad Quest for ${c.n} (${S.path}, starting ${S.time}). Please connect me with a senior counsellor.`;
        $('qWaLink').href = `https://wa.me/${WA}?text=${encodeURIComponent(msg)}`;
      });

      // Final Enquiry Form
      $('finalForm').addEventListener('submit', e => {
        e.preventDefault();
        $('finalForm').style.display = 'none';
        $('finalSuccess').style.display = 'block';
      });

      renderStep();
    })();
  </script>
</body>
</html>
"""

with open('gamified.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated gamified.html successfully! Length:", len(html_content))
