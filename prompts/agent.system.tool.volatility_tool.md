### volatility_tool:
Advanced memory forensics framework. Extract digital artifacts from RAM dumps.

#### Arguments:
 *  "memory_file" (string) : Path to memory dump file
 *  "profile" (Optional, string) : OS profile (e.g., "Win10x64", "LinuxUbuntu")
 *  "plugin" (string) : Plugin to run (e.g., "pslist", "netscan", "hashdump", "malfind")
 *  "dump_dir" (Optional, string) : Directory for output files

#### Usage examples:
##### 1: Process listing
\`\`\`json
{
    "thoughts": ["Analyzing running processes in memory dump"],
    "tool_name": "volatility_tool",
    "tool_args": {
        "memory_file": "/tmp/memory.dmp",
        "profile": "Win10x64",
        "plugin": "pslist"
    }
}
\`\`\`

##### 2: Network connections
\`\`\`json
{
    "thoughts": ["Extracting network connections from RAM"],
    "tool_name": "volatility_tool",
    "tool_args": {
        "memory_file": "/tmp/memory.dmp",
        "profile": "Win7SP1x64",
        "plugin": "netscan"
    }
}
\`\`\`
