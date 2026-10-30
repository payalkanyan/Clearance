# Zoom

**Zoom, devforum.zoom.us**

**Verdict:** Private and beta apps require no review and can be used immediately within an account, but public and unlisted apps require a formal multi-stage review covering submission completeness, branding, functionality, usability, compliance, and security testing against OWASP Top 10 risks. *(Sourced)*
> "Private and beta apps do not require review." — [source](https://developers.zoom.us/docs/distribute/app-review-process)

**Difficulty:** Hard
**Why:** Ongoing monitoring: Zoom continuously monitors published apps and may request remediation or suspend apps that pose significant risks. *(Sourced)*
**Hands-on time:** 15 to 30 minutes *(Inferred)*
**Waiting time:** Unknown *(Sourced)*

**Composio status:** Toolkit available with a Composio managed OAuth app, so you can connect without registering your own. Bringing your own app is optional, for your name on the consent screen. *(Sourced)*
> "Composio provides a managed OAuth app for Zoom, so you sign in with your normal Zoom account and approve access." — [source](https://composio.dev/toolkits/zoom)

**Prerequisites**

- Account administrator role or role permissions granting 'View' and 'Edit' for 'Zoom for developers' in the Zoom web portal under User Management > Roles > Role Settings > Advanced Features. *(Sourced)*
  > "In the Zoom web portal, the administrator must go to User Management > Roles > Role Settings > Advanced Features and select the View" — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-overview)
- An account admin or user with Marketplace permissions must pre-approve the app to enable it for end-users. *(Sourced)*
  > "To enable apps for end-users, an account admin, or user with Marketplace permissions for their Zoom Account, must pre-approve the app." — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-overview)
- For public or unlisted marketplace apps, comprehensive technical design documentation outlining architecture, security controls, and data handling is required. *(Sourced)*
  > "As part of the app submission process, all developers must complete the Technical Design section of the build flow." — [source](https://developers.zoom.us/docs/distribute/app-review-process)

**Setup steps**

1. Log in to the Zoom Marketplace and create a new application using the build flow. *(Sourced)*
   > "Create a new application in the Zoom Marketplace." — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-overview)
2. Configure basic information and set your OAuth Redirect URL (or loopback URI like http://127.0.0.1:port/callback for PKCE/native clients) in your Marketplace app configuration. *(Inferred)*
   > Derived from the Zoom OAuth redirect URI instructions and loopback URI specifications in the OAuth documentation.
3. If building a native or public client without a backend secret, navigate to App Credentials under Basic Information and toggle 'Use Public Client OAuth' to on. *(Inferred)*
   > "Open your app and navigate to App Credentials under Basic Information. Toggle Use Public Client OAuth to on." — [source](https://developers.zoom.us/docs/integrations/oauth)
   > downgraded from Sourced on 2026-10-30T12:06:54Z: quote does not appear in the cited page; its first 8 words do, so the rest looks paraphrased or stitched together
4. Navigate to Scopes, click 'Add Scopes', and select the granular scopes required for your integration. *(Inferred)*
   > "Under Scopes, click Add Scopes. Select the granular scopes you'd like to use in the app." — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-overview)
   > downgraded from Sourced on 2026-10-30T12:06:54Z: quote does not appear in the cited page
5. Mark non-essential granular scopes as 'Optional' so that users can authorize minimal permissions initially. *(Sourced)*
   > "In that list, you can mark a scope Optional. Scopes not marked as optional will be required when using the basic authorization query." — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-overview)
6. Copy your Client ID and Client Secret from App Credentials (and paste them into your integration platform or Composio custom auth config if applicable). *(Inferred)*
   > Standard procedure for confidential OAuth clients to obtain credentials from the App Credentials screen.
7. Test your app locally by going to the Local Test page and selecting 'Add App Now' to obtain user authorization within your account. *(Sourced)*
   > "To do this, navigate to the Local Test page, and choose Add App Now." — [source](https://developers.zoom.us/docs/integrations/oauth)
8. If publishing publicly or unlisted, complete the submission forms (including technical design, branding, and compliance) and submit for App Marketplace review. *(Inferred)*
   > Inferred from the review submission instructions detailed in the app review documentation.

**Scopes**

- meeting:read:list_meetings: View user meetings (granular scope). *(Sourced)*
  > "List meetings | meeting:read:list_meetings" — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-granular)
