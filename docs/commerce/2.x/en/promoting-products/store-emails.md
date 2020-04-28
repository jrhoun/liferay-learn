# Store Emails

Liferay Commerce can be configured to send email notifications that are triggered by a variety of store events. Email notifications are comprised of templates that define the content of the email. Notifications can be flexibly configured. A single event trigger (store order) can send emails to different target audiences (a customer, a sales agent, an administrator) and use templates specific to each party.

```note::
   To use Liferay Commerce's Notifications feature, system administrators first have to configure the Mail settings for Liferay Digital Experience Platform (DXP). See `Connecting to a Mail Server <https://learn.liferay.com/dxp-7.x/installation-and-upgrades/setting-up-liferay-dxp/configuring-mail/connecting-to-a-mail-server.html>`_ for more information.
```

## Configuring Store Emails

Email notifications are configured per [channel](../managing-a-catalog/creating-and-managing-products/channels/introduction-to-channels.md).<!-- is this supposed to tell me where I should go to configure store emails? --> Using an [accelerator](../starting-a-store/accelerators.md) creates a store, catalog, and channel for you to start with.

![Available Notification Templates](./store-emails/images/02.png)

## Using Notification Templates When Events are Triggered
<!-- This header implies that it will tell people how to use notification templates, but really it is just a reference. -->
The following Notification Templates are available out of the box.

| Notification Type | Event |
| --- | ---|
| Order Placed | The store has received an order. |
| Order Processing | The store has begun processing an order. |
| Order Awaiting Shipment | The order is ready to be shipped. |
| Order Partially Shipped | The customer is notified if the items are being shipped separately. |
| Order Shipped | The order has been shipped. |
| Order Completed | The order has been completed; delivery has been made. |
| Subscription Renewed | The subscription (recurring order) has been renewed. |
| Subscription Activated | The subscription has been activated. |
| Subscription Suspended | The subscription has been suspending pending review or action by the store. |
| Subscription Cancelled | The subscription has been cancelled. |

![Available Notification Templates](./store-emails/images/01.png)

## Viewing the Notification Queue

All notification events are logged in the *Notification Queue* tab <!-- which is located where? -->. <!-- what events trigger a notification? this seems like it should be its own section, UNLESS the notification templates ALSO are the event triggers as well - in which case we need to make that fact clearer. --> By default, the system checks the queue at 15 minute intervals for unsent notifications. See [Configuring the Commerce Notification Queue](./configuring-the-commerce-notification-queue.md) article to learn more about changing the Check Interval.

![Message Queues](./store-emails/images/03.png)

## Using Placeholder Values in an Email Notification Template
<!-- What's more important to someone to know here than jumping right into the placeholder value/variables? I think it would be to be sure we present the idea that the email templates are configurable/customizable - meaning - you can write your own content for them. AND THEN - Oh by the way you can use these variables/tokens/whatever to make it easier and more personalized to customize these email notifications. In other words - the way this is written makes the placeholder variables sound like the main feature - when I think the main feature is, You can customize the email templates, and a sub-feature of that is you can use placeholder values to make that easier/faster. -->
Liferay Commerce includes placeholder values that you can insert as a substitute for key values in the Notification Template's _Email Settings_ and _Body_ fields when creating an Email Notification Template. Key values include a customer's name, the Order ID, shipping and billing addresses, and a list of items in the order.

For example, the Email Body field can contain:

```note::
   Dear [%ORDER_CREATOR%],

   Your [%ORDER_ID%] has been shipped to [%ORDER_SHIPPING_ADDRESS%].
```

The Notification Template then parses those variables when sending the email.

See the [Notification Template Variables Reference Guide](./notification-template-variables-reference-guide.md) article to learn more.

## Viewing Order Communications History

Every order logs all related email notifications.<!-- needs more detail on how to get to this tab --> To view all the emails, navigate to an Order’s Email tab. See [Orders Information](../orders-and-fulfillment/orders/order-information.md) to learn more.

![Message Logs are in the Orders information.](./store-emails/images/04.png)

## Additional Information

* [Using Notification Templates](./using-notification-templates.md)
* [Configuring the Commerce Notification Queue](./configuring-the-commerce-notification-queue.md)
* [Notification Template Variables Reference Guide](./notification-template-variables-reference-guide.md)
