# Personalizing Collections

> Availability: Liferay Portal 7.3 GA6, Liferay DXP 7.3+

By default, any user can see all the Collection's content and is part of _Anyone_ group. You can create a _Personalized Variation_ of the Collection's items using [Segments](../segmentation/creating-and-managing-user-segments.md). When you use a Personalized Variation, the items that are part of your Collection don't change, but the Collection Page or Collection Display Fragment show the items filtered for the Segment.

```note::
   To customize a Collection using Segments, you must define the Segments first. For more information, see `Creating and Managing User Segments <../segmentation/creating-and-managing-user-segments.md>`_.
```

![Collections are available for anyone, by default](./personalizing-collections/images/02.png)

Consider the following example. You want to increase sales in your online Kitchenware Store by offering exclusive promotions to registered users. You create a Collection including promotions for registered users and news about your products. You want all users to see the news about your products, but you want to restrict the promotions to registered users. In this example, you can create a new Segment for registered users, and link the Segment to a new Personalized Variation that filters the promotional content.

```tip::
   You can create multiple Personalized Variations for a Collection, and edit or delete them as needed. You can also edit the *Anyone* Personalized Variation, but you cannot delete it.
```

## Creating a Personalized Variation

1. Go to _Site Administration_ &rarr; _Site Builder_ &rarr; _Collections_.
1. From the _Collections_ tab, click the _Options_ menu (![Options](../../../images/icon-staging-bar-options.png)) next to the Collection you want to customize and select _Edit_.

    ![Edit the Collection you want to customize](./personalizing-collections/images/01.png)

1. Under _Personalized Variations_, click _New Personalized Variation_ or click the New button (![New](../../../images/icon-plus.png)).
1. In the _New Personalized Variation_ dialog, click the Segment you want to associate to this Collection.
1. Configure the properties for the Personalized Variation. For more information, see [Creating Collections](../../../content-authoring-and-management/collections-and-collection-pages/creating-collections.md).

    For example, if this is Manual Collection, you can select the items you want to display in the Personalized Variation. If this is a Dynamic Collection, you can add a filter to customize the content.

    ![Configure the properties for your Personalized Variation](./personalizing-collections/images/04.png)

1. If you are customizing a Dynamic Collection, click _Save_.
1. To preview the items that are part of this Collection:

    - In the Manual Collection, click on the Personalized Variation's name to see the items.
    - In the Dynamic Collection, click the _Options_ menu (![Options](../../../images/icon-staging-bar-options.png)) next to the Personalized Variation's name and select _View Items_.

        ![Edit the Collection you want to customize](./personalizing-collections/images/03.png)

## Liferay DXP 7.2

### Content Set Personalization

Now, you'll use [Segments](../segmentation/creating-and-managing-user-segments.md) to demonstrate Content Set Personalization. For this example, create a Content Set to be the default displayed on the _Home_ page. Then you'll modify it to create a personalized variation containing technical articles for members of the _American Engineers_ segment.

If you're not familiar with Content Set, see the [Creating Content Sets](../../../content-authoring-and-management/collections-and-collection-pages/creating-collections.md#creating-content-sets) article before you get started here.

#### Creating and Setting the Default Content Set

First create the default Content Set and configure it on the Home page using the Asset Publisher.

1. Go to _Site Administration_ &rarr; _Content & Data_ &rarr; _Content Sets_.
2. Click the Add button (![Add](../../../images/icon-add.png)) and choose _Manual Selection_.
3. Name it _Home Page Content_.
4. For the new Content Set, click _Select_ next to _Asset Entries_ and select _Basic Web Content_.

    ![Click Select to add a new Asset Entries.](./personalizing-collections/images/20.png)

5. On the _Select Basic Web Content_ page, check the boxes next to the content you want to add and click _Add_.
6. Navigate to the _Home_ page and add an Asset Publisher to the page.
7. Open _Configuration_ for the Asset Publisher.
8. Under _Asset Selection_ select _Content Set_.
9. Under _Select Content Set_ click _Select_, choose _Home Page Content_, and click _Save_.

Now the Content Set that you configured appears in the Asset Publisher on the _Home Page_. Next configure the Content Set for Personalization.

#### Personalizing the Content Set

Now create the content set for engineers and configure its display.

1. Go back to the Content Set from _Site Administration_.
2. Click _New Personalized Variation_ and select the _American Engineers_ segment

    ![Create a new Personalized Variation.](./personalizing-collections/images/21.png)

3. Click _Select_ next to _Asset Entries_ and select _Basic Web Content_.
4. Select articles appropriate to an engineering audience and click _Add_.

Now anytime a member of the _American Engineers_ segment views this Content Set being displayed, they see the personalized version and not the default. Test this now, using the _Simulator_.

## Related Information

-   [Content Page Personalization](./content-page-personalization.md)
-   [About Collections and Collection Pages](../../../content-authoring-and-management/collections-and-collection-pages/about-collections-and-collection-pages.md)
-   [Creating User Segments](../segmentation/creating-and-managing-user-segments.md)
-   [Assigning Roles to User Segments](../../../users-and-permissions/roles-and-permissions/assigning-roles-to-user-segments.md)
