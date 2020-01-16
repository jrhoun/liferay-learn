# Using the Setup Wizard



If you've [configured the a database connection](./04-connecting-a-database.md) already using a `portal-ext.properties` file, the Basic Configuration page shows your configured database settings. Otherwise, use the Setup Wizard to configure the DXP database.


On [running Liferay DXP for the first time](./02-installation-overview.md#running-liferay-dxp-for-the-first-time), the Setup Wizard appears. It provides a convenient way to configure the following:

* Portal name
* Locale and time zone
* Admin user
* Database connection

> **Note**: If you have already configured Liferay DXP and its [database connection](../04-connecting-a-database.md) using a [`portal-ext.properties` file](../14-reference/03-portal-properties.md), you can disable the Setup Wizard by appending `setup.wizard.enabled=false` to that properties file.

![Supply the information for the portal and the portal's default administrator user on the Basic Configuration page.](./using-the-setup-wizard/images/01.png)

## Portal Configuration Reference

| Field | Description |
| --- | --- |
| **Portal Name** | Name of the site being created |
| **Default Language** | Determines the default site locale |
| **Time Zone**  | The instance's default time zone |

## Administrator User Configuration Reference

| Field | Description |
| --- | --- |
| **First Name** | The administrator user's first name |
| **Last Name** | The administrator user's last name |
| **Email** | The administrator user's email address |

> **Note:** the administrator user's email domain is used as the DXP instance's default domain (i.e., the [`company.default.web.id`](https://docs.liferay.com/dxp/portal/7.2-latest/propertiesdoc/portal.properties.html#Company) [portal property](../14-reference/03-portal-properties.md)).

## Database Configuration Reference

> **Important:** If you have not yet created a database, create one now following [database preparation instructions](./04-connecting-a-database.md).

Click the *Change* link if you're using DXP's built-in data source and configuring it to use the [database you created earlier](./04-connecting-a-database.md).

| Field | Description |
| --- | --- |
| **Database Type** | Select the database type to connect to |
| **JDBC URL** | Update the path to the database that has already been created for Liferay DXP |
| **User Name** | Database user name |
| **Password** | Database user password |
| **Sample Data** | Flagging this value will result in Users, Sites, and Organizations being created for demonstration purposes |

> **Warning:** HSQL must not be used in production instances of Liferay DXP.

## Completing the Setup Wizard

After filling out the Basic Configuration form, click *Finish Configuration*.

The setup wizard creates a `[LIFERAY_HOME]/portal-setup-wizard.properties` file which stores the settings that you entered. For further configurations or customizations, use a [`portal-ext.properties`](../14-reference/03-portal-properties.md) file to make configurations or customizations without directly changing `portal.properties`.

> **Note:** Property values in `portal-setup-wizard.properties` (the file the setup wizards creates in [Liferay Home](../14-reference/01-liferay-home.md)) override property values in `portal-ext.properties`.

If you have a Liferay DXP Enterprise subscription, DXP requests your activation key. [Activating Liferay DXP](.08-activating-liferay-dxp.md) is discussed next.

Lastly DXP prompts you to restart the server. DXP initializes the database the next time you start the server.

## Next Steps

* [Installation Overview](./02-installation-overview.md)
* [Activating Liferay DXP](.08-activating-liferay-dxp.md)
* [Securing Liferay DXP](../05-securing-liferay/01-securing-liferay.md)
* [Configuring Clustering for High Availability](../02-setting-up-liferay-dxp/01-performance-and-scalability/01-configuring-clustering/01-introduction-to-clustering-liferay-dxp.md)
* Maintaining Liferay DXP
