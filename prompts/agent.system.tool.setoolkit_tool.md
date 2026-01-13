### setoolkit_tool:
Social Engineering Toolkit. Perform advanced social engineering attacks.

⚠️ CRITICAL: Only use for authorized security awareness training. Illegal use carries severe penalties.

#### Arguments:
 *  "attack_type" (string) : Attack vector: "phishing", "website", "powershell", "qr_code"
 *  "template" (Optional, string) : Email/website template
 *  "payload" (Optional, string) : Payload type
 *  "listener_ip" (Optional, string) : IP for reverse connection

#### Usage examples:
##### 1: Phishing awareness test
\`\`\`json
{
    "thoughts": ["Authorized employee security training"],
    "tool_name": "setoolkit_tool",
    "tool_args": {
        "attack_type": "phishing",
        "template": "gmail",
        "listener_ip": "192.168.1.50"
    }
}
\`\`\`

##### 2: Credential harvester (training)
\`\`\`json
{
    "thoughts": ["Security awareness demonstration"],
    "tool_name": "setoolkit_tool",
    "tool_args": {
        "attack_type": "website",
        "template": "google"
    }
}
\`\`\`
