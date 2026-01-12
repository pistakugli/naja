from python.helpers.tool import Tool, Response
import subprocess
import asyncio

class AircrackTool(Tool):
    """WiFi security tool. For authorized wireless network testing."""
    
    async def execute(self, **kwargs):
        action = self.args.get("action", "crack")
        capture_file = self.args.get("capture_file", "")
        bssid = self.args.get("bssid", "")
        wordlist = self.args.get("wordlist", "/usr/share/wordlists/rockyou.txt")
        interface = self.args.get("interface", "wlan0")
        
        if action == "crack":
            if not all([capture_file, bssid]):
                return Response(
                    message="Error: 'capture_file' and 'bssid' required for cracking",
                    break_loop=False
                )
            
            args = ["aircrack-ng", "-w", wordlist, "-b", bssid, capture_file]
        
        elif action == "monitor":
            args = ["airmon-ng", "start", interface]
        
        elif action == "stop_monitor":
            args = ["airmon-ng", "stop", interface + "mon"]
        
        else:
            return Response(message=f"Error: Unknown action '{action}'", break_loop=False)
        
        try:
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=600)
            output = stdout.decode('utf-8', errors='replace')[:10000]
            
            return Response(
                message=f"# Aircrack-ng: {action}\n\n```\n{output}\n```",
                break_loop=False
            )
        except Exception as e:
            return Response(message=f"Aircrack error: {e}", break_loop=False)
