# Configuring Local Live Staging

With Local Live Staging, both your Staging and Live environments are hosted on the same Liferay server. When enabled, Liferay DXP creates a local clone of your Site that serves as the Staging environment, while your original instance becomes your Live environment.

Both environments share the same JVM, database, selected application data, and configurations, such as properties set in the `portal-ext.properties` file.

-   [Setting Up Local Live Staging](#setting-up-local-live-staging)
-   [Disabling Local Live Staging](#disabling-local-live-staging)

## Setting Up Local Live Staging

Follow these steps to set up Local Live Staging for your DXP instance:

1. Go to _Product Menu_ &rarr; _Publishing_ &rarr; _Staging_.

    ![Go to Staging in the Product menu.](./configuring-local-live-staging/images/01.jpg)

1. Select _Local Live_, which reveals additional fields for _Page Versioning_ and _Staged Content_.

    ![Select Local Live.](./configuring-local-live-staging/images/02.png)

1. Select whether you want _Page Versioning_ enabled on Public and/or Private Page sets.

    ![Enable Page Versioning for your Private and Public Page sets.](./configuring-local-live-staging/images/03.png)

1. Select the _data_ and _content_ types you want to stage.

    ![Select the data and content types you want to stage.](./configuring-local-live-staging/images/04.png)

    ```warning::
       When applications are checked, their data is copied to Staging, and it may not be possible to edit them directly in Live. When unchecking an application, first make sure that any changes in Staging are published, since they may be lost. See `Managing Data and Content Types in Staging <./managing-data-and-content-types-in-staging.md>`_ for more information.
    ```

1. Click on _Save_ to initiate the cloning process. The duration of this process depends on the size of your Site.

    ```tip::
       Stage your Site early on to reduce cloning time and record a more complete history of your Site's update history, since updates are only recorded once you enable Page Versioning.
    ```

Once the process is complete, you are ready to use Local Live Staging. See [Staging UI Reference](./staging-ui-reference.md) for information about navigating the Staging environment's publishing features.

## Disabling Local Live Staging

If for any reason you must disable Staging for your Site, you can do that from your staging environment. However, be aware that disabling Local Live Staging deletes the Staging environment, along with all unpublished content. For this reason, ensure all necessary information is published or preserved elsewhere before disabling Staging. This process may take some time, depending on the size of your Staging environment. It's best not to disable staging when your DXP instance is busy.

Follow these steps to disable Local Live Staging:

1. Open the Product Menu in your Staging environment, and go to _Publishing_ &rarr; _Staging_.

1. Click on the _Actions_ button ( ![Actions button](./../../images/icon-actions.png) ) located in the _Application_ bar, and select _Staging Configuration_.

1. Select _None_ for your Staging configuration, and click on _Save_.

## Additional Information

-   [Staging Overview](./staging-overview.md)
-   [Staging UI Reference](./staging-ui-reference.md)
-   [Managing Data and Content Types in Staging](./managing-data-and-content-types-in-staging.md)
-   [Managing Staging Permissions](./managing-staging-permissions.md)
