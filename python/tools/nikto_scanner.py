from python.helpers.tool import Tool, Response
import subprocess
import asyncio

class NiktoScannerTool(Tool):
    """Web server vulnerability scanner. Authorized testing only."""
    
    async def execute(self, **kwargs):
        target = self.args.get("target", "")
        port = self.args.get("port", "80")
        ssl = self.args.get("ssl", False)
        
        if not target:
            return Response(message="Error: 'target' required", break_loop=False)
        
        args = ["nikto", "-h", target, "-p", str(port)]
        
        if ssl:
            args.append("-ssl")
        
        try:
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=600)
            output = stdout.decode('utf-8', errors='replace')[:15000]
            
            return Response(
                message=f"# Nikto Scan: {target}\n\n```\n{output}\n```",
                break_loop=False
            )
        except Exception as e:
            return Response(message=f"Nikto error: {e}", break_loop=False)
