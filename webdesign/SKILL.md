---
name: webdesign
description: "End-to-end web design and deployment skill — from UX research to live Vercel site. Orchestrates UX analysis, UI component selection, image generation, and Next.js build+deploy. Use this skill whenever the user wants to design a website, build a landing page, create a web presence, deploy a site to Vercel, or says anything like 'build me a website', 'design a landing page', 'I need a site for my startup', 'create a web app', 'deploy my site', or 'make me a homepage'. Also triggers on 'web design', 'website redesign', 'new site', 'launch page', or any request that involves going from an idea to a live deployed website. This skill handles the FULL pipeline: research → design → build → deploy."
---

# Webdesign: From Idea to Live Website

You are a senior web design agent. Your job is to take a user from a vague idea ("I need a website for my coffee brand") all the way to a live, deployed Vercel site — through a structured creative process that produces genuinely beautiful, distinctive work.

This skill orchestrates four specialized tools in sequence. Each phase builds on the previous one, creating a coherent pipeline from research to deployment. Don’t skip phases — the quality of each phase depends on the work done before it.

---

## Phase 1: UX Discovery & Brief

**Goal:** Understand what the user actually needs before touching any code.

Most people don’t know exactly what they want — they know how they want their site to *feel*. Your job in this phase is to draw that out through conversation, visual examples, and smart questions. This phase is the foundation: a sloppy brief leads to a generic site.

### How to run this phase

1. **Start with open-ended questions.** Ask the user about:
   - What their product/service/project is
   - Who their audience is (age, tech-savviness, expectations)
   - What feeling they want visitors to have (trust? excitement? calm? urgency?)
   - Any sites they love (and *why* they love them — "I like Stripe’s site" is less useful than "I like how Stripe makes complex things feel simple")
   - Any sites they hate or want to avoid looking like
   - What the primary action visitors should take (sign up? buy? contact? read?)

2. **Show website examples.** Based on their answers, use web search to find 3-5 real websites that match their described vibe. Present them with brief descriptions of why each is relevant. Ask the user to react: "Which of these feels closest to what you want? What would you change?"

3. **Invoke UI UX Pro Max.** Once you have a sense of the user’s industry, audience, and aesthetic preferences, use the UI UX Pro Max skill to generate a design system. UUPM will analyze the product category against its database of 161 industry-specific reasoning rules and recommend:
   - UI style direction (e.g., glassmorphism, brutalist, minimal, AI-native)
   - Color palette aligned to the industry and mood
   - Typography pairings from Google Fonts
   - Layout patterns and anti-patterns to avoid
   - Animation and interaction recommendations

4. **Synthesize into a UX Brief.** Write a structured brief document that captures everything discovered. Save this as `ux-brief.md` in the project directory. The brief should include:

```
# UX Brief: [Project Name]

## Project Overview
[What is this? Who is it for?]

## Target Audience
[Demographics, behavior, expectations]

## Core Message & Feeling
[What should visitors feel? What’s the one thing they should take away?]

## Primary CTA
[What’s the main action?]

## Design Direction
- Style: [from UUPM recommendation]
- Color Palette: [hex values + mood rationale]
- Typography: [heading + body font pairing]
- Layout Pattern: [recommended structure]

## Reference Sites
[Sites the user liked, with notes on what specifically resonated]

## Anti-Patterns
[What to explicitly avoid — from both user feedback and UUPM]
```

**Present the brief to the user and get explicit approval before moving on.** This is a checkpoint — don’t proceed until the user confirms.---
name: webdesign
description: "End-to-end web design and deployment skill — from UX research to live Vercel site. Orchestrates UX analysis, UI component selection, image generation, and Next.js build+deploy. Use this skill whenever the user wants to design a website, build a landing page, create a web presence, deploy a site to Vercel, or says anything like 'build me a website', 'design a landing page', 'I need a site for my startup', 'create a web app', 'deploy my site', or 'make me a homepage'. Also triggers on 'web design', 'website redesign', 'new site', 'launch page', or any request that involves going from an idea to a live deployed website. This skill handles the FULL pipeline: research → design → build → deploy."
---

# Webdesign: From Idea to Live Website

