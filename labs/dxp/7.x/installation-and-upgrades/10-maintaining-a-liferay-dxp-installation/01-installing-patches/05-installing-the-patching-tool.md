# Installing the Patching Tool 

DXP bundles come with the Patching Tool pre-installed (`[Liferay Home]/patching-tool`) and pre-configured. If you installed DXP manually or you need to update to the latest Patching Tool, follow the steps here.  

## Installation

1.  Download the Patching Tool from the [Customer Portal](https://customer.liferay.com/downloads?p_p_id=com_liferay_osb_customer_downloads_display_web_DownloadsDisplayPortlet&_com_liferay_osb_customer_downloads_display_web_DownloadsDisplayPortlet_productAssetCategoryId=118191019&_com_liferay_osb_customer_downloads_display_web_DownloadsDisplayPortlet_fileTypeAssetCategoryId=118191066).

2.  Unzip the Patching Tool to your [Liferay Home](../../14-reference/01-liferay-home.md) folder (recommended) or to another folder. 

The Patching Tool folder `patching-tool` includes the Unix shell script `patching-tool.sh` and Windows batch script `patching-tool.bat`. The Windows command `patching-tool` is used in the examples.

To print the Patching Tool help message, execute this command in the `patching-tool` folder: 

```bash
patching-tool help
```

## Updating the Patching Tool

When a patch you're trying to install requires a newer version of the Patching Tool, the Patching Tool tells you. To update the Patching Tool:

1. Download the latest one from the [Customer Portal](https://customer.liferay.com/downloads?p_p_id=com_liferay_osb_customer_downloads_display_web_DownloadsDisplayPortlet&_com_liferay_osb_customer_downloads_display_web_DownloadsDisplayPortlet_productAssetCategoryId=118191019&_com_liferay_osb_customer_downloads_display_web_DownloadsDisplayPortlet_fileTypeAssetCategoryId=118191066).

2.  Overwrite the existing Patching Tool by unzipping the new one to the `patching-tool` folder's parent folder. 

The Patching Tool is ready to configure with your DXP installation. 

## Additional Information 

- [The Patching Process](./03-the-patching-process.md)

- [Patching a DXP WAR](./04-patching-a-dxp-war.md)

- [Configuring the Patching Tool](./06-configuring-the-patching-tool.md)

- [Comparing Patch Levels](../../14-reference/07-comparing-patch-levels.md) 

- [Keeping Up With Fix Packs and Service Packs](./08-keeping-up-with-fix-packs.md)
