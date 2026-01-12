from python.helpers.tool import Tool, Response
from python.helpers.files import get_abs_path
import os

class FileCreatorTool(Tool):
    async def execute(self, **kwargs):
        filepath = self.args.get("path", "")
        content = self.args.get("content", "")
        
        if not filepath:
            return Response(message="Error: 'path' required", break_loop=False)
        
        try:
            abs_path = get_abs_path(filepath)
            
            # Create directory if needed
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            
            with open(abs_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return Response(message=f"File created: {filepath} ({len(content)} bytes)", break_loop=False)
        except Exception as e:
            return Response(message=f"Create failed: {e}", break_loop=False)
