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
        auto_install = self.args.get("auto_install", True)  # Auto-install if tool not found
        
        # Validation
        if not tool_name:
            return Response(
                message="Error: 'tool' parameter required.\n\nExamples:\n  - nmap\n  - burpsuite\n  - wireshark\n  - sqlmap\n  - metasploit\n  - Any Kali tool name",
                break_loop=False
            )
        
        # Check if tool is installed
        tool_exists = await self._check_tool_exists(tool_name)
        
        if not tool_exists and auto_install:
            # Try to auto-install the tool
            install_result = await self._auto_install_tool(tool_name)
            if not install_result:
                return Response(
                    message=f"Error: Tool '{tool_name}' not found and auto-install failed.\n\nTry manual installation:\n  sudo apt-get install {tool_name}",
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
    
    async def _check_tool_exists(self, tool_name):
        """Check if tool is installed"""
        try:
            process = await asyncio.create_subprocess_shell(
                f"which {tool_name}",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            return process.returncode == 0
        except:
            return False
    
    async def _auto_install_tool(self, tool_name):
        """Attempt to auto-install missing tool"""
        try:
            # Try apt-get first
            process = await asyncio.create_subprocess_shell(
                f"sudo apt-get install -y -qq {tool_name}",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            await asyncio.wait_for(process.communicate(), timeout=300)
            
            if process.returncode == 0:
                return True
            
            # If apt-get failed, try common alternatives
            alternatives = {
                'wireshark': 'wireshark-gtk',
                'tshark': 'wireshark',
                'ettercap': 'ettercap-text-only',
                'john': 'john',
                'hashcat': 'hashcat',
                'beef': 'beef-xss',
            }
            
            if tool_name in alternatives:
                alt_tool = alternatives[tool_name]
                process = await asyncio.create_subprocess_shell(
                    f"sudo apt-get install -y -qq {alt_tool}",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )
                await asyncio.wait_for(process.communicate(), timeout=300)
                return process.returncode == 0
            
            return False
            
        except:
            return False

