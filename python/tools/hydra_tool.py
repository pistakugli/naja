from python.helpers.tool import Tool, Response
import subprocess
import asyncio

class HydraTool(Tool):
    """Network login cracker. Authorized testing only."""
    
    async def execute(self, **kwargs):
        target = self.args.get("target", "")
        service = self.args.get("service", "ssh")
        username = self.args.get("username", "")
        password_list = self.args.get("password_list", "")
        
        if not all([target, username, password_list]):
            return Response(
                message="Error: 'target', 'username', 'password_list' required",
                break_loop=False
            )
        
        args = ["hydra", "-l", username, "-P", password_list, service + "://" + target]
        
        try:
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=600)
            output = stdout.decode('utf-8', errors='replace')[:10000]
            
            return Response(
                message=f"# Hydra Brute Force\n\n```\n{output}\n```",
                break_loop=False
            )
        except Exception as e:
            return Response(message=f"Hydra error: {e}", break_loop=False)
