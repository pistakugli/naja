### docx_create:

Creates Microsoft Word documents (.docx) with professional formatting.

**⚠️ CRITICAL WORKFLOW - MUST FOLLOW:**

**STEP 1: Read Skill First (REQUIRED for professional output)**
```json
{
  "thoughts": ["Must read docx skill to learn professional formatting best practices"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "terminal",
    "code": "cat /home/claude/naja/skills/public/docx/SKILL.md | head -200"
  }
}
```

**STEP 2: Create Document with Learned Knowledge**
```json
{
  "thoughts": [
    "Creating professional Word document following skill guidelines",
    "Using proper heading hierarchy, styles, and formatting"
  ],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "python",
    "code": "from docx import Document\nfrom docx.shared import Inches, Pt, RGBColor\nfrom docx.enum.text import WD_ALIGN_PARAGRAPH\n\n# Create document\ndoc = Document()\n\n# Title (Heading level 0)\ntitle = doc.add_heading('Document Title', 0)\ntitle.alignment = WD_ALIGN_PARAGRAPH.CENTER\n\n# Add sections with proper hierarchy\ndoc.add_heading('Section 1', level=1)\np = doc.add_paragraph('Content goes here...')\n\n# Tables (if needed)\ntable = doc.add_table(rows=3, cols=3)\ntable.style = 'Light Grid Accent 1'\n\n# Save to /root/\ndoc.save('/root/output.docx')\nprint('✅ Document created: /root/output.docx')"
  }
}
```

**WHEN TO USE:**
- User requests: "create Word document", "write report", "make proposal"
- Professional documents: reports, proposals, letters, resumes
- Any .docx file needed

**KEY LIBRARIES (pre-installed):**
- `python-docx` for document creation
- `from docx import Document`
- `from docx.shared import Inches, Pt, RGBColor`
- `from docx.enum.text import WD_ALIGN_PARAGRAPH`

**FORMATTING CAPABILITIES:**
- Headings (levels 0-9)
- Bold, italic, underline text
- Tables with styles
- Images (using `doc.add_picture(path, width=Inches(2))`)
- Headers/footers
- Page breaks
- Bullet/numbered lists

**FILE LOCATION:**
Always save to: `/root/filename.docx`

**EXAMPLE - Security Report:**
1. Read skill: Learn structure and formatting
2. Create document with:
   - Title page (heading level 0, centered)
   - Executive summary (heading level 1)
   - Findings table (3 columns: Vulnerability, Severity, Description)
   - Detailed analysis (heading level 2 subsections)
   - Recommendations (numbered list)
   - Professional styling throughout

**NEVER:**
- Skip reading the skill file (results in amateur output)
- Use docx_create as if it's a direct tool (it doesn't exist!)
- Output only text without creating actual file
- Create files outside /root/ directory

**BEST PRACTICES FROM SKILL:**
- Use heading hierarchy: 0 for title, 1 for main sections, 2-3 for subsections
- Apply table styles for better appearance
- Add page breaks between major sections
- Use proper alignment (left for body, center for titles)
- Include formatted lists for action items

This tool uses code_execution_tool with Python runtime.
Skills make output professional vs. generic AI-looking.
