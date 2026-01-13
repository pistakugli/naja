### hashcat_tool:
GPU-accelerated password hash cracker. World's fastest password recovery tool.

⚠️ Only crack hashes you own or have authorization to crack. Unauthorized access is illegal.

#### Arguments:
 *  "hash_file" (string) : Path to file containing hashes
 *  "hash_type" (string) : Hash type (-m value): "0" (MD5), "100" (SHA1), "1400" (SHA256), "3200" (bcrypt), "1000" (NTLM)
 *  "attack_mode" (string) : "0" (dictionary), "1" (combinator), "3" (brute-force), "6" (hybrid wordlist+mask)
 *  "wordlist" (Optional, string) : Path to wordlist
 *  "rules" (Optional, string) : Path to rules file
 *  "mask" (Optional, string) : Mask for brute force (e.g., "?a?a?a?a?a?a")

#### Usage examples:
##### 1: Dictionary attack on MD5
\`\`\`json
{
    "thoughts": ["Cracking MD5 hash with rockyou"],
    "tool_name": "hashcat_tool",
    "tool_args": {
        "hash_file": "/tmp/hashes.txt",
        "hash_type": "0",
        "attack_mode": "0",
        "wordlist": "/usr/share/wordlists/rockyou.txt"
    }
}
\`\`\`

##### 2: Brute force attack
\`\`\`json
{
    "thoughts": ["Brute forcing 6-char password"],
    "tool_name": "hashcat_tool",
    "tool_args": {
        "hash_file": "/tmp/hash.txt",
        "hash_type": "100",
        "attack_mode": "3",
        "mask": "?a?a?a?a?a?a"
    }
}
\`\`\`
