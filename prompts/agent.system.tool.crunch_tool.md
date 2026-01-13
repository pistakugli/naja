### crunch_tool:
Wordlist generator. Create custom wordlists based on criteria (min/max length, character set, patterns).

#### Arguments:
 *  "min_length" (integer) : Minimum password length
 *  "max_length" (integer) : Maximum password length
 *  "charset" (Optional, string) : Character set or pattern
 *  "output_file" (string) : Output file path
 *  "pattern" (Optional, string) : Pattern with placeholders (@=lowercase, ,=uppercase, %=numbers, ^=symbols)

#### Usage examples:
##### 1: Generate 6-8 char numeric passwords
\`\`\`json
{
    "thoughts": ["Creating numeric PIN wordlist"],
    "tool_name": "crunch_tool",
    "tool_args": {
        "min_length": 6,
        "max_length": 8,
        "charset": "0123456789",
        "output_file": "/tmp/pins.txt"
    }
}
\`\`\`

##### 2: Pattern-based generation
\`\`\`json
{
    "thoughts": ["Generating passwords matching company pattern"],
    "tool_name": "crunch_tool",
    "tool_args": {
        "min_length": 8,
        "max_length": 8,
        "pattern": "Pass%%%%",
        "output_file": "/tmp/custom_list.txt"
    }
}
\`\`\`
