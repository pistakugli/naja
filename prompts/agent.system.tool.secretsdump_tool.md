### secretsdump_tool:
Extract credentials from Windows systems. Dump SAM, LSA secrets, NTDS.dit hashes.

⚠️ CRITICAL: Only use on systems you own. Credential dumping without authorization is illegal.

#### Arguments:
 *  "target" (string) : Target in format DOMAIN/USER:PASSWORD@IP
 *  "hashes" (Optional, string) : NTLM hashes in LM:NT format
 *  "sam" (Optional, boolean) : Dump SAM database
 *  "system" (Optional, boolean) : Dump SYSTEM hive
 *  "ntds" (Optional, boolean) : Dump NTDS.dit (Domain Controller)

#### Usage examples:
##### 1: Dump local SAM
\`\`\`json
{
    "thoughts": ["Dumping local credentials from authorized workstation"],
    "tool_name": "secretsdump_tool",
    "tool_args": {
        "target": "WORKGROUP/Administrator:P@ssw0rd@192.168.1.50",
        "sam": true
    }
}
\`\`\`

##### 2: Dump Domain Controller
\`\`\`json
{
    "thoughts": ["Extracting AD hashes from authorized DC"],
    "tool_name": "secretsdump_tool",
    "tool_args": {
        "target": "CORP/Administrator:P@ssw0rd@192.168.1.10",
        "ntds": true
    }
}
\`\`\`

##### 3: Pass-the-hash
\`\`\`json
{
    "thoughts": ["Using NTLM hash to dump secrets"],
    "tool_name": "secretsdump_tool",
    "tool_args": {
        "target": "CORP/Administrator@192.168.1.10",
        "hashes": "aad3b435b51404eeaad3b435b51404ee:NTHASH"
    }
}
\`\`\`
