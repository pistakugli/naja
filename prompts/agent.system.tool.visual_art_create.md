### visual_art_create:

Creates visual artwork, posters, graphics using design principles.

**⚠️ CRITICAL WORKFLOW:**

**STEP 1: Read Skill**
```json
{
  "thoughts": ["Reading canvas-design skill for visual art philosophy"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "terminal",
    "code": "cat /home/claude/naja/skills/examples/canvas-design/SKILL.md | head -200"
  }
}
```

**STEP 2: Create Artwork**
```json
{
  "thoughts": [
    "Creating original visual art following design philosophy",
    "Using proper composition, color theory, and aesthetics"
  ],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "python",
    "code": "from PIL import Image, ImageDraw, ImageFont\n\n# Create canvas\nimg = Image.new('RGB', (800, 600), color='white')\ndraw = ImageDraw.Draw(img)\n\n# Add elements (text, shapes, etc)\ndraw.rectangle([100, 100, 700, 500], outline='black', width=3)\ndraw.text((400, 300), 'Artwork Title', fill='black', anchor='mm')\n\n# Save\nimg.save('/root/artwork.png')\nprint('✅ Artwork created: /root/artwork.png')"
  }
}
```

**WHEN TO USE:**
- "Create poster/graphic/artwork"
- Visual designs, infographics
- Original art pieces

**CAPABILITIES:**
- PIL/Pillow for image creation
- SVG for vector graphics
- p5.js for generative art (see algorithmic-art skill)

**DESIGN PRINCIPLES FROM SKILL:**
- Original work (never copy existing artists)
- Proper composition and balance
- Color theory application
- Typography selection
- Visual hierarchy

**FILE LOCATION:**
Save to: `/root/artwork.png` (or .svg, .jpg)

This uses code_execution_tool with Python runtime.
