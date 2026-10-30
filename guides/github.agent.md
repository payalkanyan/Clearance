# GitHub

**GitHub, github.com/settings/applications**

**Verdict:** Self-service app registration with immediate access to client credentials and API scopes; review is only required if applying for GitHub Marketplace publisher verification. *(Inferred)*
> Page 2 describes an immediate registration form for OAuth apps, while Page 7 states reviews only apply to Marketplace publisher verification.

**Difficulty:** Easy
**Why:** nothing matched a harder level: self-serve with no review found *(Inferred)*
**Hands-on time:** 5 to 15 minutes *(Inferred)*
**Waiting time:** Immediate (None for standard OAuth apps; Unknown for Marketplace publisher verification) *(Inferred)*

**Composio status:** Toolkit available with a Composio managed OAuth app, so you can connect without registering your own. Bringing your own app is optional, for your name on the consent screen. *(Sourced)*
> "Composio provides a managed OAuth app for GitHub, so you sign in with your normal GitHub account and approve access." — [source](https://composio.dev/toolkits/github)

**Prerequisites**

- At https://github.com/settings/applications, a sign-in wall: you must log in before you can register an app. Fields visible: email. *(Tested)*
  > [source](https://github.com/settings/applications)
  > observed by the agent at 2026-10-30T10:28:19Z, HTTP 200; matched sign in, login, password, continue with google
- A personal GitHub account or administrative access to a GitHub organization. *(Sourced)*
  > "You can create and register an OAuth app under your personal account or under any organization you have administrative access to." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
- A publicly shareable homepage URL and authorization callback URL. *(Sourced)*
  > "In "Homepage URL", type the full URL to your app's website." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)

**Setup steps**

1. In the upper-right corner of any page on GitHub, click your profile picture, then click Settings. *(Sourced)*
   > "In the upper-right corner of any page on GitHub, click your profile picture, then click Settings." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
2. In the left sidebar, click Developer settings. *(Sourced)*
   > "In the left sidebar, click Developer settings." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
3. In the left sidebar, click OAuth apps. *(Sourced)*
   > "In the left sidebar, click OAuth apps." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
4. Click New OAuth App (or 'Register a new application' if you have not created an app before). *(Sourced)*
   > "Click New OAuth App. Note If you haven't created an app before, this button will say, Register a new application." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
5. In 'Application name', enter the name of your app (using only public information). *(Sourced)*
   > "In "Application name", type the name of your app." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
6. In 'Homepage URL', enter the full website URL for your app. *(Sourced)*
   > "In "Homepage URL", type the full URL to your app's website." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
7. Optionally, in 'Application description', enter a description visible to users. *(Sourced)*
   > "Optionally, in "Application description", type a description of your app that users will see." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
8. In 'Authorization callback URL', type your app's callback URL (up to 10 URLs supported). *(Sourced)*
   > "In "Authorization callback URL", type the callback URL of your app. You can enter up to 10 callback URLs." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
9. If using device flow, check 'Enable Device Flow'. *(Sourced)*
   > "If your OAuth app will use the device flow to identify and authorize users, click Enable Device Flow." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
10. Configure 'Expire user access tokens' (enabled by default; uncheck only if code lacks expiring token support). *(Sourced)*
    > "Expire user access tokens is enabled by default. If your app's authentication code hasn't been updated to support short-lived tokens, uncheck the box" — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
11. Click Register application to finish creating the OAuth app. *(Sourced)*
    > "Click Register application." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)

**Scopes**

- repo: Grants full access to public and private repositories and organization-owned resources. *(Sourced)*
  > "Grants full access to public and private repositories including read and write access to code, commit statuses, repository invitations, collaborators, deployment statuses, and repository webhooks." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)
- public_repo: Limits access to public repositories only, including code, issues, statuses, and starring. *(Sourced)*
  > "Limits access to public repositories. That includes read/write access to code, commit statuses, repository projects, collaborators, and deployment statuses for public repositories and organizations." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)
- user: Grants read/write access to profile information, including user:email and user:follow. *(Sourced)*
  > "Grants read/write access to profile info only. Note that this scope includes user:email and user:follow." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)
- read:user / user:email: Grants read-only access to profile data or email addresses without write permissions. *(Sourced)*
  > "Grants access to read a user's profile data." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)
