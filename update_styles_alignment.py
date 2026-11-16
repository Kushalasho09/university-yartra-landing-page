import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove rotation on .sticker
css = re.sub(
    r'\.sticker\s*\{([^}]+)\}',
    lambda m: '.sticker {\n' + '\n'.join([
        line for line in m.group(1).splitlines() if 'transform: rotate' not in line
    ]) + '\n}',
    css
)

# 2. Remove rotation on .hero h1 .box
css = re.sub(
    r'\.hero h1 \.box\s*\{([^}]+)\}',
    lambda m: '.hero h1 .box {\n' + '\n'.join([
        (line if 'transform: rotate' not in line else '  vertical-align: baseline;')
        for line in m.group(1).splitlines()
    ]) + '\n}',
    css
)

# 3. Remove .path .sticker rule with top: -16px and rotate(3deg)
css = re.sub(
    r'\.path \.sticker\s*\{[^}]+\}',
    '',
    css
)

# 4. Remove .calc .badge rule with top: -15px and rotate(3deg)
css = re.sub(
    r'\.calc \.badge\s*\{[^}]+\}',
    '',
    css
)

# 5. Remove rotate on .ct:hover
css = css.replace('transform: translate(-2px, -2px) rotate(-1deg);', 'transform: translate(-2px, -2px);')

# 6. Add modern, clean styles for .path-header, .path-badge, .calc-header, .calc-meta, .calc-time-badge
new_components = """
/* =====================================================
   CLEAN ALIGNMENT & HEADER COMPONENTS
   ===================================================== */
.path-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}

.path-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 0.78rem;
  padding: 5px 12px;
  border: 2px solid var(--ink);
  border-radius: 99px;
  box-shadow: 2px 2px 0 var(--ink);
  background: #fff;
  color: var(--ink);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  white-space: nowrap;
}

.path-badge.sun {
  background: var(--sun);
}

.path-badge.lime {
  background: var(--lime);
}

.path-badge.sky {
  background: var(--sky);
}

/* CALCULATOR HEADER (CLEAN & ALIGNED) */
.calc-header {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 2px dashed rgba(10, 18, 48, 0.12);
}

.calc-meta {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-left: auto;
}

.calc-time-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: var(--sun);
  border: 2px solid var(--ink);
  border-radius: 99px;
  font-weight: 800;
  font-size: 0.78rem;
  padding: 4px 10px;
  box-shadow: 2px 2px 0 var(--ink);
  color: var(--ink);
  white-space: nowrap;
}

/* Ensure mobile safe padding */
@media (max-width: 768px) {
  body {
    padding-bottom: 76px;
  }
}
"""

css += new_components

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/styles.css successfully! Length:", len(css))
