# Using Fragments

Here you'll learn how to use some of the common Fragments. These Fragments are covered here:

## Using the Content Fragment

> Available: Liferay DXP 7.3+.

You can display a single existing web content, blog entry, or document by adding a Content Fragment from the _Content Display_ panel. Follow these steps to use it:

1. Edit an existing Fragment-supported page (i.e. Content Page, Master Page, or Display Page).
1. Open the _Fragments_ Panel and expand the _Content Display_ heading and drag the _Content_ Fragment onto the page.
1. With the _Content_ Fragment selected, click the (![Cog icon](../../../images/icon-control-menu-gear.png)) icon to open the Fragment Configuration Menu.

    ![The Content Fragment lets you display a single piece of content.](./using-fragments/images/01.png)

1. Click the plus button next to the _Content_ input and select an existing web content, blog entry, or document to display.

## Using the Container Fragment

You can deploy a single _Container_ fragment or multiple _Container_ fragments on a page. In addition to having multiple _Container_ fragments on a page, these fragments can be nested.

1. Edit an existing Fragment-supported page (i.e. Content Page, Master Page, or Display Page).
1. Click the _Fragments and Widgets_ button.

    ![The Container fragment appears in the Fragments and Widgets menu.](./using-fragments/images/02.png)

1. Click the _Fragments_ tab.
1. Drag and drop the _Container_ fragment onto the page.
1. Drag and drop your desired fragments or content into the _Container_.
1. Add any additional _Container_ fragments to the page.

    ![Drag additional Container fragments on the page.](./using-fragments/images/03.png)

1. Click _Publish_ when finished.

The Page has been published with several _Container_ fragments.

### Adding Links in a Container Fragment

Lastly, _Container_ fragments contain a _Link_ field where you can add either internal or external links:

1. In the _Site Builder_ &rarr; _Pages_ menu, navigate to the Content Page where the _Container_ fragments have been published (for example, _Page 3_ in the steps above) .
1. Click _Edit_.
1. Click the _Selection_ ![Selection icon](../../../images/icon-page-tree.png) icon.
1. Click on the desired _Container_.
1. Click the _Link_ tab.
1. Enter these values:

    - **Link**: Manual
    - **URL**: the desired URL
    - **Target**: Self

    ![You can add external or internal links to a Container.](./using-fragments/images/04.png)

1. Click _Publish_ when finished.

The link has been added to the _Container_. Once published, clicking on the name of the fragment redirects the user to the link's page.

## Additional Information

-   [Using Fragment Comments](./using-fragment-comments.md)
-   [Using Widgets on a Content Page](./using-widgets-on-a-content-page.md)
