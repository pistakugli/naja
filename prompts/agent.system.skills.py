import os
import json
from typing import Any
from python.helpers.files import VariablesPlugin
from python.helpers import files
from python.helpers.print_style import PrintStyle


class SkillsLoader(VariablesPlugin):
    """Loads Claude AI skills catalog and formats for system prompt"""
    
    def get_variables(self, file: str, backup_dirs: list[str] | None = None) -> dict[str, Any]:
        try:
            # Load skills.json
            skills_path = files.get_abs_path("skills.json")
            
            if not os.path.exists(skills_path):
                PrintStyle().warning("skills.json not found - skills not available")
                return {"skills_catalog": ""}
            
            with open(skills_path, 'r') as f:
                skills_data = json.load(f)
            
            catalog = skills_data.get("skills_catalog", {})
            
            # Format skills for prompt
            output = []
            output.append("# Claude AI Skills Catalog")
            output.append("")
            output.append(f"**Base Path:** `{catalog.get('base_path', '/home/claude/naja/skills')}`")
            output.append("")
            
            # Public Skills
            output.append("## Public Skills (6)")
            output.append("")
            for skill in catalog.get("public_skills", []):
                output.append(f"### {skill['name']}")
                output.append(f"**Location:** `{skill['location']}`")
                output.append(f"**Description:** {skill['description']}")
                output.append("")
                output.append("**Use Cases:**")
                for uc in skill.get('use_cases', []):
                    output.append(f"- {uc}")
                output.append("")
            
            # Example Skills
            output.append("## Example Skills (10)")
            output.append("")
            for skill in catalog.get("example_skills", []):
                output.append(f"### {skill['name']}")
                output.append(f"**Location:** `{skill['location']}`")
                output.append(f"**Description:** {skill['description']}")
                output.append("")
            
            # Usage Instructions
            instructions = catalog.get("usage_instructions", {})
            output.append("## How to Use Skills")
            output.append("")
            output.append("**When to Read Skills:**")
            for when in instructions.get("when_to_read", []):
                output.append(f"- {when}")
            output.append("")
            
            output.append("**How to Read:**")
            how_to = instructions.get("how_to_read", {})
            output.append(f"- Method: {how_to.get('method', 'code_execution_tool')}")
            output.append(f"- Template: `{how_to.get('command_template', 'cat {location}')}`")
            output.append("")
            
            output.append("**Workflow:**")
            for step in instructions.get("workflow", []):
                output.append(step)
            output.append("")
            
            return {"skills_catalog": "\n".join(output)}
            
        except Exception as e:
            PrintStyle().error(f"Error loading skills catalog: {e}")
            return {"skills_catalog": ""}
