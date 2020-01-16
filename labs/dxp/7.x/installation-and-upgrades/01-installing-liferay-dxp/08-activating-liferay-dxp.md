# Activating Liferay DXP

> Subscription Required

On starting Liferay DXP for the first time, DXP prompts you to activate your Liferay DXP instance.

![Liferay DXP prompts you with this page to activate your DXP instance.](./activating-liferay-dxp/images/01.png)

There are two ways to activate a Liferay DXP instance:

* Using an XML activation key from [Liferay Support](https://help.liferay.com/hc/en-us).
* Online activation through Liferay Connected Services (LCS).

## Using an XML Key

To activate Liferay DXP using an XML activation key follow these steps:

1. Request a Liferay DXP activation key by opening a [Help Center](https://liferay-support.zendesk.com/agent/) ticket.

1. The Liferay Provisioning Team provides instructions on how to download the activation key.

    > **Note:** that the activation key is tied to a particular server. To migrate an existing key to a different server, please contact the Liferay Support Team by opening a [Help Center](https://liferay-support.zendesk.com/agent/) ticket.

1. Deploy the activation key in the `[LIFERAY_HOME]/deploy` folder.

1. Verify that the success message appears in the console.

    <!-- ```
    success message example
    ``` -->

1. Once the activation key has been applied, this instance has been registered.

Liferay DXP is now ready to be used with your enterprise subscription.

## Using Liferay Connected Services

Liferay DXP 7.0 introduced Liferay Connected Services (LCS) as a way to activate Liferay DXP instances. LCS can also install fix packs, monitor each instance's performance, and help administrators automatically manage Liferay DXP subscriptions. See the [LCS documentation](https://help.liferay.com/hc/articles/360029032071-Introduction-to-Managing-Liferay-DXP-with-Liferay-Connected-Services) for instructions on activating the instances with LCS.

> **Note:** Administrators must use LCS for activation of Elastic subscriptions. Otherwise, LCS for activation is optional. Instead request an XML activation key from Liferay Support.

To learn how to activate Liferay DXP using LCS see [this article](https://help.liferay.com/hc/articles/360029032071-Introduction-to-Managing-Liferay-DXP-with-Liferay-Connected-Services).

## Next Steps 

* [Securing Liferay DXP](../05-securing-liferay/01-securing-liferay.md)
* [Configuring Clustering for High Availability](../02-setting-up-liferay-dxp/01-performance-and-scalability/01-configuring-clustering/01-introduction-to-clustering-liferay-dxp.md)
* Maintaining Liferay DXP
