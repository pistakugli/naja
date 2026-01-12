from python.helpers.tool import Tool, Response

class MapTool(Tool):
    async def execute(self, **kwargs):
        markers = self.args.get("markers", [])
        title = self.args.get("title", "Map")
        
        if not markers:
            return Response(message="Error: 'markers' array required", break_loop=False)
        
        map_content = f"# {title}\n\n"
        for i, marker in enumerate(markers, 1):
            lat = marker.get("latitude", "0")
            lon = marker.get("longitude", "0")
            label = marker.get("title", f"Location {i}")
            map_content += f"{i}. **{label}** - ({lat}, {lon})\n"
        
        map_content += "\n*Map visualization would appear here*"
        
        return Response(message=map_content, break_loop=False)
