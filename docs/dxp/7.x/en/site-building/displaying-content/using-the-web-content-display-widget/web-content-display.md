# Web Content Display

Once you've created a [Web Content Article](../../../content-authoring-and-management/web-content/web-content-articles/adding-a-basic-web-content-article.md), the quickest way to display it on a page is the Web Content Display widget. Once a web content article is displayed updates to that content will be displayed immediately, unless a [workflow](../../../process-automation/workflow/user-guide/introduction-to-workflow.md) is enabled.

## Adding Web Content Display to a Page

Follow these steps to add a Web Content Display widget to a page and configure it:

1. Enter Edit ( ![Edit icon](../../../images/icon-edit.png) ) mode (if you are using a content page), and then [add the Web Content Display widget to the page](../../creating-pages/using-widget-pages/adding-widgets-to-a-page.md).

    ![Add the Web Content Display app to a page to begin displaying your new web content article.](./web-content-display/images/01.png)

1. [Open the Web Content Display widget's configuration menu](TODO:adding-widgets#configuration-menu).

1. Click the _Select_ button to select a piece of web content.

1. Search for and click on the article that you want to display.

1. [Configure the options](#web-content-display-configuration-options) you want to enable for the widget.

1. Click _Save_ to apply the changes, and close the configuration window. If you are using a content page, then click _Publish_ to publish the page with the widget.

## Web Content Display Configuration Options

All features are implemented as simple selector buttons so you can enable or disable them as you need. These features are available:

-   **User Tools**

    -   _Translations:_ Shows the available locales for your content. If you're working on the page for a particular language, you can select the translation of your content that goes with your locale.

    -   _Print:_ Opens a print dialog with a print-friendly version of the content.

    -   _Download as PDF | DOC | ODT | TXT:_ Downloads the web content in the selected format. These options are only available if [Open Office integration is enabled](../../../content-authoring-and-management/documents-and-media/devops/enabling-openoffice-libreoffice-integration.md).

-   **Content Metadata**
    -   _Related Assets_
    -   _Ratings_
    -   _Comments_
    -   _Comment Ratings_

![Publishing web content is a snap. At a minimum, you only have to select the content you wish to publish. You can also enable lots of optional features to let your users interact with your content.](./web-content-display/images/02.png)

### Enabling Comments for Guests

By default, guests can't leave comments on web content. If you want to allow guests to comment on your web content article, follow these steps:

1. Open the [Global Menu](../../../getting-started/navigating-dxp.md) ( ![Global Menu icon](../../../images/icon-applications-menu.png) ) and go to _Control Panel_ &rarr; _Roles_.

1. Select _Guest_ &rarr; _Define Permissions_.

1. From the left menu, select _Site and Asset Library Administration_ &rarr; _Content & Data_ &rarr; _Web Content_.

1. Navigate down to the Web Content Article heading and check the _Add Discussion_ checkbox.

1. Click _Save_.

Guests can now post comments on your web content article.

### Editing Content from the Web Content Display Widget

You can edit published content directly from the Web Content Display widget.

1. Hover over the Web Content Display widget.
1. Open the Actions Menu (![Options](../../../images/icon-app-options.png)) inside the widget container.
1. Select _Edit Web Content_ to launch the editor, or select _Edit Template_ to launch the template editor for the web content article's template if it has one.

### Integrating Open Office with Your Web Content Display

If you have [enabled OpenOffice/LibreOffice integration](../../../content-authoring-and-management/documents-and-media/devops/enabling-openoffice-libreoffice-integration.md) with your Liferay Portal instance, you can enable document conversion for your content. Then users can download your content in their format of choice. Enable the conversion options desired in the Web Content Display's configuration page under the _User Tools_ list.

![Conversion options are listed for the assets.](./web-content-display/images/03.png)

## Related Information

-   [Content Authoring and Management](../../../content_authoring_and_management.html)
-   Displaying Content on Display Pages
-   Displaying Content with the Asset Publisher
