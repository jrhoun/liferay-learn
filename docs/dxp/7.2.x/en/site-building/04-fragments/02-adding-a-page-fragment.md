# Adding a Page Fragment

Page Fragments are organized in *Collections*. Collections can be used to differentiate between different types of Page Fragments or Page Fragments used by different groups or departments. Follow these steps to add a Page Fragment:

1.  Make sure the Site where you want to work is selected. If you prefer creating a Page Fragment that's available for all Sites, since Liferay DXP 7.2 SP1+ and Liferay Portal 7.2 GA2+, you can create global Page Fragments. Navigate to the *Global* Site and create your Page Fragment there. 

    >**Note:** Global Page Fragments are available in Liferay DXP 7.2 SP1+ and Liferay Portal 7.2 GA2+. To expose this feature in the initial releases of these versions, you must create a `.config` file named  `com.liferay.fragment.web.internal.configuration.FragmentGlobalPanelAppConfiguration.config` and add the `enabled=B"true"` property. Then copy it to your Liferay Portal instance's `osgi/configs` folder. Global Page Fragments are inherited by child Sites, so they can only be edited from the Global Site. Any resources the Global Page Fragment references (e.g., image) from the Global Site are copied to a Site that leverages the Page Fragment.

2.  Open the Product Menu and go to *Site Builder* &rarr; *Page Fragments* under the Site Menu. From the main Page Fragments page you can manage your Page Fragments and Collections. See [Managing Page Fragments](./03-managing-page-fragments.md) for more information on the available actions for Page Fragments.

3.  Click the (![add](../../icon-add.png)) button next to *Collections* heading to add a new Collection if one doesn't already exist, or select an existing custom Collection.

    ![Figure 1: Here is the Page Fragments page with no custom Page Fragments or Collections created.](./adding-a-page-fragment/images/01.png)

4.  With the Collection selected, click the (![add button](../../icon-add.png)) under the new Collection's window to create a new Page Fragment and choose [Section](../02-creating-pages/03-content-page-elements.md#sections) or [Component](../02-creating-pages/03-content-page-elements.md#components).

4.  Give the Page Fragment a name and click *Save*.

5.  [Develop the Page Fragment](TODO) using [the editor](./05-the-page-fragments-editor.md) and publish the changes.

>**Note:** You can also create Page Fragments outside of Liferay Portal using your own tooling. See [Developing a Page Fragment Using Desktop Tools](TODO) for more information.