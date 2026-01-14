### pptx_create:

Creates PowerPoint presentations (.pptx) with professional layouts and design.

**⚠️ CRITICAL WORKFLOW - MUST FOLLOW:**

**STEP 1: Read Skill First**
```json
{
  "thoughts": ["Reading pptx skill for presentation best practices"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "terminal",
    "code": "cat /home/claude/naja/skills/public/pptx/SKILL.md | head -200"
  }
}
```

**STEP 2: Create Presentation**
```json
{
  "thoughts": [
    "Creating professional PowerPoint following skill guidelines",
    "Using proper layouts, charts, and design principles"
  ],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "python",
    "code": "from pptx import Presentation\nfrom pptx.util import Inches, Pt\nfrom pptx.enum.text import PP_ALIGN\n\n# Create presentation\nprs = Presentation()\n\n# Title slide\nslide = prs.slides.add_slide(prs.slide_layouts[0])\ntitle = slide.shapes.title\nsubtitle = slide.placeholders[1]\ntitle.text = 'Presentation Title'\nsubtitle.text = 'Subtitle or Date'\n\n# Content slide\nslide = prs.slides.add_slide(prs.slide_layouts[1])\ntitle = slide.shapes.title\ntitle.text = 'Key Points'\ncontent = slide.placeholders[1]\ntf = content.text_frame\ntf.text = 'First point'\nfor point in ['Second point', 'Third point']:\n    p = tf.add_paragraph()\n    p.text = point\n    p.level = 0\n\n# Save\nprs.save('/root/presentation.pptx')\nprint('✅ Presentation created: /root/presentation.pptx')"
  }
}
```

**SLIDE LAYOUTS (prs.slide_layouts[N]):**
- `[0]` - Title slide
- `[1]` - Title and content
- `[5]` - Title only
- `[6]` - Blank

**WHEN TO USE:**
- "Create PowerPoint/slides/presentation"
- Training materials, pitches, reports
- Any visual slide deck needed

**KEY CAPABILITIES:**
- Multiple slide layouts
- Bullet points and text formatting
- Charts (bar, line, pie)
- Tables
- Images (`slide.shapes.add_picture(path, left, top, width)`)

**FILE LOCATION:**
Always save to: `/root/filename.pptx`

**EXAMPLE - Security Training:**
1. Read skill for layout and design best practices
2. Create slides:
   - Title slide
   - Agenda slide (bulleted list)
   - Content slides with key points
   - Conclusion slide
3. Use consistent styling throughout

**NEVER:**
- Skip skill (results in poorly designed slides)
- Overcrowd slides with text
- Use more than 5-7 bullet points per slide

This uses code_execution_tool with Python and python-pptx library.
