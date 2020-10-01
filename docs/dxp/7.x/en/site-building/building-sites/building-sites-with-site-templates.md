# Building Sites with Site Templates

Site Templates define a preconfigured structure for a Site, which includes the pages, theme, content, layouts, page templates, applications and app configurations defined for each page. Changes made to a Site Template are automatically propagated to the sites that use it, unless specified otherwise.

```note::
  While Site Templates propagate changes to a Site, they should not be used as a means of propagating Site data. To propagate Site data, `export the data and import it into another Site <./importing-exporting-pages-and-content.md>`_ instead.
```

Three Site Templates are provided out-of-the-box:

-   **Blank Site:** Creates a Site that doesn't contain any pages or content.

-   **Community Site:** Creates a preconfigured Site with the Message Boards, Search, Polls, Activities, and Wiki applications pre-deployed to site pages.

-   **Intranet Site:** Creates a preconfigured Site for an intranet. The Home page displays the activities of the members of the Site, Search, a language selector, and a list of the recent content created in the intranet. It also provides two additional pages for Documents and Media and external News obtained through public feeds.

## Creating a Site from a Site Template

To create a Site using a Site Template, follow these steps:

1. Open the Product Menu and go to _Control Panel_ &rarr; _Sites_ &rarr; _Sites_.

    ![Navigating to the Control Panel to the Sites option.](./building-sites-with-site-templates/images/03.png)

1. Click the _Add_ icon (![Add Site](../../images/icon-add.png)) and select your Site Template from the menu.
1. Enter a name for the Site.

    - Checking _Create default pages as private (available only to members)._ will prevent guest users from viewing site pages.

1. Click _Save_.
1. Configure your [site settings](../site_settings.md).
1. Open the _Pages_ panel below the form.

    ![The Site Configuration Pages drop down expanded to show Site Template options.](building-sites-with-site-templates/images/04.png)

    ```note::
       *Enable propagation of changes from the Site template* enables the Site to receive updates if the Site Template is modified. If changes are made directly to a Site created from a Site Template, the Site will no longer receive updates from the Site Template. See `Merging Site Template Changes <./merging-site-template-changes.md>`_ for more information.
    ```

1. Click _Save_ to create your Site.
1. Open the Product Menu and go to _Sites_ &rarr; _Sites_ under the Control Panel.
1. Click _Actions_ and select _Go to Public Pages_ or _Go to Private Pages_ next to your new Site to view it.

    ```tip::
       To view a newly created *blank site*, you must first create a page for it. See `Adding a Page to a Site <../creating-pages/adding-pages/adding-a-page-to-a-site.md>`_ for more information.
    ```

## Related Information

-   [Introduction to Site Building](../introduction-to-site-building.md)
-   [Creating a Site Template](./building-sites-with-site-templates.md)
-   [Adding Members to Sites](./site-membership/adding-members-to-sites.md)
