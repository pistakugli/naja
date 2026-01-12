### file_creator:
Create new files with specified content. Automatically creates parent directories if needed.

!!! Use when user asks to create new files
!!! Better than code_execution for simple file creation
!!! Automatically creates directories

#### Arguments:
 *  "path" (string) : Path where file should be created
 *  "content" (string) : File content

#### Usage examples:
##### 1: Create script file
\`\`\`json
{
    "thoughts": ["Need to create a new Python script"],
    "tool_name": "file_creator",
    "tool_args": {
        "path": "scripts/backup.py",
        "content": "#!/usr/bin/env python3\n\nprint('Backup script')"
    }
}
\`\`\`

##### 2: Create config file
\`\`\`json
{
    "thoughts": ["Creating new config file"],
    "tool_name": "file_creator",
    "tool_args": {
        "path": "config/database.json",
        "content": "{\"host\": \"localhost\", \"port\": 5432}"
    }
}
\`\`\`
