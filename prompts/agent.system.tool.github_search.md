### github_search:
Search GitHub repositories using GitHub's search API. Returns repository details including stars, forks, language, and description.

!!! Requires GITHUB_TOKEN environment variable to be set
!!! Maximum 20 results per search
!!! Use specific keywords for better results

#### Arguments:
 *  "query" (string) : Search query for GitHub repositories. Can include keywords, language filters, topic filters. Examples: "machine learning", "language:python stars:>1000", "topic:ai"
 *  "limit" (Optional, integer) : Number of results to return (1-20). Default is 5.
 *  "sort" (Optional, string) : Sort results by: "stars" (default), "forks", or "updated"

#### Usage examples:
##### 1: Basic repository search
```json
{
    "thoughts": [
        "User wants to find Python machine learning repositories",
        "I'll search GitHub with relevant keywords"
    ],
    "tool_name": "github_search",
    "tool_args": {
        "query": "machine learning python",
        "limit": 10,
        "sort": "stars"
    }
}
```

##### 2: Advanced search with filters
```json
{
    "thoughts": [
        "User needs highly-starred AI repositories in Python",
        "I'll use GitHub's advanced search syntax"
    ],
    "tool_name": "github_search",
    "tool_args": {
        "query": "language:python topic:artificial-intelligence stars:>5000",
        "limit": 5,
        "sort": "stars"
    }
}
```

##### 3: Find recently updated projects
```json
{
    "thoughts": [
        "User wants to see actively maintained React projects",
        "I'll sort by last updated date"
    ],
    "tool_name": "github_search",
    "tool_args": {
        "query": "react framework",
        "limit": 10,
        "sort": "updated"
    }
}
```

##### 4: Find user's repositories
```json
{
    "thoughts": [
        "User wants to find their own repositories or specific user's repos",
        "I'll search with user: prefix"
    ],
    "tool_name": "github_search",
    "tool_args": {
        "query": "user:pistakugli",
        "limit": 20,
        "sort": "updated"
    }
}
```

##### 5: Topic-based search
```json
{
    "thoughts": [
        "User is looking for autonomous agent frameworks",
        "I'll search by topic"
    ],
    "tool_name": "github_search",
    "tool_args": {
        "query": "topic:autonomous-agents topic:ai",
        "limit": 10,
        "sort": "stars"
    }
}
```

#### Advanced Query Syntax:
- **language:python** - Filter by programming language
- **stars:>1000** - Repositories with more than 1000 stars
- **forks:>100** - Repositories with more than 100 forks
- **user:username** - Repositories from specific user
- **org:organization** - Repositories from organization
- **topic:ai** - Repositories tagged with specific topic
- **created:>2023-01-01** - Repositories created after date
- **pushed:>2024-01-01** - Repositories with recent pushes

#### Response Format:
Returns markdown-formatted list with:
- Repository name and URL
- Description
- Programming language
- Star count
- Fork count
- Last update date
