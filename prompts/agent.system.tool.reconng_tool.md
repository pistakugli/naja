### reconng_tool:
Full-featured reconnaissance framework with independent modules and database interaction.

#### Arguments:
 *  "workspace" (string) : Workspace name
 *  "module" (string) : Module to run (e.g., "recon/domains-hosts/google_site_web")
 *  "source" (string) : Source data (domain, company name, etc.)
 *  "options" (Optional, object) : Module-specific options

#### Usage examples:
##### 1: Domain to hosts via Google
\`\`\`json
{
    "thoughts": ["Finding hosts for domain using Google"],
    "tool_name": "reconng_tool",
    "tool_args": {
        "workspace": "target_recon",
        "module": "recon/domains-hosts/google_site_web",
        "source": "target.com"
    }
}
\`\`\`

##### 2: Contact harvesting
\`\`\`json
{
    "thoughts": ["Gathering contact information"],
    "tool_name": "reconng_tool",
    "tool_args": {
        "workspace": "osint",
        "module": "recon/domains-contacts/whois_pocs",
        "source": "target.com"
    }
}
\`\`\`
