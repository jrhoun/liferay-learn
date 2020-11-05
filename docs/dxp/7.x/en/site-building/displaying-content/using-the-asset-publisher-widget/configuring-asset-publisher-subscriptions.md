# Configuring Asset Publisher Subscriptions

The Asset Publisher supports two kinds of subscriptions: email subscriptions and RSS feed subscriptions.

## Email Subscriptions

Users can subscribe to the Asset Publisher to receive email notifications when new assets are published. You must enable this notification first. Follow these steps:

1. Hover over the Asset Publisher and click the Options icon (![Options](../../../images/icon-app-options.png)) in the widget's menu and select _Configuration_.
1. Toggle the _Enable Email Subscription_ selector to Yes.
1. Fill in the form and click _Save_ to apply the changes.

    ![An email subscription notifies users when new assets are published.](./configuring-asset-publisher-subscriptions/images/01.png)

1. Enable the _Subscribe_ feature under the _Display Settings_ tab &rarr; [_Set and Enable_ section](./configuring-display-settings.md#set-and-enable-options) if it's not enabled. Users can click the _subscribe_ button to receive email notifications of newly published assets.

![Enabling Email Subscription adds a Subscribe link to the Asset Publisher.](./configuring-asset-publisher-subscriptions/images/02.png)

### Configuring the Asset Check Interval

Liferay Portal periodically checks for new assets and sends emails to subscribed users informing them about the new assets. By default, assets are checked every twenty-four hours. You can change the check interval through System Settings. Follow these steps:

1. Open the Product Menu and go to _Control Panel_ &rarr; _Configuration_ &rarr; _System Settings_.
1. Select _Assets_ under the _Content and Data_ heading.
1. Go to _System Scope_ &rarr; _Asset Publisher_.
1. Change the _Check Interval_ setting to the interval (in hours) that you want to check for new assets and notify subscribed users, and click _Save_ to apply the changes.

![The Check Interval settings specifies how often assets are checked for updates.](./configuring-asset-publisher-subscriptions/images/03.png)

## RSS Feed Subscriptions

```note::
  RSS feeds are deprecated for Liferay Portal 7.2+ and are disabled by default. To leverage RSS feeds, you must enable this feature.
```

To enable RSS feed subscriptions for the Asset Publisher, follow these steps:

1. Open the Product Menu and go to _Control Panel_ &rarr; _Configuration_ &rarr; _System Settings_.
1. Select _Web Content_ under the _Content and Data_ heading.
1. Under the _System Scope_ &rarr; _Administration_ tab, check the _Show Feeds_ box. For more information on deprecated apps, see [this article](TODO:deprecated-apps).

    ![Enable RSS feeds through System Settings.](./configuring-asset-publisher-subscriptions/images/04.png)

1. Navigate back to the Asset Publisher widget, hover over it and click the Options icon (![Options](../../../images/icon-app-options.png)) in the widget's menu and select _Configuration_.
1. Toggle the _Enable RSS Subscription_ selector to Yes.
1. Fill in the form and click _Save_ to apply the changes.

    ![An RSS subscription sends RSS feeds to subscribers' RSS readers.](./configuring-asset-publisher-subscriptions/images/05.png)

1. Enable the _Subscribe_ feature under the _Display Settings_ tab &rarr; [_Set and Enable_ section](./configuring-display-settings.md#set-and-enable-options) if it's not enabled. Users can click the _RSS_ link to subscribe to the RSS feed.

![Enabling RSS Subscription adds a RSS link to the Asset Publisher.](./configuring-asset-publisher-subscriptions/images/06.png)

## Related Information

-   [Setting up Email](../../../installation-and-upgrades/setting-up-liferay-dxp/configuring-mail/connecting-to-a-mail-server.md)
