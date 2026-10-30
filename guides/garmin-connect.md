# Garmin Connect

**Garmin Connect, developerportal.garmin.com**

**Verdict:** Access to create multi-user OAuth 2.0 applications requires applying for the Garmin Connect Developer Program (Starter Access application form). Once approved, developers can register apps with up to 1,000 users. *(Sourced)*
> "Apply for the Garmin Connect Developer Program and create an app with Starter Access." — [source](https://developer.garmin.com/gc-developer-program)

**Difficulty:** Very hard
**Why:** Access to create multi-user OAuth 2.0 applications requires applying for the Garmin Connect Developer Program (Starter Access application form). Once approved, developers can register apps with up to 1,000 users. *(Sourced)*
**Hands-on time:** 15 to 30 minutes *(Inferred)*
**Waiting time:** Unknown *(Uncertain)*

**Composio status:** No Composio toolkit page found for this app. *(Inferred)*
> tried https://composio.dev/toolkits/garmin-connect, https://composio.dev/toolkits/garminconnect, https://composio.dev/toolkits/garmin; a toolkit may exist under a different slug

**Prerequisites**

- A Garmin Connect user account to access developer portals and manage developer programs. *(Inferred)*
  > Accessing the developer portal and authorization pages requires a Garmin Connect login.
- Application submitted for the Garmin Connect Developer Program Starter Access. *(Sourced)*
  > "Apply for the Garmin Connect Developer Program and create an app with Starter Access." — [source](https://developer.garmin.com/gc-developer-program)

**Setup steps**

1. Submit the Starter Access application form at https://www.garmin.com/en-US/forms/StarterGarminConnectDeveloperAccess/. *(Inferred)*
   > Page 5 links to the Starter Access form under Business 'REQUEST NOW'.
2. Log in to the Garmin Developer Portal at https://developerportal.garmin.com/developer-programs/myapp and create a new application (or convert an existing app). *(Inferred)*
   > Derived from developer portal app creation link and Nango integration instructions.
3. Configure the redirect callback URI for your application. *(Inferred)*
   > Referenced in Nango docs and OAuth 2.0 specification parameters.
4. Select and configure the API sections your application requires (e.g., Activity, Health, Training, Courses, Women's Health). *(Inferred)*
   > Supported by OAuth spec stating API sections are managed during app creation.
5. Copy the generated OAuth2 Client ID and Client Secret. *(Inferred)*
   > Mentioned in Nango instructions and standard OAuth 2.0 PKCE spec.
6. Configure data delivery settings and webhooks via Garmin API Tools at https://healthapi.garmin.com/tools/login. *(Sourced)*
   > "Configure your data delivery settings using API Tools" — [source](https://developerportal.garmin.com/developer-programs/connect-developer-api)
7. Implement OAuth 2.0 with PKCE (S256 code challenge method) using the authorization endpoint https://connect.garmin.com/oauth2Confirm and token endpoint https://diauth.garmin.com/di-oauth2-service/oauth/token. *(Sourced)*
   > "Garmin Connect Developer Program uses the OAuth2.0 PKCE version." — [source](https://developerportal.garmin.com/sites/default/files/OAuth2PKCE_1.pdf)

**Scopes**

- API scopes cannot be requested or customized in authorization or token URL parameters; scope is returned by default by the API based on application configuration (e.g., 'PARTNER_WRITE PARTNER_READ CONNECT_READ CONNECT_WRITE'). *(Sourced)*
  > "Scope is a default API scope and cannot be modified. API sections are managed during the app creation process." — [source](https://developerportal.garmin.com/sites/default/files/OAuth2PKCE_1.pdf)
- Granular user permissions (such as ACTIVITY_EXPORT, WORKOUT_IMPORT, HEALTH_EXPORT, COURSE_IMPORT, MCT_EXPORT) are chosen directly by the user on the Garmin consent screen. *(Sourced)*
  > "Users control permissions granted during the authorization step." — [source](https://developerportal.garmin.com/sites/default/files/OAuth2PKCE_1.pdf)

**Limits before approval**

- Starter Access limits user capacity to up to 1,000 connected users. *(Sourced)*
  > "Up to 1,000 connected users" — [source](https://developerportal.garmin.com/developer-programs/connect-developer-api)
- Starter Access delivers data via Push only (no Ping/Pull). *(Sourced)*
  > "Delivery: Push only" — [source](https://developerportal.garmin.com/developer-programs/connect-developer-api)
- Historical data is not included under Starter Access. *(Sourced)*
  > "Historical Data: Not included" — [source](https://developerportal.garmin.com/developer-programs/connect-developer-api)
- Access tokens expire after 24 hours (86,400 seconds) while refresh tokens are valid for approximately 90 days (7,775,998 seconds). *(Inferred)*
  > Derived from token response examples in the OAuth2 PKCE specification.

**Approval process**

- Organizations must apply for the Garmin Connect Developer Program to receive Starter Access credentials. *(Sourced)*
  > "Apply for the Garmin Connect Developer Program and create an app with Starter Access." — [source](https://developer.garmin.com/gc-developer-program)
- To scale beyond 1,000 users, receive historical data (1 month+), or use Ping/Pull delivery, an organization must request Enterprise Access with Garmin. *(Sourced)*
  > "Available options and commercial terms are tailored based on business and technical requirements." — [source](https://developerportal.garmin.com/developer-programs/connect-developer-api)

**Likely blockers**

- Commercial terms or tailored business evaluation required for Enterprise Access if needing more than 1,000 users. *(Sourced)*
  > "Available options and commercial terms are tailored based on business and technical requirements." — [source](https://developerportal.garmin.com/developer-programs/connect-developer-api)
- Attempting to build multi-user apps using the Personal API instead of the Developer Program (Personal API keys are strictly single-user). *(Sourced)*
  > "It is not intended for commercial applications serving multiple end users." — [source](https://developer.garmin.com/gc-developer-program/personal/personal-faq)
- Failing to implement required PKCE parameters (code_verifier and code_challenge with S256) on authorization and token exchanges. *(Sourced)*
  > "Garmin Connect Developer Program uses the OAuth2.0 PKCE version." — [source](https://developerportal.garmin.com/sites/default/files/OAuth2PKCE_1.pdf)
- Failing to implement the mandatory user deregistration endpoint (DELETE /wellness-api/rest/user/registration) when users disconnect or delete their accounts. *(Sourced)*
  > "This endpoint must be called if the partner website or application provides a “Delete My Account” or “Disconnect” mechanism" — [source](https://developerportal.garmin.com/sites/default/files/OAuth2PKCE_1.pdf)

**Agent can do**

- Generate code verifier and code challenge using S256 for PKCE implementation
- Format OAuth2 authorization and token refresh HTTP requests
- Draft the integration code for user permission checks and account deregistration webhooks

**You must do**

- Fill out and submit the Garmin Connect Developer Program Starter Access request form
- Log into the Garmin Developer Portal to configure callback URLs and API access
- Securely copy and store the OAuth2 Client ID and Client Secret

**Open questions**

- What are the specific review criteria and average response time for Starter Access form submissions? *(Uncertain)*
  > Documentation provides the form link but does not document evaluation criteria or review turnaround times.
- What are the commercial pricing tiers and legal contract requirements for Enterprise Access? *(Uncertain)*
  > Documentation states options and terms are tailored based on requirements, but details are not published.

**Sources**

- [How to register your own Garmin OAuth2 app - Nango Docs](https://nango.dev/docs/api-integrations/garmin-oauth2/how-to-register-your-own-garmin-oauth2-api-oauth-app)
- [[PDF] Garmin Connect Developer Program OAuth2.0 PKCE Specification](https://developerportal.garmin.com/sites/default/files/OAuth2PKCE_1.pdf)
- [Program FAQ | Garmin Connect Developer Program | Garmin Developers](https://developer.garmin.com/gc-developer-program/personal)
- [Program FAQ | Garmin Connect Developer Program | Garmin Developers](https://developer.garmin.com/gc-developer-program/personal/personal-faq)
- [Overview | Garmin Connect Developer Program | Garmin Developers](https://developer.garmin.com/gc-developer-program)
- [Garmin Connect Developer | Garmin Developer Portal](https://developerportal.garmin.com/developer-programs/connect-developer-api)
- [Home | Garmin Developers](https://developer.garmin.com/)

**Last verified:** 2026-10-30, by agent.

*Generated by Clearance using gemini-3.8-flash.*
