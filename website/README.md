# The Scientific Story of Everything — Interactive Web Platform

The official publication-grade static website for **The Scientific Story of Everything**, compiling all 106 canonical chapters across 4 seasons into a zero-latency, responsive web reading experience.

---

## 🌐 Live Deployment

* **Live Site:** [https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/](https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/)
* **Featured Episode (The Axial Age):** [https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/episodes/season-01/ep-30-the-axial-age/](https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/episodes/season-01/ep-30-the-axial-age/)
* **Visual Guide (Interesting Physics):** [https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/interesting-physics/](https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/interesting-physics/)
* **Master Timeline & Infographics:** [https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/timeline/](https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/timeline/)

---

## 🚀 Key Features

1. **All 106 Canonical Episodes Dynamic Generation:**
   - Automatically parses all 106 markdown chapters from `../seasons/` into styled reading pages.
   - Live scroll-progress reading bar, sticky Table of Contents, 4-tier Evidence Ladder badges, Honesty Beat summaries, and forward Baton navigation.
2. **Featured Chapter:**
   - Direct link: [Season 1, Episode 30 — The Axial Age](https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/episodes/season-01/ep-30-the-axial-age/)
3. **KaTeX Mathematical & Physical Typesetting:**
   - Client-side and build-time KaTeX math rendering (`remark-math`, `rehype-katex`) using offline-bundled font assets in `public/katex/`.
4. **Curated Visual Guides & Infographics:**
   - Dedicated [Interesting Physics](https://abhinav-knowledge-base.github.io/The-Scientific-Story-of-Everything/interesting-physics/) page organizing 9 core physical concepts with infographics and visual cards.
   - LLM Image Prompt card workflow allowing 1-click prompt copying and automatic image display once generated.
5. **Instant Client-Side Search:**
   - Press <kbd>Ctrl</kbd> + <kbd>K</kbd> (or <kbd>Cmd</kbd> + <kbd>K</kbd>) anywhere on the site to search all 106 episodes instantly.
6. **Zero Hosting Cost:**
   - 100% static compilation deployed to GitHub Pages via automated GitHub Actions workflow.

---

## 🛠️ Technology Stack

- **Framework:** [Astro](https://astro.build/) (Static Site Generation)
- **Styling:** Bespoke Vanilla CSS (Cosmic Dark design system, glassmorphism, responsive mobile layout, custom typography)
- **Math Rendering:** `remark-math` + `rehype-katex` with local font assets
- **Deployment:** GitHub Actions (`.github/workflows/deploy.yml`) $\rightarrow$ GitHub Pages

---

## 💻 Local Development

```bash
# 1. Install dependencies
npm install

# 2. Start local development server
npm run dev

# Server will be accessible at http://localhost:4321/The-Scientific-Story-of-Everything/

# 3. Build for production (outputs to ./dist)
npm run build

# 4. Preview production build locally
npm run preview
```

---

## 📁 Project Structure

```text
website/
├── public/
│   ├── assets/
│   │   └── images/          ← Episode illustrations, hero banners & infographics
│   ├── katex/               ← Bundled KaTeX CSS and webfonts
│   └── favicon.svg
├── src/
│   ├── components/
│   │   ├── Header.astro     ← Sticky cosmic navbar
│   │   ├── Footer.astro     ← Universal footer
│   │   ├── SearchModal.astro← Ctrl+K instant search modal
│   │   └── ImagePromptCard.astro ← LLM prompt generator & card viewer
│   ├── layouts/
│   │   └── BaseLayout.astro ← HTML shell, meta tags, and font loading
│   ├── lib/
│   │   ├── episodes.ts      ← Dynamic parser for seasons/ markdown files
│   │   └── base.ts          ← GitHub Pages subpath prefix helper
│   ├── pages/
│   │   ├── index.astro      ← Interactive homepage & hero continuum
│   │   ├── guide.astro      ← Interactive series architecture guide
│   │   ├── timeline.astro   ← Master timeline & infographic gallery
│   │   ├── interesting-physics.astro ← Visual physics guide
│   │   ├── seasons/         ← Season hubs (Seasons 1 to 4)
│   │   └── episodes/        ← Dynamic episode reader ([season]/[slug].astro)
│   └── styles/
│       └── global.css       ← Design tokens, typography & animations
├── astro.config.mjs         ← Astro configuration with GitHub Pages base path
└── package.json
```
