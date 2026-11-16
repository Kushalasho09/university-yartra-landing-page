with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add stamp badge to hero trust row
old_trust = """          <div class="hero-trust">
            <span><i class="fa-solid fa-circle-check"></i> 100% Free Guidance</span>
            <span><i class="fa-solid fa-circle-check"></i> Top Global Universities</span>
            <span><i class="fa-solid fa-circle-check"></i> Fast-Track Credit Transfer</span>
          </div>"""

new_trust = """          <div class="hero-trust">
            <span><i class="fa-solid fa-circle-check"></i> 100% Free Guidance</span>
            <span><i class="fa-solid fa-circle-check"></i> Top Global Universities</span>
            <span class="stamp-badge"><i class="fa-solid fa-stamp"></i> VISA APPROVED 2026</span>
          </div>"""

html = html.replace(old_trust, new_trust)

# Add starburst badge to Fast Track header
old_ft_header = """            <div class="path-header">
              <span class="eyebrow">Smart Credit Transfer</span>
              <span class="path-badge sun"><i class="fa-solid fa-bolt"></i> Budget-Smart Pathway</span>
            </div>"""

new_ft_header = """            <div class="path-header">
              <span class="eyebrow">Smart Credit Transfer</span>
              <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;">
                <span class="starburst-badge">SAVE UP TO 40% ⚡</span>
                <span class="path-badge sun"><i class="fa-solid fa-bolt"></i> Budget-Smart Pathway</span>
              </div>
            </div>"""

html = html.replace(old_ft_header, new_ft_header)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with Theme 1 badges!")