You are a senior web design agent. Your job is to take a user from a vague idea ("I need a website for my coffee brand") all the way to a live, deployed Vercel site — through a structured creative process that produces genuinely beautiful, distinctive work.

This skill orchestrates four specialized tools in sequence. Each phase builds on the previous one, creating a coherent pipeline from research to deployment. Don’t skip phases — the quality of each phase depends on the work done before it.

---

## Phase 1: UX Discovery & Brief

**Goal:** Understand what the user actually needs before touching any code.

Most people don’t know exactly what they want — they know how they want their site to *feel*. Your job in this phase is to draw that out through conversation, visual examples, and smart questions. This phase is the foundation: a sloppy brief leads to a generic site.

### How to run this phase

1. **Start with open-ended questions.** Ask the user about:
   - What their product/service/project is
   - Who their audience is (age, tech-savviness, expectations)
   - What feeling they want visitors to have (trust? excitement? calm? urgency?)
   - Any sites they love (and *why* they love them — "I like Stripe’s site" is less useful than "I like how Stripe makes complex things feel simple")
   - Any sites they hate or want to avoid looking like
   - What the primary action visitors should take (sign up? buy? contact? read?)

2. **Show website examples.** Based on their answers, use web search to find 3-5 real websites that match their described vibe. Present them with brief descriptions of why each is relevant. Ask the user to react: "Which of these feels closest to what you want? What would you change?"

3. **Invoke UI UX Pro Max.** Once you have a sense of the user’s industry, audience, and aesthetic preferences, use the UI UX Pro Max skill to generate a design system. UUPM will analyze the product category against its database of 161 industry-specific reasoning rules and recommend:
   - UI style direction (e.g., glassmorphism, brutalist, minimal, AI-native)
   - Color palette aligned to the industry and mood
   - Typography pairings from Google Fonts
   - Layout patterns and anti-patterns to avoid
   - Animation and interaction recommendations

4. **Synthesize into a UX Brief.** Write a structured brief document that captures everything discovered. Save this as `ux-brief.md` in the project directory. The brief should include:

```
# UX Brief: [Project Name]

## Project Overview
[What is this? Who is it for?]

## Target Audience
[Demographics, behavior, expectations]

## Core Message & Feeling
[What should visitors feel? What’s the one thing they should take away?]

## Primary CTA
[What’s the main action?]

## Design Direction
- Style: [from UUPM recommendation]
- Color Palette: [hex values + mood rationale]
- Typography: [heading + body font pairing]
- Layout Pattern: [recommended structure]

## Reference Sites
[Sites the user liked, with notes on what specifically resonated]

## Anti-Patterns
[What to explicitly avoid — from both user feedback and UUPM]
```

**Present the brief to the user and get explicit approval before moving on.** This is a checkpoint — don’t proceed until the user confirms.

---

## Phase 2: UI Component Selection & Layout

**Goal:** Translate the UX brief into concrete UI building blocks.

Now that you know *what* to build and *how it should feel*, select the actual components that will make up the page.

### How to run this phase

1. **Plan the page structure.** Based on the brief, outline the sections the landing page needs. A typical landing page follows a pattern like:
   - Hero section (headline + CTA + visual)
   - Social proof / logos bar
   - Features / benefits section
   - How it works / process
   - Testimonials
   - Pricing (if applicable)
   - Final CTA / footer

   Adapt this to the user’s needs — not every page needs every section. Confirm the section plan with the user.

2. **Select UI components from 21st.dev.** Use the 21st.dev Magic MCP to search for and generate components that match the design direction. For each section, use the `/ui` pattern to describe what you need:
   - Be specific about the visual style from the brief (e.g., "create a glassmorphic hero section with gradient text and a floating CTA button")
   - Reference the color palette and typography from the brief
   - Generate components one section at a time so you can review each

   If the 21st.dev MCP is not connected, search 21st.dev/community/components via web search for inspiration and build custom components using the design system from Phase 1.

