# The Patching Process 

DXP bundles include the Patching Tool preconfigured. Here are the steps for patching a DXP installation (specifically a DXP bundle). 

1.  [Back up your DXP system](./02-backing-up.md) in case you want to revert to it. 

1.  Download the patch to the `[Liferay Home]/patching-tool/patches` folder---don't unzip the patch. 

    Patch locations:
    
    - [Customer Portal](https://customer.liferay.com/downloads): Fix packs and service packs 
    - [Help Center](https://help.liferay.com/hc) tickets: Hotfixes

1.  Shut down your application. 

    Reasons: 

    - On Windows operating systems, files in use are locked by the OS, and can't be patched.
    - On Unix-style systems, you can usually replace files that are running, but the old ones reside in memory. 
    
1.  Install the patch by running the `patching-tool install` command: 

    ```bash
    /liferay-home/patching-tool> patching-tool  install
    One patch is ready to be installed. Applying dxp...
    Cleaning up: [1%..10%..20%..30%..40%..50%..60%..70%..80%..90%..100%]
    Installing patches: [1%..10%..20%..30%..40%..50%..60%..70%..80%..90%...100%]
    The installation was successful. One patch is installed on the system.
    ```

1.  Use the `info` command to verify that the patch is currently installed:
    
    ```
    patching-tool>patching-tool info
    Loading product and patch information...
    Product information:
      * installation type: binary
      * build number: 7210
      * service pack version:
        - available SP version: 1
        - installable SP version: 1
      * patching-tool version: 2.0.13
      * time: 2019-12-06 20:26Z
      * host: 91WRQ72 (8 cores)
      * plugins: no plugins detected
    
    Currently installed patches: 
    ...
    ```

1.  Check for [micro or minor schema/data changes](https://help.liferay.com/hc/en-us/articles/360030959231-Meaningful-Schema-Versioning) in the service pack release notes. (Service packs only)

     Use the [upgrade tool](https://help.liferay.com/hc/en-us/articles/360028711612-Introduction-to-Upgrading-to-Liferay-DXP-7-2) to apply minor changes (required) and any micro changes you want. 

1.  Clear the OSGi state information by deleting all the files in the `[Liferay Home]/osgi/state` folder. 

    As background, if a module's changes are internal only, they are invisible to the OSGi framework, that module stays installed, and its state information stays unchanged. Clearing the OSGi bundle state information before the next portal startup makes sure that all modules reinstall with the appropriate state. 

    > **Warning**: The `osgi/state` folder should ONLY be deleted when working in a development environment or when applying a patch.

1.  Restart the application server

Congratulations! Your DXP instance is patched and running. 

## Additional Information 

- [Comparing Patch Levels](../08-reference/06-comparing-patch-levels.md) 

- [Patching a DXP WAR:](./06-patching-a-dxp-war.md) 

- [Installing the Patching Tool](./07-installing-the-patching-tool.md)

- [Configuring the Patching Tool](./08-configuring-the-patching-tool.md)

- [Working With Patches](./09-working-with-patches.md)

- [Keeping Up With Fix Packs and Service Packs](./11-keeping-up-with-fix-packs.md)
