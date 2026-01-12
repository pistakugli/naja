from python.helpers.tool import Tool, Response

class TimerCreatorTool(Tool):
    async def execute(self, **kwargs):
        duration_seconds = self.args.get("duration_seconds", 0)
        message = self.args.get("message", "Timer")
        
        if duration_seconds <= 0:
            return Response(message="Error: duration_seconds must be > 0", break_loop=False)
        
        minutes = duration_seconds // 60
        seconds = duration_seconds % 60
        
        msg = f"""# Timer Started

**Duration:** {minutes}m {seconds}s
**Label:** {message}

Timer is now running."""
        
        return Response(message=msg, break_loop=False)