3. **Apply the frontend-design skill.** Before writing any component code, invoke the frontend-design skill. This ensures Claude avoids generic "AI slop" aesthetics and makes bold, distinctive design choices. The frontend-design skill pushes toward:
   - Unusual, memorable font choices
   - Bold color usage (not safe grays)
   - Atmospheric effects and purposeful animations
   - Layouts that feel crafted, not templated

4. **Create a component manifest.** Document which components go where:

```
# Component Manifest

## Hero
- Component: [name/source]
- Customizations: [color overrides, copy, CTA text]

## Features
- Component: [name/source]
- Layout: [grid/cards/list]
- Items: [3-6 feature blocks]

[... etc for each section]
```

Present the manifest to the user. This is checkpoint #2.

---

## Phase 3: Image Generation

**Goal:** Create custom visual assets that make the site feel unique and on-brand.

Stock photos kill distinctiveness. This phase uses Nano Banana (powered by Google Gemini) to generate custom images tailored to the project’s specific aesthetic.

### How to run this phase

1. **Identify image needs.** Based on the component manifest, list every place an image is needed:
   - Hero background or illustration
   - Feature icons or illustrations
   - About/team section visuals
   - Background textures or patterns
   - Product mockups or screenshots

2. **Generate images with Nano Banana.** For each image need, construct a detailed prompt that incorporates the design direction from the brief. Use the `nano-banana` CLI:

   ```bash
   nano-banana "detailed prompt here" -s 2K -a 16:9 -o hero-image -d ./public/images
   ```

   Key considerations:
   - Match the color palette from the brief in your prompts (mention specific colors)
   - Use `-a` to set the right aspect ratio for each placement
   - Use `-s 2K` or `-s 4K` for hero images, `-s 1K` for smaller assets
   - Use `-t` (transparent) for illustrations and icons that need to sit on colored backgrounds
   - Use `-r` (reference) if the user provided brand assets or style references
   - Use `-m pro` for hero images where quality matters most; flash is fine for supporting assets

3. **Review generated images.** Show the user the generated images. Regenerate any that don’t fit. Image generation is iterative — expect 2-3 rounds for hero images.

4. **Optimize for web.** After approval, ensure all images are properly sized and optimized:
   - Convert to WebP where appropriate
   - Generate responsive sizes if needed
   - Place in the Next.js `public/images/` directory

---

## Phase 4: Build & Deploy

**Goal:** Assemble everything into a working Next.js site and deploy it live to Vercel.

### How to run this phase

1. **Scaffold the Next.js project.** Create a new Next.js app with the App Router:

   ```bash
   npx create-next-app@latest [project-name] --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
   ```

   Then install any additional dependencies needed for the selected components (e.g., `framer-motion` for animations, `lucide-react` for icons).

2. **Implement the design system.** Set up the design tokens from the brief:
   - Configure Tailwind with the color palette, typography, and spacing
   - Set up Google Fonts via `next/font`
   - Create any shared components (buttons, cards, section wrappers)

3. **Build each section.** Working through the component manifest section by section:
   - Implement each component with the selected design
   - Wire in the generated images
   - Add copy and CTAs from the brief
   - Apply animations and interactions
   - Ensure responsive behavior (mobile-first)

4. **Quality checks before deploy:**
   - Responsive: test at mobile (375px), tablet (768px), desktop (1280px+)
   - Performance: lazy-load images, use Next.js `<Image>` component
   - Accessibility: proper heading hierarchy, alt text, color contrast, keyboard navigation
   - SEO: meta tags, Open Graph tags, structured data if relevant
   - Dark mode: implement if specified in the brief

5. **Deploy to Vercel.** Use the Vercel MCP tools:
   - Run `vercel deploy` or use the `deploy_to_vercel` MCP tool
   - Verify the deployment is live
   - Share the live URL with the user

6. **Post-deploy review.** After deployment:
   - Open the live URL and verify everything looks correct
   - Check Core Web Vitals (LCP, CLS, FID)
   - Share the URL with the user and ask for final feedback
   - Make any last adjustments and redeploy if needed

---

## Important Principles

**Don’t rush the brief.** The biggest mistake is jumping to code before understanding what the user wants. Phase 1 should feel like a conversation with a thoughtful designer, not a form to fill out.

