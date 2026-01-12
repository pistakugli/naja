### file_viewer:
View file contents with line numbers, or list directory contents.

!!! Use this before editing files to see current state
!!! Shows line numbers for precise editing
!!! Can view specific line ranges for large files

#### Arguments:
 *  "path" (string) : Path to file or directory
 *  "start_line" (Optional, integer) : Starting line number (default: 1)
 *  "end_line" (Optional, integer) : Ending line number (default: -1 for end of file)

#### Usage examples:
##### 1: View entire file
\`\`\`json
{
    "thoughts": ["Need to see the config file contents"],
    "tool_name": "file_viewer",
    "tool_args": {
        "path": "config/settings.py"
    }
}
\`\`\`

##### 2: View specific lines
\`\`\`json
{
    "thoughts": ["Only need to see lines 50-100"],
    "tool_name": "file_viewer",
    "tool_args": {
        "path": "src/main.py",
        "start_line": 50,
        "end_line": 100
    }
}
\`\`\`

##### 3: List directory
\`\`\`json
{
    "thoughts": ["Need to see what files are in this directory"],
    "tool_name": "file_viewer",
    "tool_args": {
        "path": "src/"
    }
}
\`\`\`
