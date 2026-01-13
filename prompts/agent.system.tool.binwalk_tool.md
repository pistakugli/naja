### binwalk_tool:
Firmware analysis tool. Search binary images for embedded files and executable code.

#### Arguments:
 *  "file" (string) : Binary file to analyze
 *  "extract" (Optional, boolean) : Extract discovered files
 *  "signature" (Optional, boolean) : Scan for common file signatures
 *  "entropy" (Optional, boolean) : Calculate entropy
 *  "output_dir" (Optional, string) : Extraction directory

#### Usage examples:
##### 1: Basic firmware analysis
\`\`\`json
{
    "thoughts": ["Analyzing firmware image"],
    "tool_name": "binwalk_tool",
    "tool_args": {
        "file": "/tmp/firmware.bin",
        "signature": true
    }
}
\`\`\`

##### 2: Extract embedded files
\`\`\`json
{
    "thoughts": ["Extracting firmware components"],
    "tool_name": "binwalk_tool",
    "tool_args": {
        "file": "/tmp/router_fw.bin",
        "extract": true,
        "output_dir": "/tmp/extracted"
    }
}
\`\`\`
