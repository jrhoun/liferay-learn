# Setting Catalog Permissions

Users can set permissions for the entire catalog. Although users cannot set permissions for individual products, they can instead [use channels](../creating-and-managing-products/channels/introduction-to-channels.md) to display specific products to specific customers.

Setting a Catalog's permissions require access to the Control Panel. A user's role must have the necessary permissions to do so; to define a user's permission, see [Defining Role Permissions](https://learn.liferay.com/dxp/7.x/en/users-and-permissions/roles-and-permissions/defining-role-permissions.html).

## Assigning the Necessary Permissions

Users can [create a custom role](../../account-management) or modify an existing Role.

To define Permissions for a new Catalog Manager Role:

1. Navigate to the _Control Panel_ &rarr; _Users_ &rarr; _Roles_.
1. Click the (![Add icon](../../images/icon-add.png)) to add a new Regular Role.
1. Enter the following:

     * **Title**: Catalog Manager.
     * **Description** This role manages catalogs.
     * **Key**: (auto-generated based on the title)

1. Click _Save_.
1. Click _Define Permissions_.
1. Click the _Control Panel_ &rarr; _Commerce_ to expand the dropdown menu.

    ![Navigate to Commerce Catalogs Permissions.](./setting-catalog-permissions/images/03.png)

1. Click _Catalogs_.
1. Select the desired Permissions; at the very least, all _General Permissions_ and _Resource Permissions_.

    ![Select Catalogs Permissions.](./setting-catalog-permissions/images/04.png)

1. Click _Save_.
1. Click the _Products_ dropdown menu.

    ![Navigate to Commerce Products Permissions.](./setting-catalog-permissions/images/05.png)

1. Select the desired Permissions; at the very least, all _General Permissions_ and _Resource Permissions_.
1. Click _Save_ when finished.

The new Catalog Manager role received the minimum connections to view the Catalog and Products menu. Users with this role are now able to access the _Control Panel_ &rarr; _Commerce_ &rarr; _Catalogs_ and _Products_ menus.

## Configuring a Catalog's Permissions

Follow the steps below to set a catalog's permissions:

1. Navigate to the _Control Panel_ &rarr; _Commerce_ &rarr; _Catalogs_.
1. Click the (![3-dot icon](../../images/icon-actions.png)) then _Permissions_.

    ![Users can edit Permissions.](./setting-catalog-permissions/images/01.png)

1. Click the desired permissions for the applicable roles.

    ![Select the desired permissions.](./setting-catalog-permissions/images/02.png)

1. Click _Save_ when finished.

The catalog's permissions are now configured.

## Additional Information

* [Understanding Roles and Permissions](https://learn.liferay.com/dxp/7.x/en/users-and-permissions/roles-and-permissions/understanding-roles-and-permissions.html)
* [Configuring Product Visibility Using Channels](../creating-and-managing-products/channels/configuring-product-visibility-using-channels.md)
