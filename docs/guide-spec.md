
## 1. Guide fields

Every guide has these fields, in this order:

| Field | What it holds |
|---|---|
| **App name & website** | e.g. "Spotify, developer.spotify.com" |
| **One-line verdict** | Plain summary, e.g. "Self-serve for testing; approval needed for real users." |
| **Quick setup checklist** - future upgrade(not now)| a checklist of actions. | 
| **Difficulty** | Easy / Medium / Hard / Very hard (from the rubric) |
| **Hands-on time** | Your active work, as a range. |
| **Waiting time** | Approval wait, as a range or "Unknown." |
| **Composio status** | Toolkit? Managed app? Bring-your-own required? |
| **Prerequisites** | Accounts, verified domain, privacy policy URL, business details, paid plan, etc. |
| **Setup steps** | Numbered steps with console links, redirect URI, scopes. |
| **Limits before approval** | User caps, test mode, rate limits, sandbox-only data. |
| **Approval process** | What's reviewed, what you submit, who decides. |
| **Likely blockers** | What commonly causes rejection or delay. |
| **Agent can do / You must do** | Two lists. |
| **Open questions** | What remains uncertain. |
| **Sources** | Every URL used. |
| **Last verified** | Date, and by whom (agent or human). |

Each fact inside the guide carries an evidence label.

---

## 2. Evidence labels

| Label | Meaning | Example |
|---|---|---|
| **Tested** | A human or the agent directly observed it on the provider's site or in a real setup attempt. done by this agent engineer from backend | "I created the app and saw the Client Secret button." |
| **Sourced** | Stated in an official provider document, linked. | "Spotify docs say dev mode allows limited users." |
| **Inferred** | Reasoned from evidence but not directly stated or observed. | "Approval likely needs a demo video, since similar apps required one." |
| **Uncertain** | Sources conflict, are outdated, or nothing was found. | "Review wait time not published; forum reports vary." |

Rules:
- A fact with no source link cannot be labelled Sourced.
- Third-party blogs or forums count as **Inferred** at best, never Sourced.
- If an official doc and a test disagree, the test wins, and the conflict is noted.
- Time estimates are never Tested unless someone actually waited it out.

---

## 3. Difficulty rubric

Pick the **highest** level whose condition applies.

| Level | Condition | Typical waiting time |
|---|---|---|
| **Easy** | Self-serve app creation, keys immediately, no review needed for real users. | None |
| **Medium** | Keys immediately, but restricted (user cap, test mode, limited scopes) until you apply for more. | Days to a few weeks |
| **Hard** | Mandatory review, assessment, or questionnaire before production use. | Weeks |
| **Very hard** | Business/partner approval before you get keys at all, a paid security audit, or approval needed from multiple parties. | Weeks to months, or unknown |

Modifiers to note (they don't change the level, but appear as blockers):
- Requires a paid plan
- Requires a verified domain or company website
- Requires privacy policy / terms URLs
- Requires a demo video or screencast
- Regional or legal restrictions
