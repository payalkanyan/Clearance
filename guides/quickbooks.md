# QuickBooks

**QuickBooks, developer.intuit.com**

**Verdict:** Supported via Composio managed OAuth app; registering your own QuickBooks OAuth app is optional unless you want custom branding on the consent screen. *(Sourced)*
> "Composio provides a managed OAuth app for Quickbooks, so you sign in with your normal Quickbooks account and approve access." — [source](https://composio.dev/toolkits/quickbooks)

**Difficulty:** Hard
**Why:** A self-assessment questionnaire confirming terms compliance may be required before public distribution. *(Sourced)*
**Hands-on time:** 10 to 20 minutes *(Inferred)*
**Waiting time:** Immediate for development and testing; review times for public release are unspecified *(Inferred)*

**Composio status:** Toolkit available with a Composio managed OAuth app, so you can connect without registering your own. Bringing your own app is optional, for your name on the consent screen. *(Sourced)*
> "Composio provides a managed OAuth app for Quickbooks, so you sign in with your normal Quickbooks account and approve access." — [source](https://composio.dev/toolkits/quickbooks)

**Prerequisites**

- At https://developer.intuit.com/app/developer/homepage, a sign-in wall: you must log in before you can register an app. Fields visible: platform. *(Tested)*
  > [source](https://developer.intuit.com/app/developer/homepage)
  > observed by the agent at 2026-10-30T11:35:42Z, HTTP 200; matched sign in
- At https://dashboard.composio.dev/login?utm_source=toolkits&utm_medium=hero&utm_campaign=toolkits-quickbooks&utm_content=%2Ftoolkits%2Fquickbooks, a sign-in wall: you must log in before you can register an app. Fields visible: email, logo. *(Tested)*
  > [source](https://dashboard.composio.dev/login?utm_source=toolkits&utm_medium=hero&utm_campaign=toolkits-quickbooks&utm_content=%2Ftoolkits%2Fquickbooks)
  > observed by the agent at 2026-10-30T11:35:45Z, HTTP 200; matched signin, login, continue with google
- An Intuit Developer account created via the developer portal. *(Sourced)*
  > "To enroll, you must create a Developer Account in the Portal by providing complete and accurate information" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- Accurate enrollment details including legal identity name, domicile address, valid email, and authorized users. *(Sourced)*
  > "Your legal name whether using the Platform as an individual or entity." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- A valid payment method if platform service fees (such as monthly or variable API usage fees) apply to your account. *(Sourced)*
  > "To use the Intuit Developer Platform, you may need to pay fees which may include a flat monthly fee and a variable API usage fee" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Setup steps**

1. Sign up for an Intuit Developer account at developer.intuit.com. *(Inferred)*
   > Derived from third-party developer guide describing Intuit Developer setup steps.
2. Navigate to the Developer Dashboard, open 'My Hub' > 'App Dashboard', and click 'Add'. *(Inferred)*
   > Derived from third-party developer guide describing Intuit Developer dashboard navigation.
3. Select 'QuickBooks Online and Payments', specify your app name, and proceed to the permissions step. *(Inferred)*
   > Derived from third-party developer guide describing app creation flow.
4. Select the required permissions for your application and click 'Done' to finalize creation. *(Inferred)*
   > Derived from third-party developer guide describing permission assignment.
5. Go to the 'Settings' tab in your application, find 'Redirect URIs', and add your callback URL. *(Inferred)*
   > Derived from third-party developer guide describing OAuth callback configuration.
6. Navigate to 'Keys and credentials', toggle 'Show credentials', and copy your Client ID and Client Secret. *(Inferred)*
   > Derived from third-party developer guide describing key retrieval.
7. Under 'My Hub' > 'Sandbox', click 'Add' to spin up a test QuickBooks company and record the Company ID / Realm ID for API requests. *(Inferred)*
   > Derived from third-party developer guide describing sandbox setup.

**Scopes**

- com.intuit.quickbooks.accounting: Grants access to the QuickBooks Online Accounting API for managing accounting entities. *(Sourced)*
  > "Grants access to the QuickBooks Online Accounting API, which focuses on accounting data." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- com.intuit.quickbooks.payment: Grants access to the QuickBooks Payments API for payment processing. *(Sourced)*
  > "Grants access to the QuickBooks Payments API, which focuses on payments processing." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- openid: Grants access to OpenID Connect features, including user profile, email, phone, and address. *(Sourced)*
  > "Grants access to OpenID Connect features. Include one or more of the following capabilities:" — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- app-foundations.custom-field-definitions: Grants read and write access to custom field definitions via the GraphQL API. *(Sourced)*
  > "Grants access to read and write Custom Fields definitions data." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- project-management.project: Grants read and write access to Project data via GraphQL. *(Sourced)*
  > "Grants access to read and write Project data." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- payroll.compensation.read: Grants read access to pay types using the Time API (requires customer to use QuickBooks Payroll). *(Sourced)*
  > "Grants read access to pay types (i.e., compensation) using the Time API." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)

**Limits before approval**

- Sandbox environments must strictly use non-live, aggregated, and anonymized data. *(Sourced)*
  > "You agree to utilize the Sandbox exclusively for the creation, testing, and internal evaluation of your Developer Applications using only non-live, Aggregated and Anonymized Data" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- The sandbox environment and test data cannot be utilized for production purposes. *(Sourced)*
  > "The Sandbox, and the data provided therein, must not be used for production purposes." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- Intuit reserves the right to audit sandbox use and impose throttling or functionality limits. *(Sourced)*
  > "Intuit reserves the right to conduct audits of your use of the Sandbox and may impose additional fees or limit functionalities (including throttling or blocking" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- QuickBooks OAuth access tokens expire after 1 hour and must be refreshed. *(Inferred)*
  > Documented in third-party documentation; official OAuth token lifetime details were not fully rendered in the provided page text.

**Approval process**

- A self-assessment questionnaire confirming terms compliance may be required before public distribution. *(Sourced)*
  > "Before your Developer Application can be publicly distributed and in other instances as determined solely by Intuit you may be required to submit a" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- Launching on Intuit Marketing Channels requires technical, marketing, and legal compliance evaluations. *(Sourced)*
  > "To launch your Application using an Intuit Marketing Channel, further assessments and reviews may be required by Intuit initially, and periodically thereafter, including, but" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- A mandatory security review evaluating data privacy and stewardship practices, potentially conducted by an Intuit-designated third party. *(Sourced)*
  > "Our security review focuses on your data privacy and stewardship policies to ensure that you are abiding by Applicable Law, this Agreement, Intuit Policies." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- Intuit retains total discretion to withhold, reject, or suspend developer applications without providing justification. *(Sourced)*
  > "Intuit reserves the right to withhold, deny, suspend, or reject your Developer Application at its sole discretion, without any obligation to provide reasons" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Likely blockers**

- The QuickBooks Payroll API is currently closed to new developers and restricted to an interest list. *(Sourced)*
  > "The payroll API is not currently open to new developers, but we can add you to our interest list so you can be kept informed" — [source](https://help.developer.intuit.com/s/question/0D5TR00000aUBQ20AO/how-to-add-scopes-for-payroll-to-a-production-app)
- The Intuit App Partner Program has regional restrictions and is only available in the US, UK, Australia, and Canada (excluding Quebec). *(Sourced)*
  > "The Intuit App Partner Program is available for partners based in the US, UK, Australia, and Canada (excluding Quebec)." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- Failure to provide published legal terms, including user terms of service and privacy policies. *(Sourced)*
  > "updates to disclosures, terms of service, and privacy policies provided to Users." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- Failing third-party security audits or not cooperating with audit information requests. *(Inferred)*
  > Section 8.1 requires working with designated third-party security reviewers, and section 6.3 notes that failure to remediate issues can lead to termination.
- Regional or legal restrictions *(Inferred)*
  > rubric modifier: noted as a blocker, it does not change the difficulty level

**Agent can do**

- Configure MCP or SDK clients with required QuickBooks tools and scopes
- Identify applicable scopes for accounting, payments, or OpenID features
- Generate OAuth 2.0 flow templates and handle token refresh logic
- Draft code to execute API queries and manage Realm ID/Company ID parameters

**You must do**

- Sign up for an Intuit Developer account and enter organization/identity details
- Create your app in the Intuit Developer Portal and obtain the Client ID and Secret
- Maintain billing details if Intuit Developer Platform fees apply
- Perform the end-user OAuth consent flow to link QuickBooks companies
- Complete the self-assessment questionnaire and security review if distributing publicly

**Open questions**

- What are the exact pricing thresholds, fee amounts, and exemption criteria for the Intuit Developer Platform service fees mentioned in Section 5.1 of the terms? *(Uncertain)*
  > Section 5.1 mentions flat monthly and variable API usage fees, but the fee schedule and exemption criteria are not detailed in the scraped text.
- When will Intuit reopen general developer access to the QuickBooks Payroll API? *(Uncertain)*
  > Community responses confirm the Payroll API is closed to new applicants, but give no timeline for public reopening.

**Sources**

- [Intuit Developer](https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0)
- [Set up Quickbooks with Nango - Nango Docs](https://nango.dev/docs/api-integrations/quickbooks/how-to-register-your-own-quickbooks-api-oauth-app)
- [Learn about scopes · QuickBooks Online](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- [Connect RapidVerify with QuickBooks Online | Intuit](https://quickbooks.intuit.com/app/apps/appdetails/rapidverify/en-us)
- [Intuit Developer Terms of Service · QuickBooks Online](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- [How to add scopes for payroll to a production app?](https://help.developer.intuit.com/s/question/0D5TR00000aUBQ20AO/how-to-add-scopes-for-payroll-to-a-production-app)
- [QuickBooks App Store](https://quickbooks.intuit.com/app/apps/appdetails/verify_iq/en-us)
- [QuickBooks MCP Server for AI Agents | Composio](https://composio.dev/toolkits/quickbooks)
- [Managed OAuth apps | Composio](https://docs.composio.dev/toolkits/managed-auth)
- [https://developer.intuit.com/app/developer/homepage](https://developer.intuit.com/app/developer/homepage)
- [https://dashboard.composio.dev/login?utm_source=toolkits&utm_medium=hero&utm_campaign=toolkits-quickbooks&utm_content=%2Ftoolkits%2Fquickbooks](https://dashboard.composio.dev/login?utm_source=toolkits&utm_medium=hero&utm_campaign=toolkits-quickbooks&utm_content=%2Ftoolkits%2Fquickbooks)

**Last verified:** 2026-10-30, by agent.

*Generated by Clearance using gemini-3.8-flash.*
