from python.helpers.tool import Tool, Response
from agent import AgentContext
import aiohttp
import os

class GithubSearchTool(Tool):
    """
    Tool for searching GitHub repositories using GitHub API.
    Requires GITHUB_TOKEN environment variable to be set.
    """
    
    async def execute(self, **kwargs):
        """
        Search GitHub repositories by query string.
        Returns top matching repositories with details.
        """
        
        # Get arguments
        query = self.args.get("query", "")
        limit = int(self.args.get("limit", 5))
        sort = self.args.get("sort", "stars")  # stars, forks, updated
        
        # Validate inputs
        if not query:
            return Response(
                message="Error: 'query' parameter is required for GitHub search",
                break_loop=False
            )
        
        if limit < 1 or limit > 20:
            return Response(
                message="Error: 'limit' must be between 1 and 20",
                break_loop=False
            )
        
        # Get GitHub token from environment
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            return Response(
                message="Error: GITHUB_TOKEN environment variable not set. Cannot authenticate with GitHub API.",
                break_loop=False
            )
        
        try:
            # Search GitHub repositories
            results = await self._search_repositories(query, limit, sort, github_token)
            
            if not results:
                return Response(
                    message=f"No repositories found for query: '{query}'",
                    break_loop=False
                )
            
            # Format results
            message = self._format_results(query, results, sort)
            
            return Response(
                message=message,
                break_loop=False
            )
            
        except aiohttp.ClientError as e:
            return Response(
                message=f"GitHub API error: {str(e)}",
                break_loop=False
            )
        except Exception as e:
            return Response(
                message=f"Unexpected error during GitHub search: {str(e)}",
                break_loop=False
            )
    
    async def _search_repositories(self, query: str, limit: int, sort: str, token: str):
        """
        Call GitHub Search API to find repositories.
        """
        url = "https://api.github.com/search/repositories"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        params = {
            "q": query,
            "sort": sort,
            "order": "desc",
            "per_page": limit
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise aiohttp.ClientError(f"GitHub API returned status {response.status}: {error_text}")
                
                data = await response.json()
                return data.get("items", [])
    
    def _format_results(self, query: str, results: list, sort: str) -> str:
        """
        Format search results into readable message.
        """
        lines = [
            f"# GitHub Repository Search Results",
            f"",
            f"**Query:** `{query}`",
            f"**Sort by:** {sort}",
            f"**Results:** {len(results)} repositories",
            f"",
            f"---",
            f""
        ]
        
        for i, repo in enumerate(results, 1):
            name = repo.get("full_name", "N/A")
            description = repo.get("description", "No description")
            stars = repo.get("stargazers_count", 0)
            forks = repo.get("forks_count", 0)
            language = repo.get("language", "Unknown")
            url = repo.get("html_url", "")
            updated = repo.get("updated_at", "")[:10]  # YYYY-MM-DD
            
            lines.extend([
                f"### {i}. [{name}]({url})",
                f"",
                f"**Description:** {description}",
                f"**Language:** {language} | **Stars:** ⭐ {stars} | **Forks:** 🍴 {forks}",
                f"**Last Updated:** {updated}",
                f"",
                f"---",
                f""
            ])
        
        return "\n".join(lines)
