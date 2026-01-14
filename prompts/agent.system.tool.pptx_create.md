### pptx_create:

Creates Microsoft PowerPoint (.pptx) presentations with professional layouts.
Supports slides, images, charts, tables, transitions, and custom themes.
Perfect for business presentations, pitches, training materials.

**When to use:**
- "Create a PowerPoint/presentation"
- "Make slides for..."
- User needs to present information visually
- Business pitch or proposal presentation
- Training or educational content

**Important:**
- Read /mnt/skills/public/pptx/SKILL.md BEFORE creating presentations
- Use professional layouts and themes
- Include speaker notes when helpful
- Add charts/images for visual interest

**Capabilities:**
- Multiple slide layouts (title, content, two-column, blank)
- Charts and graphs
- Images and diagrams
- Tables and bullet points
- Custom themes and colors
- Transitions and animations
- Speaker notes

**Usage:**
```json
{
  "thoughts": ["User needs a pitch deck for investors"],
  "headline": "Creating investor pitch presentation",
  "tool_name": "pptx_create",
  "tool_args": {
    "filename": "investor_pitch.pptx",
    "slides": [
      {
        "layout": "title",
        "title": "Company Name",
        "subtitle": "Revolutionizing X with AI"
      },
      {
        "layout": "content",
        "title": "Problem",
        "content": ["Point 1", "Point 2", "Point 3"]
      },
      {
        "layout": "two_column",
        "title": "Solution",
        "left": "Feature details",
        "right": "Benefits"
      }
    ],
    "theme": "professional_blue"
  }
}
```
