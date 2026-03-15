# Tool Integration Reference

This document provides detailed guidance on integrating each external tool in the webdesign pipeline.

## Table of Contents
1. UI UX Pro Max (UUPM)
2. 21st.dev Magic MCP
3. Nano Banana (Image Generation)
4. Frontend-Design Skill
5. Vercel Deployment

---

## 1. UI UX Pro Max (UUPM)

UUPM provides a design intelligence database with 161 product categories, 67 UI styles, 161 color palettes, 57 font pairings, and 25 chart types.

### How to invoke
UUPM activates automatically when UI/UX work is requested. To use it explicitly, describe the product type and requirements clearly. UUPM’s reasoning engine will:
- Match the product to one of 161 industry categories
- Recommend a UI style direction with BM25 scoring
- Generate a color palette with mood rationale
- Select typography pairings from Google Fonts
- Suggest layout patterns and anti-patterns

### Best practices
- Provide the product category and target audience upfront so UUPM can match accurately
- Use the anti-pattern guidance — knowing what NOT to do is as valuable as knowing what to do
- Don’t blindly follow every recommendation; use them as a strong starting point and let user preferences override

---

## 2. 21st.dev Magic MCP

21st.dev provides AI-generated React UI components through an MCP server.

### Setup
If not already configured, install via:
```bash
npx @21st-dev/cli@latest install claude --api-key YOUR_KEY
```

### Usage pattern
Use natural language to describe components. Be specific about:
- Visual style (reference the design direction from the brief)
- Color palette (provide hex values)
- Functionality (what the component does)
- Layout (responsive behavior)

Example: "Create a hero section with a gradient background from #1a1a2e to #16213e, centered headline in Inter Bold, a glowing CTA button, and a floating 3D mockup on the right"

### Fallback
If the 21st.dev MCP is not connected, use web search to browse https://21st.dev/community/components for design inspiration, then build components manually using the design system from Phase 1.

---

## 3. Nano Banana (Image Generation)

Nano Banana uses Google’s Gemini models for image generation via CLI.

### Prerequisites
- Gemini API key stored in `~/.nano-banana/.env`
- Bun runtime installed
- nano-banana CLI installed globally

### Command reference
```bash
# Basic generation
nano-banana "prompt" -o filename -d ./public/images

# High-quality hero image
nano-banana "prompt" -s 2K -a 16:9 -m pro -o hero -d ./public/images

# Transparent asset (icon/illustration)
nano-banana "prompt" -s 1K -a 1:1 -t -o icon-name -d ./public/images

# Style transfer from reference
nano-banana "prompt" -r reference.png -s 2K -o styled -d ./public/images
```

### Resolution & cost guide
| Size | Flash cost | Pro cost | Use for |
|------|-----------|----------|---------|
| 512  | ~$0.04    | ~$0.13   | Thumbnails, small icons |
| 1K   | ~$0.05    | ~$0.15   | Feature illustrations, cards |
| 2K   | ~$0.08    | ~$0.20   | Hero images, backgrounds |
| 4K   | ~$0.15    | ~$0.30   | Full-bleed hero, print-quality |

### Prompting tips
- Include the brand’s color palette in prompts: "using a color palette of deep navy #1a1a2e and warm amber #f4a261"
- Specify style explicitly: "flat illustration style" or "photorealistic" or "3D rendered"
- For consistency across images, reuse style descriptors and reference previous outputs with `-r`
- Use `-t` for any asset that needs to composite over a colored background

---

## 4. Frontend-Design Skill

Anthropic’s official frontend-design skill pushes Claude toward distinctive, non-generic UI.

### How it works
When invoked, it provides Claude with a design philosophy that emphasizes:
- Bold, unusual font choices (not just Inter and system fonts)
- Distinctive color usage (not safe corporate grays)
- Atmospheric effects (gradients, blur, grain, shadows)
- Purposeful animations (not gratuitous movement)
- Layouts that feel hand-crafted

### When to invoke
Invoke the frontend-design skill BEFORE writing any component code in Phase 4. It sets the creative tone for all code generation that follows.

### Relationship to UUPM
UUPM provides the *what* (which styles, colors, fonts to use), while frontend-design provides the *how* (the craft and attention to detail in implementation). They complement each other — use UUPM for the design system, then frontend-design for the execution quality.

---

## 5. Vercel Deployment

### Via MCP tools
If Vercel MCP is connected, use these tools:
- `deploy_to_vercel` — Deploy the project
- `list_projects` — Check existing projects
- `get_deployment` — Check deployment status
- `get_deployment_build_logs` — Debug build failures

### Via CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy (will prompt for project setup on first run)
vercel

# Deploy to production
vercel --prod
```

### Next.js optimization for Vercel
- Use `next/image` for automatic image optimization
- Use `next/font` for zero-layout-shift font loading
- Enable ISR if any content is dynamic
- Set up `vercel.json` for custom headers, redirects if needed
