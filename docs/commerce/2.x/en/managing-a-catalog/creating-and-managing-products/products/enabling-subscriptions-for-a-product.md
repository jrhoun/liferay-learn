# Enabling Subscriptions for a Product

Liferay Commerce allows store users to create and manage subscriptions to products. Example of subscriptions include (but are not limited to) magazines, service contracts with options to renew, and items consumed on a regular basis.

## Prerequisites

In order to enable subscriptions for a product, store administrators must activate a payment method that supports recurring payments. By default, Liferay Commerce supports [Paypal](../../../store-administration/configuring-payment-methods/paypal.md) as a recurring payment method.

## Enabling a Payment Subscription

Subscriptions can be enabled in a [Simple](../product-types/creating-a-simple-product.md), a [Grouped](../product-types/creating-a-grouped-product.md), or a [Virtual](../product-types/creating-a-virtual-product.md) Product. In this example, we are creating a Simple Product.

1. Create a [Simple](../product-types/creating-a-simple-product.md).
1. Enter the following:
    * **Catalog**: Sahara.com
    * **Name**: Multi-Vitamins

    ![Creating a simple product](./enabling-subscriptions-for-a-product/images/01.png)

1. Click the _Subscription_ tab when you have finished creating the product.

    ![Creating a simple product](./enabling-subscriptions-for-a-product/images/02.png)

1. Switch the toggle to _Enable_ in the Payment Subscription.
1. Select the _Month_ from the _Subscription Type_ dropdown menu.
1. Select _Order Date_ from the _Mode_ dropdown menu.
1. Enter _1_ from the _Subscription Length_ dropdown menu.
1. Switch the _Never Ends_ to _YES_.

    ![Configure payment subscription](./enabling-subscriptions-for-a-product/images/03.png)

1. Click the _Publish_ button.

A payment subscription has been enabled for this product.

To enable a Delivery Subscription:

1. Switch the toggle to _Enable_ in the Delivery Subscription.
1. Select the _Month_ from the _Subscription Type_ dropdown menu.
1. Select _Order Date_ from the _Mode_ dropdown menu.
1. Enter _1_ from the _Subscription Length_ dropdown menu.
1. Switch the _Never Ends_ to _YES_.

    ![Configure delivery subscription](./enabling-subscriptions-for-a-product/images/04.png)

1. Click the _Publish_ button.

A delivery subscription has been enabled for this product.

```tip::
   You can implement a custom payment method that has supports recurring methods. See `Implementing a New Payment Method <../../../developer-guide/tutorials/implementing-a-new-payment-method.md>`_ to learn more.
```

## Additional Information

* [Subscription Administration Reference Guide](../../../orders-and-fulfillment/subscription-administration-reference-guide.md)
* [Managing Subscriptions](../../../orders-and-fulfillment/managing-subscriptions.md)
