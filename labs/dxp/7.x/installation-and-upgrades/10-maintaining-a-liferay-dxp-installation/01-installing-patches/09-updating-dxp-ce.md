# Updating DXP CE 

Fixes for DXP CE are delivered as new DXP CE GA releases. For example, DXP CE 7.2 GA2 fixes bugs that exist in DXP CE 7.2 GA1. There is no Patching Tool for DXP CE. Here are the steps for updating to your DXP CE installation to a new GA release:

1.  [Back up your DXP system](../backing-up.md) in case you want to revert to it. 

1.  Install the new DXP CE GA release on a new server. 

1.  Migrate your DXP CE files to the new server, making sure to point your new server at your current DXP database. This is similar to [preparing a new server in an DXP upgrade](https://help.liferay.com/hc/en-us/articles/360029031951-Preparing-a-New-Liferay-DXP-Server-for-Data-Upgrade). 

1.  Clear the OSGi state information by deleting all the files in the `[Liferay Home]/osgi/state` folder. 

    As background, if a module's changes are internal only, they are invisible to the OSGi framework, that module stays installed, and its state information stays unchanged. Clearing the OSGi bundle state information before the next portal startup makes sure that all modules reinstall with the appropriate state. 

    > **Warning**: The `osgi/state` folder should ONLY be deleted when working in a development environment or when applying a patch.

1.  Check for data upgrades in one of two ways: 

    -   Run the `upgrade:check` command in Gogo Shell to list modules that need upgrading. 

    -   Start the application server---it tells you if there are required data upgrades. 

Congratulations! You've updated your DXP CE installation to the new GA release!
