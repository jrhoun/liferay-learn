# Installation Overview

A performant, resilient, and secure Liferay DXP installation has several different facets to consider. This overview covers the fundamental steps for installing Liferay DXP.

1. [Prerequisites](#prerequisites)
1. [Configuring an Application Server](#configuring-an-application-server)
1. [Connecting a Database](#connecting-a-database)
1. [Running Liferay DXP for the First Time](#running-liferay-dxp-for-the-first-time)
1. [Activating Liferay DXP](#activating-liferay-dxp)
1. [Additional Setup](#additional-setup)

> **Note:** To start Liferay DXP instance fast for touring or demonstration purposes, see [Getting Started with Liferay DXP](./01-getting-started-with-liferay-dxp.md)

## Prerequisites

### Java

**Java JDK 8 or 11** (see [www.java.com](https://www.java.com/)) are required. 

DXP requires these **JVM arguments**:

| JVM Argument | Description |
| :------- | :---------- |
| `-Dfile.encoding=UTF8` | UTF-8 file encoding supports multilingual character sets|
| `-Duser.timezone=GMT` | GMT time zone  |
| `-Djava.locale.providers=JRE,COMPAT,CLDR` | **On JDK 11 only**, this setting makes the JVM use JDK 8's default locales provider to display four digit years. JDK 8 uses four digit years by default. |
| `-Xms2560m -Xmx2560m` | Sets the 2GB recommended maximum heap size. Setting the minimum heap size to the maximum heap size value minimizes garbage collections. |

### Hosting

Liferay DXP is built with flexibility and interoperability in mind. Here are the hosting options:

* On-premise installation (_demonstrated here_)
* [Docker container](./03-downloading-liferay-dxp.md#docker-image)
* [DXP Cloud](https://learn.liferay.com/dxp-cloud-latest/index.html)

## Configuring an Application Server

The best starting point for people new to installing DXP, is the Liferay DXP Tomcat Bundle. Liferay DXP can also be manually deployed to a variety of application servers.

### Using the Tomcat Bundle

The Liferay Tomcat bundle is the simplest and fastest way to get started with Liferay DXP on-premise. The Tomcat bundle includes the Apache Tomcat application server with Liferay DXP pre-deployed. See [Downloading Liferay DXP](./03-downloading-liferay-dxp.md) to get a Tomcat bundle.

### Manually Deploying to an Application Server

Deployed DXP to an existing application server requires using the Liferay DXP `.war` file and other dependency files. To download these files and learn more about them, see [Downloading Liferay DXP](./03-downloading-liferay-dxp.md).

Then follow the instructions for installing Liferay DXP to your application server:

 * [Tomcat](./01-installing-liferay-on-an-application-server/01-installing-liferay-on-tomcat.md)
 * [WildFly](./01-installing-liferay-on-an-application-server/02-installing-liferay-on-wildfly.md)
 * [JBoss EAP](./01-installing-liferay-on-an-application-server/03-installing-liferay-on-jboss-eap.md)
 * [WebLogic](./01-installing-liferay-on-an-application-server/04-installing-liferay-on-weblogic.md)
 * [WebSphere](./01-installing-liferay-on-an-application-server/05-installing-liferay-on-websphere.md)

## Connecting a Database

Liferay DXP's pre-configured defaults (including an HSQL database) enable faster demonstration. Using Liferay DXP beyond basic exploration, however, requires a full-featured, supported RDBMS. See [Connecting a Database](./04-connecting-a-database.md) for details.

## Running Liferay DXP for the First Time

Once the JVM, application server, and database have been configured, you can run Liferay DXP. See [Running Liferay DXP for the First Time](./05-running-liferay-dxp-for-the-first-time.md).

On completing startup, DXP launches the Basic Configuration page (the Setup Wizard). See [Using the Setup Wizard](./06-using-the-setup-wizard.md) to finish basic configuration.

## Activating Liferay DXP

> Subscription Required

Liferay DXP Enterprise Subscribers must [activate Liferay DXP](./08-activating-liferay-dxp.md) to continue using all that the subscription offers beyond the initial trial period.

## Conclusion

Congratulations! You understand the fundamentals for installing Liferay DXP. Make sure to visit the articles mentioned above to install DXP in the best way to meet your needs.

## Next Steps

There are also many ways to configure and customize an installation. To learn more, see the additional setup topics at [Setting up Liferay DXP](../02-setting-up-liferay-dxp/01-config-overview.md). Here are some of those topics:

* Installing and Configuring a Search Engine
* [Securing Liferay DXP](../05-securing-liferay/01-securing-liferay.md)
* [Introduction to Clustering Liferay DXP](../02-setting-up-liferay-dxp/configuring-clustering-for-high-availability/01-introduction-to-clustering-liferay-dxp.md)
