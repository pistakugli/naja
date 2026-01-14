import os
import json
from typing import Any
from python.helpers.files import VariablesPlugin
from python.helpers import files
from python.helpers.print_style import PrintStyle


class ToolsCatalogLoader(VariablesPlugin):
    """Loads tools catalog from tools.json and formats for system prompt"""
    
    def get_variables(self, file: str, backup_dirs: list[str] | None = None) -> dict[str, Any]:
        try:
            # Load tools.json
            tools_path = files.get_abs_path("tools.json")
            
            if not os.path.exists(tools_path):
                PrintStyle().warning("tools.json not found - tools catalog not available")
                return {"tools_catalog": ""}
            
            with open(tools_path, 'r') as f:
                tools_data = json.load(f)
            
            catalog = tools_data.get("tools_catalog", {})
            
            # Format tools for prompt
            output = []
            output.append("# Tools Catalog")
            output.append("")
            output.append(f"**Total Tools:** {catalog.get('total_tools', 90)}")
            output.append("")
            
            # Categories
            categories = catalog.get('categories', {})
            output.append("**Categories:**")
            output.append(f"- Agent Zero: {categories.get('agent_zero', 20)} tools")
            output.append(f"- Security (Kali): {categories.get('security', 58)} tools")
            output.append(f"- Productivity (Claude): {categories.get('productivity', 12)} tools")
            output.append("")
            
            # Agent Zero Tools
            output.append("## Agent Zero Tools (20)")
            output.append("")
            output.append("Core AI reasoning and system tools:")
            agent_tools = catalog.get("agent_zero_tools", [])
            for tool in agent_tools[:5]:  # Show first 5 as examples
                output.append(f"**{tool['name']}** - {tool['description']}")
            output.append(f"...and {len(agent_tools) - 5} more")
            output.append("")
            
            # Kali Security Tools
            output.append("## Kali Security Tools (58)")
            output.append("")
            output.append("⚠️ **Authorization Required** - Always check before scanning")
            output.append("")
            kali_tools = catalog.get("kali_security_tools", [])
            for tool in kali_tools[:8]:  # Show all 8 main tools
                output.append(f"**{tool['name']}** - {tool['description']}")
            output.append("")
            output.append("**Plus 600+ additional tools** via kali_universal wrapper")
            output.append("")
            
            # Claude Productivity Tools
            output.append("## Claude Productivity Tools (12)")
            output.append("")
            output.append("**⚠️ CRITICAL:** Always read skill file BEFORE using these tools!")
            output.append("")
            
            claude_tools = catalog.get("claude_productivity_tools", [])
            
            # Group by category
            doc_tools = [t for t in claude_tools if t.get('category') == 'document_creation']
            design_tools = [t for t in claude_tools if t.get('category') == 'design']
            other_tools = [t for t in claude_tools if t.get('category') not in ['document_creation', 'design']]
            
            output.append("**Document Creation (4):**")
            for tool in doc_tools:
                output.append(f"- **{tool['name']}**: {tool['description']}")
                output.append(f"  Skill: `{tool.get('skill_required', 'N/A')}`")
            output.append("")
            
            output.append("**Design (2):**")
            for tool in design_tools:
                output.append(f"- **{tool['name']}**: {tool['description']}")
                output.append(f"  Skill: `{tool.get('skill_required', 'N/A')}`")
            output.append("")
            
            output.append("**Other (6):**")
            for tool in other_tools:
                output.append(f"- **{tool['name']}**: {tool['description']}")
            output.append("")
            
            # Usage Instructions
            instructions = catalog.get("usage_instructions", {})
            output.append("## Tool Usage Guidelines")
            output.append("")
            
            claude_instr = instructions.get("claude_productivity_tools", {})
            output.append("**Claude Tools:**")
            output.append(f"- {claude_instr.get('critical_workflow', 'Read skill files first')}")
            output.append(f"- Location: {claude_instr.get('skills_location', '/home/claude/naja/skills/')}")
            output.append(f"- Execution: {claude_instr.get('execution_method', 'code_execution_tool')}")
            
            quality = claude_instr.get('quality_difference', {})
            if quality:
                output.append("")
                output.append("**Quality Impact:**")
                output.append(f"- Without skills: {quality.get('without_skills', 'generic')}")
                output.append(f"- With skills: {quality.get('with_skills', 'professional')}")
            
            return {"tools_catalog": "\n".join(output)}
            
        except Exception as e:
            PrintStyle().error(f"Error loading tools catalog: {e}")
            return {"tools_catalog": ""}
