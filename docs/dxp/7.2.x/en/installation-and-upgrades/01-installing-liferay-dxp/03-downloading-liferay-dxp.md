# Downloading Liferay DXP

Downloading Liferay DXP is the first fundamental step for [installing Liferay DXP](./01-installation-overview.md). The following sections describe the installer types and the [Downloads](#downloads) section lists the installer-related files.

## Tomcat Bundle

The best starting point for _most_ people is the Liferay DXP Tomcat Bundle. Using the Liferay Tomcat bundle is the simplest and fastest way to get started with Liferay DXP. The Liferay Tomcat bundle includes the Apache Tomcat application server with DXP pre-deployed.

## Docker Image

A Docker image may also be used to get started quickly on Liferay DXP. Docker images may be obtained from [Docker Hub](https://hub.docker.com/u/liferay).

## WAR and Dependency JARs

A `.war` file is also provided that can be deployed to any [supported application server](https://help.liferay.com/hc/categories/360000894391-Product-Support) along with the supporting dependency JARs. This method of installation requires a user to install DXP by deploying the Liferay DXP `.war` and dependencies to an application server.

* DXP 7.2 WAR file
* Dependencies ZIP file
* OSGi Dependencies ZIP file

## Downloads

Liferay DXP and related resources can be downloaded from the [Help Center](https://help.liferay.com/hc) (subscribers only) and the [Community Downloads page](https://www.liferay.com/downloads-community).

The following files are available to download:

| File | Description |
| --- | --- |
| Client | Client dependencies for invoking DXP APIs  |
| Dependencies | DXP dependency libraries |
| OSGi Dependencies | DXP dependency OSGi modules |
| Reference Docs | DXP Javadocs, DTDs, Taglib docs, and Properties documentation  |
| Source | Liferay DXP source code |
| SQL | SQL scripts for preparing supported databases for DXP |
| Tomcat Bundle (`.tar.gz`) | GZipped bundle archive that installs on any OS |
| Tomcat Bundle (`.7z`) | 7-Zipped bundle archive that installs on any OS |
| Tools | Contains the Liferay Upgrade Client tool |
| WAR (Liferay DXP) | The Liferay DXP application for installing to any supported application server |

## Installing

Here are the installation instructions.

| Installation | Instructions |
| --- | --- |
| Tomcat Bundle | Extract the bundle to a location on your DXP host. This location is called your [Liferay Home](../14-reference/01-liferay-home.md). |
| WAR and Dependencies | Follow instructions for your app server: [Tomcat](./01-installing-liferay-on-an-application-server/01-installing-liferay-on-tomcat.md), [WildFly](placeholder-link), [JBoss EAP](placeholder-link), [WebLogic](placeholder-link), or [WebSphere](./01-installing-liferay-on-an-application-server/05-installing-liferay-on-websphere.md) |

## Next Steps

* [Connecting a Database](./04-connecting-a-database.md)
* [Using the Setup Wizard](./05-using-the-setup-wizard.md)
* [Running Liferay DXP for the First Time](./02-installation-overview.md#running-liferay-dxp-for-the-first-time)