- admin:org: Grants full management of an organization, including teams, projects, and memberships. *(Sourced)*
  > "Fully manage the organization and its teams, projects, and memberships." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)
- offline_access: Requests an expiring access token and a refresh token even if not configured globally. *(Sourced)*
  > "Requests an expiring access token and a refresh token, even if your OAuth app is not configured to use expiring tokens." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)

**Limits before approval**

- A user or organization can own up to 100 OAuth apps. *(Sourced)*
  > "A user or organization can own up to 100 OAuth apps." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
- OAuth apps can register a maximum of 10 callback URLs. *(Sourced)*
  > "You can enter up to 10 callback URLs. To add additional callback URLs, click Add callback URL." — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
- Users can edit or reduce token scopes during authorization or after the flow is completed. *(Sourced)*
  > "However, users can edit their scopes, effectively granting your application less access than you originally requested. Also, users can edit token scopes after the" — [source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)

**Approval process**

- Standard OAuth apps do not require review or approval by GitHub before use. *(Inferred)*
  > Page 2 describes the complete registration flow without any review stage before credentials can be used.
- If listing on GitHub Marketplace with paid plans or a badge, your organization must complete publisher verification. *(Sourced)*
  > "To offer paid plans for your app or to include a marketplace badge in your app listing, you must complete the publisher verification process" — [source](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/applying-for-publisher-verification-for-your-organization)
- Publisher verification requires submitting profile info, enabling org-wide 2FA, and verifying an organization domain. *(Sourced)*
  > "Publisher verification ensures that GitHub has a way to contact you, that you've enabled two-factor authentication for your organization, and that your organization's domain" — [source](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/applying-for-publisher-verification-for-your-organization)

**Likely blockers**

- OAuth services cannot be used as the sole identity provider for an application. *(Sourced)*
  > "Such Account Authorization Services are not intended to be used as the sole identity provider for your application or service." — [source](https://docs.github.com/en/site-policy/github-terms/github-registered-developer-agreement)
- Suspension if presenting the app or login page in a manner that suggests GitHub sponsorship or endorsement. *(Sourced)*
  > "presents itself or its login page in a manner that suggests sponsorship, endorsement, or affiliation with GitHub;" — [source](https://docs.github.com/en/site-policy/github-terms/github-registered-developer-agreement)
- Suspension if performing undocumented actions on behalf of the user, such as starring repositories without explicit disclosure. *(Sourced)*
  > "misrepresents or obscures what it does (for example, if an application takes any actions, like starring repositories, on behalf of a user without this" — [source](https://docs.github.com/en/site-policy/github-terms/github-registered-developer-agreement)
- Offering paid plans in GitHub Marketplace requires organization ownership, 2FA, and a verified domain. *(Sourced)*
  > "To offer paid plans for your app, the app must be owned by an organization and you must have owner permissions in the organization." — [source](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/applying-for-publisher-verification-for-your-organization)

**Agent can do**

- Navigate developer documentation and specify exact scope parameters.
- Draft configuration payloads and redirect callback lists.
- Provide guidance on handling token expiration and normalized scopes.

**You must do**

- Sign in to your GitHub account and navigate to Developer settings.
- Fill out and submit the OAuth App registration form.
- Store and manage the generated client ID and client secret securely.
- Configure organization 2FA and verify domain if requesting Marketplace publisher verification.

**Open questions**

- What is the expected turnaround time for GitHub Marketplace publisher verification reviews? *(Uncertain)*
  > Page 7 mentions GitHub will review details and notify you, but provides no specific timeline.

**Sources**

- [Scopes for OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)
- [Creating an OAuth app - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
- [GitHub Registered Developer Agreement - GitHub Docs](https://docs.github.com/en/site-policy/github-terms/github-registered-developer-agreement)
- [Authorizing GitHub Apps - GitHub Docs](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps)
- [Permissions required for GitHub Apps - GitHub Docs](https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps)
- [Registering a GitHub App - GitHub Docs](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app)
- [Applying for publisher verification for your organization - GitHub Docs](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/applying-for-publisher-verification-for-your-organization)
- [GitHub MCP Server | Composio](https://composio.dev/toolkits/github)
- [Managed OAuth apps | Composio](https://docs.composio.dev/toolkits/managed-auth)
- [https://github.com/settings/applications](https://github.com/settings/applications)

**Last verified:** 2026-10-30, by agent.

*Generated by Clearance using gemini-3.8-flash.*
