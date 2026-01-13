### enum4linux_tool:
Enumerate information from Windows and Samba systems. Extract users, shares, groups, and more.

⚠️ Only enumerate systems you own or have authorization to test.

#### Arguments:
 *  "target" (string) : Target IP address
 *  "username" (Optional, string) : Username for authentication
 *  "password" (Optional, string) : Password for authentication
 *  "all" (Optional, boolean) : Run all enumeration
 *  "users" (Optional, boolean) : Enumerate users
 *  "shares" (Optional, boolean) : Enumerate shares
 *  "groups" (Optional, boolean) : Enumerate groups

#### Usage examples:
##### 1: Full enumeration
\`\`\`json
{
    "thoughts": ["Complete SMB enumeration on authorized target"],
    "tool_name": "enum4linux_tool",
    "tool_args": {
        "target": "192.168.1.100",
        "all": true
    }
}
\`\`\`

##### 2: User enumeration with credentials
\`\`\`json
{
    "thoughts": ["Enumerating domain users with valid credentials"],
    "tool_name": "enum4linux_tool",
    "tool_args": {
        "target": "192.168.1.100",
        "username": "guest",
        "password": "guest",
        "users": true,
        "groups": true
    }
}
\`\`\`
