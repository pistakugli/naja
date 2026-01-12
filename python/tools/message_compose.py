from python.helpers.tool import Tool, Response

class MessageComposeTool(Tool):
    async def execute(self, **kwargs):
        msg_type = self.args.get("kind", "other")
        subject = self.args.get("subject", "")
        body = self.args.get("body", "")
        to_addr = self.args.get("to", "")
        
        if not body:
            return Response(message="Error: 'body' required", break_loop=False)
        
        template = f"""# Message Draft ({msg_type})
"""
        
        if subject:
            template += f"**Subject:** {subject}\n"
        if to_addr:
            template += f"**To:** {to_addr}\n"
        
        template += f"""
**Message:**
{body}

---
*Draft created - ready to send*"""
        
        return Response(message=template, break_loop=False)
