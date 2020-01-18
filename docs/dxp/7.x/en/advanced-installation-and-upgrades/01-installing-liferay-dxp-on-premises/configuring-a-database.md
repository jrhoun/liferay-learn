# Configuring a Database

By default, Liferay DXP uses an embedded HSQL database for demonstration purposes. For purposes beyond touring and demonstrating DXP, we recommend using a full-featured, supported RDBMS, such as:

* MySQL
* MariaDB
* Oracle
* PostgreSQL

> **Note:** the [Liferay DXP Compatibility Matrix](https://web.liferay.com/documents/14/21598941/Liferay+DXP+7.2+Compatibility+Matrix/b6e0f064-db31-49b4-8317-a29d1d76abf7) lists the supported databases and versions.

<!-- TODO Update the matrix link to the 7.3 matrix, when it's published - jhinkey -->

Connecting Liferay DXP to a database requires:

* [Database Configuration](#database-configuration)
* [Installing a JDBC Connector](#installing-a-jdbc-connector)
* [Configuring a Data Source](#configure-a-data-source)

## Database Configuration

Once you've selected a database, follow these steps to configure it:

* [Use the GMT Time Zone](#use-the-gmt-time-zone)
* [Create a Blank Database With UTF-8 Support](#creatre-a-blank-database-with-utf-8-support)
* [Configure Database User Access](#configure-user-database-access)
* [Configure the Query Result Sort Order (Optional)](#configure-the-query-result-sort-order-optional)

> **Note:** Always consult the database vendor's documentation before modifying the database.

### Use the GMT Time Zone

Configure your database server to use the GMT Time Zone. Setting the database server time zone to GMT preserves database integrity through Liferay DXP database upgrades, no matter the time zones you set in Liferay DXP. Refer to your database vendor documentation for details.

### Create a Blank Database With UTF-8 Support

Multilingual character sets require using UTF-8. This MySQL command example:

```sql
create database lportal character set utf8;
```

### Configure Database User Access

Liferay DXP uses a database user's credentials to connect to the database either directly or through the application server.

The simplest, easiest way to maintain a Liferay DXP database is through a database user that has full database permissions up to and including permissions to Create and Drop tables. Such a user enables Liferay DXP to maintain its database automatically during upgrades and enables seamless functionality of Liferay DXP plugins that interact with the database.

If your organization has more stringent security policies that require limiting database Liferay DXP database user permissions once the database is initialized, see [High Security Database User Practices](./high-security-database-user-practices).

### Configure the Query Result Sort Order (Optional)

Every database has a default order for sorting results (see [this article](https://help.liferay.com/hc/en-us/articles/360029315971-Sort-Order-Changed-with-a-Different-Database)). Consult the database vendor documentation to learn your database's sort order and if necessary, configure the database to use a default query result order you expect for entities Liferay DXP lists.

You've configured your database and database user. You're ready to install a JDBC connecter.

## Install a JDBC Connector

Liferay DXP requires a JDBC connector for communicating with your database. 

### Open Source Databases

The Liferay DXP bundle includes several open source JDBC connectors that connect DXP to a variety of databases. The connector files are normally located in a global `/lib/ext` folder (e.g., Tomcat) or a `/module` folder (e.g., JBoss EAP and WildFly 10).

### Proprietary Databases

Liferay DXP does not include JDBC connectors for proprietary databases like Oracle and DB2. Such connectors must be obtained from the database vendor and deployed to the application server.

| Database | Connector | Vendor Site | Notes |
| :------- | :-------- | :---------- | :---- |
| Oracle | `ojdbc8.jar` | [Oracle](https://www.oracle.com/index.html) | The `ojdbc8.jar` library with at least Oracle 12.2.0.1.0 JDBC 4.2 versioning is required because of [data truncation issues](https://issues.liferay.com/browse/LPS-79229) that have been detected reading data from CLOB columns. |
| DB2 | `db2jcc4.jar` | [IBM](https://www.ibm.com/) |  The `dbc2jcc` connector has been deprecated after 3.72. |

Add the connector JAR file to the application server’s designated location for connector files, such as a global `/lib/ext` folder (e.g., Tomcat) or a `module` folder (e.g., JBoss EAP and WildFly 10).

## Configuring a Data Source

There are two methods for connecting Liferay DXP to a database:

* Using DXP's built-in data source (demonstrated below)

* Using a data source managed on your application server. See the instructions for your application server: [Tomcat](./01-installing-liferay-on-an-application-server/01-installing-liferay-on-tomcat.md), [WildFly](./01-installing-liferay-on-an-application-server/02-installing-liferay-on-wildfly.md), [JBoss EAP](./01-installing-liferay-on-an-application-server/03-installing-liferay-on-jboss-eap.md), [WebLogic](./01-installing-liferay-on-an-application-server/04-installing-liferay-on-weblogic.md), or [WebSphere](./01-installing-liferay-on-an-application-server/05-installing-liferay-on-websphere.md).

The best option for most people is to set up a built-in data source connection during DXP startup [using the Setup Wizard](./using-the-setup-wizard.md). You'll use the Setup Wizard next when you [run Liferay DXP for the First Time](./running-liferay-dxp-for-the-first-time.md).

![The Setup Wizard's database section lets you configure DXP's built-in data source.](./configuring-a-database/images/01.png)

## Next steps

* [Running Liferay DXP for the First Time](./running-liferay-dxp-for-the-first-time.md)

* [Using the Setup Wizard](./using-the-setup-wizard.md)
