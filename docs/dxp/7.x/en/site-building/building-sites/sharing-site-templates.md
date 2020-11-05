# Sharing Site Templates

To export a Site that uses Site Templates or Page Templates to a different Liferay DXP installation (through a LAR file or remote publication), the Site Templates must be exported and imported manually first, before the Site.

To export a Site using a Site Template, follow these steps:

1. Open the [Global Menu](../../getting-started/navigating-dxp.md) ( ![Global Menu icon](../../images/icon-applications-menu.png) ) and go to _Control Panel_ &rarr; _Site Templates_.

1. Open the _Actions_ Menu (![Actions icon](../../images/icon-actions.png)) for the Site Template you want to export and select _Manage_.

1. While managing the Site Template, go to the Site Menu and navigate to _Publishing_ &rarr; _Export_.

1. Click the _Add_ icon (![Add icon](../../images/icon-add.png)) to create a new custom export.

    ![You can Export Site Templates to share them between other Sites.](./sharing-site-templates/images/01.png)

1. Select the content and pages you want to export and click _Export_.

1. Click on the _Download_ icon for the template that you exported.

1. In your target environment (Liferay Portal instance), open the Global Menu ( ![Global Menu icon](../../images/icon-applications-menu.png) ) and go to _Control Panel_ &rarr; _Site Templates_.

1. Create a new Site Template.

1. Open the _Actions_ Menu (![Actions icon](../../images/icon-actions.png)) for the Site Template and select _Manage_.

1. While managing the Page Template, go to the Site Menu and navigate to _Publishing_ &rarr; _Import_.

1. Import the Site Template LAR you downloaded.

![Exported Site Templates can be imported into other Sites.](./sharing-site-templates/images/02.png)

The Site Template can be used normally in the new environment. For more information on exporting/importing content, see [Importing/Exporting Pages and Content](./importing-exporting-pages-and-content.md).
