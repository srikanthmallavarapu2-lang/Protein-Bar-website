# PULSE — Plant Protein Bars ⚡

> **Five bold flavours. Real food. Pressed, not baked.**  
> A high-performance, single-file interactive landing page featuring a real-time 3D wrapper that travels down the page across four interactive sections.

---

## 🌟 Key Features

1. **Travelling 3D WebGL Wrapper (Three.js 0.160.0)**
   - Custom displaced wrapper geometry with crimped seals and puffed pillow volume.
   - Dynamic canvas texture synthesis: Authentic metallic foil sheen, FDA-compliant nutrition panel, barcode, and embossed typography.
   - Travelling 3D bar lerps across the hero arc, pinned 180° step flips in Section 2, and lands seamlessly on its shop card in Section 3.
   - **Free 360° Drag-to-Inspect Mode**: Full pitch & yaw rotation with inertial damping and mouse wheel zoom.

2. **Interactive Hero Arc & Flavour Transitions**
   - 5 distinct flavours: **Peanut Cocoa**, **Berry Oat**, **Salted Caramel**, **Mint Chip**, **Strawberry**.
   - Expanding background colour transition matching the active flavour.
   - Drag, swipe, and autoplay navigation.

3. **Pinned "What's Inside" Section**
   - Pinned 1440×900 viewport frame with 4 progressive steps.
   - Real-time ingredient storm particle burst.
   - 180° wrapper step-flip animation.

4. **Modern D2C Shop & 3-Pack Custom Box Builder**
   - 5 flavour cards with real-time hover tilt & squash.
   - 3-Pack Builder: Mix-and-match 3 flavours, saving $1.49 vs individual bars with cubic Bezier fly-to-cart animation.

5. **Slide-Out Cart Drawer & Full Checkout Flow**
   - Live item tracking, quantity steppers, and free shipping progress bar ($25.00 threshold).
   - **Subscribe & Save 15%** toggle with customizable delivery intervals (Every 2, 4, or 6 weeks).
   - **Smart Promo Code Engine**: Supports `PULSE15`, `PULSE10`, `PLANTPOWER` with a 3-bar order threshold rule.
   - Secure checkout simulation with validation, dispatch tracker, and printable receipt.

6. **Nutrition & Taste Profile Modal**
   - Complete FDA nutrition breakdown panel with allergen advisories.
   - **Flavour Taste Profile & Texture Meters**: Interactive visual ratings for *Sweetness*, *Crunchiness*, and *Fudginess* with custom tasting notes.

7. **Social Proof & 21st.dev Component Standards**
   - Infinite press marquee (Vogue Wellness, Men's Health, Runner's World).
   - Bento-style athlete review grid with flavour filters and verified buyer badges.
   - Expandable FAQ accordion and brand guarantees footer.

---

## 🛠️ Tech Stack

- **Three.js 0.160.0** (ES Modules via Import Maps) + `RoomEnvironment`
- **Vanilla Modern JavaScript** (ES6+, zero build-step runtime)
- **CSS Custom Properties & Math Scaling** (`--u`, `--w`, `--ease`)
- **Self-Hosted WOFF2 Fonts** (Embedded Base64: *Archivo Black*, *DM Mono*, *Inter*)
- **Pure Canvas 2D Texture Generator**

---

## 🚀 Getting Started

Clone the repository and serve locally:

```bash
# Clone repository
git clone https://github.com/srikanthmallavarapu2-lang/Protein-Bar-website.git
cd Protein-Bar-website

# Start any local HTTP server
python -m http.server 8000
# or npx serve .
```

Open [http://localhost:8000/index.html](http://localhost:8000/index.html) in your browser.

---

## 📄 License

MIT License. Designed & Developed for PULSE Nutrition.
