---
name: icondesign
description: |
  Design custom icons for websites and presentations from plain-language descriptions. Use this skill whenever the user asks to "create an icon", "design an icon", "make me an icon", "I need an icon for...", "generate an icon", "icon set", "icon pack", or describes needing a visual symbol, pictogram, glyph, or small graphic element for a UI, website, app, slide deck, or presentation. Also triggers on requests like "make a settings gear icon", "I need a shopping cart icon in blue", or "create icons for my navigation menu". Even if the user just says "I need a little image for X" and the context suggests an icon, use this skill. This skill combines hand-crafted SVG, Canva design generation, and Nano Banana Pro AI image generation to deliver production-ready icons in PNG and SVG.
---

# Icon Designer

You design icons from plain-language descriptions and deliver production-ready files — by default **PNG** and **SVG** — using a combination of hand-crafted SVG, **Canva** for AI-generated design options, and **Nano Banana Pro** for photorealistic or complex artistic styles.

## Gather Requirements

Before generating anything, collect the essentials. If the user already provided most of these, just confirm and fill gaps — don't re-ask everything:

1. **Subject** — What does the icon depict? ("shopping cart", "padlock", "cloud with download arrow")
2. **Style** — Flat/minimal (default), outlined, filled, gradient, 3D, or sketch
3. **Colors** — Hex codes, names, or palette ("blue #3B82F6 on transparent", "navy and gold")
4. **Background** — Transparent (default) or specific color
5. **Sizes** — Defaults: 16, 24, 32, 48, 64px (web) + 128, 256, 512px (presentation). User can override.
6. **Formats** — Default: PNG + SVG. May also want ICO (favicon), JPG.
7. **Quantity** — Single icon or a set? If a set, what does each icon represent?

## Generation Strategy

Choose your approach based on the icon's style. This matters because each tool has different strengths:

### Path A: SVG-First (preferred for flat, outlined, filled icons)

This is the **default path** for most icon requests. Icons are inherently vector graphics — clean geometric shapes, consistent strokes, precise colors. Writing SVG directly produces the crispest, most scalable results and gives you both formats (SVG native, PNG via conversion) in one shot.

Write an SVG file with these characteristics:
- Use a `viewBox="0 0 256 256"` for a comfortable working canvas
- Build from basic SVG primitives: `<circle>`, `<rect>`, `<path>`, `<line>`, `<polygon>`
- Use the user's exact hex colors (set via `fill` and `stroke` attributes)
- Keep shapes simple and bold — icons need to read clearly at 16px
- Center the composition with comfortable padding (~15% margin)
- Use `stroke-linecap="round"` and `stroke-linejoin="round"` for polished edges
- No bitmap effects, filters, or embedded images — keep it pure vector

**SVG quality checklist** (verify before delivering):
- Does it look correct when you mentally render it? Trace through each shape.
- Are all paths closed properly?
- Is the icon centered and balanced?
- Do the colors match what the user asked for?
- Would it still be recognizable at 32px?

**Example: Shopping cart icon in SVG**
```xml
<svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
  <!-- Cart body -->
  <polyline points="44,56 76,56 108,168 204,168"
    fill="none" stroke="#3B82F6" stroke-width="14"
    stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Cart basket -->
  <polyline points="84,96 212,96 196,168"
    fill="none" stroke="#3B82F6" stroke-width="14"
    stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Wheels -->
  <circle cx="124" cy="204" r="16" fill="#3B82F6"/>
  <circle cx="188" cy="204" r="16" fill="#3B82F6"/>
</svg>
```

Notice how the SVG uses simple shapes with generous stroke widths — this reads well at any size. This is the quality bar to aim for.

### Path B: Canva Generation (for polished, branded, or complex designs)

Use this when the user wants something more polished than geometric SVG can provide, or when they want multiple design options to choose from.

1. Call `generate-design-structured` (preferred) or `generate-design` with:
   - `design_type`: `"logo"` (this is the closest match for icon design)
   - A detailed query describing the icon: subject, style, colors, "simple icon" framing
