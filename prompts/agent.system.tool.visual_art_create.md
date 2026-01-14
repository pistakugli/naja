### visual_art_create:

Creates beautiful visual art in PNG and PDF formats using design philosophy.
Use for posters, graphics, artwork, or any static visual piece.
Creates original designs - never copies existing artists' work.

**When to use:**
- "Create a poster"
- "Design artwork for..."
- "Make a visual/graphic"
- User needs visual design (not code)
- Any static piece of art

**Important:**
- Read /mnt/skills/examples/canvas-design/SKILL.md FIRST
- Create ORIGINAL art - never copy existing artists
- Use design principles (color theory, composition, typography)
- Output both PNG (for web) and PDF (for print)

**Capabilities:**
- Posters and flyers
- Social media graphics
- Infographics
- Album art
- Logo concepts
- Illustrations
- Typography art

**Usage - Event poster:**
```json
{
  "thoughts": ["User needs a concert poster"],
  "headline": "Creating concert poster with bold typography",
  "tool_name": "visual_art_create",
  "tool_args": {
    "art_type": "poster",
    "title": "Summer Music Festival 2026",
    "content": {
      "headline": "SUMMER MUSIC FESTIVAL",
      "date": "July 15-17, 2026",
      "location": "Central Park",
      "artists": ["Artist 1", "Artist 2", "Artist 3"]
    },
    "style": "bold_modern",
    "colors": ["#FF6B6B", "#4ECDC4", "#FFD93D"],
    "size": "18x24_inches",
    "output_formats": ["png", "pdf"]
  }
}
```

**Usage - Social media graphic:**
```json
{
  "thoughts": ["User wants an Instagram post about their product launch"],
  "headline": "Designing product launch graphic",
  "tool_name": "visual_art_create",
  "tool_args": {
    "art_type": "social_media",
    "platform": "instagram",
    "message": "New Product Launch!",
    "visual_elements": [
      "Product mockup",
      "Bold headline",
      "Launch date",
      "Call to action"
    ],
    "style": "minimalist_modern",
    "output_formats": ["png"]
  }
}
```

**Design approach:**
- Original concepts only
- Strong visual hierarchy
- Color theory application
- Typography mastery
- Composition balance
- Cultural sensitivity
