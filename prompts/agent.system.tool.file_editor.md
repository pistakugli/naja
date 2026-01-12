### file_editor:
Edit existing files by replacing a unique string. String must appear exactly once in the file.

!!! Perfect for targeted code changes
!!! String must be unique - tool will error if it appears multiple times
!!! Use file_viewer first to see current content

#### Arguments:
 *  "path" (string) : Path to file to edit
 *  "old_str" (string) : Exact string to find and replace (must be unique)
 *  "new_str" (string) : Replacement string (can be empty to delete)

#### Usage examples:
##### 1: Update configuration value
\`\`\`json
{
    "thoughts": ["Need to change API endpoint in config"],
    "tool_name": "file_editor",
    "tool_args": {
        "path": "config/settings.py",
        "old_str": "API_URL = 'https://old-api.com'",
        "new_str": "API_URL = 'https://new-api.com'"
    }
}
\`\`\`

##### 2: Fix bug in code
\`\`\`json
{
    "thoughts": ["Found the bug, need to replace faulty logic"],
    "tool_name": "file_editor",
    "tool_args": {
        "path": "src/calculator.py",
        "old_str": "result = a - b",
        "new_str": "result = a + b"
    }
}
\`\`\`
