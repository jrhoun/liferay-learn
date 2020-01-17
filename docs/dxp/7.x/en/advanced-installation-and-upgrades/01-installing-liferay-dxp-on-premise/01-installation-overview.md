# Advanced Installation Overview

A performant, resilient, and secure Liferay DXP installation has several different facets to consider. This overview covers the fundamental steps for installing Liferay DXP on-premise.

1. [Prerequisites](#prerequisites)
1. [Downloading DXP](#downloading-dxp)
1. [Connecting a Database](#connecting-a-database)
1. [Running DXP](#running-dxp)

> **Note:** To start Liferay DXP instance fast for touring or demonstration purposes, see [Getting Started with Liferay DXP](../../getting-started/starting-with-the-dxp-docker-image.md)

## Prerequisites

**Java JDK 8 or 11** (see [www.java.com](https://www.java.com/)) are required. 

## Downloading DXP

Download DXP for the installation you want:

* **Tomcat bundle:** The Apache Tomcat application server with Liferay DXP pre-deployed. It's the simplest and fastest way to get started with Liferay DXP on-premise.

* **Already using an application server?** The DXP `.war` file and dependencies are available for installing DXP on existing application servers.

[Download DXP](./03-downloading-liferay-dxp.md) to get it either way.

## Connecting a Database

Database options:

* A full-featured, supported RDBMS is required for using DXP beyond basic exploration. See [Connecting a Database](./04-connecting-a-database.md).

* HSQL database (included for demonstration purposes only).

## Running DXP

Execute DXP's startup script to [run DXP](./05-running-liferay-dxp-for-the-first-time.md).

Then use the [Setup Wizard](./06-using-the-setup-wizard.md) to complete basic configuration.

> **Note:** If you have a Liferay DXP Enterprise subscription, [activate Liferay DXP](./08-activating-liferay-dxp.md) to use all that the subscription offers.

## Conclusion

Congratulations! You understand the fundamentals for installing Liferay DXP. Make sure to visit the articles linked above to install DXP in the best way to meet your needs.

Then you can explore ways to configure and customize your installation (see next steps below), or start building solutions on Liferay DXP.

## Next Steps

[Additional Liferay DXP setup](../02-setting-up-liferay-dxp/01-config-overview.md) includes these topics:

* [Setting up Marketplace](../02-setting-up-liferay-dxp/setting-up-marketplace.md)
* [Trial Plugin Installation](../02-setting-up-liferay-dxp/trial-plugin-installation.md)
* Installing and Configuring a Search Engine
* [Securing Liferay DXP](../05-securing-liferay/01-securing-liferay.md)
* [Introduction to Clustering Liferay DXP](../02-setting-up-liferay-dxp/configuring-clustering-for-high-availability/01-introduction-to-clustering-liferay-dxp.md)
