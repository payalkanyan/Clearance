##### Table of Contents

# Authorization through OAuth 2.0

Before setting up any integration with the Boltrics Solution, OAuth2.0 authorization must be configured. This Learn page provides guidance for setting up **OAuth2 authentication via Azure** (including App Registrations and Client Secrets). Alternatively, you can set up OAuth2.0 through another service.

There are two authentication methods possible:

- **Service-to-Service (Client Credentials)**\-\- an integration runs as an application (no user)

  - **Use:** For automated processes such as daily operations and automatic refreshing
  - **Requirements:** 1) App registration in Microsoft Entra ID and 2) Registration of the Entra App in Business Central
- **User Delegated (Authorization Code)**\-\- an integration runs on behalf of a signed-in user

  - **Use:** For user-initiated activities such as testing
  - **Requirements:** 1) App registration in Microsoft Entra ID and 2) configuration of User Permissions in Business Central

* * *

## In Microsoft Entra ID [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#in-microsoft-entra-id)

##### Tip

**Best Practice:** Create a dedicated permission set for each type of authorization (user vs client credential) and for each integration.

#### Create the App [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#create-the-app)

1. Go to **Microsoft Entra ID** and open **App registrations**.
2. Select **New registration**.
3. Fill in:
   - **Name** (e.g. _MyIntegration_)
   - **Supported account types** (typically _Single tenant_)
   - **Redirect URI** with **Web** as the platform (S2S requires a specific format; see the Microsoft Learn resource below)
4. Click **Register**.
5. Copy and store:
   - **Application (Client) ID**
   - **Directory (Tenant) ID**

**Microsoft Learn Resources:**

- General: [How to register an app in Microsoft Entra ID - Microsoft identity platform \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)
- Service-to-Service: [Using Service to Service Authentication - Business Central \| Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/automation-apis-using-s2s-authentication)
- Adding Redirect URI _after_ registration: [How to add a redirect URI to your application - Microsoft identity platform \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri)


#### Next Steps per Authentication Type [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#next-steps-per-authentication-type)

Click the ▶ for your type of authentication of choice for the next steps and/or key information.

User Delegated (Authorization Code)

#### Add App Permissions [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#add-app-permissions)

Go to **API permissions** and add Business Central permissions:

- Add **Delegated permissions**
- Permissions are enforced through the signed-in user
- **Microsoft Learn Resource:** [Web API app registration and API permissions - Microsoft identity platform \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis)

**Next: open the User Delegated section under Business Central below.**

Service-to-Service (Client Credentials)

#### Add App Permissions [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#add-app-permissions-1)

Go to **API permissions** and add Business Central permissions.

- Add **Application permissions**
- Click **Grant admin consent** (required)
- **Microsoft Learn Resource:** [Web API app registration and API permissions - Microsoft identity platform \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis)


#### Create Credentials [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#create-credentials)

For Client Credentials you need a credential:

- **Certificates** (recommended for production), or
- **Client secret** (easier for testing, higher risk)

Go to **Certificates & secrets** and add a certificate or create a client secret.

- **Microsoft Learn Resource:** [Add and manage app credentials in Microsoft Entra ID - Microsoft identity platform \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=certificate)

**Next: open the Service-to-Service section under Business Central below.**

* * *

## In Business Central [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#in-business-central)

Click the ▶ for your type of authentication of choice for the next steps and/or key information.

User Delegated (Authorization Code)

❌ You do **NOT** register the app in Business Central

- Permissions are determined by:
  - the user's BC license
  - the user's permission sets
- For more information, read this Boltrics blog: [Give your users access to the right actions using user permissions - Boltrics](https://www.boltrics.com/en/2023/02/23/blog-give-your-users-access-to-the-right-actions-using-user-permissions/)

##### Caution

- A **limited user** will typically **NOT** work for integration/API scenarios. If the user lacks rights, calls fail — even if the token is valid.
- Avoid overly broad rights; give the user only what is needed.

Service-to-Service (Client Credentials)

#### Why Business Central Needs an "Entra Application" Record [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#why-business-central-needs-an-entra-application-record)

When using **Client Credentials**, Business Central receives an access token that represents an **application identity** (not a person). Because there is no user account to determine permissions from, Business Central needs an internal mapping:

**Azure App Registration (Client ID) → Business Central permission sets**

This mapping is the **security boundary** for integrations: without it, the app can authenticate in Entra ID, but Business Central won't know what it is allowed to do. The mapping is configured via **Microsoft Entra Applications**.

#### Step 1: Register the Application in Business Central [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#step-1-register-the-application-in-business-central)

**Note:** Make sure you have set up a Redirect URI in your Microsoft Entra app.

|     |     |
| --- | --- |
| 1. In Business Central, search for **Microsoft Entra Applications**.<br>2. Create a new record.<br>3. Enter the **Client ID** from the Entra App Registration.<br>4. Add a clear description (e.g. _Boltrics DataHub Integration_).<br>5. Set **State** to **Enabled**.<br>6. Click **Grant Consent**. | ![](https://learn.boltrics.com/media/Integrations/EntraApplications.png) |

This creates the required link between **Azure Entra ID** and **Business Central**.

#### Step 2: Assign Permission Sets [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#step-2-assign-permission-sets)

After registration, assign permission sets that define what the integration may do.

Examples:

- Read/write specific WMS tables
- Execute specific Codeunits, including DIPost.

**Customer Responsibility**

The customer is responsible for:

- defining permission sets
- assigning them to the Entra application
- ongoing security review

Boltrics provides the integration platform; **security configuration stays with the environment owner**.

##### Caution

⛔ **Do NOT assign Super permissions to a service-to-service application.**

With SUPER, an integrated party can:

- read/modify/delete all data
- call any API endpoint
- access sensitive financial and operational information

If credentials are compromised, the impact is **full environment exposure**.

##### Tip

**Principles of Least Privilege:** Create a dedicated permission set per integration and only include:

- the required tables
- the required Codeunits
- the required API objects

This limits blast radius if credentials leak or misuse occurs.

* * *

## Test Using Boltrics' Postman Collections [Anchor](https://learn.boltrics.com/appIntegration/core/AuthorizationOAuth2.html\#test-using-boltrics-postman-collections)

Once authentication has been set up, you can test if it works using Boltrics' Postman Collections. Find more information on the **Boltrics Postman Collections** Learn page.

[Edit this page](https://dev.azure.com/boltrics2/Learn/_git/Documentation?path=Documentation/appIntegration/core/AuthorizationOAuth2.md&version=GBmaster&line=1)

Next [Analytics API](https://learn.boltrics.com/appIntegration/AnalyticsAPI.html)