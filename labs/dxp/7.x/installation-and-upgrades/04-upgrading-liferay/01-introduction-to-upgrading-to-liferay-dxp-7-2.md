# Introduction to Upgrading to Liferay DXP 7.2

Upgrading to Liferay DXP 7.2 involves updating your data, files, plugins, and custom code, as well as optimizing and testing the upgrade to ensure it goes as quickly and smoothly as possible for your final production data upgrade. Each step's complexity scales up with the amount of data and number of customizations in your installation. The main steps shown below can potentially be done in parallel.

> **Note:** Dev Studio's [Upgrade Planner](https://help.liferay.com/hc/en-us/articles/360029147451-Liferay-Upgrade-Planner) walks through the upgrade process and automates parts of it. The Planner uses a terse [step listing](../14-reference/06-liferay-upgrade-planner-steps.md) you can follow or refer to throughout the upgrade process.

## Adapting to Feature Changes

New DXP versions can deprecate features, remove features, or [move features into maintenance mode](./99-features-in-maintenance-mode.md). The [DXP 7.2 deprecations article](./98-deprecations-in-liferay-dxp-7-2.md) explains the ramifications so you can adapt to the changes.

## Upgrading Custom Code and Plugins

Custom code upgrade involves adapting themes and apps you've developed to DXP 7.2. This can be as simple as updating dependencies for the new version, or it may involve major code changes. [Upgrading Code to Liferay DXP 7.2](https://help.liferay.com/hc/en-us/articles/360029316391-Introduction-to-Upgrading-Code-to-Liferay-DXP-7-2) (a separate guide) demonstrates the process. The code upgrade can be done in parallel with the data upgrade.

### Upgrading Marketplace Apps

You must also upgrade your installation's Marketplace apps (Kaleo, Calendar, Notifications, etc.) to their latest version for your current Liferay DXP installation. Troubleshoot any issues with these apps on your current DXP installation before upgrading to DXP 7.2.

## Upgrading Your Database

Upgrading the database is the biggest milestone in the upgrade process to DXP 7.2. See [Upgrading the Database](./02-upgrading-the-database.md) for an overview of the main steps in performing the data upgrade.

## Preparing a New Liferay DXP Server

[New DXP server setup](./06-preparing-a-new-application-server-for-liferay-dxp.md) involves installing DXP 7.2, migrating and updating your portal properties and OSGi properties, and installing any necessary patches.

## Installing the Search Engine

If you do not already have your own Elasticsearch/Solr installation running, you must set one up for Liferay DXP. By default, Liferay DXP ships with an embedded configuration for Elasticsearch. The embedded configuration works great for demo purposes, but is not supported in production. See [Installing Elasticsearch](https://help.liferay.com/hc/en-us/articles/360028711132-Installing-Elasticsearch) or [Installing Solr](https://help.liferay.com/hc/en-us/articles/360032264052-Installing-Solr) for more information.

Once the major preparation tasks are identified, it's time to examine the data upgrade tasks.
