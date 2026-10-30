# Spotify

**Spotify, developer.spotify.com/dashboard**

**Verdict:** App registration is immediate in Development Mode, but production access requires meeting strict organization partner criteria (including 250k MAUs) and undergoing an app review that takes up to six weeks. *(Inferred)*
> Immediate creation of Development Mode apps is supported by the dashboard setup docs, while Extended Quota Mode requires passing partner requirements and a review process lasting up to six weeks.

**Difficulty:** Hard
**Why:** App registration is immediate in Development Mode, but production access requires meeting strict organization partner criteria (including 250k MAUs) and undergoing an app review that takes up to six weeks. *(Inferred)*
**Hands-on time:** 10 to 20 minutes *(Inferred)*
**Waiting time:** Up to 6 weeks *(Sourced)*

**Composio status:** Toolkit available, but you must register your own OAuth app and give Composio its client ID and secret. *(Sourced)*
> "Spotify requires connections to go through your own OAuth app." — [source](https://composio.dev/toolkits/spotify)

**Prerequisites**

- At https://developer.spotify.com/dashboard, an application form is shown, behind a sign-in or an access request. Fields visible: email, privacy policy, terms of service. *(Tested)*
  > [source](https://developer.spotify.com/dashboard)
  > observed by the agent at 2026-10-30T11:39:09Z, HTTP 200; matched login, continue with google, continue with apple
- The app owner must hold an active Spotify Premium account. *(Sourced)*
  > "The app owner must have a Spotify Premium account for apps in development mode to function." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Production Extended Quota access requires an established, legally registered business entity (individuals are not eligible) with a company email. *(Sourced)*
  > "Please note that as of May 15th 2025, Spotify only accepts applications from organizations (not individuals)." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Production access requires an active, launched service maintaining at least 250,000 monthly active users (MAUs). *(Sourced)*
  > "Maintaining a minimum of active users (at least 250k MAUs)" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)

**Setup steps**

1. Log in to the Spotify Developer Dashboard at https://developer.spotify.com/dashboard using your Spotify account. *(Sourced)*
   > "Login to the Spotify Developer Dashboard. If necessary, read the latest Developer Terms of Service to complete your account set up." — [source](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
2. Click on the 'Create an App' button on your dashboard. *(Sourced)*
   > "To create an app, go to your Dashboard and click on the Create an App button to open the following dialog box:" — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)
3. Enter an App Name and App Description, and accept the Developer Terms of Service. *(Sourced)*
   > "Enter an App Name and App Description of your choice (they will be displayed to the user on the grant screen), put a tick" — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)
4. Open the app's overview page and click on 'Settings' (or 'Edit Settings') to configure your application. *(Sourced)*
   > "Click on Edit Settings to view and update your app settings." — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)