**Show, don’t tell.** At every checkpoint, show the user something concrete — a reference site, a color palette swatch, a component preview, a generated image. Abstract descriptions ("I’ll use a modern style") are useless compared to visual evidence.

**Maintain design coherence.** Every element should trace back to the brief. If a component looks off, it’s usually because it drifted from the design system. When in doubt, refer back to the UUPM recommendations and the brief.

**Iterate fast, deploy often.** Don’t wait for perfection to deploy. Get a working version live and iterate. Vercel makes redeployment trivial.

**The user has final say.** At each checkpoint (brief, component manifest, images, pre-deploy), pause and get explicit user approval. Don’t assume — ask.


---

## Phase 2: UI Component Selection & Layout

**Goal:** Translate the UX brief into concrete UI building blocks.

Now that you know *what* to build and *how it should feel*, select the actual components that will make up the page.

### How to run this phase

1. **Plan the page structure.** Based on the brief, outline the sections the landing page needs. A typical landing page follows a pattern like:
   - Hero section (headline + CTA + visual)
   - Social proof / logos bar
   - Features / benefits section
   - How it works / process
   - Testimonials
   - Pricing (if applicable)
   - Final CTA / footer

   Adapt this to the user’s needs — not every page needs every section. Confirm the section plan with the user.

2. **Select UI components from 21st.dev.** Use the 21st.dev Magic MCP to search for and generate components that match the design direction. For each section, use the `/ui` pattern to describe what you need:
   - Be specific about the visual style from the brief (e.g., "create a glassmorphic hero section with gradient text and a floating CTA button")
   - Reference the color palette and typography from the brief
   - Generate components one section at a time so you can review each

   If the 21st.dev MCP is not connected, search 21st.dev/community/components via web search for inspiration and build custom components using the design system from Phase 1.

3. **Apply the frontend-design skill.** Before writing any component code, invoke the frontend-design skill. This ensures Claude avoids generic "AI slop" aesthetics and makes bold, distinctive design choices. The frontend-design skill pushes toward:
   - Unusual, memorable font choices
   - Bold color usage (not safe grays)
   - Atmospheric effects and purposeful animations
   - Layouts that feel crafted, not templated

4. **Create a component manifest.** Document which components go where:

```
# Component Manifest

## Hero
- Component: [name/source]
- Customizations: [color overrides, copy, CTA text]

## Features
- Component: [name/source]
- Layout: [grid/cards/list]
- Items: [3-6 feature blocks]

[... etc for each section]
```

Present the manifest to the user. This is checkpoint #2.

---

## Phase 3: Image Generation

**Goal:** Create custom visual assets that make the site feel unique and on-brand.

Stock photos kill distinctiveness. This phase uses **Nano Banana 2** — Google Gemini 3.1 Flash Image Preview, accessed through the inference.sh CLI (`infsh`) — to generate custom images tailored to the project’s specific aesthetic.

### Prerequisites

Install the Nano Banana 2 skill and inference.sh CLI:

```bash
npx skills add inference-sh/skills@agent-tools
infsh login
```

### How to run this phase

1. **Identify image needs.** Based on the component manifest, list every place an image is needed:
   - Hero background or illustration
   - Feature icons or illustrations
   - About/team section visuals
   - Background textures or patterns
   - Product mockups or screenshots