2. Present the candidates to the user — Canva returns several options
3. Use `create-design-from-candidate` for the user's pick
4. Export as PNG with `export-design` using `transparent_background: true` and `lossless: true`

For SVG output from Canva-generated icons: recreate the design as clean SVG based on what Canva produced. Use the Canva output as a visual reference and build the SVG with the same shapes, colors, and proportions.

### Path C: Nano Banana Pro (for artistic, photorealistic, or highly detailed icons)

Use this for icon styles that benefit from AI image generation — gradient-heavy, 3D/isometric, sketch/hand-drawn, or photorealistic. These are hard to achieve with pure SVG.

Craft the prompt carefully:
```
A [style] icon of [subject], [exact color hex codes], clean edges, simple shapes,
centered composition, transparent background, no text, crisp edges suitable for
display at small sizes, modern UI style
```

The prompt should always include "icon" or "pictogram" to keep the generation anchored to symbolic imagery rather than detailed illustrations.

After generation, the Nano Banana Pro output is a raster image. For SVG output of artistic icons, trace the image or let the user know that the SVG will be a simplified/geometric version of the AI-generated design.

## Converting to Multiple Formats and Sizes

Once you have your primary output (SVG from Path A, or PNG from Path B/C), generate the other formats:

### SVG → PNG (for Path A)

Run the bundled conversion script. Read and execute the script at `scripts/svg_to_png.py` relative to this skill's directory:

```bash
pip install Pillow cairosvg --break-system-packages 2>/dev/null
python <skill-dir>/scripts/svg_to_png.py icon.svg --sizes 16,24,32,48,64,128,256,512 --output-dir ./sizes/
```

If `cairosvg` fails to install, fall back to Pillow's SVG rendering or use Python to generate PNGs directly from the SVG shapes (translate the SVG elements to PIL drawing commands). In the worst case, write a simple HTML page with the SVG embedded, screenshot it, and resize.

### PNG → SVG (for Path B/C)

For flat/solid icons generated as PNG, auto-trace to SVG:
```bash
pip install Pillow numpy --break-system-packages 2>/dev/null
```
Build the SVG by hand based on the shapes visible in the PNG. For flat icons with solid colors, this works well — identify the major shapes and colors, then write SVG elements that recreate them.

For complex icons where auto-tracing won't produce clean vectors, be upfront: deliver the high-res PNG and explain that a clean SVG would need manual design work.

### ICO Generation (for favicons)

If the user needs a favicon:
```python
from PIL import Image
img = Image.open("icon_32.png")
img.save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
```

## Deliver the Files

Save everything to the output directory with clear naming:

```
icon-output/
├── icon.svg              (vector source)
├── icon_512.png          (largest PNG)
├── sizes/
│   ├── icon_16x16.png
│   ├── icon_24x24.png
│   └── ... (all requested sizes)
├── favicon.ico           (if requested)
└── canva_link.txt        (if Canva was used — link to editable design)
```

Present the user with file links and a brief summary: what was generated, style/colors used, sizes included. If Canva was used, include the link to the editable design.

## For Icon Sets

When the user asks for multiple icons (like a navigation set or presentation icons):
- Design all icons in the **same visual style** — consistent stroke width, corner radius, padding, and color palette
- If using SVG (Path A), establish the style parameters once (stroke-width, colors, corner radii) and reuse them across all icons
- Deliver each icon as its own file, plus a preview showing all icons together
- Name files by what they represent: `lightbulb.svg`, `target.svg`, `handshake.svg`

## Compatibility

This skill works best with:
- **Canva MCP connector** — for AI-powered design generation and PNG export
- **Nano Banana Pro** — for AI image generation of artistic/complex icons (install via `npx skills add https://github.com/inference-sh-9/skills --skill nano-banana`)
- **Python + Pillow + cairosvg** — for format conversion and resizing

If tools are unavailable, the SVG-first path (Path A) works with no external dependencies at all — just write the SVG code and use Pillow for PNG conversion.
