# GitHub Search Tool

Tool za pretraživanje GitHub repositories direktno iz Agent Zero.

## Setup

```bash
export GITHUB_TOKEN="your_github_token_here"
```

## Usage

Agent Zero će automatski koristiti ovaj tool kada detektuje potrebu za GitHub pretraživanjem:

```
"Search GitHub for Python machine learning projects"
"Find my recent repositories"
"Show me highly-starred AI frameworks"
```

## Tool Files

- `python/tools/github_search.py` - Tool implementation
- `prompts/agent.system.tool.github_search.md` - AI interface definition

## Features

- Advanced search syntax support
- Filter by language, stars, forks
- Sort by stars/forks/updated date
- User/organization repository search
- Topic-based filtering

## Example Queries

**Basic search:**
```
query: "machine learning python"
limit: 10
sort: "stars"
```

**Advanced filters:**
```
query: "language:python topic:ai stars:>5000"
limit: 5
sort: "stars"
```

**User repositories:**
```
query: "user:pistakugli"
limit: 20
sort: "updated"
```

## API Limits

- Max 20 results per search
- 5000 requests/hour (authenticated)

---

Created: 2026-01-12
Author: Claude λ₄
