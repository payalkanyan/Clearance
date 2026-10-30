# Spotify

**Spotify, developer.spotify.com/dashboard**

**Verdict:** Development mode credentials are created immediately without approval for up to 5 allowlisted users, but extending access to unlimited users requires an organization application and formal review. *(Inferred)*
> Inferred from documentation stating newly created apps begin immediately in development mode with a 5-user cap, while moving to extended quota requires submitting partner forms and awaiting review.

**Difficulty:** Hard
**Why:** Development mode credentials are created immediately without approval for up to 5 allowlisted users, but extending access to unlimited users requires an organization application and formal review. *(Inferred)*
**Hands-on time:** 5 to 15 minutes *(Inferred)*
**Waiting time:** Up to six weeks *(Sourced)*

**Composio status:** Toolkit available, but you must register your own OAuth app and give Composio its client ID and secret. *(Sourced)*
> "Spotify requires connections to go through your own OAuth app." — [source](https://composio.dev/toolkits/spotify)

**Prerequisites**

- At https://developer.spotify.com/dashboard, an application form is shown, behind a sign-in or an access request. Fields visible: email, privacy policy, terms of service. *(Tested)*
  > [source](https://developer.spotify.com/dashboard)
  > observed by the agent at 2026-10-30T10:26:57Z, HTTP 200; matched login, continue with google, continue with apple
- The app owner must hold an active Spotify Premium account. *(Sourced)*
  > "The app owner must have a Spotify Premium account for apps in development mode to function." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- You must accept the Spotify Developer Terms of Service when registering an app. *(Sourced)*
  > "put a tick in the Developer Terms of Service checkbox and finally click on CREATE." — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)

**Setup steps**

1. Log in to the Spotify Developer Dashboard at developer.spotify.com/dashboard. *(Sourced)*
   > "Login to the Spotify Developer Dashboard." — [source](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
2. Click on the 'Create an App' button. *(Sourced)*
   > "click on the Create an App button to open the following dialog box:" — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)
3. Enter an App Name and App Description, check the Developer Terms of Service checkbox, and click CREATE. *(Sourced)*
   > "Enter an App Name and App Description of your choice (they will be displayed to the user on the grant screen)" — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)
4. On the app overview page, click on 'Edit Settings' (or 'Settings'). *(Sourced)*
   > "It is time to configure our app. Click on Edit Settings to view and update your app settings." — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)
5. Enter your callback addresses into the 'Redirect URIs' field and click SAVE. *(Sourced)*
   > "In Redirect URIs enter one or more addresses that you want to allowlist with Spotify." — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)
6. Obtain your Client ID and Client Secret (accessible under 'View client secret') to use in your application. *(Sourced)*
   > "The Client ID can be found here. The Client Secret can be found behind the View client secret link." — [source](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
7. To allow team members or testers to use the app in Development Mode, open the 'Users Management' tab, click 'Add new user', and enter their name and Spotify email address. *(Sourced)*
   > "Tap on the Add new user button and enter the name and Spotify email address of the user that you want to enable" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)

**Scopes**

- user-read-private: Read access to user subscription details and account type. *(Sourced)*
  > "Read access to user’s subscription details (type of user account)." — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- user-read-email: Read access to the user's email address. *(Sourced)*
  > "Read access to user’s email address." — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- playlist-read-private: Read access to a user's private playlists. *(Sourced)*
  > "Read access to user's private playlists." — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- playlist-modify-public: Write access to manage a user's public playlists. *(Sourced)*
  > "Write access to a user's public playlists." — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- user-read-playback-state: Read access to the user's player state and Spotify Connect devices. *(Sourced)*
  > "Read access to a user’s player state." — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- user-modify-playback-state: Write access to control playback across user clients and devices. *(Sourced)*
  > "Write access to a user’s playback state" — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)

**Limits before approval**

