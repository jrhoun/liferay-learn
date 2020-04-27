# Store Emails

Liferay Commerce includes a series of email notification templates which sends notifications when triggered by a variety of events. These notification templates can be used and reused for multiple events and multiple audiences. For example, when a order is placed, you can use the _Order Placed_ notification template to send one email to the buyer, a different email to the order administrator, and a third email to the sales agent who manages the account.

```note::
   To use Liferay Commerce's Notifications feature, system administrators first have to configure the Mail settings for Liferay Digital Experience Platform (DXP). See `Connecting to a Mail Server <https://learn.liferay.com/dxp-7.x/installation-and-upgrades/setting-up-liferay-dxp/configuring-mail/connecting-to-a-mail-server.html>`_ for more information.
```

## Store Email Configurations

Email notifications are configured per [channel](../managing-a-catalog/creating-and-managing-products/channels/introduction-to-channels.md). (If you had used an [accelerator like Minium](../starting-a-store/accelerators.md) to create your store, a corresponding channel has already been created.)

![Available Notification Templates](./store-emails/images/02.png)

## Notification Templates

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

## Message Queues

When an event triggers an notification (for example, an order is placed), the notification is placed temporarily in the _Notification Queue_ tab.

## Viewing Order Communications History

Every order logs all the related email notifications. To view all the emails, navigate to an Order’s Email tab. See [Orders Information](../orders-and-fulfillment/orders/order-information.md) to learn more.

## Additional Information

* [Using Notification Templates](./using-notification-templates.md)
* [Notification Template Variables Reference Guide](./notification-template-variables-reference-guide.md)
* [Configuring the Commerce Notification Queue](./configuring-the-commerce-notification-queue.md)
