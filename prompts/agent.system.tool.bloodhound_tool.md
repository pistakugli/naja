### bloodhound_tool:
Active Directory attack path mapper. Visualize and analyze AD relationships for privilege escalation.

⚠️ Only use on Active Directory environments you own or have authorization to test.

#### Arguments:
 *  "collection_method" (string) : Collection method: "All", "DCOnly", "Session", "LoggedOn", "Group"
 *  "domain" (string) : Target domain
 *  "username" (string) : Domain username
 *  "password" (string) : Domain password
 *  "domain_controller" (Optional, string) : Domain controller IP
 *  "output_dir" (Optional, string) : Output directory for JSON files

#### Usage examples:
##### 1: Collect all data
\`\`\`json
{
    "thoughts": ["Collecting AD data for authorized assessment"],
    "tool_name": "bloodhound_tool",
    "tool_args": {
        "collection_method": "All",
        "domain": "corp.local",
        "username": "auditor",
        "password": "P@ssw0rd",
        "output_dir": "/tmp/bloodhound"
    }
}
\`\`\`

##### 2: DC-only collection
\`\`\`json
{
    "thoughts": ["Quick DC enumeration"],
    "tool_name": "bloodhound_tool",
    "tool_args": {
        "collection_method": "DCOnly",
        "domain": "corp.local",
        "username": "user",
        "password": "pass",
        "domain_controller": "192.168.1.10"
    }
}
\`\`\`
