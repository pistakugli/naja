from python.helpers.tool import Tool, Response
import subprocess
import asyncio
import os

class KaliSecurityTool(Tool):
    """
    Universal wrapper for Kali Linux security tools.
    Enables Agent Zero to use nmap, metasploit, sqlmap, nikto, hydra, etc.
    
    ⚠️ WARNING: Only use for authorized security testing and research.
    Unauthorized use is illegal. User must have explicit permission.
    """
    
    # Allowed Kali tools (whitelist for safety)
    ALLOWED_TOOLS = {
        # Network Scanning
        'nmap': 'Network scanner',
        'masscan': 'Fast port scanner',
        'netdiscover': 'ARP scanner',
        
        # Web Application Testing
        'nikto': 'Web server scanner',
        'sqlmap': 'SQL injection tool',
        'wpscan': 'WordPress scanner',
        'dirb': 'Directory brute forcer',
        'gobuster': 'Directory/DNS bruteforcer',
        'ffuf': 'Fast web fuzzer',
        
        # Password Cracking
        'john': 'John the Ripper password cracker',
        'hydra': 'Network logon cracker',
        'hashcat': 'Advanced password recovery',
        'crunch': 'Wordlist generator',
        
        # Exploitation
        'msfconsole': 'Metasploit console',
        'msfvenom': 'Payload generator',
        'searchsploit': 'Exploit database search',
        
        # Wireless
        'aircrack-ng': 'WiFi security',
        'reaver': 'WPS attacks',
        'bully': 'WPS brute force',
        
        # Packet Analysis
        'tshark': 'Terminal Wireshark',
        'tcpdump': 'Packet capture',
        
        # Information Gathering
        'whois': 'Domain info',
        'dnsenum': 'DNS enumeration',
        'fierce': 'DNS scanner',
        'theHarvester': 'Email/subdomain harvester',
        'maltego': 'Intelligence gathering',
        
        # Vulnerability Scanning
        'openvas': 'Vulnerability scanner',
        'nessus': 'Vulnerability scanner'
    }
    
    async def execute(self, **kwargs):
        tool_name = self.args.get("tool", "")
        tool_args = self.args.get("args", [])
        target = self.args.get("target", "")
        timeout = int(self.args.get("timeout", 300))
        
        # Validation
        if not tool_name:
            return Response(
                message="Error: 'tool' parameter required. Example: 'nmap', 'nikto', 'sqlmap'",
                break_loop=False
            )
        
        if tool_name not in self.ALLOWED_TOOLS:
            available = "\n".join(f"  - {k}: {v}" for k, v in self.ALLOWED_TOOLS.items())
            return Response(
                message=f"Error: Tool '{tool_name}' not in whitelist.\n\nAllowed tools:\n{available}",
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
