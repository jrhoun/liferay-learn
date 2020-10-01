# Managing Master Page Templates

> Available: Liferay DXP 7.3+

To manage a Master Page Template, follow these steps:

1. Open the Product Menu and go to _Site Builder_ &rarr; _Page Templates_ under the Site menu, and select the _Masters_ tab.

    ![Manage the Master Page Template from the Masters tab of the Page Templates application.](./managing-master-pages/images/01.png)

1. Open the Actions Menu for a Master Page Template and select one of the options listed below:

    - **Edit:** Configure the Master Page Template. Alternatively, you can edit the Master Page Template for a page through the page's [_Look and Feel_ Menu](../building-and-managing-content-pages/content-pages-overview.md#look-and-feel), by clicking the _Edit Master_ button.

    - **Change Thumbnail:** Select a thumbnail image to display for the Master Page Template's card in the _Masters_ tab

    - **Rename:** Change the name of the Master Page Template

    - **Make a Copy:** Duplicate the Master Page Template. The copy is automatically named after the original Master Page Template with "Copy" appended to the end.

    - **Permissions:** Define permissions for the Master Page Template

    - **Delete:** Remove the Master Page Template. You can also bulk delete Master Page Templates by checking the box for each template and clicking the `X`, or selecting the _Delete_ action from the Management Toolbar.

```note::
   After changes are made and published, they are propagated to all pages that use the Master Page Template.
```

## Changing the Master Page Template of a Page

You can change the Master Page Template of a page through the page's [_Look and Feel_ Menu](../building-and-managing-content-pages/content-pages-overview.md#look-and-feel). Follow these steps:

1. Navigate to the page that you want to change the Master Page Template for.
1. Click the _Look and Feel_ icon (![Look and Feel](../../../images/icon-look-and-feel.png)).
1. Click the _Change Master_ button under the _Look and Feel_ tab.

    ![Click the Change Master button to choose a different Master Page Template.](./managing-master-pages/images/03.png)

1. Select a new Master Page Template and click _Done_. Click _save_ to apply the changes.

    ![Select a new Master Page Template from the available options.](./managing-master-pages/images/04.png)

## Changing a Master Page Template's Theme

When a custom Master Page Template is applied to a page, the Theme is no longer defined through the page. It is defined through the Master Page Template. Follow these steps to update the Theme for the Master Page Template:

1. Edit the Master Page Template through the Actions Menu as described above.
1. Open the page's _Look and Feel_ Menu (![Look and Feel](../../../images/icon-look-and-feel.png)).
1. Select the _Define a specific look and feel for this page_ button.

    ![Select a new Master Page Template from the available options.](./managing-master-pages/images/05.png)

1. Scroll down and click the _Change Current Theme_ button, select a new Theme, and click _Save_ to apply the changes.
