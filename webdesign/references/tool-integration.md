# Tool Integration Reference

This document provides detailed guidance on integrating each external tool in the webdesign pipeline.

## Table of Contents
1. UI UX Pro Max (UUPM)
2. 21st.dev Magic MCP
3. Nano Banana 2 (Image Generation)
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

## 3. Nano Banana 2 (Image Generation)

Nano Banana 2 uses Google Gemini 3.1 Flash Image Preview for image generation via the inference.sh CLI (`infsh`).

Source: https://github.com/inference-sh/skills/tree/main/tools/image/nano-banana-2

### Prerequisites
```bash
# Install the inference.sh skills and CLI
npx skills add inference-sh/skills@agent-tools
infsh login
```

### Command reference
```bash
# Basic text-to-image generation
infsh app run google/gemini-3-1-flash-image-preview --input '{
  "prompt": "A futuristic cityscape at sunset with flying cars"
}'

# High-quality hero image (2K, wide)
infsh app run google/gemini-3-1-flash-image-preview --input '{
  "prompt": "detailed prompt here",
  "aspect_ratio": "16:9",
  "resolution": "2K"
}'

# Multiple variants to choose from
infsh app run google/gemini-3-1-flash-image-preview --input '{
  "prompt": "Minimalist logo design for a coffee shop",
  "num_images": 4
}'

# Edit an existing image
infsh app run google/gemini-3-1-flash-image-preview --input '{
  "prompt": "Add a rainbow in the sky",
  "images": ["https://example.com/landscape.jpg"]
}'

# 4K resolution
infsh app run google/gemini-3-1-flash-image-preview --input '{
  "prompt": "Detailed illustration of a medieval castle",
  "resolution": "4K"
}'

# With Google Search grounding (real-world accuracy)
infsh app run google/gemini-3-1-flash-image-preview --input '{
  "prompt": "Current weather in Tokyo visualized as an artistic scene",
  "enable_google_search": true
}'
```

### Input parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `prompt` | string | Required. What to generate or edit |
| `images` | array | Input images for editing (up to 14). JPEG, PNG, WebP |
| `num_images` | integer | Number of images to generate |
| `aspect_ratio` | string | "1:1", "16:9", "9:16", "4:3", "3:4", "auto" |
| `resolution` | string | "1K" (default), "2K", "4K" |
| `enable_google_search` | boolean | Enable real-time info grounding |

### Prompting tips
- **Styles:** photorealistic, illustration, watercolor, oil painting, digital art, anime, 3D render
- **Composition:** close-up, wide shot, aerial view, macro, portrait, landscape
- **Lighting:** natural light, studio lighting, golden hour, dramatic shadows, neon
- **Details:** add specific textures, colors (use hex values from the brief), mood, atmosphere
- **Consistency:** reuse style descriptors across prompts for a cohesive image set

### Sample workflow
```bash
# 1. Generate a sample input to see all available options
infsh app sample google/gemini-3-1-flash-image-preview --save input.json

# 2. Edit the prompt in input.json

# 3. Run with the edited input
infsh app run google/gemini-3-1-flash-image-preview --input input.json
```

### Related skills
```bash
# Original Nano Banana (Gemini 3 Pro / Gemini 2.5 Flash)
npx skills add inference-sh/skills@nano-banana

# All image generation models
npx skills add inference-sh/skills@ai-image-generation
```

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
