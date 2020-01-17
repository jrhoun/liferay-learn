# Connecting a Database

By default, Liferay DXP uses an embedded HSQL database for demonstration purposes. For purposes beyond touring and demonstrating DXP, we recommend using a full-featured, supported RDBMS, such as:

* MySQL
* MariaDB
* Oracle
* PostgreSQL

> **Note:** the [Liferay DXP Compatibility Matrix](https://web.liferay.com/documents/14/21598941/Liferay+DXP+7.2+Compatibility+Matrix/b6e0f064-db31-49b4-8317-a29d1d76abf7) lists the supported databases and versions.

<!-- TODO Update the matrix link to the 7.3 matrix, when it's published - jhinkey -->

Connecting Liferay DXP to a database requires:

* [Configuring the Database](#configuring-the-database)
* [Installing a JDBC Connector](#installing-a-jdbc-connector)
* [Configuring a Data Source](#configuring-a-data-source)

## Configuring the Database

Once you've selected a database, follow these steps to configure it:

* [Use the GMT Time Zone](#use-the-gmt-time-zone)
* [Create a Blank Database With UTF-8 Support](#creatre-a-blank-database-with-utf-8-support)
* [Configure the Query Result Sort Order (Optional)](#configure-the-query-result-sort-order-optional)
* [Configure Database User Access](#configure-user-database-access)

> **Note:** Always consult the database vendor's documentation before modifying the database.

### Use the GMT Time Zone

Configure your database server to use the GMT Time Zone. Setting the database server time zone to GMT preserves database integrity through Liferay DXP database upgrades, no matter the time zones you set in Liferay DXP. Refer to your database vendor documentation for details.

### Create a Blank Database With UTF-8 Support

Multilingual character sets require using UTF-8. This MySQL command, for example, creates a UTF-8 compliant database named `lportal`:

```sql
create database lportal character set utf8;
```

### Configure the Query Result Sort Order (Optional)

Every database has a default order for sorting results (see [this article](https://help.liferay.com/hc/en-us/articles/360029315971-Sort-Order-Changed-with-a-Different-Database)). Consult the database vendor documentation to learn your database's sort order and if necessary, configure the database to use a default query result order you expect for entities Liferay DXP lists.

### Configure User Database Access

Liferay DXP uses a database user's credentials to connect to the database either directly or through the application server.

#### Create a Database User With Full Permissions

The simplest, easiest way to maintain a Liferay DXP database is through a database user that has full database permissions up to and including permissions to Create and Drop tables. Such a user enables Liferay DXP to maintain its database automatically during upgrades and enables seamless functionality of Liferay DXP plugins that interact with the database.

#### Supporting High Security Practices

Your organization may have more stringent security policies that require limiting database Liferay DXP database user permissions once the database is initialized. If permissions for Select, Insert, Update and Delete operations are the only ones allowed for the user, you must initialize and maintain the database manually. Here's what's recommended to accomplish this:

1. Grant full rights for the Liferay DXP database user to do anything to the database.
1. Install Liferay DXP and start it so that it automatically populates the database.
1. Once the database has been populated with the Liferay DXP tables, remove all permissions from the Liferay DXP database user except permissions to perform Select, Insert, Update and Delete operations.

> **Warning:** There are some caveats to running Liferay DXP with these constraints. Many plugins create new tables when they’re deployed. Additionally, you must manually run the database upgrade function to upgrade Liferay DXP. If the Liferay DXP database user does not have adequate rights to create/modify/drop tables in the database, you must grant those rights to that user before deploying one of these plugins or starting the Liferay DXP upgrade. Once the tables are created or the upgrade completes, you can remove those rights until the next deploy or upgrade. If your team creates plugins that create their own tables, you must similarly grant temporary rights to the Liferay DXP database user before deploying the plugin.

You've configured your database. You're ready to install a JDBC connecter for it. 

## Installing a JDBC Connector

Liferay DXP requires a JDBC connector for communicating with your database. 

### Open Source Databases

The Liferay DXP bundle includes several open source JDBC connectors that connect DXP to a variety of databases. The connector files are normally located in a global `/lib/ext` folder (e.g., Tomcat) or a `/module` folder (e.g., for JBoss EAP and WildFly 10).

### Proprietary Databases

Liferay DXP does not include JDBC connectors for proprietary databases like Oracle and DB2. Such connectors must be obtained from the database vendor and deployed to the application server.

| Database | Connector | Vendor Site | Notes |
| :------- | :-------- | :---------- | :---- |
| Oracle | `ojdbc8.jar` | [Oracle](https://www.oracle.com/index.html) | The `ojdbc8.jar` library with at least Oracle 12.2.0.1.0 JDBC 4.2 versioning is required because of [data truncation issues](https://issues.liferay.com/browse/LPS-79229) that have been detected reading data from CLOB columns. |
| DB2 | `db2jcc4.jar` | [IBM](https://www.ibm.com/) |  The `dbc2jcc` connector has been deprecated after 3.72. |

Add the connector JAR file to the application server’s designated location for connector files, such as a global `/lib/ext` folder (e.g., Tomcat) or a `module` folder (e.g., for JBoss EAP and WildFly 10).

## Configuring a Data Source

There are two methods for connecting Liferay DXP to a database:

* Using DXP's built-in data source
* Using a data source managed on your application server

The best option for most people is to use the built-in data source.

### Built-In Data Source

To connect Liferay DXP to a database using the built-in data source follow these steps:

1. Create a [`portal-ext.properties`](../14-reference/03-portal-properties.md) file in your [`LIFERAY_HOME`](../14-reference/01-liferay-home.md) folder.

1. Copy a set of `jdbc.*` properties from one of the [JDBC templates](../14-reference/05-database-templates.md) into your `portal-ext.properties` file. For example, MySQL:

    ```properties
    jdbc.default.driverClassName=com.mysql.cj.jdbc.Driver
    jdbc.default.url=jdbc:mysql://localhost/lportal?characterEncoding=UTF-8&dontTrackOpenResources=true&holdResultsOpenOverStatementClose=true&serverTimezone=GMT&useFastDateParsing=false&useUnicode=true
    jdbc.default.username=
    jdbc.default.password=
    ```

1. Modify the properties to specify your database and database user credentials.

    ```properties
    jdbc.default.driverClassName=com.mysql.cj.jdbc.Driver
    jdbc.default.url=jdbc:mysql://path-to-my-database/my-liferay-database?characterEncoding=UTF-8&dontTrackOpenResources=true&holdResultsOpenOverStatementClose=true&serverTimezone=GMT&useFastDateParsing=false&useUnicode=true
    jdbc.default.username=test
    jdbc.default.password=password
    ```

Liferay DXP is set to connect to the data source when you start your DXP server.

An alternative to configuring the built-in data source *before* starting DXP is configuring it after DXP startup [using the Setup Wizard](./06-using-the-setup-wizard.md).

![The Setup Wizard's database section lets you configure DXP's built-in data source.](./connecting-a-database/images/01.png)

### Data Source on Your Application Server

If you want to use your application server to manage your DXP data source, follow the database configuration instructions applicable for your application server:

* [Installing Liferay DXP on Tomcat](./01-installing-liferay-on-an-application-server/01-installing-liferay-on-tomcat.md#database-configuration)
* [Installing Liferay DXP on WildFly](https://help.liferay.com/hc/en-us/articles/360029123751-Installing-Liferay-DXP-on-Wildfly#database-configuration)
* [Installing Liferay DXP on JBoss EAP](https://help.liferay.com/hc/en-us/articles/360028810012-Installing-Liferay-DXP-on-JBoss-EAP#database-configuration)
* [Installing Liferay DXP on WebLogic 12c R2](https://help.liferay.com/hc/en-us/articles/360028831932-Installing-Liferay-DXP-on-WebLogic-12c-R2#database-configuration)
* [Installing Liferay DXP on WebSphere](./01-installing-liferay-on-an-application-server/05-installing-liferay-on-websphere.md)

## Next steps

Once you have configured the database connection, or decided to configure it [using the Setup Wizard](./06-using-the-setup-wizard.md) you can start the application server. See [Running Liferay DXP for the First Time](./05-running-liferay-dxp-for-the-first-time.md).
