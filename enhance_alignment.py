with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Enhance input alignments
enhanced_css = """
/* PRECISION FORM ALIGNMENT */
.fi {
  height: 52px;
  box-sizing: border-box;
}

.ph {
  display: flex;
  align-items: stretch;
}

.ph span {
  height: 52px;
  box-sizing: border-box;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.form .btn {
  height: 52px;
  box-sizing: border-box;
}

/* RESPONSIVE ALIGNMENT FIXES */
@media (max-width: 600px) {
  .hero-card-badge {
    bottom: 14px;
    left: 14px;
    font-size: 0.76rem;
    padding: 6px 12px;
  }
  .dest-cards,
  .support-grid,
  .inside,
  .testi-grid {
    grid-template-columns: 1fr;
  }
  .dest-img-wrap,
  .testi-media {
    height: 180px;
  }
  .sec-cta-wrap {
    flex-direction: column;
    align-items: stretch;
    text-align: center;
  }
  .calc-header {
    flex-wrap: wrap;
    gap: 10px;
  }
  .calc-meta {
    width: 100%;
    justify-content: space-between;
    margin-left: 0;
  }
}
"""

css += enhanced_css

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added precision form & responsive alignment to css/styles.css")
