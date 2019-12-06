# Patching a DXP WAR

If you [installed DXP manually](https://help.liferay.com/hc/en-us/articles/360029031451-Obtaining-Liferay-DXP#downloading-the-liferay-war-and-dependency-jars) as a WAR file on a supported application server, you must apply patches to the WAR file and supporting files and re-deploy them. Here are the steps for patching your DXP WAR:

1.  Download the necessary artifacts from the [Customer Portal:](https://customer.liferay.com/downloads)

    - DXP WAR file (`liferay-dxp-[version].war`)
    - Dependencies ZIP file (`liferay-dxp-dependencies-[version].zip`)
    - OSGi JARs ZIP file (`liferay-dxp-osgi-[version].zip`) 
    - [Latest Patching Tool](https://customer.liferay.com/downloads?p_p_id=com_liferay_osb_customer_downloads_display_web_DownloadsDisplayPortlet&_com_liferay_osb_customer_downloads_display_web_DownloadsDisplayPortlet_productAssetCategoryId=118191019&_com_liferay_osb_customer_downloads_display_web_DownloadsDisplayPortlet_fileTypeAssetCategoryId=118191066)

1.  Create an arbitrary folder to be your *patching home*. Unzip the dependency artifacts and the Patching Tool into it. The folder contents should look like this:

    - `[patching-home]/`
        - `liferay-dxp-dependencies-[version]/` &larr; Unzipped Dependencies
        - `osgi/` &larr; Unzipped OSGi JARs
        - `patching-tool/` &larr; Unzipped Patching Tool
        - `liferay-dxp-[version].war/` &larr; DXP WAR File

1.  [Configure the Patching Tool](./08-configuring-the-patching-tool.md) using `auto-discovery` or by editing a configuration profile (e.g.,  `patching-tool/default.properties`). The configuration should look like this:

    ```properties
    patching.mode=binary
    war.path=../../patching-home/liferay-dxp-[version].war
    global.lib.path=../../patching-home/liferay-dxp-dependencies-[version]
    liferay.home=../../patching-home
    ```

    If you're using a different OSGi folder structure, [account for it in your configuration](./08-configuring-the-patching-tool.md). 

1.  Download the patch to the `patching-tool/patches` folder---don't unzip the patch. 

    Patch download locations:

    - Fix packs and service packs are on the [Customer Portal](https://customer.liferay.com/downloads) 
    - Hotfixes are in [Help Center](https://help.liferay.com/hc) tickets

1.  Install the patch. 

    ```bash
    /patching-home/patching-tool> patching-tool.sh  install
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

1.  If you're installing a Service Pack, check for [micro or minor schema/data changes](https://help.liferay.com/hc/en-us/articles/360030959231-Meaningful-Schema-Versioning) in the service pack release notes. Use the [upgrade tool](https://help.liferay.com/hc/en-us/articles/360028711612-Introduction-to-Upgrading-to-Liferay-DXP-7-2) to apply minor changes (required) and any micro changes you want. 

**Important:** Before deploying the artifacts, make sure to prepare your DXP installation based on the suggested [patching process](./05-the-patching-process.md). 

## Conclusion 

Great! You have successfully patched the artifacts, and they are ready to be deployed on any supported application server. 

## Additional Information

- [The Patching Process](./05-the-patching-process.md)

- [Installing the Patching Tool](./07-installing-the-patching-tool.md)

- [Configuring the Patching Tool](./08-configuring-the-patching-tool.md)

- [Working With Patches](./09-working-with-patches.md)

- [Keeping Up With Fix Packs and Service Packs](./11-keeping-up-with-fix-packs.md)
