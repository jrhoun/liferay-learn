# Backing Up

Once you have your DXP installation running, you should implement a comprehensive backup plan. In case some kind of catastrophic hardware failure occurs, you'll be thankful to have backups and procedures for restoring DXP from one of them. The backup copies are also valuable for testing updates (e.g., DXP upgrades, new plugins, and more). In this way, DXP backups and updates work hand in hand. 

DXP isn't very different from other Java web applications that might be running on your application server. Nevertheless, there are some specific components you should include in your backup plan.

## Overview

-   [Backing up Source Code](#backing-up-source-code)
-   [Backing up DXP's File System](#backing-up-dxps-file-system)
-   [Backing up DXP's Database](#backing-up-dxps-database)

## Backing up Source Code

If you have extended DXP or have written any plugins, they should be stored in a source code repository such as Git, Subversion, or CVS. You should back up your source code repository on a regular basis to preserve your ongoing work. 

## Backing up DXP's File System

It's best to back up your entire application server and [Liferay Home folder](../08-reference/01-liferay-home.md) contents.

The application server has the DXP descriptors, deployments, and dependencies you might have customized. If you've customized DXP's `web.xml` file, for example, you'll want to back it up because a DXP patch's `web.xml` always overwrites the existing one. Backing up your entire application server is suggested. 

The Liferay Home folder is important to back up because it contains the following files (and more):

- **Portal properties:** The Liferay Home folder stores DXP's [portal properties files](https://help.liferay.com/hc/en-us/articles/360028712292-Portal-Properties), such as `portal-setup-wizard.properties` and `portal-ext.properties`. You should absolutely back them up. 

- **`/data` folder:** DXP stores configuration files, search indexes, and cache information in Liferay Home's `/data` folder. If you're using the File System store or the Advanced File System store, the [Documents and Media repository](https://help.liferay.com/hc/en-us/articles/360028810112-Document-Repository-Configuration) is also stored here by default. It's always important to back up your `/data` folder.

- **`/osgi` folder:** The files that comprise DXP's OSGi runtime are stored in Liferay Home's `/osgi` folder. It contains all of the app and module JAR files deployed to DXP. The `/osgi` folder also contains other required JAR files, [configuration files](https://help.liferay.com/hc/en-us/articles/360029131651-Understanding-System-Configuration-Files), and log files. 

- **`/logs` folder:** Contains DXP's log files. If a problem occurs on DXP, the log files provide information for determining what went wrong. 

The `/data`, `/osgi`, and `/logs` folders are all contained in the Liferay Home folder. Thus, if you're backing up both your application server folder and your Liferay Home folder, you're in good shape. 

**Important:** If you configured your [Documents and Media repository](https://help.liferay.com/hc/en-us/articles/360028810112-Document-Repository-Configuration) to a location other than the default location, back up that location.

## Backing up DXP's Database

DXP's database is the central repository for all of the portal's information. It's the most important component to back up. You can back up the database live (if your database allows this) or by exporting (dumping) the database into a file and then backing up the exported file.

For example, MySQL ships with a `mysqldump` utility which lets you export the entire database and data into a large SQL file. This file can then be backed up. On restoring the database you can import this file into the database to recreate the database state to that of the time you exported the database.

**Important:** If you've placed your search index into a database (not recommended; see the [DXP Clustering](https://help.liferay.com/hc/en-us/articles/360029123831-Liferay-DXP-Clustering) article for information on using Cluster Link or Solr), you should back up that database too. 

If you wish to avoid re-indexing your content after restoring your database, back up your search indexes. This is easiest to do if you have a separate [Elasticsearch or Solr](https://help.liferay.com/hc/en-us/articles/360028711092-Introduction-to-Installing-a-Search-Engine) environment on which your index is stored. If you're in a clustered configuration and you're replicating indexes, you must back up each index replica.

## Conclusion 

Restoring your application server, your Liferay Home folder, the locations of any file system-based media repositories, and your database from a backup system should give you a functioning portal. Restoring search indexes should avoid the need to re-index when you bring your site back up after a catastrophic failure. Exercising good, consistent backup procedures such as these, are key to recovering successfully from a hardware failure.
