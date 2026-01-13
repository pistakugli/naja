### smbclient_tool:
SMB client for file access and enumeration. Access and download files from SMB shares.

⚠️ Only access SMB shares you own or have authorization to access.

#### Arguments:
 *  "target" (string) : Target in format //IP/SHARE
 *  "username" (Optional, string) : Username
 *  "password" (Optional, string) : Password
 *  "command" (Optional, string) : Command to execute (e.g., "ls", "get file.txt")
 *  "list" (Optional, boolean) : List available shares

#### Usage examples:
##### 1: List shares
\`\`\`json
{
    "thoughts": ["Listing SMB shares on authorized server"],
    "tool_name": "smbclient_tool",
    "tool_args": {
        "target": "//192.168.1.100",
        "list": true
    }
}
\`\`\`

##### 2: Access share
\`\`\`json
{
    "thoughts": ["Accessing authorized share to download files"],
    "tool_name": "smbclient_tool",
    "tool_args": {
        "target": "//192.168.1.100/shared",
        "username": "user",
        "password": "pass",
        "command": "ls"
    }
}
\`\`\`

##### 3: Download file
\`\`\`json
{
    "thoughts": ["Downloading authorized file"],
    "tool_name": "smbclient_tool",
    "tool_args": {
        "target": "//192.168.1.100/shared",
        "username": "user",
        "password": "pass",
        "command": "get important.docx"
    }
}
\`\`\`
