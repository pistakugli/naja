### cewl_tool:
Custom wordlist generator from website content. Spider websites and extract words for targeted password attacks.

#### Arguments:
 *  "url" (string) : Target website URL
 *  "depth" (Optional, integer) : Spider depth (default: 2)
 *  "min_word_length" (Optional, integer) : Minimum word length (default: 3)
 *  "output_file" (string) : Output wordlist file
 *  "email" (Optional, boolean) : Also extract email addresses

#### Usage examples:
##### 1: Generate wordlist from company website
\`\`\`json
{
    "thoughts": ["Creating targeted wordlist from company site"],
    "tool_name": "cewl_tool",
    "tool_args": {
        "url": "https://targetcompany.com",
        "depth": 3,
        "min_word_length": 6,
        "output_file": "/tmp/company_words.txt"
    }
}
\`\`\`

##### 2: Extract emails and words
\`\`\`json
{
    "thoughts": ["OSINT - gathering emails and words"],
    "tool_name": "cewl_tool",
    "tool_args": {
        "url": "https://target.com",
        "output_file": "/tmp/wordlist.txt",
        "email": true
    }
}
\`\`\`
