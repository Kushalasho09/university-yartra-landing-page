import re

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>University Yatra | Study Abroad After 12th & Graduation</title>
  <meta name="description" content="Explore international universities, compare Direct vs Fast Track study pathways, estimate costs, and download free country guides for Indian students." />
  
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <link rel="stylesheet" href="css/styles.css" />
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="container nav">
      <a href="#top" class="logo" aria-label="University Yatra">
        <i><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/></svg></i>
        <span>University <b>Yatra</b></span>
      </a>
      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#pathways">Study Pathways</a>
        <a href="#post-study">Post-Study</a>
        <a href="#calculator">Cost Calculator</a>
        <a href="#destinations">Destinations</a>
        <a href="#support">360° Support</a>
        <a href="#faqs">FAQs</a>
      </nav>
      <div class="nav-actions">
        <a class="btn btn-primary" href="#calculator">Get Free Guide</a>
      </div>
    </div>
  </header>

  <main id="top">
    <!-- SECTION 1 — HERO -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <span class="sticker">Study Abroad After 12th &amp; Graduation</span>
          <h1>Study Abroad After 12th or <span class="box">Graduation</span></h1>
          <p class="lead">
            Explore international universities and degree programmes. Compare countries, admission requirements and tuition fees before deciding where to study.
          </p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#destinations">
              Explore Universities <i class="fa-solid fa-arrow-right"></i>
            </a>
            <a class="btn" href="#pathways">
              Compare Study Pathways
            </a>
          </div>
          <div class="hero-trust">
            <span><i class="fa-solid fa-circle-check"></i> 100% Free Guidance</span>
            <span><i class="fa-solid fa-circle-check"></i> Top Global Universities</span>
            <span><i class="fa-solid fa-circle-check"></i> Fast-Track Credit Transfer</span>
          </div>
        </div>
        <div class="hero-card">
          <img src="assets/images/study-abroad.webp" alt="Students studying abroad at global campus" loading="eager" />
          <div class="hero-card-badge">
            <i class="fa-solid fa-graduation-cap"></i> Verified Admissions 2026
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2 — STUDY PATHWAYS -->
    <section class="section" id="pathways">
      <div class="container">
        <div class="sec-head">
          <span class="sticker pink">Study Pathways</span>
          <h2>Direct Admission or Fast Track? <span class="hl">Compare Your Study Options.</span></h2>
          <p>There is more than one way to pursue an international degree. Understand how each pathway works before choosing your programme.</p>
        </div>

        <div class="path-grid">
          <!-- Direct Study Abroad -->
          <div class="path">
            <div class="eyebrow">On-Campus Overseas</div>
            <h3>DIRECT STUDY ABROAD</h3>
            <p><strong>Begin Your Degree at an Overseas University</strong><br />Apply for an undergraduate or postgraduate programme and study at your chosen international university from the first semester.</p>
            <ul>
              <li>Apply directly to an overseas university.</li>
              <li>Choose your course and study destination.</li>
              <li>Complete your degree on campus abroad.</li>
            </ul>
            <p class="best">
              <strong>Best if:</strong> your academics, English test scores and budget are ready for full on-campus education from day one.
            </p>
            <a href="#destinations" class="btn">Explore Direct Programmes</a>
          </div>

          <!-- Fast Track Study Abroad -->
          <div class="path fast">
            <span class="sticker sun">Budget-Smart Pathway</span>
            <div class="eyebrow">Smart Credit Transfer</div>
            <h3>FAST TRACK STUDY ABROAD</h3>
            <p><strong>Complete the Initial Study Phase in India. Continue Abroad.</strong><br />Start selected programmes online in India for approximately 8–12 months, then continue your degree at a partner university abroad, subject to eligibility and credit-transfer approval.</p>
            <ul>
              <li>Begin your selected programme online in India.</li>
              <li>Complete the required academic phase.</li>
              <li>Transfer eligible credits and continue abroad.</li>
            </ul>
            <p class="best">
              <strong>Best if:</strong> you want to save up to 40% on overall expenses, build your academic profile, or need a flexible start.
            </p>
            <a href="#calculator" class="btn btn-lime">View Fast Track Programmes</a>
            <p class="fine">*Credit-transfer terms and eligibility vary by programme and partner university.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3 — POST-STUDY OPPORTUNITIES (BELOW PATHWAY SECTION) -->
    <section class="section" id="post-study" style="padding-top:0">
      <div class="container">
        <div class="sec-head">
          <span class="sticker sun">Post-Study Opportunities</span>
          <h2>What Can You Do <span class="hl">After Graduating Abroad?</span></h2>
          <p>Your options after graduation depend on your degree, destination and current immigration rules.</p>
        </div>

        <div class="inside">
          <div class="ic">
            <div class="n">01</div>
            <h3>Post-Study Work Permits</h3>
            <p>Access legal post-study work rights (such as UK Graduate Visa, Canada PGWP, or Australia PSW) to gain international work experience.</p>
          </div>
          <div class="ic">
            <div class="n">02</div>
            <h3>Graduate Employment Opportunities</h3>
            <p>Participate in campus recruitment drives, industry internships, and professional networking with multinational employers.</p>
          </div>
          <div class="ic">
            <div class="n">03</div>
            <h3>Further Studies &amp; Specialisation</h3>
            <p>Seamlessly transition from undergraduate degrees into Master's or specialized doctoral research programs worldwide.</p>
          </div>
          <div class="ic">
            <div class="n">04</div>
            <h3>Country-Specific Work &amp; Immigration</h3>
            <p>Explore legal long-term settlement, skilled worker sponsorship, and residency routes tailored to high-demand skills.</p>
          </div>
        </div>

        <div class="sec-cta-wrap">
          <p>
            <i class="fa-solid fa-circle-info hl"></i> Post-study work eligibility and duration vary by country and immigration policy. Employment or visa approval is not guaranteed.
          </p>
          <a class="btn btn-primary" href="#enquiry">Explore Post-Study Options</a>
        </div>
      </div>
    </section>

    <!-- SECTION 4 — STUDY ABROAD COST CALCULATOR -->
    <section class="calc-sec" id="calculator">
      <div class="container">
        <div class="sec-head">
          <span class="sticker">Cost Calculator &amp; Free Guide</span>
          <h2>What Is Your Budget for <span class="hl">Studying Abroad?</span></h2>
          <p>Tuition fees are only one part of your study abroad expenses. Estimate the overall budget and download a free comprehensive country guide.</p>
        </div>

        <div class="calc-wrap">
          <div class="calc" id="calc">
            <span class="badge">Takes 30 sec</span>
            <div class="top">
              <button class="back" id="backBtn" aria-label="Go back" hidden>←</button>
              <div class="dots" id="dots"><i class="on"></i><i></i><i></i><i></i></div>
              <span class="stepno" id="stepNo">1/4</span>
            </div>
            <div class="crumbs" id="crumbs"></div>

            <!-- DYNAMIC STEP VIEW -->
            <div id="stepView"></div>

            <!-- GATE VIEW (LEAD CAPTURE & PDF DELIVERY) -->
            <div class="gate" id="gateView" hidden>
              <div id="gateForm">
                <span class="tick">✓</span>
                <div class="q" id="gateTitle">Your guide is ready.</div>
                <p class="qsub" id="gateSub">Enter your details to download it free.</p>
                <form class="form" id="leadForm">
                  <input type="hidden" name="country" id="h_country" />
                  <input type="hidden" name="level" id="h_level" />
                  <input type="hidden" name="pathway" id="h_path" />
                  <input type="hidden" name="timeline" id="h_time" />
                  
                  <input class="fi" name="name" id="f_name" placeholder="Your full name" required autocomplete="name" />
                  <div class="r2">
                    <div class="ph">
                      <span>+91</span>
                      <input class="fi" name="phone" id="f_phone" type="tel" inputmode="numeric" pattern="[0-9]{10}" maxlength="10" placeholder="10-digit WhatsApp number" required />
                    </div>
                    <input class="fi" name="email" id="f_email" type="email" placeholder="Email address" required autocomplete="email" />
                  </div>
                  <button class="btn btn-primary btn-block" type="submit" id="gateBtn">
                    Download Free PDF Guide ↓
                  </button>
                  <p class="cons">
                    By continuing you agree to be contacted by University Yatra via call, SMS, email and WhatsApp. We respect your privacy.
                  </p>
                </form>
              </div>

              <!-- DONE VIEW -->
              <div class="done" id="doneView">
                <span class="tick">✓</span>
                <div class="q" id="doneTitle">Done! Check your downloads.</div>
                <p class="qsub" id="doneSub"></p>
                <div class="dl" id="dl"></div>
                <a id="waNext" class="btn btn-wa btn-block" href="#" target="_blank" rel="noopener">
                  <i class="fa-brands fa-whatsapp"></i> Talk to a Counsellor on WhatsApp
                </a>
                <p class="fine" style="color:var(--muted);margin-top:14px">
                  A University Yatra senior counsellor will also connect with you. Final expenses depend on the university, course, city and duration of study.
                </p>
              </div>
            </div>
          </div>

          <!-- ASIDE COVER (PREVIEW CARD) -->
          <aside class="cover" aria-hidden="true">
            <div class="cv-t">Free Country Guide · PDF</div>
            <div class="cv-h" id="cvTitle">Your Country <em>Guide.</em></div>
            <ul class="cv-l">
              <li><b>01</b> What it really costs (Tuition + Living)</li>
              <li><b>02</b> Step-by-step admission &amp; document flow</li>
              <li><b>03</b> IELTS, funds proof &amp; visa checklist</li>
              <li><b>04</b> Top student cities &amp; lifestyle costs</li>
              <li><b>05</b> Post-study work permits &amp; career routes</li>
            </ul>
          </aside>
        </div>
      </div>
    </section>

    <!-- SECTION 5 — DESTINATIONS & STUDY OPTIONS -->
    <section class="section" id="destinations" style="padding-top:0">
      <div class="container">
        <div class="sec-head">
          <span class="sticker">Top Destinations</span>
          <h2>Explore Countries. Compare Universities. <span class="hl">Choose Your Course.</span></h2>
          <p>Looking for a Bachelor's in Germany or a Master's in Canada? Explore study destinations and compare the academic options available to you.</p>
        </div>

        <div class="cgrid" id="cgrid"></div>

        <div class="dest-cards">
          <!-- Germany -->
          <div class="dest-card">
            <div class="dest-img-wrap">
              <img src="assets/images/country/germany.webp" alt="Study in Germany" loading="lazy" />
              <span class="dest-badge">Low / Zero Tuition</span>
            </div>
            <div class="dest-body">
              <h3>GERMANY</h3>
              <p>Explore undergraduate and postgraduate programmes at world-renowned German public and private technical universities.</p>
              <div class="dest-stats">
                <div><span>Tuition Fees</span><b>€0 – €3,000/yr</b></div>
                <div><span>Blocked Account</span><b>€11,208/yr</b></div>
              </div>
              <button class="btn btn-primary" onclick="startCountryGuide('germany')">Get Germany Guide</button>
            </div>
          </div>

          <!-- Canada -->
          <div class="dest-card">
            <div class="dest-img-wrap">
              <img src="assets/images/country/canada.webp" alt="Study in Canada" loading="lazy" />
              <span class="dest-badge">3-Yr PGWP</span>
            </div>
            <div class="dest-body">
              <h3>CANADA</h3>
              <p>Compare colleges, universities and international degree programmes offering hands-on co-op work terms.</p>
              <div class="dest-stats">
                <div><span>Tuition Fees</span><b>CAD 18K – 35K/yr</b></div>
                <div><span>GIC Living Cost</span><b>CAD 20,635/yr</b></div>
              </div>
              <button class="btn btn-primary" onclick="startCountryGuide('canada')">Get Canada Guide</button>
            </div>
          </div>

          <!-- UK -->
          <div class="dest-card">
            <div class="dest-img-wrap">
              <img src="assets/images/country/uk.webp" alt="Study in United Kingdom" loading="lazy" />
              <span class="dest-badge">1-Year Masters</span>
            </div>
            <div class="dest-body">
              <h3>UNITED KINGDOM</h3>
              <p>Explore Bachelor's and Master's programmes across UK Russell Group and high-employability modern universities.</p>
              <div class="dest-stats">
                <div><span>Tuition Fees</span><b>£14,000 – £28,000/yr</b></div>
                <div><span>Living Cost</span><b>£10,000 – £14,000/yr</b></div>
              </div>
              <button class="btn btn-primary" onclick="startCountryGuide('uk')">Get UK Guide</button>
            </div>
          </div>

          <!-- Australia -->
          <div class="dest-card">
            <div class="dest-img-wrap">
              <img src="assets/images/country/australia.webp" alt="Study in Australia" loading="lazy" />
              <span class="dest-badge">Post-Study Rights</span>
            </div>
            <div class="dest-body">
              <h3>AUSTRALIA</h3>
              <p>Find courses and universities for international students with high quality of life, scholarships, and post-study work rights.</p>
              <div class="dest-stats">
                <div><span>Tuition Fees</span><b>AUD 24,000 – 45,000/yr</b></div>
                <div><span>Living Cost</span><b>AUD 24,505/yr</b></div>
              </div>
              <button class="btn btn-primary" onclick="startCountryGuide('australia')">Get Australia Guide</button>
            </div>
          </div>

          <!-- United States -->
          <div class="dest-card">
            <div class="dest-img-wrap">
              <img src="assets/images/campus-dreams.webp" alt="Study in United States" loading="lazy" />
              <span class="dest-badge">STEM OPT (3 Years)</span>
            </div>
            <div class="dest-body">
              <h3>UNITED STATES</h3>
              <p>Explore undergraduate and graduate study opportunities at world-leading Ivy League, public flagship, and state institutions.</p>
              <div class="dest-stats">
                <div><span>Tuition Fees</span><b>$22,000 – $50,000/yr</b></div>
                <div><span>Living Cost</span><b>$14,000 – $20,000/yr</b></div>
              </div>
              <button class="btn btn-primary" onclick="startCountryGuide('usa')">Get USA Guide</button>
            </div>
          </div>
        </div>

        <div style="text-align:center;margin-top:36px">
          <a class="btn btn-primary" href="#calculator">Explore All Countries &amp; Costs</a>
        </div>
      </div>
    </section>

    <!-- SECTION 6 — 360° STUDY ABROAD SUPPORT -->
    <section class="section" id="support" style="padding-top:0">
      <div class="container">
        <div class="sec-head">
          <span class="sticker sky">360° Study Abroad Support</span>
          <h2>From University Application <span class="hl">to Student Visa.</span></h2>
          <p>Studying abroad involves several important steps. Get assistance with the application process, documentation and preparations before departure.</p>
        </div>

        <div class="support-grid">
          <div class="sc">
            <div class="sc-num">01 <i class="fa-solid fa-compass"></i></div>
            <h3>Course &amp; University Shortlisting</h3>
            <p>Compare universities and courses based on your academic qualifications, budget preferences, and career ambitions.</p>
          </div>
          <div class="sc">
            <div class="sc-num">02 <i class="fa-solid fa-file-pen"></i></div>
            <h3>Admission &amp; Application</h3>
            <p>Prepare error-free university applications, academic transcripts, Statements of Purpose (SOP), and Letters of Recommendation (LOR).</p>
          </div>
          <div class="sc">
            <div class="sc-num">03 <i class="fa-solid fa-language"></i></div>
            <h3>IELTS &amp; English Test Prep</h3>
            <p>Understand English-language requirements and prepare for accepted proficiency tests like IELTS, TOEFL, PTE, or Duolingo.</p>
          </div>
          <div class="sc">
            <div class="sc-num">04 <i class="fa-solid fa-hand-holding-dollar"></i></div>
            <h3>Scholarships &amp; Education Loans</h3>
            <p>Explore eligible university scholarships, financial aid, and collateral-free education loans through trusted banking partners.</p>
          </div>
          <div class="sc">
            <div class="sc-num">05 <i class="fa-solid fa-passport"></i></div>
            <h3>Student Visa Application</h3>
            <p>Prepare the required financial documentation, blocked accounts/GIC, and master your destination country's student visa interview.</p>
          </div>
          <div class="sc">
            <div class="sc-num">06 <i class="fa-solid fa-house-user"></i></div>
            <h3>Accommodation &amp; Travel</h3>
            <p>Plan verified student housing, international flight bookings, forex currency cards, and health insurance before you leave.</p>
          </div>
          <div class="sc">
            <div class="sc-num">07 <i class="fa-solid fa-plane-departure"></i></div>
            <h3>Pre-Departure Preparation</h3>
            <p>Attend comprehensive briefing sessions to understand cultural adaptation, packing checklists, and campus life abroad.</p>
          </div>
        </div>

        <div style="text-align:center;margin-top:36px">
          <a class="btn btn-primary" href="#enquiry">Start Your Application</a>
        </div>
      </div>
    </section>

    <!-- SECTION 7 — TESTIMONIALS (2 HIGH IMPACT CARDS) -->
    <section class="section" id="testimonials" style="padding-top:0">
      <div class="container">
        <div class="sec-head">
          <span class="sticker sun">Verified Guidance</span>
          <h2>Trusted Guidance, <span class="hl">Real Results.</span></h2>
          <p>See how Indian students navigate their university admissions, scholarships, and visa approvals with our team.</p>
        </div>

        <div class="testi-grid">
          <!-- Card 1: 1-on-1 Google Meet Session -->
          <div class="testi-card">
            <div class="testi-media">
              <img src="assets/images/consultation-desk.webp" alt="1-on-1 Counselling via Google Meet" loading="lazy" />
              <span class="testi-tag"><i class="fa-solid fa-video"></i> Live 1-on-1 Mentorship</span>
            </div>
            <div class="testi-body">
              <div class="testi-quote">
                "The 1-on-1 video session with University Yatra completely cleared up the confusion between Germany's direct and fast-track admissions. They mapped my exact budget and handled my blocked account without hidden charges."
              </div>
              <div class="testi-author">
                <div class="testi-avatar">R</div>
                <div class="testi-meta">
                  <b>Rohan Sharma</b>
                  <span>M.Sc. Automotive Systems, Germany (Admitted 2026)</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 2: Visa Approval & Celebration -->
          <div class="testi-card">
            <div class="testi-media">
              <img src="assets/images/student-graduation-celebration.webp" alt="Student Celebration and Visa Approval" loading="lazy" />
              <span class="testi-tag sun"><i class="fa-solid fa-stamp"></i> Visa Approved</span>
            </div>
            <div class="testi-body">
              <div class="testi-quote">
                "From IELTS guidance to getting my Canada student visa approved in 3 weeks! The team helped me secure a $4,000 entrance scholarship and kept my parents updated at every milestone. Truly 360-degree support!"
              </div>
              <div class="testi-author">
                <div class="testi-avatar">P</div>
                <div class="testi-meta">
                  <b>Priya Patel</b>
                  <span>Bachelor of Computer Science, Canada</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8 — FAQS + ENQUIRY SECTION -->
    <section class="section" id="faqs" style="padding-top:0">
      <div class="container">
        <div class="sec-head center">
          <span class="sticker sky">FAQs</span>
          <h2>Study Abroad: <span class="hl">Common Questions Answered.</span></h2>
          <p>Everything you need to know about eligibility, pathways, costs and visas.</p>
        </div>

        <div class="faq">
          <details>
            <summary>1. Can I study abroad after 12th?</summary>
            <p>Yes. You can apply for Bachelor's and other undergraduate programmes after Class 12, depending on your academic marks, subject requirements and university eligibility.</p>
          </details>
          <details>
            <summary>2. Can I study abroad after graduation?</summary>
            <p>Yes. You can apply for Master's and postgraduate programmes based on your Bachelor's degree, academic background and the university's admission criteria.</p>
          </details>
          <details>
            <summary>3. What is the difference between Direct and Fast Track?</summary>
            <p>Direct Study starts at an overseas university from the first semester. Selected Fast Track programmes begin online in India before continuing at a partner university abroad, subject to credit-transfer approval.</p>
          </details>
          <details>
            <summary>4. How much does it cost to study abroad?</summary>
            <p>The cost depends on the country, university, course and city. Tuition fees and living expenses should both be included in your budget.</p>
          </details>
          <details>
            <summary>5. Do I need IELTS to study abroad?</summary>
            <p>It depends on the university and programme. Some institutions accept alternative English tests or other evidence of English proficiency.</p>
          </details>
          <details>
            <summary>6. Can I get a scholarship or education loan?</summary>
            <p>Scholarships depend on university criteria and your academic profile. Education loans are available through eligible lenders, subject to their approval.</p>
          </details>
          <details>
            <summary>7. How long does the admission process take?</summary>
            <p>It varies by university, intake and destination. Start checking application deadlines and documentation requirements well before your intended intake.</p>
          </details>
          <details>
            <summary>8. Can I work after completing my degree abroad?</summary>
            <p>Some countries provide post-study work options to eligible graduates. The rules and duration depend on the destination country's current immigration policy.</p>
          </details>
        </div>

        <!-- FINAL ENQUIRY SECTION -->
        <div class="enquiry-wrap" id="enquiry">
          <!-- CTA Info Box -->
          <div class="cta-box">
            <h2>Ready to Start Your Yatra?</h2>
            <p>Get personalized guidance on university selection, fast-track eligibility, and visa procedures.</p>
            <ul class="cta-perks">
              <li><i class="fa-solid fa-circle-check"></i> Free profile assessment by senior counsellors</li>
              <li><i class="fa-solid fa-circle-check"></i> Shortlist of universities within your budget</li>
              <li><i class="fa-solid fa-circle-check"></i> Visa documentation and financial guidance</li>
            </ul>
            <div class="cta-box-actions">
              <a class="btn btn-lime" href="#calculator">Get Free Guide ↑</a>
              <a class="btn btn-wa" href="https://wa.me/919217368750?text=Hi%20University%20Yatra%2C%20I%20want%20to%20know%20more%20about%20study%20abroad%20programmes." target="_blank" rel="noopener">
                <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp
              </a>
            </div>
          </div>

          <!-- ENQUIRY FORM (NAME, NUMBER, EMAIL ONLY) -->
          <div class="enquiry-card">
            <h3>Tell Us What You Want to Study.</h3>
            <p class="sub">Share your details to discuss available universities, courses and admission requirements.</p>

            <form class="form" id="enquiryForm">
              <input class="fi" name="name" id="eq_name" placeholder="Full Name" required autocomplete="name" />
              <div class="ph">
                <span>+91</span>
                <input class="fi" name="mobile" id="eq_mobile" type="tel" inputmode="numeric" pattern="[0-9]{10}" maxlength="10" placeholder="10-digit Mobile Number" required autocomplete="tel" />
              </div>
              <input class="fi" name="email" id="eq_email" type="email" placeholder="Email Address" required autocomplete="email" />
              
              <button class="btn btn-primary btn-block" type="submit" id="enquirySubmitBtn">
                Submit Study Enquiry <i class="fa-solid fa-arrow-right"></i>
              </button>
            </form>

            <div class="enquiry-success" id="enquirySuccess">
              <h4>Thank you!</h4>
              <p>Your enquiry has been received. Our senior counselling team will contact you shortly.</p>
            </div>
          </div>
        </div>

        <!-- CONTACT TRIO -->
        <div class="contact-trio">
          <div class="cc">
            <small>Call / WhatsApp</small>
            <a href="https://wa.me/919217368750" target="_blank" rel="noopener">+91 92173 68750</a>
          </div>
          <div class="cc">
            <small>Email</small>
            <a href="mailto:info@universityyatra.com">info@universityyatra.com</a>
          </div>
          <div class="cc">
            <small>Office Address</small>
            <span>Unit 917, 9th Floor, Supernova Astralis, Sector 94, Noida, UP 201301</span>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer>
    <div class="container">
      <div class="ft">
        <a href="#top" class="logo">
          <i><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/></svg></i>
          <span>University <b>Yatra</b></span>
        </a>
        <div class="ftl">
          <a href="#pathways">Study Pathways</a>
          <a href="#calculator">Free Guide</a>
          <a href="#destinations">Destinations</a>
          <a href="#faqs">FAQs</a>
          <a href="#">Privacy Policy</a>
          <a href="#">Terms &amp; Conditions</a>
        </div>
      </div>
      <p class="copy">
        &copy; <span id="yearVal">2026</span> Future Yatra Private Limited. University Yatra is a brand of Future Yatra Private Limited. All information is for educational guidance only. University admissions and student visas are subject to institutional eligibility and government regulations.
      </p>
    </div>
  </footer>

  <!-- MOBILE BOTTOM STICKY BAR (.mbar) -->
  <div class="mbar">
    <a class="btn btn-primary" href="#calculator">Get Free Guide</a>
    <a class="btn btn-wa" href="https://wa.me/919217368750?text=Hi%20University%20Yatra%2C%20I%20want%20to%20know%20more%20about%20study%20abroad%20programmes." target="_blank" rel="noopener">
      <i class="fa-brands fa-whatsapp"></i> WhatsApp
    </a>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js"></script>
  <script src="js/main.js"></script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully! Length:", len(html_content))