5. In the 'Redirect URIs' field, enter your application callback URL (for example http://127.0.0.1:8080 or your service callback URI) and save changes. *(Sourced)*
   > "In Redirect URIs enter one or more addresses that you want to allowlist with Spotify." — [source](https://developer.spotify.com/documentation/web-api/concepts/apps)
6. Retrieve your Client ID and Client Secret from the app overview/settings page (under 'View client secret') for OAuth configuration. *(Sourced)*
   > "The Client ID can be found here. The Client Secret can be found behind the View client secret link." — [source](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
7. If testing in Development Mode, navigate to the 'Users Management' tab in your app settings and allowlist each test user by entering their name and Spotify email address. *(Sourced)*
   > "Tap on the Add new user button and enter the name and Spotify email address of the user that you want to enable to" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)

**Scopes**

- user-read-private: Grants read access to the user's subscription details and account type. *(Sourced)*
  > "Read access to user’s subscription details (type of user account)." — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- user-read-email: Grants read access to the user's real email address. *(Sourced)*
  > "Read access to user’s email address." — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- playlist-read-private: Grants read access to the user's private playlists. *(Sourced)*
  > "Read access to user's private playlists." — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- playlist-modify-public and playlist-modify-private: Grants write access to create, modify, or reorder public or private playlists. *(Inferred)*
  > Derived from the playlist scope definitions in the scopes reference page.
- user-modify-playback-state: Grants write access to control playback on Spotify clients and Spotify Connect devices. *(Sourced)*
  > "Write access to a user’s playback state" — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- user-library-read: Grants read access to check and view saved tracks, albums, and episodes in the user's library. *(Sourced)*
  > "Read access to a user's library." — [source](https://developer.spotify.com/documentation/web-api/concepts/scopes)

**Limits before approval**

- Development Mode apps are strictly limited to at most 5 authenticated Spotify users who must be explicitly allowlisted. *(Sourced)*
  > "Up to 5 authenticated Spotify users can use an app that is in development mode" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Non-allowlisted users who authenticate receive a 403 status code on API calls. *(Sourced)*
  > "However, API requests with an access token associated to that user and app will receive a 403 status code error." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Developers are limited to one Development Mode Client ID. *(Sourced)*
  > "Developers will be limited to one Development Mode Client ID" — [source](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security)
- Development Mode requests are constrained by quota buckets across the developer account, returning 429 QUOTA_EXCEEDED when exceeded. *(Sourced)*
  > "Spotify's Web API has a quota system that limits the number of requests made through development mode apps that belong to a single developer account." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Development Mode apps will not function unless the app owner maintains an active Spotify Premium account. *(Sourced)*
  > "Development Mode use will require a Spotify Premium account" — [source](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security)

**Approval process**

- Step 1: Submit a Partner Application form from a corporate email address to qualify as an organization. *(Sourced)*
  > "Application must be sent through a company email by using this form." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Step 2: If the Partner Application is approved, go to Dashboard > App > Settings > 'Quota extension Request' tab. *(Sourced)*
  > "If your Partner Application form is approved, you can ask Spotify to move your app from development mode into extended quota mode." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Step 3: Complete the 4-step questionnaire detailing your app and use case, then submit. *(Sourced)*
  > "Tell us about your app by filling out the provided questionnaire (4 steps)" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Step 4: Spotify's review team evaluates your app for policy compliance, tests the app, and communicates decisions via email within up to six weeks. *(Sourced)*
  > "The app review team will review the information that you have provided, test out your app and send you feedback by email" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)

**Likely blockers**

- Individual developers cannot obtain Extended Quota Mode; applications are accepted only from registered organizations. *(Sourced)*
  > "Please note that as of May 15th 2025, Spotify only accepts applications from organizations (not individuals)." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Failure to demonstrate at least 250,000 monthly active users (MAUs) on an existing launched service. *(Sourced)*
  > "Maintaining a minimum of active users (at least 250k MAUs)" — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Lack of an active Spotify Premium subscription for the app owner. *(Sourced)*
  > "The app owner must have a Spotify Premium account for apps in development mode to function." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Attempting to create multiple Development Mode Client IDs under one developer account. *(Sourced)*
  > "Developers will be limited to one Development Mode Client ID" — [source](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security)
- Submitting the partner extension application using a personal email rather than a company domain email. *(Sourced)*
  > "Application must be sent through a company email by using this form." — [source](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- Requires privacy policy or terms URLs *(Inferred)*
  > rubric modifier: noted as a blocker, it does not change the difficulty level

**Agent can do**

- Identify and format the required OAuth scopes for your application use case.
- Draft the authorization URL and handle the token exchange implementation (Authorization Code or PKCE flow).
- Prepare API requests according to the Web API specification.

**You must do**

- Log in to the Spotify Developer Dashboard with a Spotify Premium account.
- Register the application and configure the exact Redirect URIs in app settings.
- Securely copy and store the Client ID and Client Secret.
- Manually add up to 5 tester accounts (name and Spotify email) under User Management for Development Mode testing.
- Submit the official organization partner application and quota extension review form if planning to deploy to production.

**Open questions**

- What specific quota bucket limits are enforced for Development Mode apps, given Spotify notes they are subject to change without published numeric thresholds? *(Inferred)*
  > Documentation indicates that endpoints are grouped into quota buckets and return 429 when exceeded, but does not state the exact numeric request limits.
- The input 'Spotfy' does not match the provider's own name 'Spotify'; the guide follows the pages found. *(Uncertain)*
  > the app name given did not match the provider's own

**Sources**

- [Authorization | Spotify for Developers](https://developer.spotify.com/documentation/web-api/concepts/authorization)
- [Scopes | Spotify for Developers](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- [Quota modes | Spotify for Developers](https://developer.spotify.com/documentation/web-api/concepts/quota-modes)
- [Apps | Spotify for Developers](https://developer.spotify.com/documentation/web-api/concepts/apps)
- [Getting started with Web API | Spotify for Developers](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
- [Spotify Developer Terms | Spotify for Developers](https://developer.spotify.com/terms)
- [Update on Developer Access and Platform Security | Spotify for Developers](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security)
- [Spotify MCP Server | Composio](https://composio.dev/toolkits/spotify)
- [Managed OAuth apps | Composio](https://docs.composio.dev/toolkits/managed-auth)
- [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)

**Last verified:** 2026-10-30, by agent.

*Generated by Clearance using gemini-3.8-flash.*
