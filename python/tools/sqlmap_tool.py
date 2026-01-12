from python.helpers.tool import Tool, Response
import subprocess
import asyncio

class SqlmapTool(Tool):
    """SQL injection detection and exploitation. Authorized testing only."""
    
    async def execute(self, **kwargs):
        url = self.args.get("url", "")
        data = self.args.get("data", "")
        technique = self.args.get("technique", "")
        
        if not url:
            return Response(message="Error: 'url' required", break_loop=False)
        
        args = ["sqlmap", "-u", url, "--batch"]
        
        if data:
            args.extend(["--data", data])
        if technique:
            args.extend(["--technique", technique])
        
        try:
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=300)
            output = stdout.decode('utf-8', errors='replace')[:10000]
            
            return Response(
                message=f"# SQLMap Scan\n\n```\n{output}\n```",
                break_loop=False
            )
        except Exception as e:
            return Response(message=f"SQLMap error: {e}", break_loop=False)
