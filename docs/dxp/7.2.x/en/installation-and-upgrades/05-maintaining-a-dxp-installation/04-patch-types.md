# Patch Types 

Liferay packages up DXP fixes regularly and for particular customer situations, and makes critical security fixes available fast. These packaged-up fixes are known as *patches* and undergo [different levels of testing](#patch-testing). Liferay provides subscribers fixes through these patch types: 

- [Hotfixes](#hotfixes) 
- [Fix packs](#fix-packs) 
- [Service packs](#service-packs) 

DXP CE fixes are incorporated in [CE GA releases](#ce-ga-releases). 

## HotFixes

A hotfix is provided to customers when they contact Liferay about an emergency situation, and Liferay's support team---working with the customer---determines that the problem is a product issue that must be fixed very quickly. Support fixes the bug and provides a hotfix to the customer immediately. This is a short-term fix. Hotfixes can patch the core, the applications, and modules. 

Some hotfixes depend on fix packs. If you attempt to install a hotfix that depends on a fix pack, the Patching Tool notifies you. Go to the [Customer Portal](https://customer.liferay.com/downloads) and obtain the hotfix dependency. Once all the necessary patches are downloaded to the `patches` folder, the Patching Tool installs them. 

## Fix Packs 

Fix packs include fixes for both the core and the applications and modules that ship with DXP. The fixes address regressions or obvious bugs and don't require you to make additional changes. Each fix pack contains all previous fix packs since the last service pack. 

[Security Fix Packs](https://help.liferay.com/hc/en-us/articles/360035038331) are a special fix pack type for deploying critical security fixes quickly without changing the DXP installation's fix pack level.

If you already have a hotfix installed and a fix pack that contains that hotfix is released, the Patching Tool manages this for you. Fix packs always supersede hotfixes; so when you install a fix pack, any hotfixes it contains are uninstalled and the fix pack version of the fix is installed in its place. 

The Patching Tool applies fixes to fix packs automatically. If a new (fixed) version of a fix pack is released, install it with the Patching Tool. The Patching Tool uninstalls the old fix pack and installs the new version in its place. 

Fixes that don't fit the fix pack requirements are considered for service packs or hotfixes. 

## Service Packs

Service packs are built on top of the original DXP release and repackaged with the latest fix pack, Patching Tool, and modules. Since a service pack is a fix pack, it contains all previous fix packs since the last service pack. Each one includes the most recent patches and updates. 

Service packs can also include changes that have these characteristics:

- Require more extensive testing
- Require some of your attention, such as updating your documentation 
- [Micro and minor version schema changes](https://help.liferay.com/hc/en-us/articles/360030959231-Meaningful-Schema-Versioning) 

Rather than updating your DXP installation with service packs, however you should keep it up-to-date with fix packs (according to your own deployment schedule). This method applies updates in smaller doses sooner while still achieving service pack levels.  

## CE GA Releases 

Liferay DXP CE GA releases are based on DXP service packs and are typically available a few weeks after the corresponding service packs. They include the same fixes, minus those for EE-only features. 

## Patch Testing

The following table describes the testing applied to each patch type. 

| **Patch Type** | **Testing** |
| :------------- | :---------- |
| Hotfixes       | Hotfixes receive automated regression testing similar to fix packs (see below), and the support engineer who fixes the reported issue tests it. |
| Fix packs      | Go through both automated regression testing and manual testing. |
| Service packs  | Liferay runs test suites on the packaged service pack. |
| CE GA Releases | The same testing as the corresponding service pack, plus upgrade testing from the previous GA. | 

## Conclusion 

Now that you know the patch types Liferay provides for delivering fixes, you can [stay updated on relevant patches](./keeping-up-with-fix-packs.md) and [install](./05-the-patching-process.md) them. 

## Additional Information 

- [The Patching Process](./05-the-patching-process.md)

- [Patching a DXP WAR:](./06-patching-a-dxp-war.md)

- [Installing the Patching Tool](./07-installing-the-patching-tool.md)

- [Keeping Up With Fix Packs and Service Packs](./11-keeping-up-with-fix-packs.md)
