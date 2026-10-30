# Slack

**Slack, api.slack.com/developer-program/dashboard**

**Verdict:** Immediate for development workspace installs; up to 10 business days preliminary and 10 weeks functional review for public Slack Marketplace listing. *(Inferred)*
> Developers can create an app and install it to their development workspace immediately without review. Public listing in the Slack Marketplace requires passing an automated and manual multi-stage review.

**Difficulty:** Hard
**Why:** Immediate for development workspace installs; up to 10 business days preliminary and 10 weeks functional review for public Slack Marketplace listing. *(Inferred)*
**Hands-on time:** 15 to 30 minutes *(Inferred)*
**Waiting time:** Immediate to 10 weeks *(Inferred)*

**Composio status:** Toolkit available with a Composio managed OAuth app, so you can connect without registering your own. Bringing your own app is optional, for your name on the consent screen. *(Sourced)*
> "Composio provides a managed OAuth app for Slack, so you sign in with your normal Slack account and approve access." — [source](https://composio.dev/toolkits/slack)

**Prerequisites**

- At https://api.slack.com/developer-program/dashboard, a sign-in wall: you must log in before you can register an app. Fields visible: organization, platform. *(Tested)*
  > [source](https://api.slack.com/developer-program/dashboard)
  > observed by the agent at 2026-10-30T12:13:58Z, HTTP 200; matched sign in, signin
- At https://api.slack.com/apps, a sign-in wall: you must log in before you can register an app. *(Tested)*
  > [source](https://api.slack.com/apps)
  > observed by the agent at 2026-10-30T12:14:32Z, HTTP 200; matched sign in, signin
- A Slack account and access to a development workspace where the app will be built and tested. *(Inferred)*
  > Slack requires signing into a workspace to access app management and to install an undistributed app.
- For Marketplace review submission, your app must be installed on 10 or more active workspaces used in the past 28 days. *(Sourced)*
  > "Your app has been installed on 10 or more active workspaces and the service has been tested on those workspaces" — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)

**Setup steps**

1. Go to the Slack App Management console at https://api.slack.com/apps and sign in with your Slack account. *(Sourced)*
   > "Include both your app's client ID, which is found in the App Management page, and a comma-separated list of scopes" — [source](https://docs.slack.dev/authentication/installing-with-oauth)
2. Create a new app by choosing either 'From scratch' or using an App Manifest, give it an app name, and pick your development workspace. *(Inferred)*
   > Standard app creation flow in Slack App Management.
3. In the left sidebar under 'OAuth & Permissions', configure your HTTPS Redirect URL (must not include an anchor '#'). *(Sourced)*
   > "Alternatively, you can configure a Redirect URL in the App Management page under OAuth & Permissions. A Redirect URL must also use HTTPS." — [source](https://docs.slack.dev/authentication/installing-with-oauth)
4. Under 'OAuth & Permissions', add the required Bot Token Scopes and User Token Scopes needed for your integration. *(Sourced)*
   > "Bot scopes should be added as scope=<bot_scope>, and user scopes should be added as user_scope=<user_scope>." — [source](https://docs.slack.dev/authentication/installing-with-oauth)
5. Retrieve your Client ID and Client Secret from the App Management page for exchanging authorization codes via oauth.v2.access. *(Sourced)*
   > "curl -F code=1234 -F client_id=3336676.569200954261 -F client_secret=ABCDEFGH https://slack.com/api/oauth.v2.access" — [source](https://docs.slack.dev/authentication/installing-with-oauth)
6. Redirect users to https://slack.com/oauth/v2/authorize with your client_id, scopes, and redirect_uri to initiate installation. *(Sourced)*
   > "To request scopes, redirect Slack users to https://slack.com/oauth/v2/authorize." — [source](https://docs.slack.dev/authentication/installing-with-oauth)
7. If publishing publicly, test across 10 active workspaces and navigate to 'Submit to the Slack Marketplace' in your app configuration page. *(Sourced)*
   > "Your app submission (and subsequent updates to your app) happens from the Submit to the Slack Marketplace section of your app's configuration page." — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)

**Scopes**

- chat:write: Send messages as your Slack app. *(Sourced)*
  > "Send messages as your Slack app" — [source](https://docs.slack.dev/reference/scopes)
- channels:read: View basic information about public channels in a workspace. *(Sourced)*
  > "View basic information about public channels in a workspace" — [source](https://docs.slack.dev/reference/scopes)
- channels:history: View messages and other content in public channels that your Slack app has been added to. *(Sourced)*
  > "View messages and other content in public channels that your Slack app has been added to" — [source](https://docs.slack.dev/reference/scopes)
- commands: Add shortcuts and slash commands that people can use. *(Sourced)*
  > "Add shortcuts and slash commands that people can use" — [source](https://docs.slack.dev/reference/scopes)
- incoming-webhook: Post messages to specific channels in Slack. *(Sourced)*
  > "Post messages to specific channels in Slack" — [source](https://docs.slack.dev/reference/scopes)
- users:read: View people in a workspace. *(Sourced)*
  > "View people in a workspace" — [source](https://docs.slack.dev/reference/scopes)

**Limits before approval**

- Undistributed apps can only be installed on the workspace where they were created, unless configured for an Enterprise org that supports org-wide installs. *(Sourced)*
  > "Your app can only be installed on the workspace that owns it. Slack asks the user to sign in to that workspace" — [source](https://docs.slack.dev/authentication/installing-with-oauth)
- Apps must reach at least 10 active workspaces before they are eligible to submit for public Slack Marketplace review. *(Sourced)*
  > "Your app has been installed on 10 or more active workspaces and the service has been tested on those workspaces" — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)
- Web API calls are rate limited per method per workspace per app across four tiers (Tier 1: 1+/min, Tier 2: 20+/min, Tier 3: 50+/min, Tier 4: 100+/min). *(Sourced)*
  > "Broadly, you'll encounter limits like these, applied on a " per API method per workspace/team per app" basis." — [source](https://docs.slack.dev/apis/web-api/rate-limits)
- Message posting is limited to 1 message per second per channel, with short bursts allowed. *(Sourced)*
  > "In general, apps may post no more than one message per second per channel, whether a message is posted via chat.postMessage" — [source](https://docs.slack.dev/apis/web-api/rate-limits)
- Events API deliveries max out at 30,000 per workspace per app per 60 minutes. *(Sourced)*
  > "Event deliveries to your server via the Events API currently max out at 30,000 per workspace/team per app per 60 minutes." — [source](https://docs.slack.dev/apis/web-api/rate-limits)

**Approval process**

- Automated tests run during the submission process and detected issues must be resolved before manual submission. *(Sourced)*
  > "Before you can submit your app, we will run some automated tests on your app. Once you’ve fixed any issues we detect, you can submit" — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)
- Preliminary review takes up to 10 business days, reviewing listing details, links, documentation, and scope justifications. *(Sourced)*
  > "Currently, the preliminary part of the review takes up to 10 business days to receive feedback, while the functional review takes up to 10" — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)
- Functional review takes up to 10 weeks for new submissions and tests the end-to-end user experience, install/uninstall, and scope usage. *(Sourced)*
  > "Once your app enters this stage of the review, your submission will be assigned to a reviewer and you’ll receive feedback about your app’s" — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)
- Endpoints are checked for TLS and request signing verification, though Slack does not perform code reviews. *(Sourced)*
  > "Tests an app’s endpoints for TLS and request signing verification (used by apps to validate requests they receive are coming from Slack)." — [source](https://slack.com/blog/developers/slack-marketplace-review-process)
- Once approved and published to the Slack Marketplace, the live app configuration is locked and changes require resubmitting for review. *(Sourced)*
  > "Once your app is published in the Slack Marketplace, the live version of your app is locked." — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)

**Likely blockers**

- Not meeting the minimum requirement of 10 active workspace installations blocks submission to the Marketplace. *(Sourced)*
  > "apps that do not meet this requirement will be blocked from submitting to the Marketplace" — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)
- Requesting legacy, coded workflow, or high-privilege scopes such as admin.*, search:read, triggers:*, read, post, or client. *(Sourced)*
  > "you’ll also need to ensure that your app does not request legacy/restricted scopes, scopes that provide extensive access to workspace data, or coded workflow scopes" — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)
- Requesting scopes for future functionality rather than features actively available and testable in the current app build. *(Sourced)*
  > "Please do not submit your app with scopes for a feature that you plan to build at some point in future." — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)
- Failing to provide test account credentials (or sufficiently long free trials) for third-party or paid services required by the app. *(Sourced)*
  > "If a paid account is required for your service, you’ll need to share login credentials with us for an account with the required level" — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)
- Frequent bugs, low quality, or submitting in private beta before full end-to-end and uninstall testing is completed. *(Sourced)*
  > "If your app is submitted with bugs, poor user experience, or we repeatedly run into issues of low quality when reviewing, we will return it" — [source](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)

**Agent can do**

- Explain bot vs user scopes and provide appropriate scope lists for your integration.
- Generate OAuth authorize URLs with parameters like client_id, scopes, and redirect_uri.
- Format API requests for token exchange using oauth.v2.access.
- Draft app manifest YAML or JSON configurations for app setup.

**You must do**

- Log in to the Slack App Management console at https://api.slack.com/apps.
- Create the app and copy your Client ID and Client Secret.
- Configure your HTTPS Redirect URL and authorize test workspace installs.
- Fulfill the 10-active-workspace requirement and submit for Slack Marketplace review if distributing publicly.

**Open questions**

- Can an app be distributed to multiple external workspaces via direct install links without submitting to the Slack Marketplace, beyond initial test workspaces? *(Uncertain)*
  > Documentation discusses workspace installs on 10 active workspaces prior to Marketplace submission, but does not state the hard cap on direct link installs without Marketplace listing.

**Sources**

- [How to register your own Slack OAuth app - Nango Docs](https://nango.dev/docs/api-integrations/slack/how-to-register-your-own-slack-api-oauth-app)
- [Installing via OAuth authorization code flow | Slack Developer Docs](https://docs.slack.dev/authentication/installing-with-oauth)
- [Scopes | Slack Developer Docs](https://docs.slack.dev/reference/scopes)
- [Slack Marketplace review process | Slack Developer Docs](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide)
- [Rate limits | Slack Developer Docs](https://docs.slack.dev/apis/web-api/rate-limits)
- [FAQ: Slack’s Marketplace review process | Slack](https://slack.com/blog/developers/slack-marketplace-review-process)
- [Understand app permissions | Slack](https://slack.com/help/articles/115003461503-Understand-app-permissions)
- [Slack MCP Server for AI Agents | Composio](https://composio.dev/toolkits/slack)
- [Managed OAuth apps | Composio](https://docs.composio.dev/toolkits/managed-auth)
- [https://api.slack.com/developer-program/dashboard](https://api.slack.com/developer-program/dashboard)
- [https://api.slack.com/apps](https://api.slack.com/apps)

**Last verified:** 2026-10-30, by agent.

*Generated by Clearance using gemini-3.8-flash.*
