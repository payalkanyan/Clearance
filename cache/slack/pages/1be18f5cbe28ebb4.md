reference

[Skip to main content](https://docs.slack.dev/reference/scopes/#__docusaurus_skipToContent_fallback)

Copy as markdown

Scopes are the permissions your Slack app requests in order to act.

Each scope grants access to a specific set of actions or data, such as reading messages in a channel or viewing a user's profile. An app has no access by default. It can only do what its scopes allow. You choose the scopes your app needs when configuring it, then request them during installation through the [OAuth flow](https://docs.slack.dev/authentication/installing-with-oauth).

Scopes are granted to your app's [tokens](https://docs.slack.dev/authentication/tokens) when a user installs your app. Two types of scopes cover most situations:

- **Bot scopes** grant permissions to your app's bot user, which acts with its own identity. Most apps use bot scopes.
- **User scopes** let your app act on behalf of the user who installed or authorized it, accessing only what that user can.

The full list of available scopes is below. Each entry notes the token types it applies to and the API methods it unlocks.

AllUserConfigurationBotLegacy BotApp-level

Name

Description

Token Types

[`admin`](https://docs.slack.dev/reference/scopes/admin)

Administer a workspace

User

[`admin.analytics:read`](https://docs.slack.dev/reference/scopes/admin.analytics.read)

Access analytics data about the organization

User

[`admin.app_activities:read`](https://docs.slack.dev/reference/scopes/admin.app_activities.read)

View execution logs within an organization

User

[`admin.apps:read`](https://docs.slack.dev/reference/scopes/admin.apps.read)

View apps and app requests in a workspace

User

[`admin.apps:write`](https://docs.slack.dev/reference/scopes/admin.apps.write)

Manage apps in a workspace

User

[`admin.barriers:read`](https://docs.slack.dev/reference/scopes/admin.barriers.read)

Read information barriers in the organization

User

[`admin.barriers:write`](https://docs.slack.dev/reference/scopes/admin.barriers.write)

Manage information barriers in the organization

User

[`admin.chat:read`](https://docs.slack.dev/reference/scopes/admin.chat.read)

Read messages in conversations

User

[`admin.chat:write`](https://docs.slack.dev/reference/scopes/admin.chat.write)

Delete, restore, and update messages in conversations

User

[`admin.conversations:manage_objects`](https://docs.slack.dev/reference/scopes/admin.conversations.manage_objects)

Manage channel details and create conversations related to external connections, objects, and records

User

[`admin.conversations:read`](https://docs.slack.dev/reference/scopes/admin.conversations.read)

View the channel's member list, topic, purpose and channel name

User

[`admin.conversations:write`](https://docs.slack.dev/reference/scopes/admin.conversations.write)

Start a new conversation, modify a conversation and modify channel details

User

[`admin.invites:read`](https://docs.slack.dev/reference/scopes/admin.invites.read)

View a workspace's invites and invite requests

User

[`admin.invites:write`](https://docs.slack.dev/reference/scopes/admin.invites.write)

Invite members to a workspace and approve or deny invitation requests

User

[`admin.roles:read`](https://docs.slack.dev/reference/scopes/admin.roles.read)

List role assignments for your workspace.

User

[`admin.roles:write`](https://docs.slack.dev/reference/scopes/admin.roles.write)

Add and remove role assignments for your workspace.

User

[`admin.skills:read`](https://docs.slack.dev/reference/scopes/admin.skills.read)

View all Slackbot skills in an organization

User

[`admin.skills:write`](https://docs.slack.dev/reference/scopes/admin.skills.write)

Publish and deploy Slackbot skills in an organization

User

[`admin.teams:read`](https://docs.slack.dev/reference/scopes/admin.teams.read)

Access information about a workspace

User

[`admin.teams:write`](https://docs.slack.dev/reference/scopes/admin.teams.write)

Make changes to a workspace

User

[`admin.usergroups:read`](https://docs.slack.dev/reference/scopes/admin.usergroups.read)

Access information about user groups

User

[`admin.usergroups:write`](https://docs.slack.dev/reference/scopes/admin.usergroups.write)

Make changes to your usergroups

User

[`admin.users:read`](https://docs.slack.dev/reference/scopes/admin.users.read)

Access a workspace's profile information

User

[`admin.users:write`](https://docs.slack.dev/reference/scopes/admin.users.write)

Modify account information

User

[`admin.workflows:read`](https://docs.slack.dev/reference/scopes/admin.workflows.read)

View all workflows in a workspace

User

[`admin.workflows:write`](https://docs.slack.dev/reference/scopes/admin.workflows.write)

Manage workflows in a workspace

User

[`app_configurations:read`](https://docs.slack.dev/reference/scopes/app_configurations.read)

Read app configuration info via App Manifest APIs. When used by a manager app, access is restricted to apps created by that manager app.

Configuration

[`app_configurations:write`](https://docs.slack.dev/reference/scopes/app_configurations.write)

Create apps and write app configuration info via App Manifest APIs. When used by a manager app, access is restricted to apps created by that manager app.

Configuration

[`app_mentions:read`](https://docs.slack.dev/reference/scopes/app_mentions.read)

View messages that directly mention your Slack app in conversations that the app is in

BotLegacy Bot

[`assistant:write`](https://docs.slack.dev/reference/scopes/assistant.write)

Allow your Slack app to act as an App Agent

BotLegacy Bot

[`auditlogs:read`](https://docs.slack.dev/reference/scopes/auditlogs.read)

View events from all workspaces, channels and users (Enterprise orgs only)

User

[`authorizations:read`](https://docs.slack.dev/reference/scopes/authorizations.read)

Grants permission to list authorizations associated with the Events API

App-level

[`bookmarks:read`](https://docs.slack.dev/reference/scopes/bookmarks.read)

List bookmarks

BotUserLegacy Bot

[`bookmarks:write`](https://docs.slack.dev/reference/scopes/bookmarks.write)

Create, edit, and remove bookmarks

BotUserLegacy Bot

[`bot`](https://docs.slack.dev/reference/scopes/bot)

Add the ability for people to direct message or mention @your\_slack\_app

Legacy Bot

[`calls:read`](https://docs.slack.dev/reference/scopes/calls.read)

View information about ongoing and past calls

BotUserLegacy Bot

[`calls:write`](https://docs.slack.dev/reference/scopes/calls.write)

Start and manage calls in a workspace

BotUserLegacy Bot

[`canvases:read`](https://docs.slack.dev/reference/scopes/canvases.read)

Access contents of canvases created inside Slack.

BotUserLegacy Bot

[`canvases:write`](https://docs.slack.dev/reference/scopes/canvases.write)

your Slack app will be able to create, edit and remove canvases, Create, edit and remove canvases

BotUser

[`channels:history`](https://docs.slack.dev/reference/scopes/channels.history)

View messages and other content in public channels that your Slack app has been added to

BotUserLegacy Bot

[`channels:join`](https://docs.slack.dev/reference/scopes/channels.join)

Join public channels in a workspace

BotLegacy Bot

[`channels:manage`](https://docs.slack.dev/reference/scopes/channels.manage)

Manage public channels that your Slack app has been added to and create new ones

BotLegacy Bot

[`channels:read`](https://docs.slack.dev/reference/scopes/channels.read)

View basic information about public channels in a workspace

BotUserLegacy Bot

[`channels:write`](https://docs.slack.dev/reference/scopes/channels.write)

Manage a user's public channels and create new ones on a user's behalf

User

[`channels:write.invites`](https://docs.slack.dev/reference/scopes/channels.write.invites)

Invite members to public channels

BotUserLegacy Bot

[`channels:write.topic`](https://docs.slack.dev/reference/scopes/channels.write.topic)

Set the description of public channels

BotUserLegacy Bot

[`chat:write`](https://docs.slack.dev/reference/scopes/chat.write)

Send messages as your Slack app

BotUser

[`chat:write.customize`](https://docs.slack.dev/reference/scopes/chat.write.customize)

Send messages as your Slack app with a customized username and avatar

BotLegacy Bot

[`chat:write.public`](https://docs.slack.dev/reference/scopes/chat.write.public)

Send messages to channels your Slack app isn't a member of

BotLegacy Bot

[`client`](https://docs.slack.dev/reference/scopes/client)

Receive all events from a workspace in real time

[`code_channels:manage`](https://docs.slack.dev/reference/scopes/code_channels.manage)

Create and manage code channels and their properties

Bot

[`commands`](https://docs.slack.dev/reference/scopes/commands)

Add shortcuts and slash commands that people can use

Bot

[`connections:write`](https://docs.slack.dev/reference/scopes/connections.write)

Grants permission to generate websocket URIs and connect to Socket Mode

App-level

[`conversations.connect:manage`](https://docs.slack.dev/reference/scopes/conversations.connect.manage)

Allows your Slack app to manage Slack Connect channels

BotLegacy Bot

[`conversations.connect:read`](https://docs.slack.dev/reference/scopes/conversations.connect.read)

Receive Slack Connect invite events sent to the channels your Slack app is in

BotLegacy Bot

[`conversations.connect:write`](https://docs.slack.dev/reference/scopes/conversations.connect.write)

Create Slack Connect invitations for channels that your Slack app has been added to, and accept invitations sent to your Slack app

BotLegacy Bot

[`datastore:read`](https://docs.slack.dev/reference/scopes/datastore.read)

View and see data from Slack App Datastore

BotLegacy Bot

[`datastore:write`](https://docs.slack.dev/reference/scopes/datastore.write)

Write data to Slack App Datastore

BotLegacy Bot

[`dnd:read`](https://docs.slack.dev/reference/scopes/dnd.read)

View Do Not Disturb settings for people in a workspace

BotUser

[`dnd:write`](https://docs.slack.dev/reference/scopes/dnd.write)

Edit a user's Do Not Disturb settings

User

[`email`](https://docs.slack.dev/reference/scopes/email)

View a user's email address

User

[`emoji:read`](https://docs.slack.dev/reference/scopes/emoji.read)

View custom emoji in a workspace

BotUserLegacy Bot

[`files:read`](https://docs.slack.dev/reference/scopes/files.read)

View files shared in channels and conversations that your Slack app has been added to

BotUserLegacy Bot

[`files:write`](https://docs.slack.dev/reference/scopes/files.write)

Upload, edit, and delete files as your Slack app

BotUser

[`groups:history`](https://docs.slack.dev/reference/scopes/groups.history)

View messages and other content in private channels that your Slack app has been added to

BotUserLegacy Bot

[`groups:read`](https://docs.slack.dev/reference/scopes/groups.read)

View basic information about private channels that your Slack app has been added to

BotUserLegacy Bot

[`groups:write`](https://docs.slack.dev/reference/scopes/groups.write)

Manage private channels that your Slack app has been added to and create new ones

BotUserLegacy Bot

[`groups:write.invites`](https://docs.slack.dev/reference/scopes/groups.write.invites)

Invite members to private channels

BotUserLegacy Bot

[`groups:write.topic`](https://docs.slack.dev/reference/scopes/groups.write.topic)

Set the description of private channels

BotUserLegacy Bot

[`hosting:read`](https://docs.slack.dev/reference/scopes/hosting.read)

View and see information about Slack apps

User

[`identify`](https://docs.slack.dev/reference/scopes/identify)

View information about a user's identity

User

[`im:history`](https://docs.slack.dev/reference/scopes/im.history)

View messages and other content in direct messages that your Slack app has been added to

BotUserLegacy Bot

[`im:read`](https://docs.slack.dev/reference/scopes/im.read)

View basic information about direct messages that your Slack app has been added to

BotUserLegacy Bot

[`im:write`](https://docs.slack.dev/reference/scopes/im.write)

Start direct messages with people

BotUserLegacy Bot

[`im:write.topic`](https://docs.slack.dev/reference/scopes/im.write.topic)

Set the description in direct messages

BotUserLegacy Bot

[`incoming-webhook`](https://docs.slack.dev/reference/scopes/incoming-webhook)

Post messages to specific channels in Slack

BotLegacy Bot

[`links:read`](https://docs.slack.dev/reference/scopes/links.read)

View URLs in messages

BotUserLegacy Bot

[`links:write`](https://docs.slack.dev/reference/scopes/links.write)

Show previews of URLs in messages

BotUserLegacy Bot

[`links.embed:write`](https://docs.slack.dev/reference/scopes/links.embed.write)

Embed video player URLs in messages and app surfaces

BotUser

[`lists:read`](https://docs.slack.dev/reference/scopes/lists.read)

View Slack Lists

BotUser

[`lists:write`](https://docs.slack.dev/reference/scopes/lists.write)

Create, edit, and delete Slack Lists

BotUser

[`managed_apps:install`](https://docs.slack.dev/reference/scopes/managed_apps.install)

Install managed child apps on workspaces

BotUser

[`mcp:connect`](https://docs.slack.dev/reference/scopes/mcp.connect)

Allows your Slack app to connect to Slack AI features through Model Context Protocol (MCP) servers

Bot

[`metadata.message:read`](https://docs.slack.dev/reference/scopes/metadata.message.read)

Allows your Slack app to read message metadata in channels that your Slack app has been added to

BotLegacy Bot

[`mpim:history`](https://docs.slack.dev/reference/scopes/mpim.history)

View messages and other content in group direct messages that your Slack app has been added to

BotUserLegacy Bot

[`mpim:read`](https://docs.slack.dev/reference/scopes/mpim.read)

View basic information about group direct messages that your Slack app has been added to

BotUserLegacy Bot

[`mpim:write`](https://docs.slack.dev/reference/scopes/mpim.write)

Start group direct messages with people

UserLegacy Bot

[`mpim:write.topic`](https://docs.slack.dev/reference/scopes/mpim.write.topic)

Set the description in group direct messages

BotUserLegacy Bot

[`openid`](https://docs.slack.dev/reference/scopes/openid)

View information about a user's identity

User

[`pins:read`](https://docs.slack.dev/reference/scopes/pins.read)

View pinned content in channels and conversations that your Slack app has been added to

BotUserLegacy Bot

[`pins:write`](https://docs.slack.dev/reference/scopes/pins.write)

Add and remove pinned messages and files

BotUserLegacy Bot

[`profile`](https://docs.slack.dev/reference/scopes/profile)

View a user's Slack avatar and Slack workspace's basic information

User

[`reactions:read`](https://docs.slack.dev/reference/scopes/reactions.read)

View emoji reactions and their associated content in channels and conversations that your Slack app has been added to

BotUserLegacy Bot

[`reactions:write`](https://docs.slack.dev/reference/scopes/reactions.write)

Add and edit emoji reactions

BotUserLegacy Bot

[`reminders:read`](https://docs.slack.dev/reference/scopes/reminders.read)

View reminders created by your Slack app

BotUserLegacy Bot

[`reminders:write`](https://docs.slack.dev/reference/scopes/reminders.write)

Add, remove, or mark reminders as complete

BotUserLegacy Bot

[`remote_files:read`](https://docs.slack.dev/reference/scopes/remote_files.read)

View remote files added by the app in a workspace

BotUserLegacy Bot

[`remote_files:share`](https://docs.slack.dev/reference/scopes/remote_files.share)

Share remote files on a user's behalf

BotUserLegacy Bot

[`remote_files:write`](https://docs.slack.dev/reference/scopes/remote_files.write)

Add, edit, and delete remote files on a user's behalf

BotLegacy Bot

[`search:read`](https://docs.slack.dev/reference/scopes/search.read)

Search a workspace's content

User

[`search:read.enterprise`](https://docs.slack.dev/reference/scopes/search.read.enterprise)

Search content in your enterprise.

BotLegacy Bot

[`search:read.files`](https://docs.slack.dev/reference/scopes/search.read.files)

Search a workspace's content in files

BotLegacy BotUser

[`search:read.im`](https://docs.slack.dev/reference/scopes/search.read.im)

Search a workspace's content in direct messages

User

[`search:read.mpim`](https://docs.slack.dev/reference/scopes/search.read.mpim)

Search a workspace's content in group direct messages

User

[`search:read.private`](https://docs.slack.dev/reference/scopes/search.read.private)

Search a workspace's content in private channels

User

[`search:read.public`](https://docs.slack.dev/reference/scopes/search.read.public)

Search a workspace's content in public channels

BotUser

[`search:read.users`](https://docs.slack.dev/reference/scopes/search.read.users)

Search a workspace's users

BotUser

[`skills:read`](https://docs.slack.dev/reference/scopes/skills.read)

View Slackbot skills a user or app can access

BotUser

[`skills:write`](https://docs.slack.dev/reference/scopes/skills.write)

Create, edit, and remove Slackbot skills as a user or app, and manage their skill library

BotUser

[`stars:read`](https://docs.slack.dev/reference/scopes/stars.read)

View a user's starred messages and files

User

[`stars:write`](https://docs.slack.dev/reference/scopes/stars.write)

Add or remove stars for a user

User

[`team:read`](https://docs.slack.dev/reference/scopes/team.read)

View the name, email domain, and icon for workspaces your Slack app is connected to

BotUser

[`team.billing:read`](https://docs.slack.dev/reference/scopes/team.billing.read)

Allows your Slack app to read the billing plan for workspaces your Slack app has been installed to

BotUserLegacy Bot

[`team.preferences:read`](https://docs.slack.dev/reference/scopes/team.preferences.read)

Allows your Slack app to read the preferences for workspaces your Slack app has been installed to

BotUserLegacy Bot

[`tokens.basic`](https://docs.slack.dev/reference/scopes/tokens.basic)

Execute methods without needing a scope

UserBotLegacy Bot

[`triggers:read`](https://docs.slack.dev/reference/scopes/triggers.read)

Read new Platform triggers

Bot

[`triggers:write`](https://docs.slack.dev/reference/scopes/triggers.write)

Create new Platform triggers

Bot

[`usergroups:read`](https://docs.slack.dev/reference/scopes/usergroups.read)

View user groups in a workspace

BotUserLegacy Bot

[`usergroups:write`](https://docs.slack.dev/reference/scopes/usergroups.write)

Create and manage user groups

BotUserLegacy Bot

[`users:read`](https://docs.slack.dev/reference/scopes/users.read)

View people in a workspace

BotUserLegacy Bot

[`users:read.email`](https://docs.slack.dev/reference/scopes/users.read.email)

View email addresses of people in a workspace

BotUserLegacy Bot

[`users:write`](https://docs.slack.dev/reference/scopes/users.write)

Set presence for your Slack app

BotUserLegacy Bot

[`users.profile:read`](https://docs.slack.dev/reference/scopes/users.profile.read)

View profile details about people in a workspace

BotUserLegacy Bot

[`users.profile:write`](https://docs.slack.dev/reference/scopes/users.profile.write)

Edit a user's profile information and status

User

[`workflows.templates:read`](https://docs.slack.dev/reference/scopes/workflows.templates.read)

Manage Slack workflow template on user's behalf

BotUser

[`workflows.templates:write`](https://docs.slack.dev/reference/scopes/workflows.templates.write)

Write Slack workflow template on user's behalf

BotUser

 [Search](https://docs.slack.dev/search)