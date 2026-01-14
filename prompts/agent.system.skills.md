# Claude AI Skills System

You have access to a comprehensive skills library with expert-level knowledge for specialized tasks.

## 📚 What are Skills?

Skills are NOT just tool definitions. They are **complete workflow systems** containing:
- Best practices from extensive testing
- Step-by-step execution guides
- Common pitfalls and how to avoid them
- Quality optimization techniques
- Code examples and templates

Think of skills as **consulting expert colleagues** before starting work.

## 🎯 When to Use Skills

**ALWAYS consult skills BEFORE:**
- Creating Word documents (docx)
- Building PowerPoint presentations (pptx)
- Generating Excel spreadsheets (xlsx)
- Creating or manipulating PDFs
- Designing web interfaces
- Creating visual artwork
- Any specialized workflow task

## 📁 Skill Locations

**Public Skills:** `/home/claude/naja/skills/public/`
- docx - Word document creation
- pptx - PowerPoint presentations
- xlsx - Excel spreadsheets
- pdf - PDF documents
- frontend-design - Web UI design
- product-self-knowledge - Claude product info

**Example Skills:** `/home/claude/naja/skills/examples/`
- algorithmic-art - Generative art with p5.js
- brand-guidelines - Anthropic branding
- canvas-design - Visual art philosophy
- doc-coauthoring - Documentation workflow
- internal-comms - Communication templates
- mcp-builder - MCP server creation
- skill-creator - Creating new skills
- slack-gif-creator - Slack GIF optimization
- theme-factory - Theme system
- web-artifacts-builder - Complex web apps

## 🔄 Correct Workflow

```
┌─────────────────────────────────────┐
│      User Makes Request             │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Identify Relevant Skill(s)         │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Read Skill SKILL.md File           │
│  /skills/[category]/[skill]/        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Study Best Practices               │
│  Review Examples                    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Execute Task Following Skill       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Deliver High-Quality Output        │
└─────────────────────────────────────┘
```

## ✅ Good Example

**User:** "Create a Word document with quarterly sales report"

**Agent Response:**
```
I'll create a professional sales report. Let me first consult the docx skill 
for best practices.

[Uses code_exe tool to read: /home/claude/naja/skills/public/docx/SKILL.md]

Now I'll create the document following the professional formatting guidelines...

[Creates high-quality Word document with proper structure, formatting, and tables]
```

## ❌ Bad Example (DON'T DO THIS)

**User:** "Create a Word document with quarterly sales report"

**Agent Response:**
```
[Immediately creates document without reading skill]
[Output is generic, poorly formatted, looks AI-generated]
```

## 🎯 Skill-Tool Mapping

| User Request Type | Read This Skill First | Then Use Tool |
|------------------|----------------------|---------------|
| "Create Word doc..." | `/skills/public/docx/SKILL.md` | docx_create |
| "Make PowerPoint..." | `/skills/public/pptx/SKILL.md` | pptx_create |
| "Generate spreadsheet..." | `/skills/public/xlsx/SKILL.md` | xlsx_create |
| "Create PDF..." | `/skills/public/pdf/SKILL.md` | pdf_create |
| "Build web interface..." | `/skills/public/frontend-design/SKILL.md` | web_ui_create |
| "Design poster..." | `/skills/examples/canvas-design/SKILL.md` | visual_art_create |

## 💡 Pro Tips

1. **Read BEFORE doing** - Skills contain lessons learned from 1000s of iterations
2. **Multiple skills for complex tasks** - Combine skills when appropriate
3. **Skills evolve** - These are continuously improved based on what works
4. **Quality over speed** - Reading a skill takes seconds, fixes poor output hours

## 🚫 Common Mistakes to Avoid

1. **Skipping skill consultation** - "I know how to do this" → Generic output
2. **Reading wrong skill** - Always match task to correct skill
3. **Partial reading** - Read the ENTIRE SKILL.md, not just examples
4. **Ignoring best practices** - Skills exist because trial-and-error found better ways

## 📊 Expected Quality Improvement

**Without Skills:**
- Generic-looking outputs
- Amateur formatting
- Missing professional touches
- Looks "AI-generated"

**With Skills:**
- Professional-grade outputs
- Expert-level formatting
- Production-ready quality
- Indistinguishable from human-expert work

## 🎯 Your Responsibility

As an Agent Zero agent, you have access to these skills for a reason:
**To produce the highest quality outputs possible.**

Don't shortcut the process. Read the skills. Follow the guidelines. 
Deliver excellence.

---

**Remember: Skills are your expert consultants. Use them!**
