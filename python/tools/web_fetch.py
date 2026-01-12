from python.helpers.tool import Tool, Response
import aiohttp
from bs4 import BeautifulSoup

class WebFetchTool(Tool):
    async def execute(self, **kwargs):
        url = self.args.get("url", "")
        extract_text = self.args.get("extract_text", True)
        
        if not url or not url.startswith(("http://", "https://")):
            return Response(message="Error: Valid URL required", break_loop=False)
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers={'User-Agent': 'Mozilla/5.0'}) as resp:
                    if resp.status != 200:
                        return Response(message=f"HTTP {resp.status}", break_loop=False)
                    html = await resp.text()
            
            if extract_text:
                soup = BeautifulSoup(html, 'html.parser')
                for tag in soup(["script", "style", "nav", "footer"]):
                    tag.decompose()
                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())
                text = '\n'.join(line for line in lines if line)[:50000]
                return Response(message=f"Content from {url}:\n\n{text}", break_loop=False)
            else:
                return Response(message=f"HTML from {url}:\n\n{html[:10000]}", break_loop=False)
        except Exception as e:
            return Response(message=f"Fetch failed: {e}", break_loop=False)
