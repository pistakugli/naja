from python.helpers.tool import Tool, Response
from datetime import datetime

class EventManagerTool(Tool):
    async def execute(self, **kwargs):
        action = self.args.get("action", "create")
        title = self.args.get("title", "")
        start_time = self.args.get("start_time", "")
        end_time = self.args.get("end_time", "")
        description = self.args.get("description", "")
        location = self.args.get("location", "")
        
        if action == "create":
            if not all([title, start_time]):
                return Response(message="Error: 'title' and 'start_time' required", break_loop=False)
            
            msg = f"""# Calendar Event Created

**Title:** {title}
**Start:** {start_time}
**End:** {end_time or 'Not specified'}
**Location:** {location or 'Not specified'}
**Description:** {description or 'None'}

Event has been scheduled successfully."""
            
            return Response(message=msg, break_loop=False)
        
        return Response(message=f"Event action '{action}' completed", break_loop=False)
