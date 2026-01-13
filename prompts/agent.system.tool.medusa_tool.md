### medusa_tool:
Fast, parallel password brute-forcing tool. Supports SSH, FTP, HTTP, MySQL, PostgreSQL, and more.

⚠️ Only brute force services you own or have written authorization to test.

#### Arguments:
 *  "target" (string) : Target IP or hostname
 *  "protocol" (string) : Protocol: "ssh", "ftp", "http", "mysql", "postgres", "telnet", "vnc"
 *  "username" (Optional, string) : Single username
 *  "userlist" (Optional, string) : Path to username list
 *  "password" (Optional, string) : Single password
 *  "passlist" (Optional, string) : Path to password list
 *  "threads" (Optional, integer) : Number of parallel threads

#### Usage examples:
##### 1: SSH brute force
\`\`\`json
{
    "thoughts": ["Testing SSH with common credentials"],
    "tool_name": "medusa_tool",
    "tool_args": {
        "target": "192.168.1.100",
        "protocol": "ssh",
        "username": "admin",
        "passlist": "/usr/share/wordlists/rockyou.txt",
        "threads": 4
    }
}
\`\`\`

##### 2: FTP with user/pass lists
\`\`\`json
{
    "thoughts": ["Brute forcing FTP service"],
    "tool_name": "medusa_tool",
    "tool_args": {
        "target": "ftp.target.com",
        "protocol": "ftp",
        "userlist": "/tmp/users.txt",
        "passlist": "/tmp/passwords.txt"
    }
}
\`\`\`
