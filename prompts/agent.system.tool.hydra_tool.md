### hydra_tool:
Network login password cracker. For authorized password strength testing.

⚠️ Only test systems you own or have explicit written authorization to test.

#### Arguments:
 *  "target" (string) : Target IP or hostname
 *  "service" (string) : Service type (ssh, ftp, http-get, http-post, rdp, smb, etc.)
 *  "username" (string) : Username to test
 *  "password_list" (string) : Path to password wordlist

#### Usage examples:
##### 1: Test SSH login
\`\`\`json
{
    "thoughts": ["Testing password strength on authorized system"],
    "tool_name": "hydra_tool",
    "tool_args": {
        "target": "192.168.1.100",
        "service": "ssh",
        "username": "testuser",
        "password_list": "/usr/share/wordlists/rockyou.txt"
    }
}
\`\`\`

##### 2: Test FTP login
\`\`\`json
{
    "thoughts": ["Checking FTP password security"],
    "tool_name": "hydra_tool",
    "tool_args": {
        "target": "ftp.example.local",
        "service": "ftp",
        "username": "admin",
        "password_list": "/usr/share/wordlists/common.txt"
    }
}
\`\`\`