- Development mode apps are limited to a maximum of 5 authenticated Spotify users. *(Sourced)*
  > "Up to 5 authenticated Spotify users can use an app that is in development mode" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Each user must be manually added to the app allowlist before they can use it. *(Sourced)*
  > "Each Spotify user who installs your app will need to be added to your app's allowlist before they can use it." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Requests made using tokens from non-allowlisted users return a 403 Forbidden status code error. *(Sourced)*
  > "However, API requests with an access token associated to that user and app will receive a 403 status code error." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Requests are restricted by quota buckets that limit requests across all development mode apps for a developer account. *(Sourced)*
  > "Endpoints are grouped into quota buckets and requests to endpoints in the same bucket count toward a shared limit." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Developers are capped at creating up to 25 apps per developer account. *(Sourced)*
  > "You can create up to 25 apps per developer account." — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)

**Approval process**

- Only legally registered organizations, not individual developers, can apply for extended quota access. *(Sourced)*
  > "Please note that as of May 15th 2025, Spotify only accepts applications from organizations (not individuals)." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- An initial partner application must be submitted through a company email via Spotify's designated form. *(Sourced)*
  > "Application must be sent through a company email by using this form." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Once a partner application is approved, developers submit a 4-step questionnaire under the 'Quota extension Request' tab in app settings. *(Sourced)*
  > "Tell us about your app by filling out the provided questionnaire (4 steps)" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- The Spotify app review team tests the app and delivers feedback by email to the app owner's registered address. *(Sourced)*
  > "The app review team will review the information that you have provided, test out your app and send you feedback by email" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- The quota extension review process takes up to six weeks. *(Sourced)*
  > "This review process can take up to six weeks." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)

**Likely blockers**

- Individual developers cannot apply; applicant must be an established business entity with a company email. *(Sourced)*
  > "Please note that as of May 15th 2025, Spotify only accepts applications from organizations (not individuals)." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Extended quota applicants must maintain an active, launched service with at least 250,000 monthly active users (MAUs). *(Sourced)*
  > "Maintaining a minimum of active users (at least 250k MAUs)" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- The developer account owner must have a Spotify Premium account or development mode apps will not function. *(Sourced)*
  > "The app owner must have a Spotify Premium account for apps in development mode to function." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- The applicant must operate an active, launched service available in key Spotify markets. *(Sourced)*
  > "Operating an active, and Launched Service" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Requires privacy policy or terms URLs *(Inferred)*
  > rubric modifier: noted as a blocker, it does not change the difficulty level

**Agent can do**

- Explain Spotify OAuth flows, scopes, and API endpoint specifications.
- Draft code to exchange authorization codes or client credentials for access tokens.
- Help construct redirect URIs and API request payloads.

**You must do**

- Log in to the Spotify Developer Dashboard with a Spotify Premium account.
- Register the application and accept the Developer Terms of Service.
- Add your redirect URIs and copy the Client ID and Client Secret.
- Add test users to the Users Management allowlist by Spotify account email.
- Submit an organization partner application if public release (Extended Quota Mode) is required.

**Open questions**

- What specific request numbers and time windows define the shared limit for each development mode quota bucket? *(Sourced)*
  > "The specific groupings and limits are subject to change." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)

**Sources**

- [Authorization | Spotify for Developers](https://developer.spotify.com/documentation/web-api/concepts/authorization)
- [Scopes | Spotify for Developers](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- [Quota modes | Spotify for Developers](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- [Apps | Spotify for Developers](https://developer.spotify.com/documentation/web-api/concepts/apps)
- [Getting started with Web API | Spotify for Developers](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
- [Verified by Spotify - Spotify](https://support.spotify.com/us/article/verified-by-spotify)
- [Spotify Developer Terms | Spotify for Developers](https://developer.spotify.com/terms)
- [Spotify MCP Server | Composio](https://composio.dev/toolkits/spotify)
- [Managed OAuth apps | Composio](https://docs.composio.dev/toolkits/managed-auth)
- [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)

**Last verified:** 2026-10-30, by agent.

*Generated by Clearance using gemini-3.8-flash.*
