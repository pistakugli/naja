from python.helpers.tool import Tool, Response

class AlarmCreatorTool(Tool):
    async def execute(self, **kwargs):
        hour = self.args.get("hour", 0)
        minute = self.args.get("minute", 0)
        message = self.args.get("message", "Alarm")
        days = self.args.get("days", [])
        
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            return Response(message="Error: Invalid time (hour: 0-23, minute: 0-59)", break_loop=False)
        
        time_str = f"{hour:02d}:{minute:02d}"
        repeat = "daily" if days else "once"
        
        msg = f"""# Alarm Set

**Time:** {time_str}
**Label:** {message}
**Repeat:** {repeat}
**Days:** {days if days else 'N/A'}

Alarm configured successfully."""
        
        return Response(message=msg, break_loop=False)
