### exiftool_tool:
Metadata extraction and analysis tool. Extract EXIF data from images, documents, and files.

#### Arguments:
 *  "file" (string) : File path or directory
 *  "remove" (Optional, boolean) : Remove all metadata
 *  "geotag" (Optional, boolean) : Extract GPS/location data

#### Usage examples:
##### 1: Extract metadata
\`\`\`json
{
    "thoughts": ["Extracting metadata from image"],
    "tool_name": "exiftool_tool",
    "tool_args": {
        "file": "/tmp/photo.jpg"
    }
}
\`\`\`

##### 2: Extract GPS data
\`\`\`json
{
    "thoughts": ["Looking for location information"],
    "tool_name": "exiftool_tool",
    "tool_args": {
        "file": "/tmp/photos/",
        "geotag": true
    }
}
\`\`\`

##### 3: Remove metadata
\`\`\`json
{
    "thoughts": ["Sanitizing file metadata"],
    "tool_name": "exiftool_tool",
    "tool_args": {
        "file": "/tmp/document.pdf",
        "remove": true
    }
}
\`\`\`
