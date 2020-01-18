# Using the Setup Wizard

On [running Liferay DXP for the first time](./running-liferay-dxp-for-the-first-time.md), the Setup Wizard appears. It facilitates configuring the:

* Portal name, default language, and time zone
* Administrative user
* Database

![DXP's Basic Configuration page (the Setup Wizard) facilitates configuring the portal and database.](./using-the-setup-wizard/images/01.png)

The following sections describe the fields for configuring your DXP instance. 

## Portal

| Field | Description |
| --- | --- |
| **Portal Name** | Name of the site being created |
| **Default Language** | The site's default locale |
| **Time Zone**  | The instance's default time zone |

## Administrator User

| Field | Description |
| --- | --- |
| **First Name** | The administrator user's first name |
| **Last Name** | The administrator user's last name |
| **Email** | The administrator user's email address |

> **Note:** The administrator user's email domain is used as the DXP instance's default domain (i.e., the [`company.default.web.id`](https://docs.liferay.com/dxp/portal/7.2-latest/propertiesdoc/portal.properties.html#Company) [portal property](../14-reference/03-portal-properties.md)).

## Database

> **Warning:** HSQL must not be used in production-grade Liferay DXP instances.

> **Important:** If you have not yet created a database, create one now following [database preparation instructions](./configuring-a-database.md).

Click the *Change* link to DXP's built-in data source to use your database.

![On clicking the Change link in the Database section, fields appear for configuring DXP's built-in data source.](./using-the-setup-wizard/images/02.png)

| Field | Description |
| --- | --- |
| **Database Type** | Select the database type to connect to |
| **JDBC URL** | Update the path to the database that you have created for Liferay DXP |
| **User Name** | Database user name |
| **Password** | Database user password |
| **Sample Data** | Selecting this adds Users, Sites, and Organizations for demonstration purposes. If you're creating a production-grade DXP instance or otherwise don't need the data, leave the sample data field unselected. |

## Completing the Setup

After filling out the Basic Configuration form, click *Finish Configuration*.

The Setup Wizard stores your configuration values in a `portal-setup-wizard.properties` file in your [Liferay Home](../14-reference/01-liferay-home.md).

If you have a Liferay DXP Enterprise subscription, DXP requests your activation key. See [Activating Liferay DXP](./activating-liferay-dxp.md).

Lastly DXP prompts you to restart your server. You can stop your server using the shutdown script bundled with your application server. Tomcat bundle example:

```bash
./liferay-dxp-version/tomcat-version/bin/shutdown.sh
```

Then [start the server](./running-liferay-dxp-for-the-first-time) again. Tomcat bundle example:

```bash
./liferay-dxp-version/tomcat-version/bin/startup.sh
```

DXP initializes the database and displays the DXP home page.

![Once you've configured DXP and restarted the server, the DXP home page appears and is ready for you to sign in!](./using-the-setup-wizard/images/03.png)

Congratulations on launching Liferay DXP! 

## Next Steps

You can sign in as your administrator user and start [building a solution on DXP](TODO). Or you can explore [additional Liferay DXP setup](../02-setting-up-liferay-dxp/01-config-overview.md) topics:

* [Setting up Marketplace](../02-setting-up-liferay-dxp/setting-up-marketplace.md)
* [Trial Plugin Installation](../02-setting-up-liferay-dxp/trial-plugin-installation.md)
* Installing and Configuring a Search Engine
* [Securing Liferay DXP](../05-securing-liferay/01-securing-liferay.md)
* [Introduction to Clustering Liferay DXP](../02-setting-up-liferay-dxp/configuring-clustering-for-high-availability/01-introduction-to-clustering-liferay-dxp.md)