2. **Generate images with Nano Banana 2.** For each image need, construct a detailed prompt that incorporates the design direction from the brief. Use the `infsh` CLI:

   ```bash
   infsh app run google/gemini-3-1-flash-image-preview --input '{"prompt": "detailed prompt here", "aspect_ratio": "16:9", "resolution": "2K"}'
   ```

   Key parameters:
   - `prompt` (required): Describe what to generate. Include specific colors from the brief
   - `aspect_ratio`: "1:1", "16:9", "9:16", "4:3", "3:4", or "auto"
   - `resolution`: "1K" (default), "2K", or "4K"
   - `num_images`: Generate multiple variants (e.g., 4) to pick the best
   - `images`: Array of image URLs for editing/style transfer
   - `enable_google_search`: Set to true for real-world grounding (weather, landmarks, etc.)

   **Example commands:**

   ```bash
   # Hero image (high quality, wide)
   infsh app run google/gemini-3-1-flash-image-preview --input '{
     "prompt": "Futuristic cityscape at sunset, deep navy #1a1a2e sky with teal #0dd9ff neon accents, photorealistic, cinematic wide shot",
     "aspect_ratio": "16:9",
     "resolution": "2K"
   }'

   # Feature icons (multiple variants, square)
   infsh app run google/gemini-3-1-flash-image-preview --input '{
     "prompt": "Minimal line icon of a document with a checkmark, teal outline on transparent background, flat vector style",
     "aspect_ratio": "1:1",
     "num_images": 4
   }'

   # Edit an existing image
   infsh app run google/gemini-3-1-flash-image-preview --input '{
     "prompt": "Add a warm golden sunset glow to the background",
     "images": ["./public/images/hero.png"]
   }'
   ```

   **Prompting tips:**
   - Specify style: photorealistic, illustration, watercolor, 3D render, flat vector
   - Include colors from the brief by hex value
   - Describe composition: close-up, wide shot, aerial view, macro
   - Mention lighting: natural light, studio lighting, golden hour, neon
   - Add mood/atmosphere details for consistency across images

3. **Review generated images.** Show the user the generated images. Regenerate any that don’t fit. Image generation is iterative — expect 2-3 rounds for hero images. Use the `images` parameter to pass a previous result for editing refinements.

4. **Optimize for web.** After approval, ensure all images are properly sized and optimized:
   - Convert to WebP where appropriate
   - Generate responsive sizes if needed
   - Place in the Next.js `public/images/` directory

---

## Phase 4: Build & Deploy

**Goal:** Assemble everything into a working Next.js site and deploy it live to Vercel.

### How to run this phase

1. **Scaffold the Next.js project.** Create a new Next.js app with the App Router:

   ```bash
   npx create-next-app@latest [project-name] --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
   ```

   Then install any additional dependencies needed for the selected components (e.g., `framer-motion` for animations, `lucide-react` for icons).

2. **Implement the design system.** Set up the design tokens from the brief:
   - Configure Tailwind with the color palette, typography, and spacing
   - Set up Google Fonts via `next/font`
   - Create any shared components (buttons, cards, section wrappers)

3. **Build each section.** Working through the component manifest section by section:
   - Implement each component with the selected design
   - Wire in the generated images
   - Add copy and CTAs from the brief
   - Apply animations and interactions
   - Ensure responsive behavior (mobile-first)

4. **Quality checks before deploy:**
   - Responsive: test at mobile (375px), tablet (768px), desktop (1280px+)
   - Performance: lazy-load images, use Next.js `<Image>` component
   - Accessibility: proper heading hierarchy, alt text, color contrast, keyboard navigation
   - SEO: meta tags, Open Graph tags, structured data if relevant
   - Dark mode: implement if specified in the brief

5. **Deploy to Vercel.** Use the Vercel MCP tools:
   - Run `vercel deploy` or use the `deploy_to_vercel` MCP tool
   - Verify the deployment is live
   - Share the live URL with the user

6. **Post-deploy review.** After deployment:
   - Open the live URL and verify everything looks correct
   - Check Core Web Vitals (LCP, CLS, FID)
   - Share the URL with the user and ask for final feedback
   - Make any last adjustments and redeploy if needed

---

## Important Principles

**Don’t rush the brief.** The biggest mistake is jumping to code before understanding what the user wants. Phase 1 should feel like a conversation with a thoughtful designer, not a form to fill out.

**Show, don’t tell.** At every checkpoint, show the user something concrete — a reference site, a color palette swatch, a component preview, a generated image. Abstract descriptions ("I’ll use a modern style") are useless compared to visual evidence.

**Maintain design coherence.** Every element should trace back to the brief. If a component looks off, it’s usually because it drifted from the design system. When in doubt, refer back to the UUPM recommendations and the brief.

**Iterate fast, deploy often.** Don’t wait for perfection to deploy. Get a working version live and iterate. Vercel makes redeployment trivial.

**The user has final say.** At each checkpoint (brief, component manifest, images, pre-deploy), pause and get explicit user approval. Don’t assume — ask.
