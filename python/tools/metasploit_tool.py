from python.helpers.tool import Tool, Response
import subprocess
import asyncio

class MetasploitTool(Tool):
    """Metasploit Framework interface. For authorized exploitation testing."""
    
    async def execute(self, **kwargs):
        action = self.args.get("action", "search")
        query = self.args.get("query", "")
        module = self.args.get("module", "")
        options = self.args.get("options", {})
        
        if action == "search":
            if not query:
                return Response(message="Error: 'query' required for search", break_loop=False)
            
            args = ["msfconsole", "-q", "-x", f"search {query}; exit"]
        
        elif action == "info":
            if not module:
                return Response(message="Error: 'module' required for info", break_loop=False)
            
            args = ["msfconsole", "-q", "-x", f"info {module}; exit"]
        
        elif action == "generate_payload":
            payload = self.args.get("payload", "")
            lhost = self.args.get("lhost", "")
            lport = self.args.get("lport", "4444")
            format_type = self.args.get("format", "elf")
            
            if not all([payload, lhost]):
                return Response(
                    message="Error: 'payload', 'lhost' required for payload generation",
                    break_loop=False
                )
            
            args = ["msfvenom", "-p", payload, f"LHOST={lhost}", f"LPORT={lport}", 
                    "-f", format_type, "-o", "/tmp/payload." + format_type]
        
        else:
            return Response(message=f"Error: Unknown action '{action}'", break_loop=False)
        
        try:
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=300)
            output = stdout.decode('utf-8', errors='replace')[:15000]
            
            return Response(
                message=f"# Metasploit: {action}\n\n```\n{output}\n```",
                break_loop=False
            )
        except Exception as e:
            return Response(message=f"Metasploit error: {e}", break_loop=False)
