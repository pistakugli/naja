### web_ui_create:

Creates web interfaces (React, HTML) with professional design.

**⚠️ CRITICAL WORKFLOW:**

**STEP 1: Read Skill**
```json
{
  "thoughts": ["Reading frontend-design skill for non-generic UI patterns"],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "terminal",
    "code": "cat /home/claude/naja/skills/public/frontend-design/SKILL.md | head -200"
  }
}
```

**STEP 2: Create Interface**
```json
{
  "thoughts": [
    "Creating distinctive web UI following design skill",
    "Avoiding generic AI aesthetics"
  ],
  "tool_name": "code_execution_tool",
  "tool_args": {
    "runtime": "terminal",
    "code": "cat > /root/interface.html << 'HTMLEOF'\n<!DOCTYPE html>\n<html>\n<head>\n<script src=\"https://cdn.tailwindcss.com\"></script>\n<title>Web Interface</title>\n</head>\n<body class=\"bg-gray-50\">\n  <div class=\"container mx-auto p-6\">\n    <h1 class=\"text-3xl font-bold mb-4\">Dashboard</h1>\n    <div class=\"grid grid-cols-3 gap-4\">\n      <div class=\"bg-white p-4 rounded shadow\">\n        <h2 class=\"text-xl\">Section 1</h2>\n      </div>\n    </div>\n  </div>\n</body>\n</html>\nHTMLEOF\necho '✅ Interface created: /root/interface.html'"
  }
}
```

**WHEN TO USE:**
- "Create website/dashboard/interface"
- Web UI, landing page, admin panel
- Interactive web applications

**FRAMEWORKS AVAILABLE:**
- React (for complex apps)
- HTML + Tailwind CSS (for static pages)
- JavaScript for interactivity

**KEY PRINCIPLES FROM SKILL:**
- Avoid generic "AI look" (centered cards, excessive gradients)
- Use distinctive design patterns
- Proper spacing and typography
- Professional color schemes
- Responsive layouts

**FILE LOCATION:**
Save to: `/root/interface.html` or `/root/app.jsx`

**EXAMPLE - Security Dashboard:**
1. Read frontend-design skill
2. Create:
   - Clean navigation
   - Status cards with real data
   - Charts/graphs
   - Action buttons
   - Professional non-generic styling

This uses code_execution_tool with terminal runtime for HTML files.
