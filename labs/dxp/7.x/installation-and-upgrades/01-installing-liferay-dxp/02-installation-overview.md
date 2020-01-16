# Installation Overview

A performant, resilient, and secure Liferay DXP installation has several different facets to consider. This overview covers the fundamental steps for installing Liferay DXP.

1. [Prerequisites](#prerequisites)
1. [Configuring an Application Server](#configuring-an-application-server)
1. [Connecting a Database](#connecting-a-database)
1. [Running Liferay DXP for the First Time](#running-liferay-dxp-for-the-first-time)
1. [Activating Liferay DXP](#activating-liferay-dxp)
1. [Next Steps](#next-steps)

> **Note:** To start Liferay DXP instance fast for touring or demonstration purposes, see [Getting Started with Liferay DXP](./01-getting-started-with-liferay-dxp.md)

## Prerequisites

### Java

Liferay Digital Experience Platform requires **JAVA JDK 8 or 11** in order to run. Visit [java.com](https://www.java.com/) to learn more. See [JVM Configurations](../14-reference/05-jvm-configurations.md) for specific information on how to configure the JVM for a Liferay DXP installation.

### Hosting

Liferay DXP is built with flexibility and interoperability in mind. DXP can be installed and run locally or on a server, or it can be run in a Docker Container or on the cloud. We recommend [DXP Cloud](https://learn.liferay.com/dxp-cloud-latest/index.html) as the best way to get a secure, performant, and scalable Liferay DXP solutions up and running quickly. The instructions that follow concentrate on installing and running DXP on-premise.

## Configuring an Application Server

The best starting point for people new to installing DXP, is the Liferay DXP Tomcat Bundle. Liferay DXP can also be manually deployed to a variety of application servers.

### Using the Tomcat Bundle

The Liferay Tomcat bundle is the simplest and fastest way to get started with Liferay DXP on-premise. The Tomcat bundle includes the Apache Tomcat application server with Liferay DXP pre-deployed. See [Downloading Liferay DXP](./03-downloading-liferay-dxp.md) to get a Liferay Tomcat bundle.

### Manually Deploying to an Application Server

Liferay DXP can be manually deployed to an existing application server. This requires using the Liferay DXP `.war` file and other dependencies. To learn more about these files and other available Liferay DXP downloads see [Downloading Liferay DXP](./03-downloading-liferay-dxp.md).

Then follow the instructions for installing Liferay DXP to your application server:

 * [Tomcat](./01-installing-liferay-on-an-application-server/01-installing-liferay-on-tomcat.md)
 * [WildFly](./01-installing-liferay-on-an-application-server/02-installing-liferay-on-wildfly.md)
 * [JBoss EAP](./01-installing-liferay-on-an-application-server/03-installing-liferay-on-jboss-eap.md)
 * [WebLogic](./01-installing-liferay-on-an-application-server/04-installing-liferay-on-weblogic.md)
 * [WebSphere](./01-installing-liferay-on-an-application-server/05-installing-liferay-on-websphere.md)

## Connecting a Database

Liferay DXP's pre-configured defaults (including an HSQL database) enable faster demonstration. A full-featured supported RDBMS is required for using Liferay DXP beyond basic exploration. See [Connecting a Database](./04-connecting-a-database.md) for more information.

## Running Liferay DXP for the First Time

Once the JVM, application server, and database have been configured, you can [start Liferay DXP](./05-running-liferay-dxp-for-the-first-time.md). On completing startup, DXP launches a web browser that displays the Basic Configuration page (the Setup Wizard). The page lets you set the DXP instance's name, administrative user, time zone, and more. See [Using the Setup Wizard](./06-using-the-setup-wizard.md) to learn more.

## Activating Liferay DXP

> Subscription Required

Liferay DXP Enterprise Subscribers must [activate Liferay DXP](./08-activating-liferay-dxp.md) to continue using all that the subscription offers beyond the initial trial period.

## Next Steps

Congratulations! You understand the fundamentals for installing Liferay DXP. To dive deeper into those topics, visit the articles mentioned in the sections above. There are also many ways to configure and customize an installation to meet your needs. To learn more, continue with [Setting up Liferay DXP](../02-setting-up-liferay-dxp/01-config-overview.md) or explore the following topics:

* Installing and Configuring a Search Engine
* [Securing Liferay DXP](../05-securing-liferay/01-securing-liferay.md)
* [Configuring Clustering for High Availability](../02-setting-up-liferay-dxp/01-performance-and-scalability/01-configuring-clustering/01-introduction-to-clustering-liferay-dxp.md)
* Maintaining Liferay DXP
