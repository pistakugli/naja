### foremost_tool:
File carving tool. Recover files from disk images or raw data based on headers/footers.

#### Arguments:
 *  "input_file" (string) : Input file or device
 *  "output_dir" (string) : Output directory for recovered files
 *  "type" (Optional, string) : File types to recover (e.g., "jpg,png,pdf,doc")
 *  "all" (Optional, boolean) : Extract all file types

#### Usage examples:
##### 1: Recover images
\`\`\`json
{
    "thoughts": ["Carving images from disk dump"],
    "tool_name": "foremost_tool",
    "tool_args": {
        "input_file": "/tmp/disk.img",
        "output_dir": "/tmp/recovered",
        "type": "jpg,png,gif"
    }
}
\`\`\`

##### 2: Recover all file types
\`\`\`json
{
    "thoughts": ["Complete file carving"],
    "tool_name": "foremost_tool",
    "tool_args": {
        "input_file": "/dev/sdb1",
        "output_dir": "/tmp/carved",
        "all": true
    }
}
\`\`\`
