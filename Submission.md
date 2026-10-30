# Clearance: Submission

Oct 30, 2026 

**Live app:** \[link\]

**Repo:** [github.com/payalkanyan/Clearance](https://github.com/payalkanyan/Clearance)

**Demo video:** \[link\]

Clearance tells a developer how hard it is to get their OAuth app approved with any provider, how long it will take, what might block them, and what they must do themselves. Every claim carries a label saying how it was verified.

## How I approached this

I hadn't worked with OAuth or API integrations at this level before, so I treated the first part of this assignment as genuine learning, and I want to show that honestly.

### Learning the basics

I started with Okta's "OAuth 2.0 and OpenID Connect in plain English" talk to understand authorization codes, client IDs and secrets, scopes and redirect URIs. Then I went through Composio's docs to understand how a provider OAuth app, a Composio auth config, and a user's connected account relate to each other.

### Getting hands-on with Composio

I used the playground to connect Firecrawl and hit two errors, which taught me more than the docs did:

1. **"Tools restricted":** my allow-list was too narrow, so the agent couldn't pick a search tool. (A permission problem on my side.)
2. **401 Unauthorized:** the tool ran, but the provider rejected the stored API key. (A credentials problem with the provider.)

That difference, between "the agent isn't allowed" and "the provider won't accept the credentials", is exactly the kind of thing a developer gets stuck on. It also gave me an idea for later: a small assistant that explains what each integration error means.

I then created my own GitHub OAuth app and connected it through a Composio custom auth config, and compared its consent screen with the managed one.

&#91;screenshot: playground errors\]

&#91;screenshot: GitHub consent screen with my app name\]

### Phase 0: Understanding the problem

I rewrote the problem in my own words: Composio's managed apps solve day one, but going to production often means creating your own OAuth app, and nobody tells you whether that takes ten minutes or ten weeks. I chose four apps with different blockers: GitHub (none), Spotify (user cap until extended access), QuickBooks (production assessment) and Garmin Connect (business approval).

&#91;screenshot: Phase 0 notes and app-selection table\]

### Phase 1: Designing the guide spec

Before writing any code, I designed what a guide should contain: fields, a difficulty rubric, and four evidence labels (Tested, Sourced, Inferred, Uncertain). I then wrote the GitHub guide by hand, verified it against my own setup, and used it as the gold standard for the agent.

&#91;screenshot: guide spec / GitHub gold guide\]

### Architecture

I worked through the architecture with Claude, openly. Its first suggestion was an eight-stage pipeline with two model tiers and an LLM self-check. I then asked about scraping and LLM cost strategy, which brought in Firecrawl, and when I pushed it to critique the design against a 6 to 8 hour budget, I cut it down:

- **One LLM call** instead of many, so cross-page facts aren't lost.
- **A deterministic citation check** instead of an LLM judge: every "Sourced" claim needs a quote, and code checks that quote really exists in the cited page. A model reviewing the same sources can't catch what they miss, but a string match reliably catches invented quotes.
- **A portal probe** that visits the developer portal and records what it actually sees, since the brief asked agents to attempt setup, not just read about it.
- **Difficulty scored in code**, never by the model.

&#91;architecture diagram\]

### Building, verifying and deploying

I built it stage by stage, testing each one on its own before connecting them. I switched from Anthropic to Gemini for extraction because I didn't have Anthropic billing, and the README lists that and the other deviations.

## Results

**Difficulty: what I expected vs what the agent concluded**

| App | Expected | Agent result | Triggered by | Match? |
| --- | --- | --- | --- | --- |
| GitHub | Easy | Easy | Nothing matched a harder level: self-serve, no review before real users | Yes |
| Spotify | Medium | Hard | Verdict matched *"formal review"*: extended quota needs one before unlimited users | No |
| QuickBooks | Hard | Hard | Verdict matched *"questionnaire"*: a self-assessment before public distribution | Yes |
| Garmin Connect | Very hard | Very hard | Verdict matched *"apply for the Garmin Connect Developer Program"* before credentials exist | Yes |

Three of four. The Spotify mismatch is the interesting one, and I left it rather than tune the rubric to agree: you do get development-mode credentials immediately, which is why the rubric explicitly ruled out Very hard, but the spec puts "mandatory review before production use" at Hard, and extended quota mode does require a formal review. The log records both the level and the fact that triggered it, so the verdict is arguable rather than opaque.

I later ran two apps the rubric had never seen, after writing my predictions down first, because the four above were the ones I had tuned it against. Both disagreed with me and both found real bugs: Zoom scored Easy despite a multi-stage marketplace security review (I had treated the word "marketplace" as an optional extra, true for GitHub and false for Zoom), and Slack scored Medium despite a ten-week functional review (my patterns wanted the words "app review", so named review phases slipped past). Fixing those moved both to Hard without moving any of the four.

**Verification**

- **GitHub agent guide vs my hand-written gold guide:** 6 facts matched, 11 missing, 29 found by the agent that I hadn't written, 2 label differences. Separately, 10 of my facts are labelled Tested, which an agent cannot reproduce because it can't log in to GitHub; the diff reports those in their own bucket rather than counting them as failures.
- **Both label differences were the agent being more careful than I was.** I wrote the verdict and the waiting time as Sourced; the agent labelled both Inferred, because no GitHub page actually says "fully self-serve" or "none" in those words.
- **Citation check downgraded 5 of 212 Sourced claims to Inferred** across eight guides. All five were in the Zoom guide, and four carried the same diagnosis: the first eight words of the quote are on the page and the rest is not, which is a model starting to copy and then drifting. One example claimed Zoom's security testing covers "automated web scanning, least-privilege verification, library vulnerability checks", quoting a sentence that really says apps are "tested against the OWASP Top 10 risks". Close enough to believe, not close enough to cite.
- **What I corrected:** my own gold guide. I had written "One callback URL per OAuth app, so you may need separate apps for development and production", annotated *"worth verifying"*. The agent found GitHub's own page saying *"You can enter up to 10 callback URLs"* and the quote checks out against the cached page, so my guide was out of date and the agent caught it.
- **What I couldn't verify:** real approval wait times, which providers almost never publish; anything behind a login, since the portal probe only records what is visible signed out; and Garmin's process past the Starter Access application form.
- **One thing the agent still misses.** My gold guide's best gotcha is that an organisation admin can block a third-party OAuth app, so a user connects successfully and then sees no org data. Adding a seventh search query did pull GitHub's three org-restriction pages into the scrape, but the model read them and still didn't write the blocker. That is an extraction gap rather than a research one, and it is the clearest thing I would fix next.

## Limitations

- Approval wait times are rarely published, so most are "Unknown".
- The portal probe only sees what's visible without logging in.
- Guides are a snapshot; provider policies change.

## What I'd build next

A step-by-step progress checklist, an error-explainer for integration failures, an LLM reviewer on top of the citation check, and parallel research for faster generation.

## Before submitting (remove this section)

**Worth adding:**

- The difficulty table above. A mismatch with a good explanation is as valuable as a match.
- Verification numbers from the logs, e.g. "downgraded 7 of 52 claims".
- One corrected-claim example: what the agent said and what was actually true.

**Unnecessary:** full guide contents, detailed architecture explanations (the README covers them), code walkthroughs.
