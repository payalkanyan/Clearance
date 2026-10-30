# Notion

**Notion, www.notion.so/signup**

**Verdict:** Creating a public connection is straightforward in the Developer portal, but submitting the connection for review is required before the authorization URL populates. *(Inferred)*
> Based on the public connection auth flow documentation stating the authorization URL field populates after submission for review.

**Difficulty:** Hard
**Why:** Creating a public connection is straightforward in the Developer portal, but submitting the connection for review is required before the authorization URL populates. *(Inferred)*
**Hands-on time:** 10 to 15 minutes *(Inferred)*
**Waiting time:** Unknown *(Uncertain)*

**Composio status:** Toolkit available with a Composio managed OAuth app, so you can connect without registering your own. Bringing your own app is optional, for your name on the consent screen. *(Sourced)*
> "Composio provides a managed OAuth app for Notion, so you sign in with your normal Notion account and approve access." — [source](https://composio.dev/toolkits/notion)

**Prerequisites**

- At https://app.notion.com/developers/connections, an application form is shown, behind a sign-in or an access request. Fields visible: organization, email, privacy policy. *(Tested)*
  > [source](https://app.notion.com/developers/connections)
  > observed by the agent at 2026-10-30T11:58:39Z, HTTP 200; matched log in, login
- A Notion account with Workspace Owner permissions in the workspace where the connection is managed. *(Sourced)*
  > "You are required to be a workspace owner to create a connection." — [source](https://developers.notion.com/guides/get-started/authorization)

**Setup steps**

1. At https://www.notion.so/signup, the app registration form is open: its fields were visible without signing in. Fields visible: organization, email, privacy policy. *(Tested)*
   > [source](https://www.notion.so/signup)
   > observed by the agent at 2026-10-30T11:58:27Z, HTTP 200
2. Navigate to the Notion Developer portal at https://app.notion.com/developers/connections. *(Sourced)*
   > "Navigate to the Developer portal and create a new public connection." — [source](https://developers.notion.com/guides/get-started/authorization)
3. Start creating a new public connection and set the installation scope to either 'Any workspace' or 'Selected workspaces only' (this cannot be changed after creation). *(Sourced)*
   > "This can’t be changed after creation." — [source](https://developers.notion.com/guides/get-started/authorization)
4. Under the OAuth configuration section, enter your redirect URI(s). If integrating via Composio, provide your Composio callback URI. *(Sourced)*
   > "Fill out the form with your connection details, including your redirect URI(s) under the OAuth configuration section and the connection’s installation scope" — [source](https://developers.notion.com/guides/get-started/authorization)
5. Optionally, enter a Notion page URL in the 'Notion URL for optional template' input if you want users to duplicate a template page during authorization. *(Sourced)*
   > "add the URL of the Notion page you selected to the Notion URL for optional template input." — [source](https://developers.notion.com/guides/get-started/authorization)
6. Submit the public connection for review to populate the Authorization URL field. *(Sourced)*
   > "The Authorization URL field populates after a public connection is submitted for review" — [source](https://developers.notion.com/guides/get-started/authorization)
7. Open the Configuration tab, copy your Client ID and Client Secret, and store them securely or input them into Composio. *(Sourced)*
   > "access the connection’s secrets in the Configuration tab. Similarly to the internal connections, these values should be protected and should never be included in" — [source](https://developers.notion.com/guides/get-started/authorization)

**Scopes**

- Standard public OAuth connections do not use a scope parameter in the authorization URL; permissions are granted dynamically when the user selects pages to share via Notion's page picker. *(Inferred)*
  > Notion's public connection authorization URL specification lists only client_id, redirect_uri, response_type, owner, and state, with access governed by the user's selected pages.
- Admin API connections use resource and capability pairs (such as workspace:read or workflows:write) to govern access for organization bot tokens. *(Sourced)*
  > "When you create an organization bot token, you assign scopes that control which resources the token can access and which actions it can take." — [source](https://developers.notion.com/reference/admin/scopes)
- The user and permission-group Admin API scopes require an eligible Enterprise organization plan. *(Sourced)*
  > "The user and permission-group scopes are available only to eligible Enterprise organizations. If these scopes don’t appear in the organization console, contact your Notion representative." — [source](https://developers.notion.com/reference/admin/scopes)

**Limits before approval**

- The Authorization URL field is only populated after the public connection is submitted for review. *(Sourced)*
  > "The Authorization URL field populates after a public connection is submitted for review" — [source](https://developers.notion.com/guides/get-started/authorization)
- Users can only share pages and databases with the connection if they have full access to those resources. *(Sourced)*
  > "The page picker only displays pages or databases to which a user has full access, because a user needs full access to a resource" — [source](https://developers.notion.com/guides/get-started/authorization)

**Approval process**

- The public connection configuration must be submitted for review before the public authorization URL becomes available. *(Sourced)*
  > "The Authorization URL field populates after a public connection is submitted for review" — [source](https://developers.notion.com/guides/get-started/authorization)
- Marketplace listing details such as descriptions, categories, and images are managed separately through the Listings section. *(Inferred)*
  > Documentation distinguishes technical OAuth public connection setup from public Marketplace listing management.

**Likely blockers**

- Only workspace owners have permission to create connections in the Developer portal. *(Sourced)*
  > "You are required to be a workspace owner to create a connection." — [source](https://developers.notion.com/guides/get-started/authorization)
- The connection's installation scope ('Any workspace' vs 'Selected workspaces only') is fixed at creation time and cannot be changed later. *(Sourced)*
  > "This can’t be changed after creation." — [source](https://developers.notion.com/guides/get-started/authorization)
- End users cannot share pages or databases with the connection if they lack full access permissions to those resources. *(Sourced)*
  > "The page picker only displays pages or databases to which a user has full access, because a user needs full access to a resource" — [source](https://developers.notion.com/guides/get-started/authorization)
- Enterprise-specific Admin API scopes cannot be used without an eligible Enterprise plan. *(Sourced)*
  > "The user and permission-group scopes are available only to eligible Enterprise organizations. If these scopes don’t appear in the organization console, contact your Notion representative." — [source](https://developers.notion.com/reference/admin/scopes)
- Requires privacy policy or terms URLs *(Inferred)*
  > rubric modifier: noted as a blocker, it does not change the difficulty level

**Agent can do**

- Explain Notion OAuth parameters, redirect requirements, and token exchange requests.
- Format client credentials and redirect callback URIs for your integration configuration.

**You must do**

- Sign in to the Notion Developer portal as a Workspace Owner.
- Fill in the public connection details and submit the application for review.
- Copy the Client ID and Client Secret and store them in your secure environment or Composio.

**Open questions**

- How long does the review process take after submitting a public connection? *(Uncertain)*
  > The documentation mentions that the authorization URL populates upon review submission, but does not provide review duration or criteria.
- Can a public connection be tested by external users before the review process is approved? *(Uncertain)*
  > The docs explain how the authorization URL generates upon submission, but do not specify whether development/sandbox test modes exist prior to review.

**Sources**

- [How to register your own Notion OAuth app - Nango Docs](https://nango.dev/docs/api-integrations/notion/how-to-register-your-own-notion-api-oauth-app)
- [OAuth - Notion Docs](https://developers.notion.com/workers/guides/oauth)
- [Authorization - Notion Docs](https://developers.notion.com/guides/get-started/authorization)
- [Scopes - Notion Docs](https://developers.notion.com/reference/admin/scopes)
- [Verify knowledge your teammates can trust](https://www.notion.com/help/guides/verify-knowledge-your-teammates-can-trust-with-page-verification)
- [Sharing & permissions settings in Notion | Notion Help](https://www.notion.com/help/sharing-and-permissions)
- [Product Limit and Quota Policy Template by RunBook | Notion Marketplace](https://www.notion.com/templates/product-limit-and-quota-policy?srsltid=AYCX9vKQ6fDfYSLxQFt98WbztwIgCEQWUYJYsIJq_78yHOZ-YMCUS442)
- [Notion MCP Server | Composio](https://composio.dev/toolkits/notion)
- [Managed OAuth apps | Composio](https://docs.composio.dev/toolkits/managed-auth)
- [https://app.notion.com/developers/connections](https://app.notion.com/developers/connections)
- [https://www.notion.so/signup](https://www.notion.so/signup)

**Last verified:** 2026-10-30, by agent.

*Generated by Clearance using gemini-3.8-flash.*
