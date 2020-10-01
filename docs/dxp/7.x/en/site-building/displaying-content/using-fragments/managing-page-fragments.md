# Managing Page Fragments

As your Site grows, you'll have many Collections of Page Fragments. You can work with them in several ways:

-   You can edit them directly.
-   You can export and import them.
-   You can move and copy Fragments between Collections.

## Managing Collections of Page Fragments

To access the collections management menu, follow these steps:

1. Open the Product Menu and go to _Site Builder_ &rarr; _Page Fragments_ under the Site menu.

1. Select the Collection you want to manage from the _Collections_ list.

1. Open the (![Actions](../../../images/icon-actions.png)) menu next to the Collection name.

1. Select an action for the Collection:

    **Edit**: change the name or description for the collection.

    **Export**: Download a `.zip` file containing all Page Fragments in the Collection without exporting any Collection data. To export the Collection with Collection data, select the _Export_ option from the Actions Menu next to the _Collections_ heading and choose one or more Collections to export. Each collection exports in a separate `.zip` file.

    **Import**: Select a `.zip` file to upload with additional Page Fragments. If you want to replace an existing collection, make sure the box is checked for _Overwrite Existing Files_. You can import a Collection that was created in Liferay DXP, a Collection created using external tools, or Page Fragments without a Collection.

    ```note::
      Exporting and importing Page Fragments is the preferred way to share code or bring it into your Site.
    ```

    **Delete**: Remove the current collection and all its contents.

![You can export all of the Page Fragments in a Collection.](./managing-page-fragments/images/01.png)

## Managing Individual Page Fragments

To access the Page Fragment management menu, follow these steps:

1. Open the Product Menu and go to _Site Builder_ &rarr; _Page Fragments_ under the Site menu.

1. Select the Collection containing the Page Fragment you want to manage from the _Collections_ list.

1. Open the (![Actions](../../../images/icon-actions.png)) menu next to the Page Fragment.

1. Select An action:

    **Edit**: Modify the Page Fragment's code and configuration.

    **Rename**: Change the Page Fragment's name.

    **Move**: Move the Page Fragment to a different Collection.

    **Make a Copy**: Duplicate the Page Fragment. Duplicated Page Fragments share the same name with _(Copy)_ appended to the end.

    **Change Thumbnail**: Change the thumbnail image for the Page Fragment.

    **Export**: Download a `.zip` file of the Page Fragment.

    **Delete**: Remove the Page Fragment from the Collection.

### Copying a Default Fragment

> Availability: Liferay DXP 7.2 SP1+ and Liferay Portal 7.2 GA2+.

Default Page Fragments cannot be directly edited. However, you can copy the default Page Fragment, move it to your custom Collection, and edit it there.

1. Navigate to the default Page Fragment Collection.
1. Open the Page Fragment's _Actions_ (![Actions](../../../images/icon-actions.png)) Menu and select _Copy To_.
1. Select the Collection where you want to copy the default Page Fragment.
