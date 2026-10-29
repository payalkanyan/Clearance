
## 4. GitHub guide (draft, verify against your notes)

**GitHub, github.com/settings/developers**

**Verdict:** Fully self-serve. You can create an OAuth app and have real users connect in minutes, with no review. *(Sourced)*

**Quick setup checklist:** Go to GitHub → Settings → Developer settings → OAuth Apps → **New OAuth App**. *(Sourced; upgrade to Tested if you did this in your lab)*

**Difficulty:** Easy
**Hands-on time:** 5 to 15 minutes *(Tested only if you timed it)*
**Waiting time:** None *(Sourced)*

**Composio status:** Toolkit available, with a Composio managed app. Bring-your-own is optional, used for your own branding on the consent screen. *(Sourced: Composio docs; Tested if you saw both consent screens)*

**Prerequisites**
- A GitHub account *(Sourced)*
- A homepage URL for your app (any valid URL works) *(Sourced)*
- The callback URL from Composio's dashboard if you're using Composio *(Sourced)*

**Setup steps**

1. Start here: On GitHub, go to Settings → Developer settings → OAuth Apps → New OAuth App. (Tested)
2. Fill in the application name and homepage URL. While testing, any valid URL works, such as your portfolio or GitHub profile; GitHub doesn’t verify it. (Tested)
3. Click Register application and copy the Client ID. (Tested)
4. Click Generate a new client secret and copy it immediately, since it’s shown only once. (Tested, if you saw it disappear after leaving the page; otherwise Sourced)
5. In Composio, go to Toolkits and select GitHub. GitHub appears as two toolkits: choose the GitHub card (OAuth2, marked “Managed”), not GitHub MCP, which uses an API key and skips OAuth entirely. (Tested)
6. Click Add to Project. (Tested)
7. Create the auth config with your own credentials: keep the default config name or give your own, paste the Client ID and Secret, then click Create Auth Config. (Tested)
8. Copy the callback URL Composio shows and paste it into your GitHub OAuth app’s “Authorization callback URL” field, then save on GitHub. (Tested, if you did this; adjust the order to match what you actually did)
9. In Composio, go to Auth Configs → select your GitHub config → Connect Account. You’re redirected to GitHub’s own login page, where you sign in with your GitHub username/email and password. (Tested)
10. On GitHub’s consent screen, confirm it shows your OAuth app’s name, check the requested permissions, and click Authorize.(Tested)

**Scopes:** Request only what you need, e.g. `read:user`, `repo` (full repo access) or `public_repo`. Scopes are chosen at authorization time, not in the app settings. *(Sourced)*

**Limits before approval:** None; there's no approval step for OAuth apps. *(Sourced)*

**Approval process:** None for using the app. Listing on GitHub Marketplace is optional and has its own review. *(Sourced)*

**Likely blockers and nuances**
- **Organisation restrictions:** If a user's organisation restricts third-party OAuth apps, an org owner must approve your app before it can access org repos. Users may connect successfully but see no org data. *(Sourced; this is a great "gotcha" to verify if you have an org)*
- **One callback URL per OAuth app**, so you may need separate apps for development and production. *(Sourced; worth verifying)*
- **GitHub Apps vs OAuth Apps:** GitHub generally recommends GitHub Apps for finer permissions. Check which type Composio's custom auth expects. *(Uncertain, confirm in Composio docs)*
- **Rate limits** apply per user token. *(Sourced)*

**Agent can do**
- Find the right console pages and docs
- Explain scopes and recommend minimal ones
- Fill in the guide and check Composio's status

**You must do**
- Log in to GitHub
- Create the app and generate the secret
- Store the secret safely and paste it into Composio
- Click Allow on the consent screen

**Open questions**
- Exact rate limits under Composio's managed app vs your own app *(Uncertain)*
- Whether Composio's GitHub custom auth supports GitHub Apps as well as OAuth Apps *(Uncertain)*

**Sources:** GitHub Docs "Creating an OAuth app" and "Authorizing OAuth apps"; GitHub Docs on organisation OAuth app access restrictions; Composio docs "Managed vs custom auth."

**Last verified:** [Oct 29], by [0xpastril], the flow was confirmed.