- meeting:write:meeting: Create and manage meetings. *(Sourced)*
  > "Create a meeting | meeting:write:meeting" — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-granular)
- cloud_recording:read:list_user_recordings: View and list cloud recordings. *(Sourced)*
  > "List all recordings | cloud_recording:read:list_user_recordings" — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-granular)
- chat:read: View chat message and shared space information. *(Sourced)*
  > "View Chat Message Info" — [source](https://developers.zoom.us/docs/integrations/oauth-scopes)
- chat:write: Manage chat messages, channels, and spaces. *(Sourced)*
  > "Manage Chat Message Info" — [source](https://developers.zoom.us/docs/integrations/oauth-scopes)
- report:read:meeting:admin: Access meeting detail and activity reports. *(Sourced)*
  > "Get meeting detail reports | report:read:meeting:admin" — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-granular)

**Limits before approval**

- Private and beta apps are exempt from marketplace review and can be shared and used internally without submitting for review. *(Sourced)*
  > "Private and beta apps do not require review." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
- Access tokens expire after 1 hour (3600 seconds) and must be refreshed. *(Sourced)*
  > "Access tokens expire after one hour. After your access token expires, you can follow the refresh flow to get a new one." — [source](https://developers.zoom.us/docs/integrations/oauth)
- Refresh tokens expire after 90 days, requiring users to re-authenticate if inactive. *(Sourced)*
  > "Refresh tokens expire after 90 days. You should always use the latest refresh token for the next refresh request." — [source](https://developers.zoom.us/docs/integrations/oauth)
- Non-admin end-users cannot install or use apps until an account admin pre-approves the app. *(Sourced)*
  > "To enable apps for end-users, an account admin, or user with Marketplace permissions for their Zoom Account, must pre-approve the app." — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-overview)
- Production apps must implement a deauthorization notification endpoint URL to handle user data deletion upon app uninstall. *(Sourced)*
  > "The request goes to the deauthorization notification endpoint URL you specified on the App Listing page." — [source](https://developers.zoom.us/docs/integrations/oauth)

**Approval process**

- Submission completeness & branding review: Zoom verifies minimal submission criteria, metadata, technical design documentation, and adherence to Zoom branding guidelines. *(Sourced)*
  > "We verify that your app meets the minimal criteria required to be accepted into our review process." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
- Functionality & usability review: The review team tests installation, uninstallation, configuration settings, user sign-up, and real data flow. *(Sourced)*
  > "We review your app's functionality and confirm that it works as you described." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
- Scope evaluation: The Marketplace Security Review Team verifies that the app only requests the minimum necessary OAuth scopes required for its functionality. *(Sourced)*
  > "The Marketplace Security Review Team verifies that the app only requests the minimum necessary OAuth scopes required for its functionality." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
- Security testing: Apps undergo automated web scanning, least-privilege verification, library vulnerability checks, and manual assessments against OWASP Top 10 risks. *(Inferred)*
  > "Apps are tested against the OWASP Top 10 risks and undergo a variety of assessments, including: Verification of least-privilege access. Web application security scanning." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
  > downgraded from Sourced on 2026-10-30T12:06:54Z: quote does not appear in the cited page; its first 8 words do, so the rest looks paraphrased or stitched together
- Remediation & re-submission: Zoom provides a report explaining reasons for rejection and action items to fix before resubmitting. *(Sourced)*
  > "We provide a report explaining the reasons we did not accept the app and action items you can complete to remediate the issues." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
- Ongoing monitoring: Zoom continuously monitors published apps and may request remediation or suspend apps that pose significant risks. *(Sourced)*
  > "We monitor applications that have passed app review and been published to the App Marketplace to ensure continued compliance with our guidelines." — [source](https://developers.zoom.us/docs/distribute/app-review-process)

**Likely blockers**

- Requesting excessive or unjustified scopes beyond the minimal requirements of the integration. *(Sourced)*
  > "The Marketplace Security Review Team verifies that the app only requests the minimum necessary OAuth scopes required for its functionality." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
- Security vulnerabilities or failing OWASP Top 10 assessments during technical security scanning. *(Inferred)*
  > "Apps are tested against the OWASP Top 10 risks and undergo a variety of assessments, including: Verification of least-privilege access. Web application security scanning." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
  > downgraded from Sourced on 2026-10-30T12:06:54Z: quote does not appear in the cited page; its first 8 words do, so the rest looks paraphrased or stitched together
- Presenting ads to users or collecting user data for marketing purposes, which violates usability policies. *(Sourced)*
  > "Your app should not present advertising to Zoom users or collect user information for marketing purposes." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
- Incomplete technical design documentation or unclear test plans and listing descriptions. *(Sourced)*
  > "Apps with poorly described scopes, confusing UI, or unclear listing information may require a lengthy review process." — [source](https://developers.zoom.us/docs/distribute/app-review-process)
- Violating Zoom branding guidelines or intellectual property rules in the app name, description, or assets. *(Inferred)*
  > "Zoom reserves the right to remove or require a revision to any content, in whole or part, including an app name, that violates: Zoom's" — [source](https://developers.zoom.us/docs/distribute/app-review-process)
  > downgraded from Sourced on 2026-10-30T12:06:54Z: quote does not appear in the cited page; its first 8 words do, so the rest looks paraphrased or stitched together
- Missing account administrator permissions or pre-approval in the Zoom organization. *(Sourced)*
  > "To enable apps for end-users, an account admin, or user with Marketplace permissions for their Zoom Account, must pre-approve the app." — [source](https://developers.zoom.us/docs/integrations/oauth-scopes-overview)

**Agent can do**

- Read Zoom API and OAuth specification documentation
- Identify exact granular scopes needed for specific API endpoints
- Generate code for OAuth token exchanges and PKCE challenge generation
- Draft technical architecture descriptions and compliance notes for review

**You must do**

- Sign in to the Zoom Marketplace as an account administrator or authorized developer
- Create the app in the Marketplace build flow and copy the Client ID and Secret
- Configure redirect URIs and deauthorization webhooks
- Authorize the app during local testing or production OAuth consent
- Submit the app for Marketplace review and remediate any reported security findings

**Open questions**

- What is the typical SLA or average duration in business days for the Zoom Marketplace team to complete the security review? *(Uncertain)*
  > The documentation states review time varies by quality, feature count, and documentation clarity, but does not specify a turnaround time.
- Does Zoom offer an isolated developer sandbox environment for public OAuth testing separate from production customer accounts? *(Uncertain)*
  > The supplied pages mention testing via 'Local Test' with 'Add App Now' on regular Zoom accounts, but do not detail separate sandbox accounts.

**Sources**

- [Server-to-Server OAuth app permissions and scopes - API and Webhooks / Meetings - Zoom Developer Forum](https://devforum.zoom.us/t/server-to-server-oauth-app-permissions-and-scopes/92331)
- [Integrations - OAuth scopes - Integrations - Zoom Developer Docs](https://developers.zoom.us/docs/integrations/oauth-scopes-overview)
- [Integrations - Classic scopes - Integrations - Zoom Developer Docs](https://developers.zoom.us/docs/integrations/oauth-scopes)
- [Granular scopes - Integrations - Zoom Developer Docs](https://developers.zoom.us/docs/integrations/oauth-scopes-granular)
- [How to add / change scopes in an OAuth app I created? - API and Webhooks - Zoom Developer Forum](https://devforum.zoom.us/t/how-to-add-change-scopes-in-an-oauth-app-i-created/78166)
- [OAuth 2.0 - Integrations - Zoom Developer Docs](https://developers.zoom.us/docs/integrations/oauth)
- [App Review Process - Distribute - Zoom Developer Docs](https://developers.zoom.us/docs/distribute/app-review-process)
- [Zoom MCP Server | Composio](https://composio.dev/toolkits/zoom)
- [Managed OAuth apps | Composio](https://docs.composio.dev/toolkits/managed-auth)

**Last verified:** 2026-10-30, by agent.

*Generated by Clearance using gemini-3.8-flash.*
