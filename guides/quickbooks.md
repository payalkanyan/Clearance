# QuickBooks

**QuickBooks, developer.intuit.com/app/developer/homepage**

**Verdict:** App registration and sandbox credential generation are instant upon creating an Intuit Developer account, but moving to production or public distribution requires submitting a self-assessment questionnaire and undergoing technical, security, and marketing reviews. *(Sourced)*
> "Before your Developer Application can be publicly distributed and in other instances as determined solely by Intuit you may be required to submit a" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Difficulty:** Hard
**Why:** App registration and sandbox credential generation are instant upon creating an Intuit Developer account, but moving to production or public distribution requires submitting a self-assessment questionnaire and undergoing technical, security, and marketing reviews. *(Sourced)*
**Hands-on time:** 10 to 20 minutes *(Inferred)*
**Waiting time:** Unknown *(Uncertain)*

**Composio status:** Toolkit available with a Composio managed OAuth app, so you can connect without registering your own. Bringing your own app is optional, for your name on the consent screen. *(Sourced)*
> "Composio provides a managed OAuth app for Quickbooks, so you sign in with your normal Quickbooks account and approve access." — [source](https://composio.dev/toolkits/quickbooks)

**Prerequisites**

- At https://developer.intuit.com/app/developer/homepage, a sign-in wall: you must log in before you can register an app. Fields visible: platform. *(Tested)*
  > [source](https://developer.intuit.com/app/developer/homepage)
  > observed by the agent at 2026-10-30T11:51:48Z, HTTP 200; matched sign in
- An Intuit Developer account. *(Sourced)*
  > "Create an Intuit Developer account or sign on to your existing account." — [source](https://help.developer.intuit.com/s/article/Configuring-the-Oauth-2-0-Playground-for-QuickBooks-Online)
- Basic company information and a workspace name during account registration. *(Sourced)*
  > "You'll be asked to enter some basic company information and a name for your workspace." — [source](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app)
- Legal identity details, domicile address, valid email address, and valid payment information if applicable. *(Sourced)*
  > "Your legal name whether using the Platform as an individual or entity." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Setup steps**

1. Sign in to your Intuit Developer account at https://developer.intuit.com/dashboard. *(Sourced)*
   > "Sign in to your developer account." — [source](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app)
2. Navigate to My Hub > App dashboard from the upper-right corner toolbar. *(Sourced)*
   > "Select My Hub > App dashboard from the upper-right corner of the toolbar." — [source](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app)
3. Select the app card with a '+' to create a new application. *(Sourced)*
   > "Select the app card with a + to create a new app." — [source](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app)
4. Follow the on-screen creation flow and configure scopes (such as accounting or payments) based on the data your app needs. *(Sourced)*
   > "When you create apps, you'll pick your app's scopes. Scopes limit the type of data your app can access." — [source](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app)
5. In your app's settings/keys section, add your OAuth 2.0 Redirect URI (for example, the OAuth2 Playground URL or your callback URL). *(Sourced)*
   > "navigating to your app -> keys section and setting the Redirect URI" — [source](https://help.developer.intuit.com/s/article/Configuring-the-Oauth-2-0-Playground-for-QuickBooks-Online)
6. Retrieve your Client ID and Client Secret from your app dashboard to use for OAuth 2.0 authentication. *(Sourced)*
   > "Use your credentials (i.e., Client ID and Client Secret) to connect your app to OAuth 2.0." — [source](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app)
7. If connecting via custom credentials in Composio, enter the Client ID and Client Secret into your Composio app settings. *(Inferred)*
   > Standard integration step when bringing your own OAuth credentials into Composio.

**Scopes**

- com.intuit.quickbooks.accounting: Grants access to the QuickBooks Online Accounting API, focusing on accounting data. *(Sourced)*
  > "Grants access to the QuickBooks Online Accounting API, which focuses on accounting data." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- com.intuit.quickbooks.payment: Grants access to the QuickBooks Payments API, focusing on payment processing. *(Sourced)*
  > "Grants access to the QuickBooks Payments API, which focuses on payments processing." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- openid: Grants access to OpenID Connect features, including sub-capabilities profile, email, phone, and address. *(Sourced)*
  > "Grants access to OpenID Connect features. Include one or more of the following capabilities:" — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- GraphQL scopes: Dedicated scopes including project-management.project, indirect-tax.tax-calculation.quickbooks, and app-foundations.custom-field-definitions. *(Sourced)*
  > "Grants access to read and write Project data." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)

**Limits before approval**

- Apps in development are tested using sandbox companies with sample data and cannot access live production data until approved. *(Sourced)*
  > "The Sandbox, and the data provided therein, must not be used for production purposes." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- QuickBooks OAuth access tokens expire after 1 hour. *(Inferred)*
  > Mentioned in community integration guides and developer documentation regarding token refreshes.
- Payroll API scopes cannot be used by new developers as the Payroll API is currently closed to new signups. *(Sourced)*
  > "The payroll API is not currently open to new developers, but we can add you to our interest list" — [source](https://help.developer.intuit.com/s/question/0D5TR00000aUBQ20AO/how-to-add-scopes-for-payroll-to-a-production-app)

**Approval process**

- Developers must submit a self-assessment questionnaire confirming compliance with Intuit terms prior to entering production or public distribution. *(Sourced)*
  > "Before your Developer Application can be publicly distributed and in other instances as determined solely by Intuit you may be required to submit a" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- A security review focusing on data privacy, stewardship policies, and legal compliance, potentially conducted by Intuit's designated third party. *(Sourced)*
  > "Our security review focuses on your data privacy and stewardship policies to ensure that you are abiding by Applicable Law, this Agreement, Intuit Policies." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- A technical review evaluating adherence to technical and design criteria specified on the platform. *(Sourced)*
  > "Our technical review focuses on your adherence to technical usage standards as your Developer Application must comply with specified technical and design criteria as" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- A marketing review verifying compliance with Intuit branding, trademark, and logo policies. *(Sourced)*
  > "Our marketing review evaluates your compliance with our marketing standards as you must comply with Intuit's Policies related to marketing, branding, trademark and logo use." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Likely blockers**

- Geographic restriction: The Intuit App Partner Program is restricted to partners based in the US, UK, Australia, and Canada (excluding Quebec). *(Sourced)*
  > "The Intuit App Partner Program is available for partners based in the US, UK, Australia, and Canada (excluding Quebec)." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- Closed APIs: The Payroll API is currently not open to new developers, causing authorization failures and 403 errors if payroll scopes are requested. *(Sourced)*
  > "The payroll API is not currently open to new developers, but we can add you to our interest list" — [source](https://help.developer.intuit.com/s/question/0D5TR00000aUBQ20AO/how-to-add-scopes-for-payroll-to-a-production-app)
- Platform service fees: Usage of the platform may require recurring monthly or API usage fees. *(Sourced)*
  > "To use the Intuit Developer Platform, you may need to pay fees which may include a flat monthly fee and a variable API usage fee" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- Failure to cooperate with or pass third-party security assessments and privacy compliance audits. *(Sourced)*
  > "You may be required to work with Intuit's designated third party to conduct these reviews and you agree to cooperate with and timely respond" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Agent can do**

- Navigate developer documentation to explain OAuth flow, API entities, and scopes
- Prepare sample cURL requests and API payload definitions
- Guide developers through the step-by-step dashboard app creation procedure

**You must do**

- Sign in to the Intuit Developer Portal with your credentials
- Create the app in the dashboard and assign permissions
- Enter and save the OAuth redirect URIs
- Copy and secure the Client ID and Client Secret
- Complete and submit the self-assessment questionnaire and undergo security reviews for production release

**Open questions**

- Does an internal-only custom app connecting to a developer's own production QuickBooks account require the same self-assessment and security review as an App Store app? *(Uncertain)*
  > Documentation mentions app review is needed before public distribution and entering production, but exact criteria for private integrations are ambiguous in terms.
- What is the typical review duration for Intuit's self-assessment questionnaire and third-party security audits? *(Uncertain)*
  > Review turnaround timeframes are not documented in the provided pages.

**Sources**

- [Set up Quickbooks with Nango - Nango Docs](https://nango.dev/docs/api-integrations/quickbooks/how-to-register-your-own-quickbooks-api-oauth-app)
- [Learn about scopes · QuickBooks Online](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- [Connect RapidVerify with QuickBooks Online | Intuit](https://quickbooks.intuit.com/app/apps/appdetails/rapidverify/en-us)
- [Intuit Developer Terms of Service · QuickBooks Online](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- [How to add scopes for payroll to a production app?](https://help.developer.intuit.com/s/question/0D5TR00000aUBQ20AO/how-to-add-scopes-for-payroll-to-a-production-app)
- [Configuring the Oauth 2.0 Playground for QuickBooks Online](https://help.developer.intuit.com/s/article/Configuring-the-Oauth-2-0-Playground-for-QuickBooks-Online)
- [Create and start developing your app · QuickBooks Online](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app)
- [QuickBooks MCP Server for AI Agents | Composio](https://composio.dev/toolkits/quickbooks)
- [Managed OAuth apps | Composio](https://docs.composio.dev/toolkits/managed-auth)
- [https://developer.intuit.com/app/developer/homepage](https://developer.intuit.com/app/developer/homepage)

**Last verified:** 2026-10-30, by agent.

*Generated by Clearance using gemini-3.8-flash.*
