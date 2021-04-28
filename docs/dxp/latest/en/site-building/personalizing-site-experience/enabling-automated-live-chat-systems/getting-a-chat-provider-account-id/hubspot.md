# Hubspot

[Hubspot](https://www.hubspot.com/) is a CRM platform that includes Live Chat functionality. Enabling integration with Hubspot requires two tokens: the Chat Provider Token and the Hubspot API Token.

## Locating the Chat Provider Token

1. Log in to your [Hubspot Account](https://app.hubspot.com/login).

1. Go to your profile in the top right corner.

    Copy the account number that corresponds to the channel you want to use. This number corresponds with the Account ID used when enabling Click to Chat on Liferay Portal.

    ![Id token](./hubspot/images/01.png)

## Getting the Hubspot API Token



While logged in to your Hubspot account:

1. Click the *Settings* button.

    ![Settings](./hubspot/images/02.png)

2. Click on *Integrations* &rarr; *API Key* on the left side of the page.

    ![Api Key](./hubspot/images/03.png)

3. During your first acess you need to activate the API Key. Click *Actions* &rarr; *Generate*

    ![Active API Key](./hubspot/images/04.png)
   

    3.1 If you are not able to see your API Key, click *Show* to reveal it.

    ![Show API Key](./hubspot/images/05.png) 

4. Your account ID is **ID Tolken/API Key**. 

    ![Account ID](./hubspot/images/06.png)
   
5. Use this Account ID to [enable automated live chat integration](../enabling-automated-live-chat-systems.md) with your Liferay instance. 
