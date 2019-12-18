# Manually Migrating from Audience Targeting

Some Audience Targeting rules do not have a direct equivalent in DXP 7.2. These rules cannot be migrated automatically. The recommended solutions for each rule type are listed below.

**Contents:**

* [User Attribute Rules](#user-attribute-rules)
* [Session Rules](#session-rules)
* [Behavior Rules](#behavior-rules)
* [Custom Rules](#custom-rules)
* [Display Widgets](#display-widgets)

## User Attribute Rules

Some User Attributes, like Gender or Age, do not have a direct equivalent in DXP 7.2. User Attributes retrieved from external sources like Facebook also do not have a replacement. To replace these, you must create a [custom user field](https://help.liferay.com/hc/en-us/articles/360029041731-Creating-Segments-with-Custom-Fields-and-Session-Data) and use that to define your new Segment.

## Session Rules

For Session attributes that do not have a direct equivalent, the recommended solution is to use a URL field for the current URL or a previously visited URL on your site as criteria. You can also use a cookie for more advanced session tracking needs.

## Behavior Rules

In DXP 7.2, analytics is now managed through Analytics Cloud. You can learn more about creating behavior based rules in the [Analytics Cloud documentation](https://help.liferay.com/hc/en-us/articles/360006947671-Creating-Segments).

## Migrating Custom Rules

In DXP 7.1, Audience Targeting segmentation features could be extended using custom rules. As part of the upgrade planning process, the function of any such rules should be re-evaluated with the new Segmentation features of DXP 7.2 in mind. 

First, check the [Segmentation reference](https://help.liferay.com/hc/en-us/articles/360029147011-Defining-Segmentation-Criteria) for whether any new criteria fields can replace their function. In particular, custom fields, URL fields, and cookies might help to migrate existing custom rules.

If none of these fields cover your requirements, follow the development guide for instructions on [how to add new criteria fields and contributors](https://help.liferay.com/hc/en-us/articles/360028721372-Introduction-to-Segmentation-and-Personalization).

## Migrating Display Widgets

With Audience Targeting in DXP 7.1, you could display personalized content with the User Segment Display Content widget or by using an Asset Publisher with the [Segments filter enabled](https://help.liferay.com/hc/en-us/articles/360018174271-Using-the-Audience-Targeting-Widgets-). In DXP 7.2, you must choose the most appropriate personalization option for your use cases. See the [introduction to Personalization](https://help.liferay.com/hc/en-us/articles/360028721372-Introduction-to-Segmentation-and-Personalization#personalizing-experiences) for more information.

### User Segment Content Display

The User Segment Content Display widget was used in DXP 7.1 to display existing content based on segment membership rules. In DXP 7.2, you can cover the same use case by defining manual content sets with variations for your different audiences and applying it to an Asset Publisher. With this feature, you can assign any number of assets to the Content List for the given audience, and then use the Asset Publisher to define how content is displayed on the page. See the documentation for [creating personalized Content Sets](https://help.liferay.com/hc/en-us/articles/360029041771-Content-Set-Personalization). 

### Asset Publisher Personalization

Finally, if you want to display a dynamic list of content for your different audiences based on a filter in the same way you did with in Audience Targeting using a Segments filter in an Asset Publisher, you can create a dynamic content set with variations for your audiences and apply it to an Asset Publisher.

<!-- TODO: [Link to Personalized Content Sets, dynamic section]. -->

Additionally, the new [Experience-based Content Page personalization](https://help.liferay.com/hc/en-us/articles/360028721452-Content-Page-Personalization) feature may fulfill a use case that you addressed in earlier versions with one of the methods previously available.
