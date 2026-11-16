# University Yatra — Official Client Design System

Design reference created directly from the client's design module (`index (4).html`).

## 1. Typography
* **Display & Headings**: `'Bricolage Grotesque'`, sans-serif (Weights 600, 700, 800), line-height: 1.08, letter-spacing: -0.03em
* **Body Font**: `'DM Sans'`, system-ui, -apple-system, sans-serif (Weights 400, 500, 700), line-height: 1.55
* **Font Scaling**: Fluid clamping: `font-size: clamp(1.9rem, 4.5vw, 3.1rem)` for `h2`, `clamp(2.3rem, 5.8vw, 4.2rem)` for `h1`

## 2. Color Palette & Tokens
* `--blue`: `#1765F5` (Electric Cobalt Blue — Primary brand, buttons, accents)
* `--blue-d`: `#0F4FCC` (Deep Cobalt)
* `--ink`: `#0A1230` (Obsidian Navy/Ink — Deep text, solid 2.5px borders, drop shadows)
* `--cream`: `#F4F7FF` (Subtle icy canvas tint)
* `--white`: `#FFFFFF`
* `--lime`: `#C8FF3E` (Vibrant Lime — Stickers, active tile highlights, badges)
* `--pink`: `#FF8AD0` (Warm Pink Sticker Accent)
* `--sun`: `#FFD84A` (Sunny Yellow Sticker Accent)
* `--sky`: `#BFD6FF` (Soft Sky Blue — Breadcrumbs, background dots)
* `--muted`: `#4D5878` (Slate Muted Gray for subtitles and captions)
* `--b`: `2.5px solid var(--ink)` (Signature high-contrast solid border)
* `--sh`: `5px 5px 0 var(--ink)` (Signature hard offset drop-shadow)
* `--sh-s`: `3px 3px 0 var(--ink)` (Small button/badge shadow)
* `--sh-lg`: `8px 8px 0 var(--ink)` (Hero/CTA box shadow)
* `--r`: `24px` (Card border-radius)

## 3. Signature UI Components
* **Rotating Pill Stickers**:
  - `border: var(--b); border-radius: 99px; box-shadow: var(--sh-s); transform: rotate(-1.5deg);`
  - Variants: Lime (default), Pink, Sun, Sky, White.
* **Boxed Tilted Heading Words**:
  - `.hero h1 .box`: `background: var(--blue); color: #fff; transform: rotate(-1.5deg); border: var(--b); box-shadow: var(--sh-s);`
* **Tactile Hard-Shadow Buttons (`.btn`)**:
  - `border: var(--b); border-radius: 99px; box-shadow: 3px 3px 0 var(--ink);`
  - Hover: `transform: translate(-2px, -2px); box-shadow: 5px 5px 0 var(--ink);`
  - Active: `transform: translate(2px, 2px); box-shadow: 0 0 0;`
* **Interactive 4-Step Calculator**:
  - Dynamic progress dots + editable crumb buttons with pencil icon (`✎`).
  - Dark ink guide aside preview card (`.cover`) with glowing radial blue backdrop.
  - Automatic country PDF download or on-the-fly PDF generation via `pdf-lib`.
* **Mobile Sticky Bottom Bar (`.mbar`)**:
  - Fixed at screen bottom (`@media (max-width: 768px)`), safe-area insets enabled.
  - Primary button to `#calculator` + Direct WhatsApp button to `919217368750`.

## 4. Content & Lead Forms
* All 8 original content sections preserved in exact order.
* Enquiry Form trimmed to **3 essential fields**: Full Name, 10-Digit Mobile Number (`+91`), Email Address.

