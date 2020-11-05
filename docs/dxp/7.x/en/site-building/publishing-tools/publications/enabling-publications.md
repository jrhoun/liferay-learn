# Enabling Publications

Publications provides a convenient and flexible way for you and your teams to develop, track, and publish changes to your DXP instance. When enabled, Publications is activated globally and can be accessed anywhere to edit supported entities in your instance.

```important::
   Staging and Publications cannot be enabled at the same time. If Staging is enabled on any of your Sites, you must first disable Staging before enabling Publications. See `Disabling Local Live Staging <../staging/configuring-local-live-staging.html#disabling-local-live-staging>`_ and `Disabling Remote Live Staging <../staging/configuring-remote-live-staging.html#disabling-remote-live-staging>`_ for more information.
```

## How to Enable Publications

1. Go to the _Global Menu_ (![Global Menu](../../../images/icon-applications-menu.png)) and click on _Settings_ under _Publications_.

    ![In the Global Menu, click on Settings under Publications.](./enabling-publications/images/01.png)

1. Set the toggle switch to _Yes_ to enable Publications for your DXP instance.

1. Click on _Submit_ to save your configuration.

    Alternatively, you can click on _Save and Go to Overview_, which saves your configuration and redirects you to the Publications overview page.

    ![Set the Toggle to Yes and click on Submit or Save and Go to Overview.](./enabling-publications/images/02.png)

Once enabled, you can access the drop-down Publications bar menu from any page in your DXP instance. You can use this menu to create new publications, select which publication you want to work on, switch between edit and production modes, and review and publish your select publication's changes, either immediately or at a later time. See [Creating and Managing Publications](./creating-and-managing-publications.md) to learn about creating, editing, and removing individual publications.

## How to Disable Publications

Once enabled, you can disable Publications at any time, via the Publications _Settings_ page. Set the toggle switch to _No_ and then click on _Submit_.

```important::
   Once disabled, all active publications are deactivated, scheduled publications are canceled, and you can no longer access your publication history. DXP, however, retains your instance's publication history, so you can access it again if you re-enable Publications.
```

## Additional Information

-   [Publications Overview](./publications-overview.md)
-   [Creating and Managing Your Publications](./creating-and-managing-your-publications.md)
-   [Making and Publishing Changes](./making-and-publishing-changes.md)
