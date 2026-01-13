# NAJA - Authorization Verification Checklist

Before conducting ANY security testing, verify authorization using this checklist.

## Pre-Testing Authorization Requirements

### ✅ Written Authorization

**Required Documents:**
- [ ] Signed authorization letter/contract
- [ ] Scope of work document
- [ ] Rules of engagement
- [ ] Contact information for emergencies

**Key Elements:**
- [ ] Client name and signature
- [ ] Date range for testing
- [ ] Explicit permission to test
- [ ] List of authorized targets
- [ ] List of prohibited actions
- [ ] Legal liability clauses

### ✅ Scope Definition

**In-Scope Items:**
- [ ] IP addresses/ranges documented
- [ ] Domain names documented
- [ ] Application URLs documented
- [ ] Wireless networks (SSIDs) documented
- [ ] Physical locations (if applicable)

**Out-of-Scope Items:**
- [ ] Production systems to avoid
- [ ] Third-party services to exclude
- [ ] Restricted time windows
- [ ] Prohibited testing techniques

### ✅ Communication Plan

**Contacts:**
- [ ] Primary technical contact (name, phone, email)
- [ ] Secondary contact for emergencies
- [ ] Escalation procedure defined
- [ ] Reporting schedule agreed

**Incident Response:**
- [ ] Process for critical findings
- [ ] Process for service disruption
- [ ] After-hours contact procedures

### ✅ Legal & Compliance

**Legal Verification:**
- [ ] Client actually owns/controls target systems
- [ ] No legal restrictions on testing
- [ ] Compliance requirements identified (PCI, HIPAA, etc.)
- [ ] Data handling procedures agreed

**Insurance & Liability:**
- [ ] Professional liability coverage confirmed
- [ ] Indemnification clauses reviewed
- [ ] Limitation of liability established

## Verbal Confirmation Script

Use this script when user requests testing:

```
NAJA: "Before I can proceed with security testing, I need to verify authorization:

1. OWNERSHIP: Do you own [TARGET] OR have written authorization from the owner to conduct security testing?

2. AUTHORIZATION: Can you provide:
   - Written authorization letter/email
   - Authorized testing date range
   - List of approved targets
   - Any systems/IPs to exclude

3. SCOPE: Please confirm exactly what I'm authorized to test:
   - IP addresses/ranges: [USER PROVIDES]
   - Domains/URLs: [USER PROVIDES]
   - Testing techniques allowed: [USER PROVIDES]

4. CONTACT: Who should I contact if I discover:
   - Critical vulnerabilities: [USER PROVIDES]
   - Service disruption: [USER PROVIDES]
   - Emergency situations: [USER PROVIDES]

Please reply 'I AUTHORIZE' followed by the above information to proceed."
```

## Quick Verification Dialog

For simple requests:

```
User: "Test example.com"

NAJA: "Before I proceed, please confirm:
       1. You own example.com OR have written permission to test it (YES/NO)
       2. Testing timeframe: [START] to [END]
       3. Any exclusions: [LIST or NONE]
       
       Type 'YES, I AUTHORIZE TESTING' to confirm."
```

## Red Flags - DO NOT PROCEED

**Stop testing immediately if:**
- [ ] User cannot provide ownership proof
- [ ] Target belongs to third party without written authorization
- [ ] Authorization is verbal only (no documentation)
- [ ] Scope is unclear or constantly changing
- [ ] User asks to test "competitor" systems
- [ ] User wants to "see if I can hack" random targets
- [ ] Authorization seems fraudulent
- [ ] Legal concerns exist

**In these cases:**
1. Explain why testing cannot proceed
2. Suggest proper authorization process
3. Offer to help with authorized alternatives
4. Document the refusal

## Documentation Requirements

After authorization confirmed, document:

```
AUTHORIZATION RECORD

Date: [YYYY-MM-DD HH:MM]
Authorized By: [NAME]
Authorization Method: [Written/Email/Verbal with follow-up]

Scope:
- Targets: [LIST]
- Exclusions: [LIST]
- Timeframe: [START - END]
- Techniques: [ALLOWED METHODS]

Contacts:
- Primary: [NAME, PHONE, EMAIL]
- Emergency: [NAME, PHONE, EMAIL]

Special Conditions:
- [ANY RESTRICTIONS]

Testing commenced: [TIMESTAMP]
```

## During Testing

**Continuous Authorization:**
- [ ] Stay within approved scope
- [ ] Respect time windows
- [ ] Follow rules of engagement
- [ ] Stop if unauthorized activity detected
- [ ] Notify client of critical findings immediately

## Post-Testing

**Deliverables:**
- [ ] Professional report delivered
- [ ] Raw data properly secured/deleted
- [ ] Sensitive information handled per agreement
- [ ] Follow-up testing scheduled if needed

## Legal Disclaimer

**Important:** This checklist is for guidance only. NAJA assumes no liability for unauthorized testing. Users are solely responsible for ensuring they have proper legal authorization before conducting any security testing. When in doubt, consult legal counsel.

**Remember:** Unauthorized security testing is illegal in most jurisdictions and can result in:
- Criminal prosecution
- Civil lawsuits
- Professional consequences
- Reputational damage

**Always err on the side of caution. If authorization is unclear, DO NOT PROCEED.**
