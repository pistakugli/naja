from python.helpers.tool import Tool, Response
from python.helpers.files import get_abs_path
import os

class FileViewerTool(Tool):
    async def execute(self, **kwargs):
        filepath = self.args.get("path", "")
        start_line = self.args.get("start_line", 1)
        end_line = self.args.get("end_line", -1)
        
        if not filepath:
            return Response(message="Error: 'path' required", break_loop=False)
        
        try:
            abs_path = get_abs_path(filepath)
            
            if os.path.isdir(abs_path):
                items = os.listdir(abs_path)
                listing = "\n".join(f"  {'📁' if os.path.isdir(os.path.join(abs_path, i)) else '📄'} {i}" for i in sorted(items))
                return Response(message=f"Directory: {filepath}\n\n{listing}", break_loop=False)
            
            with open(abs_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            if end_line == -1:
                end_line = len(lines)
            
            start_idx = max(0, start_line - 1)
            end_idx = min(len(lines), end_line)
            
            numbered = "\n".join(f"{i+start_line:4d} | {lines[i].rstrip()}" for i in range(start_idx, end_idx))
            
            return Response(message=f"File: {filepath} (lines {start_line}-{end_idx})\n\n{numbered}", break_loop=False)
        except Exception as e:
            return Response(message=f"View failed: {e}", break_loop=False)
