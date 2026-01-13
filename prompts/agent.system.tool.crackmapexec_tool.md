### crackmapexec_tool:
Swiss army knife for pentesting Windows/Active Directory networks. Enumerate, authenticate, and execute commands.

⚠️ CRITICAL: Only use on authorized Active Directory environments. Unauthorized access is illegal.

#### Arguments:
 *  "protocol" (string) : Protocol: "smb", "winrm", "mssql", "ssh", "ldap"
 *  "target" (string) : Target IP or range (e.g., "192.168.1.0/24")
 *  "username" (Optional, string) : Single username
 *  "password" (Optional, string) : Single password
 *  "hash" (Optional, string) : NTLM hash for pass-the-hash
 *  "domain" (Optional, string) : Domain name
 *  "shares" (Optional, boolean) : Enumerate shares
 *  "users" (Optional, boolean) : Enumerate users
 *  "execute" (Optional, string) : Command to execute

#### Usage examples:
##### 1: SMB enumeration
\`\`\`json
{
    "thoughts": ["Enumerating SMB shares on authorized network"],
    "tool_name": "crackmapexec_tool",
    "tool_args": {
        "protocol": "smb",
        "target": "192.168.1.0/24",
        "shares": true
    }
}
\`\`\`

##### 2: Pass-the-hash attack
\`\`\`json
{
    "thoughts": ["Using captured NTLM hash for authentication"],
    "tool_name": "crackmapexec_tool",
    "tool_args": {
        "protocol": "smb",
        "target": "192.168.1.50",
        "username": "admin",
        "hash": "NTLMHASH:HERE",
        "domain": "CORP"
    }
}
\`\`\`

##### 3: Execute command
\`\`\`json
{
    "thoughts": ["Running command on compromised system"],
    "tool_name": "crackmapexec_tool",
    "tool_args": {
        "protocol": "smb",
        "target": "192.168.1.50",
        "username": "admin",
        "password": "P@ssw0rd",
        "execute": "whoami"
    }
}
\`\`\`
