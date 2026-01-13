### lynis_tool:
Security auditing and hardening tool for Unix/Linux systems. Comprehensive system audit.

⚠️ Only audit systems you own or have authorization to audit.

#### Arguments:
 *  "audit_type" (string) : Audit type: "system", "dockerfile", "network"
 *  "quick" (Optional, boolean) : Quick scan mode
 *  "pentest" (Optional, boolean) : Pentest mode (minimal output)

#### Usage examples:
##### 1: System audit
\`\`\`json
{
    "thoughts": ["Auditing system security configuration"],
    "tool_name": "lynis_tool",
    "tool_args": {
        "audit_type": "system"
    }
}
\`\`\`

##### 2: Quick pentest scan
\`\`\`json
{
    "thoughts": ["Quick security assessment"],
    "tool_name": "lynis_tool",
    "tool_args": {
        "audit_type": "system",
        "quick": true,
        "pentest": true
    }
}
\`\`\`
