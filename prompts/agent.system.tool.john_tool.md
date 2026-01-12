### john_tool:
John the Ripper password cracker. For authorized password strength testing and recovery.

⚠️ Only crack passwords you own or have authorization to test.

#### Arguments:
 *  "hash_file" (string) : File containing password hashes
 *  "wordlist" (Optional, string) : Wordlist for dictionary attack
 *  "format" (Optional, string) : Hash format (md5, sha256, bcrypt, etc.)

#### Usage examples:
##### 1: Crack password hashes
\`\`\`json
{
    "thoughts": ["Testing password strength on authorized hashes"],
    "tool_name": "john_tool",
    "tool_args": {
        "hash_file": "/tmp/hashes.txt",
        "wordlist": "/usr/share/wordlists/rockyou.txt"
    }
}
\`\`\`

##### 2: Crack specific hash format
\`\`\`json
{
    "thoughts": ["Cracking MD5 hashes"],
    "tool_name": "john_tool",
    "tool_args": {
        "hash_file": "/tmp/md5_hashes.txt",
        "wordlist": "/usr/share/wordlists/common.txt",
        "format": "raw-md5"
    }
}
\`\`\`
