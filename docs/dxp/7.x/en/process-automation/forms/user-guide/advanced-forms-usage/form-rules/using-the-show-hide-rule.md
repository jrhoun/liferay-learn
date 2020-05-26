# Using the Show-Hide Rule

Using _Show_ action allows users to determine whether to show a field if the condition is met. This article demonstrates the "Show" action using the following example: If you're under 18 years old, you need the approval of a legal guardian to to participate in a camp. If you enter a number less than 18, the Legal Guardian Email Address field appears. Otherwise, this field is hidden.

## Prerequisites

[Create a form](../../creating-forms.md) that includes these two text fields:

* _I am 18 Years Old or Older_: a required single selection field with two options: _Yes_ and _No_.
* _Legal Guardian Email Address_: a text field that accepts valid email addresses.

## Configuring the Show Action Rule

To configure a Show-Hide action rule:

1. Click the _Rules_ tab.
1. Click the Add (![Add](../../../../../images/icon-add.png)) button.
1. Select _I am 18 Years Old or Older_ from the _If_ dropdown menu.
1. Select _Is equal to_ from the next dropdown menu.
1. Select _Value_ from the third dropdown menu.
1. Select _No_ from the final dropdown menu.

    ![Build form rules quickly by defining your conditions and actions.](./using-the-show-hide-rule/images/01.png)

1. In the _Actions_ section, select _Show_ from the dropdown menu.
1. Select _Legal Guardian Email Address_ from the second Options dropdown menu.
1. Click _Save_ when finished.

     ![Once a rule is saved, it is displayed so that you can easily understand what it does.](./using-the-show-hide-rule/images/02.png)

Now the *Legal Guardian Email Address* field is only displayed in the form if the user selects *No* in the *I am 18 years old or older* field.

## Additional Information

* [Creating Forms](../../creating-forms.md)
* [Introduction to Form Rules](./introduction-to-form-rules.md)
* [Using the Require Rule](./using-the-require-rule.md)
* [Using the Enable Rule]()
* [Using the Jump to Page Rule](./using-the-jump-to-page-rule.md)
* [Using the Autofill Rule]()
* [Using the Calculate Rule]()
