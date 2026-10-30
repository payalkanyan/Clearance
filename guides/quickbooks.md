# QuickBooks

**QuickBooks, developer.intuit.com/app/developer/homepage**

**Verdict:** Developers can register an account and test immediately in sandbox mode, but public production distribution requires submitting a self-assessment questionnaire and potentially passing technical, security, and marketing reviews. *(Sourced)*
> "Before your Developer Application can be publicly distributed and in other instances as determined solely by Intuit you may be required to submit a" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Difficulty:** Hard
**Why:** Developers can register an account and test immediately in sandbox mode, but public production distribution requires submitting a self-assessment questionnaire and potentially passing technical, security, and marketing reviews. *(Sourced)*
**Hands-on time:** 15 to 30 minutes *(Inferred)*
**Waiting time:** Unknown *(Uncertain)*

**Composio status:** Toolkit available with a Composio managed OAuth app, so you can connect without registering your own. Bringing your own app is optional, for your name on the consent screen. *(Sourced)*
> "Composio provides a managed OAuth app for Quickbooks, so you sign in with your normal Quickbooks account and approve access." — [source](https://composio.dev/toolkits/quickbooks)

**Prerequisites**

- At https://developer.intuit.com/app/developer/homepage, a sign-in wall: you must log in before you can register an app. Fields visible: platform. *(Tested)*
  > [source](https://developer.intuit.com/app/developer/homepage)
  > observed by the agent at 2026-10-30T11:35:42Z, HTTP 200; matched sign in
- At https://dashboard.composio.dev/login?utm_source=toolkits&utm_medium=hero&utm_campaign=toolkits-quickbooks&utm_content=%2Ftoolkits%2Fquickbooks, a sign-in wall: you must log in before you can register an app. Fields visible: email, logo. *(Tested)*
  > [source](https://dashboard.composio.dev/login?utm_source=toolkits&utm_medium=hero&utm_campaign=toolkits-quickbooks&utm_content=%2Ftoolkits%2Fquickbooks)
  > observed by the agent at 2026-10-30T11:35:45Z, HTTP 200; matched signin, login, continue with google
- An Intuit Developer Account with accurate identity and domicile information. *(Sourced)*
  > "To enroll, you must create a Developer Account in the Portal by providing complete and accurate information" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- A valid payment method if platform service fees or subscription requirements apply to your integration tier. *(Sourced)*
  > "If applicable, valid and current payment method to facilitate financial transactions related to the Intuit Developer Platform." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Setup steps**

1. Navigate to the Intuit Developer Portal at https://developer.intuit.com/app/developer/homepage and sign up or log in. *(Inferred)*
   > Based on developer sign-in wall observations and the Intuit Developer homepage URL.
2. Navigate to the App Dashboard from the developer console and click to add a new app. *(Inferred)*
   > Standard app creation flow described in developer integration walkthroughs.
3. Select 'QuickBooks Online and Payments', provide your application name, and select the initial permissions. *(Inferred)*
   > App creation steps described in developer guides.
4. Open the app's settings and add your OAuth callback URL to the 'Redirect URIs' field (e.g., your Composio callback or custom server endpoint). *(Inferred)*
   > Required redirect URI configuration in developer settings.
5. Go to 'Keys and credentials' to view and copy your Client ID and Client Secret. *(Inferred)*
   > Location of client credentials in the Intuit developer portal.
6. If testing, go to My Hub > Sandbox and create a Sandbox test company to retrieve your test Company ID / Realm ID. *(Inferred)*
   > Standard practice for QuickBooks sandbox environment setup.
7. Paste your Client ID and Client Secret into Composio or your application configuration. *(Inferred)*
   > Standard credential handoff step when configuring a custom OAuth application.

**Scopes**

- com.intuit.quickbooks.accounting: Provides read and write access to QuickBooks Online Accounting API data. *(Sourced)*
  > "Grants access to the QuickBooks Online Accounting API, which focuses on accounting data." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- com.intuit.quickbooks.payment: Provides access to QuickBooks payments processing and bank account records. *(Sourced)*
  > "Grants access to the QuickBooks Payments API, which focuses on payments processing." — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)
- openid: Accesses OpenID Connect user identity details such as profile, email, phone, and address. *(Sourced)*
  > "Grants access to OpenID Connect features. Include one or more of the following capabilities:" — [source](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)

**Limits before approval**

- Sandbox environments and test data may only be used for testing and development, never production data. *(Sourced)*
  > "The Sandbox, and the data provided therein, must not be used for production purposes." — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- Platform access may be subject to variable API usage fees or flat monthly platform service fees. *(Sourced)*
  > "To use the Intuit Developer Platform, you may need to pay fees which may include a flat monthly fee and a variable API usage fee" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Approval process**

- Developers may need to submit a self-assessment questionnaire demonstrating policy compliance before moving to production. *(Sourced)*
  > "Before your Developer Application can be publicly distributed and in other instances as determined solely by Intuit you may be required to submit a" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- Publishing to Intuit marketing channels requires technical, security, legal compliance, and marketing reviews. *(Sourced)*
  > "To launch your Application using an Intuit Marketing Channel, further assessments and reviews may be required by Intuit initially, and periodically thereafter" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)
- Intuit reserves total discretion to approve, reject, or suspend developer applications. *(Sourced)*
  > "Intuit reserves the right to withhold, deny, suspend, or reject your Developer Application at its sole discretion" — [source](https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services)

**Likely blockers**

- Certain APIs like QuickBooks Payroll are closed to new developers and require getting onto an interest list. *(Sourced)*
  > "The payroll API is not currently open to new developers, but we can add you to our interest list" — [source](https://help.developer.intuit.com/s/question/0D5TR00000aUBQ20AO/how-to-add-scopes-for-payroll-to-a-production-app)
- Failure to complete security review questionnaires or satisfy data stewardship requirements. *(Inferred)*
  > Section 8.1 requires apps to satisfy third-party data privacy and security reviews.
- Incomplete business profile, missing terms of service or privacy policy URLs, or unverified contact details. *(Inferred)*
  > Inferred from developer portal enrollment rules and listing review requirements.
- Requires privacy policy or terms URLs *(Inferred)*
  > rubric modifier: noted as a blocker, it does not change the difficulty level

**Agent can do**

- Identify and format necessary OAuth scopes for the target QuickBooks APIs
- Provide code samples and integration instructions for OAuth 2.0 flow handling
- Monitor API response payloads and explain error codes

**You must do**

- Sign in to the Intuit Developer Portal and complete developer account registration
- Create the app in the developer console and obtain Client ID and Client Secret
- Set the valid redirect URIs in the Intuit app configuration
- Complete the self-assessment questionnaire and security compliance forms for production approval

**Open questions**

- What is the expected turnaround time for Intuit to review the production self-assessment questionnaire? *(Uncertain)*
  > The documentation does not provide standard SLAs or time estimates for application review.
- What specific tiers or thresholds trigger mandatory developer platform service fees? *(Uncertain)*
  > The terms state that monthly or variable API fees may apply, but exact fee schedules are not detailed on the pages provided.

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
