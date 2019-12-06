# Maintaining a Liferay DXP Installation

Once you have Liferay DXP deployed, you can add to it, update it, and apply fixes. In preparation any failure or unwanted side affects from modifying your DXP installation, you should implement a plan for backing up your system and restoring it. The articles here start with identifying the system components you should back up and then continue demonstrating how to update your DXP system with the latest fixes. 

## Backing Up Your System

Storing copies of your DXP files, databases, and customization source code allows you to restore your system. [Backing Up](./02-backing-up.md) provides guidance for persisting and restoring your system components. 

## Updating DXP 

Maintaining your DXP instance involves [patching](./03-patching-liferay-dxp.md) it, deploying [configuration changes](https://help.liferay.com/hc/en-us/articles/360029131651-Understanding-System-Configuration-Files), [updating apps](https://help.liferay.com/hc/en-us/articles/360029134911-Managing-and-Configuring-Apps), and updating third-party software (e.g., the application server, JVM, and more). Any updates that affect your production instance require careful planning. The [DXP cluster update instructions](../10-maintaining-clusters/01-maintaining-clustered-installations.md) describe ways to handle these updates.

Patching your system regularly (if you're a DXP subscriber) or [upgrading your CE instance](./upgrading-to-liferay-dxp-7-2.md) to a new GA gives you the latest bug fixes. The [patching articles](./03-patching-liferay-dxp.md) explain the different DXP patch types and how to install them using the Patching Tool. 

Read on to learn how to keep your system running well. 
