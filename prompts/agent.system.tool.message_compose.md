### message_compose:
Create a formatted message draft (email, SMS, or other). Provides clean template ready to send.

!!! Use this when user asks to "write", "draft", "compose" a message
!!! Better UX than plain text response

#### Arguments:
 *  "kind" (string) : Message type - "email", "textMessage", or "other"
 *  "body" (string) : The message content
 *  "subject" (Optional, string) : Email subject line
 *  "to" (Optional, string) : Recipient address or number

#### Usage examples:
##### 1: Draft email
\`\`\`json
{
    "thoughts": ["User wants to draft an email"],
    "tool_name": "message_compose",
    "tool_args": {
        "kind": "email",
        "subject": "Meeting Follow-up",
        "to": "colleague@example.com",
        "body": "Thank you for the productive meeting today..."
    }
}
\`\`\`

##### 2: Draft text message
\`\`\`json
{
    "thoughts": ["Quick SMS draft needed"],
    "tool_name": "message_compose",
    "tool_args": {
        "kind": "textMessage",
        "to": "+1234567890",
        "body": "Running 10 minutes late, see you soon!"
    }
}
\`\`\`
