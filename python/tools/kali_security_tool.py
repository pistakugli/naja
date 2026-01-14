from python.helpers.tool import Tool, Response
import subprocess
import asyncio
import os

class KaliSecurityTool(Tool):
    """
    Universal wrapper for ALL Kali Linux security tools.
    
    🔓 UNRESTRICTED ACCESS - No whitelist or blacklist.
    Can execute ANY tool available in Kali Linux (600+ tools).
    
    ⚠️ WARNING: Only use for authorized security testing and research.
    Unauthorized use is illegal. User assumes all legal responsibility.
    
    Examples: nmap, metasploit, burpsuite, wireshark, sqlmap, nikto, hydra,
              aircrack-ng, john, hashcat, gobuster, dirb, wpscan, beef, 
              zaproxy, ettercap, netcat, socat, proxychains, etc.
    """
    
    async def execute(self, **kwargs):
        tool_name = self.args.get("tool", "")
        tool_args = self.args.get("args", [])
        target = self.args.get("target", "")
        timeout = int(self.args.get("timeout", 300))
        
        # Validation
        if not tool_name:
            return Response(
                message="Error: 'tool' parameter required.\n\nExamples:\n  - nmap\n  - burpsuite\n  - wireshark\n  - sqlmap\n  - metasploit\n  - Any Kali tool name",
                break_loop=False
            )
        
        # Security warning
        warning = """
⚠️  SECURITY NOTICE ⚠️
This tool is for AUTHORIZED security testing only.
Unauthorized access to systems is ILLEGAL.
User assumes all legal responsibility.
"""
        
        # Build command
        if isinstance(tool_args, str):
            tool_args = [tool_args]
        
        if target and target not in tool_args:
            tool_args.append(target)
        
        command = [tool_name] + tool_args
        
        try:
            # Execute with timeout
            result = await self._run_command(command, timeout)
            
            # Truncate if too long
            if len(result) > 20000:
                result = result[:20000] + "\n\n[... truncated, use 'timeout' to adjust ...]"
            
            return Response(
                message=f"{warning}\n# Kali Tool: {tool_name}\n\n## Command:\n```bash\n{' '.join(command)}\n```\n\n## Output:\n```\n{result}\n```",
                break_loop=False
            )
            
        except subprocess.TimeoutExpired:
            return Response(
                message=f"Error: Command timed out after {timeout} seconds. Increase 'timeout' parameter.",
                break_loop=False
            )
        except Exception as e:
            return Response(
                message=f"Error executing {tool_name}: {str(e)}",
                break_loop=False
            )
    
    async def _run_command(self, command, timeout):
        """Execute command with timeout"""
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        try:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=timeout
            )
            
            output = stdout.decode('utf-8', errors='replace')
            errors = stderr.decode('utf-8', errors='replace')
            
            if errors:
                output += f"\n\n## Errors:\n{errors}"
            
            return output
            
        except asyncio.TimeoutError:
            process.kill()
            raise subprocess.TimeoutExpired(command, timeout)
