from python.helpers.tool import Tool, Response
from datetime import datetime
import pytz

class UserTimeTool(Tool):
    async def execute(self, **kwargs):
        timezone = self.args.get("timezone", "UTC")
        
        try:
            tz = pytz.timezone(timezone)
            now = datetime.now(tz)
            
            result = {
                "current_time": now.isoformat(),
                "timezone": timezone,
                "date": now.strftime("%Y-%m-%d"),
                "time": now.strftime("%H:%M:%S"),
                "day_of_week": now.strftime("%A"),
                "unix_timestamp": int(now.timestamp())
            }
            
            msg = f"""Current Time Information:
Time: {result['time']}
Date: {result['date']} ({result['day_of_week']})
Timezone: {result['timezone']}
ISO Format: {result['current_time']}"""
            
            return Response(message=msg, break_loop=False)
        except Exception as e:
            return Response(message=f"Time error: {e}", break_loop=False)
