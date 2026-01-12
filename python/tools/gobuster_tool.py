from python.helpers.tool import Tool, Response
import subprocess
import asyncio

class GobusterTool(Tool):
    """Directory/DNS/Vhost brute forcer. For authorized web testing."""
    
    async def execute(self, **kwargs):
        mode = self.args.get("mode", "dir")  # dir, dns, vhost
        url = self.args.get("url", "")
        wordlist = self.args.get("wordlist", "/usr/share/wordlists/dirb/common.txt")
        extensions = self.args.get("extensions", "")
        
        if not url:
            return Response(message="Error: 'url' required", break_loop=False)
        
        args = ["gobuster", mode, "-u", url, "-w", wordlist]
        
        if extensions and mode == "dir":
            args.extend(["-x", extensions])
        
        try:
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=600)
            output = stdout.decode('utf-8', errors='replace')[:15000]
            
            return Response(
                message=f"# Gobuster: {mode} on {url}\n\n```\n{output}\n```",
                break_loop=False
            )
        except Exception as e:
            return Response(message=f"Gobuster error: {e}", break_loop=False)
