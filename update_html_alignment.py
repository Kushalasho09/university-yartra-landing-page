import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Direct Study Abroad card header in pathways
old_direct = """          <!-- Direct Study Abroad -->
          <div class="path">
            <div class="eyebrow">On-Campus Overseas</div>
            <h3>DIRECT STUDY ABROAD</h3>"""

new_direct = """          <!-- Direct Study Abroad -->
          <div class="path">
            <div class="path-header">
              <span class="eyebrow">On-Campus Overseas</span>
              <span class="path-badge">Direct Route</span>
            </div>
            <h3>DIRECT STUDY ABROAD</h3>"""

html = html.replace(old_direct, new_direct)

# 2. Update Fast Track Study Abroad card header in pathways
old_fast = """          <!-- Fast Track Study Abroad -->
          <div class="path fast">
            <span class="sticker sun">Budget-Smart Pathway</span>
            <div class="eyebrow">Smart Credit Transfer</div>
            <h3>FAST TRACK STUDY ABROAD</h3>"""

new_fast = """          <!-- Fast Track Study Abroad -->
          <div class="path fast">
            <div class="path-header">
              <span class="eyebrow">Smart Credit Transfer</span>
              <span class="path-badge sun"><i class="fa-solid fa-bolt"></i> Budget-Smart Pathway</span>
            </div>
            <h3>FAST TRACK STUDY ABROAD</h3>"""

html = html.replace(old_fast, new_fast)

# 3. Update Calculator card header
old_calc = """          <div class="calc" id="calc">
            <span class="badge">Takes 30 sec</span>
            <div class="top">
              <button class="back" id="backBtn" aria-label="Go back" hidden>←</button>
              <div class="dots" id="dots"><i class="on"></i><i></i><i></i><i></i></div>
              <span class="stepno" id="stepNo">1/4</span>
            </div>"""

new_calc = """          <div class="calc" id="calc">
            <div class="calc-header">
              <button class="back" id="backBtn" aria-label="Go back" hidden><i class="fa-solid fa-arrow-left"></i></button>
              <div class="dots" id="dots"><i class="on"></i><i></i><i></i><i></i></div>
              <div class="calc-meta">
                <span class="calc-time-badge"><i class="fa-regular fa-clock"></i> 30 sec</span>
                <span class="stepno" id="stepNo">1/4</span>
              </div>
            </div>"""

html = html.replace(old_calc, new_calc)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully! Length:", len(html))
