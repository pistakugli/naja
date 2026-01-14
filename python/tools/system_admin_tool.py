from python.helpers.tool import Tool, Response
import subprocess
import asyncio
import os
import getpass

class SystemAdminTool(Tool):
    """
    System Administration Tool with ROOT/SUDO privileges.
    
    🔐 FULL SYSTEM ACCESS - For direct system administration tasks.
    
    Capabilities:
    - Execute commands with sudo/root
    - System administration (user management, services, packages)
    - Network administration (firewall, routing, interfaces)
    - Hardware management
    - Kali tools requiring root (nmap -sS, aircrack, etc.)
    
    ⚠️ CRITICAL: This tool has UNRESTRICTED system access.
    Use with extreme caution. Can modify/delete system files.
    """
    
    async def execute(self, **kwargs):
        command = self.args.get("command", "")
        use_sudo = self.args.get("use_sudo", True)
        timeout = int(self.args.get("timeout", 300))
        working_dir = self.args.get("working_dir", None)
        
        # Validation
        if not command:
            return Response(
                message="Error: 'command' parameter required.\n\nExamples:\n  - apt-get update\n  - systemctl restart nginx\n  - iptables -L\n  - useradd newuser",
                break_loop=False
            )
        
        # Check if already running as root
        is_root = os.geteuid() == 0
        current_user = getpass.getuser()
        
        # Build command with sudo if needed
        if use_sudo and not is_root:
            if isinstance(command, str):
                full_command = f"sudo {command}"
            else:
                full_command = ["sudo"] + (command if isinstance(command, list) else [command])
        else:
            full_command = command
        
        # Security warning
        warning = f"""
🔐 SYSTEM ADMINISTRATION MODE 🔐
Current user: {current_user}
Running as root: {is_root}
Using sudo: {use_sudo and not is_root}

⚠️  This command has FULL SYSTEM ACCESS.
    Can modify/delete critical system files.
    Use with extreme caution.
"""
        
        try:
            # Execute command
            result = await self._run_command(full_command, timeout, working_dir)
            
            # Truncate if too long
            if len(result) > 30000:
                result = result[:30000] + "\n\n[... output truncated ...]"
            
            return Response(
                message=f"{warning}\n## Command:\n```bash\n{full_command if isinstance(full_command, str) else ' '.join(full_command)}\n```\n\n## Output:\n```\n{result}\n```",
                break_loop=False
            )
            
        except subprocess.TimeoutExpired:
            return Response(
                message=f"Error: Command timed out after {timeout} seconds.",
                break_loop=False
            )
        except PermissionError:
            return Response(
                message=f"Error: Permission denied. May need sudo or root access.\n\nTry setting 'use_sudo': true",
                break_loop=False
            )
        except Exception as e:
            return Response(
                message=f"Error executing command: {str(e)}",
                break_loop=False
            )
    
    async def _run_command(self, command, timeout, working_dir=None):
        """Execute command with timeout"""
        # Parse command if string
        if isinstance(command, str):
            shell = True
            cmd = command
        else:
            shell = False
            cmd = command
        
        process = await asyncio.create_subprocess_shell(
            cmd if shell else ' '.join(cmd),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=working_dir
        )
        
        try:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=timeout
            )
            
            output = stdout.decode('utf-8', errors='replace')
            errors = stderr.decode('utf-8', errors='replace')
            
            if errors:
                output += f"\n\n## Errors/Warnings:\n{errors}"
            
            return output
            
        except asyncio.TimeoutError:
            process.kill()
            raise subprocess.TimeoutExpired(cmd, timeout)
