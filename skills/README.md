# Claude AI Skills for Agent Zero

This directory contains **16 Claude AI Skills** - comprehensive workflow guides and best practices for specialized tasks.

## 📚 What are Skills?

Skills are NOT just tool definitions - they are **comprehensive workflow systems** with:
- Best practices learned from extensive testing
- Step-by-step instructions
- Code examples and templates
- Common pitfalls to avoid
- Quality optimization techniques

Think of skills as **expert knowledge bases** that Agent Zero should consult before executing complex tasks.

## 🎯 How Agent Zero Should Use Skills

**CRITICAL:** Agent Zero should **ALWAYS read the relevant SKILL.md file BEFORE** starting work on:
- Document creation (Word, PowerPoint, Excel, PDF)
- Web UI design and development
- Visual art creation
- Complex workflows

**Workflow:**
```
1. User Request → Identify relevant skill
2. Read /skills/[category]/[skill]/SKILL.md
3. Follow best practices from skill
4. Execute task with learned knowledge
5. Deliver high-quality output
```

## 📦 Available Skills

### PUBLIC SKILLS (6)

#### 📄 docx
**Path:** `/skills/public/docx/`
**Purpose:** Microsoft Word document creation and editing
**When to use:** Creating reports, proposals, letters, professional documents
**Key features:**
- Tracked changes and comments
- Professional formatting and styles
- Tables, images, headers/footers
- Multi-section documents

#### 📊 pptx
**Path:** `/skills/public/pptx/`
**Purpose:** PowerPoint presentation creation
**When to use:** Business pitches, slides, training materials
**Key features:**
- Professional layouts and themes
- Charts and diagrams
- Master slides and templates
- Animations and transitions

#### 📈 xlsx
**Path:** `/skills/public/xlsx/`
**Purpose:** Excel spreadsheet creation and analysis
**When to use:** Data analysis, financial models, tracking sheets
**Key features:**
- Complex formulas and functions
- Pivot tables and charts
- Conditional formatting
- Data validation

#### 📄 pdf
**Path:** `/skills/public/pdf/`
**Purpose:** PDF document creation and manipulation
**When to use:** Final documents, form filling, PDF processing
**Key features:**
- Create PDFs from content
- Fill interactive forms
- Extract text and tables
- Merge/split documents

#### 🎨 frontend-design
**Path:** `/skills/public/frontend-design/`
**Purpose:** Web UI design and development
**When to use:** Creating web interfaces, dashboards, landing pages
**Key features:**
- Distinctive, non-generic designs
- React + Tailwind CSS patterns
- Responsive layouts
- Professional aesthetics

#### 📖 product-self-knowledge
**Path:** `/skills/public/product-self-knowledge/`
**Purpose:** Authoritative Claude product information
**When to use:** User asks about Claude features, API, pricing
**Key features:**
- Accurate product details
- API documentation references
- Feature capabilities

### EXAMPLE SKILLS (10)

#### 🎨 algorithmic-art
**Path:** `/skills/examples/algorithmic-art/`
**Purpose:** Creating algorithmic art using p5.js
**When to use:** Generative art, flow fields, particle systems
**Includes:** Seeded randomness, interactive parameters

#### 🏢 brand-guidelines
**Path:** `/skills/examples/brand-guidelines/`
**Purpose:** Anthropic brand colors and typography
**When to use:** Applying Anthropic branding to artifacts
**Includes:** Official color palette, font specifications

#### 🖼️ canvas-design
**Path:** `/skills/examples/canvas-design/`
**Purpose:** Visual art creation philosophy
**When to use:** Posters, graphics, static artwork
**Includes:** Design principles, color theory, composition

#### 📝 doc-coauthoring
**Path:** `/skills/examples/doc-coauthoring/`
**Purpose:** Structured documentation workflow
**When to use:** Technical specs, proposals, decision docs
**Includes:** Context transfer, iteration, verification

#### 💼 internal-comms
**Path:** `/skills/examples/internal-comms/`
**Purpose:** Internal communication templates
**When to use:** Status reports, newsletters, updates
**Includes:** Company-specific formats

#### 🔧 mcp-builder
**Path:** `/skills/examples/mcp-builder/`
**Purpose:** Building MCP (Model Context Protocol) servers
**When to use:** Creating tool integrations for Claude
**Includes:** FastMCP and MCP SDK patterns

#### 📚 skill-creator
**Path:** `/skills/examples/skill-creator/`
**Purpose:** Guide for creating new skills
**When to use:** User wants to extend Claude with custom skills
**Includes:** Skill structure, best practices

#### 🎬 slack-gif-creator
**Path:** `/skills/examples/slack-gif-creator/`
**Purpose:** Creating optimized GIFs for Slack
**When to use:** Animated GIFs with Slack constraints
**Includes:** Size limits, optimization techniques

#### 🎨 theme-factory
**Path:** `/skills/examples/theme-factory/`
**Purpose:** Styling artifacts with themes
**When to use:** Applying consistent design to artifacts
**Includes:** 10 pre-set themes, custom theme generation

#### 🌐 web-artifacts-builder
**Path:** `/skills/examples/web-artifacts-builder/`
**Purpose:** Complex multi-component web artifacts
**When to use:** Elaborate React apps with routing, state management
**Includes:** Modern web technologies, shadcn/ui components

## 🚀 Integration with Agent Zero

### For Tool Prompts

Each tool prompt should reference the relevant skill:

```markdown
### docx_create:

Creates Microsoft Word documents with professional formatting.

**Important:** 
Read /skills/public/docx/SKILL.md BEFORE creating documents.
Follow the best practices and formatting guidelines.

**Usage:**
[tool usage examples]
```

### For Agent System Prompt

Agent Zero's system prompt should include:

```
When creating documents, presentations, spreadsheets, or web interfaces:
1. FIRST read the relevant skill file from /skills/[category]/[skill]/SKILL.md
2. Study the best practices and examples
3. Apply the learned techniques
4. Create high-quality output following skill guidelines

Available skills are in:
- /skills/public/ - Core document and design skills
- /skills/examples/ - Specialized workflow skills
```

## 📊 Skill Statistics

```
Total Skills:          16
Public Skills:         6
Example Skills:        10
Total Size:           ~12 MB
Documentation:        Comprehensive markdown files
Code Examples:        Included in each skill
```

## 🎯 Expected Outcomes

With proper skill integration, Agent Zero will produce:
- ✅ Professional-quality Word documents
- ✅ Polished PowerPoint presentations
- ✅ Complex Excel spreadsheets with formulas
- ✅ Properly formatted PDFs
- ✅ Distinctive, non-generic web UIs
- ✅ High-quality visual artwork
- ✅ Optimized outputs for specific platforms

## 📖 Usage Example

**User Request:** "Create a professional project proposal document"

**Agent Zero Workflow:**
```
1. Identify skill: docx (document creation)
2. Read: /skills/public/docx/SKILL.md
3. Learn: Document structure, formatting, styles
4. Execute: Create proposal using learned best practices
5. Output: Professional Word document with proper formatting
```

**Result:** High-quality document that looks professionally made, not AI-generated.

## ⚠️ Important Notes

1. **Always read skills BEFORE execution** - Don't skip this step!
2. **Skills evolve** - These contain tested, optimized approaches
3. **Combine skills** - Use multiple skills for complex tasks
4. **Quality over speed** - Taking time to read skills produces better outputs

---

**Skills are the secret sauce that makes NAJA outputs production-ready!**

For questions about specific skills, consult the SKILL.md file in each skill directory.
