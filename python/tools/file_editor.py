from python.helpers.tool import Tool, Response
from python.helpers.files import get_abs_path
import os

class FileEditorTool(Tool):
    async def execute(self, **kwargs):
        filepath = self.args.get("path", "")
        old_str = self.args.get("old_str", "")
        new_str = self.args.get("new_str", "")
        
        if not all([filepath, old_str is not None]):
            return Response(message="Error: 'path' and 'old_str' required", break_loop=False)
        
        try:
            abs_path = get_abs_path(filepath)
            
            with open(abs_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_str not in content:
                return Response(message=f"String not found in {filepath}", break_loop=False)
            
            if content.count(old_str) > 1:
                return Response(message=f"String appears {content.count(old_str)} times - must be unique", break_loop=False)
            
            new_content = content.replace(old_str, new_str)
            
            with open(abs_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return Response(message=f"File {filepath} updated successfully", break_loop=False)
        except Exception as e:
            return Response(message=f"Edit failed: {e}", break_loop=False)
