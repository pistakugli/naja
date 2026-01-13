### responder_tool:
LLMNR, NBT-NS, and MDNS poisoner. Capture credentials on Windows networks.

⚠️ CRITICAL: Only use on authorized penetration tests. Credential theft is illegal.

#### Arguments:
 *  "interface" (string) : Network interface
 *  "analyze" (Optional, boolean) : Analyze mode (no poisoning)
 *  "wpad" (Optional, boolean) : WPAD rogue proxy server
 *  "force_wpad_auth" (Optional, boolean) : Force WPAD authentication

#### Usage examples:
##### 1: Analysis mode (safe)
\`\`\`json
{
    "thoughts": ["Analyzing network for LLMNR/NBT-NS traffic"],
    "tool_name": "responder_tool",
    "tool_args": {
        "interface": "eth0",
        "analyze": true
    }
}
\`\`\`

##### 2: Active poisoning (authorized test only)
\`\`\`json
{
    "thoughts": ["Active LLMNR poisoning on authorized pentest"],
    "tool_name": "responder_tool",
    "tool_args": {
        "interface": "eth0",
        "wpad": true
    }
}
\`\`\`
