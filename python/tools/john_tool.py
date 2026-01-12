from python.helpers.tool import Tool, Response
import subprocess
import asyncio

class JohnTool(Tool):
    """John the Ripper password cracker. For authorized password recovery."""
    
    async def execute(self, **kwargs):
        hash_file = self.args.get("hash_file", "")
        wordlist = self.args.get("wordlist", "")
        format_type = self.args.get("format", "")
        
        if not hash_file:
            return Response(message="Error: 'hash_file' required", break_loop=False)
        
        args = ["john", hash_file]
        
        if wordlist:
            args.extend(["--wordlist=" + wordlist])
        if format_type:
            args.extend(["--format=" + format_type])
        
        try:
            # Run john
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=600)
            output = stdout.decode('utf-8', errors='replace')
            
            # Show cracked passwords
            show_process = await asyncio.create_subprocess_exec(
                "john", "--show", hash_file,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            show_stdout, _ = await show_process.communicate()
            cracked = show_stdout.decode('utf-8', errors='replace')
            
            full_output = f"## Cracking Progress:\n{output}\n\n## Cracked Passwords:\n{cracked}"
            
            return Response(
                message=f"# John the Ripper\n\n```\n{full_output[:10000]}\n```",
                break_loop=False
            )
        except Exception as e:
            return Response(message=f"John error: {e}", break_loop=False)
