from python.helpers.tool import Tool, Response
import subprocess
import asyncio

class NmapScannerTool(Tool):
    """Network port scanner using nmap. For authorized testing only."""
    
    async def execute(self, **kwargs):
        target = self.args.get("target", "")
        scan_type = self.args.get("scan_type", "basic")
        ports = self.args.get("ports", "")
        
        if not target:
            return Response(message="Error: 'target' required (IP or hostname)", break_loop=False)
        
        # Build nmap command based on scan type
        scan_profiles = {
            "basic": ["-sV", "-sC"],  # Version detection + default scripts
            "fast": ["-F"],  # Fast scan (100 ports)
            "full": ["-p-"],  # All 65535 ports
            "stealth": ["-sS", "-T2"],  # SYN stealth scan
            "aggressive": ["-A", "-T4"],  # OS detection, version, scripts, traceroute
            "udp": ["-sU"],  # UDP scan
            "os": ["-O"],  # OS detection
        }
        
        args = scan_profiles.get(scan_type, ["-sV"])
        
        if ports:
            args.extend(["-p", ports])
        
        args.append(target)
        
        command = ["nmap"] + args
        
        try:
            process = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=600)
            output = stdout.decode('utf-8', errors='replace')
            
            return Response(
                message=f"# Nmap Scan: {target}\n\n```\n{output}\n```",
                break_loop=False
            )
        except Exception as e:
            return Response(message=f"Nmap error: {e}", break_loop=False)
