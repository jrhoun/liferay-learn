# Configuring the Patching Tool 

Liferay DXP bundles ship with the Patching Tool preconfigured. If any of the following scenarios describes your DXP installation, however, you must configure the Patching Tool:

- Installed DXP manually on an existing application server
- Customized your DXP folder structure
- Running in a cluster

The following sections demonstrate how to configure the Patching Tool using auto-discovery (easiest) and using other ways DXP runtime environments may require. 

- [Automatic Configuration Using `auto-discovery`](#automatic-configuration-using-auto-discovery) 
- [Editing Configurations](#editing-configurations) 
- [Using Profiles](#using-profiles)
- [Troubleshooting](#troubleshooting)

## Automatic Configuration Using Auto-Discovery

The Patching Tool is configured using a properties file. The tool's `auto-discovery` command generates or updates the specified properties file (default is `patching-tool/default.properties`) based on local DXP files it discovers. 

Run the auto-discovery command in your `patching-tool/` folder: 

```bash
patching-tool auto-discovery
```

By default the Patching Tool looks for DXP files in the parent folder. If DXP is not installed in the parent folder, specify its location: 

```bash
patching-tool auto-discovery /path/to/liferay-dxp
```

When the Patching Tool is configured, running `patching-tool info` reports product information and patch information like this: 

``` 
/patching-tool>patching-tool info
Loading product and patch information...
Product information:
  * installation type: binary
  * build number: 7210
  * service pack version:
    - available SP version: 1
    - installable SP version: 1
  * patching-tool version: 2.0.13
  * time: 2019-12-05 14:02Z
  * host: 91WRQ72 (8 cores)
  * plugins: no plugins detected
  ...
```

The Patching Tool is ready to install patches! 

Note: If auto-discovery can't find your DXP files, follow the [troubleshooting steps](#troubleshooting). If your DXP files still aren't discovered or you're using a custom folder structure for DXP, manually edit the Patching Tool configuration. 

## Editing Configurations 

Patching Tool configuration files (e.g., `default.properties`) typically looks like this:

```properties
patching.mode=binary
war.path=../tomcat-9.0.17/webapps/ROOT/
global.lib.path=../tomcat-9.0.17/lib/ext/
liferay.home=../
```

The properties above (described fully in [Patching Tool Configuration Properties](../08-reference/07-patching-tool-configuration-properties.md)) specify these things:

- Patching mode (binary or source)
- Path to your DXP WAR file
- Global library path (this is where the DXP Dependency JARs reside)
- Location of [Liferay Home](../08-reference/01-liferay-home.md)

The auto-discovery command bases the OSGi module framework paths on the Liferay Home. If, however, you changed the OSGi module framework paths to something different than those under the default folder `[Liferay Home]/osgi`, you must manually specify the following properties: 

```properties
module.framework.core.path=path/to/modules/core/folder
module.framework.marketplace.path=path/to/modules/marketplace/folder
module.framework.modules.path=path/to/modules/modules/folder
module.framework.portal.path=path/to/modules/portal/folder
module.framework.static.path=path/to/modules/static/folder
```

Using auto-discovery and working with the default profile `default.properties` is the easiest way to use the Patching Tool, and is great for smaller, single server installations. But many DXP installations serve millions of pages per day, and the Patching Tool is designed for this as well. So if you're running a small, medium, or large cluster of DXP machines, you can use Patching Tool profiles to manage patching for all of them. 

## Using Profiles 

You can create profiles for multiple runtimes by running auto-discovery or creating profiles manually. To auto-discover a DXP runtime, run the Patching Tool with parameters like this: 

```bash
patching-tool [name of profile] auto-discovery [path/to/Liferay Home]
```

This runs the same discovery process and writes the profile information to a file called `[name of profile].properties`. Alternatively, you can create and edit profile property files in your `patching-tool/` folder. See [Patching Tool configuration properties](../08-reference/07-patching-tool-configuration-properties.md) for a complete list of properties. 

Once you've created a profile, you can use it in your Patching Tool commands. For example, this command installs a patch using a profile file called `test-server.properties`:

```bash
patching-tool test-server install 
```

## Troubleshooting 

If you specify the wrong DXP location to auto-discovery or DXP is not in the parent folder, the Patching Tool can't find the [Liferay Home](../08-reference/01-liferay-home.md) and reports an error like this: 

```
The .liferay-home has not been detected in the given directory tree.

Configuration:
patching.mode=binary
war.path=../tomcat-9.0.17/webapps/ROOT/
global.lib.path=../tomcat-9.0.17/lib/ext/
liferay.home=**[please enter manually]**

The configuration hasn't been saved. Please save this to the default.properties file.
```

Here are ways to resolve the Liferay Home issue:

- Specify the Liferay Home path in the `default.properties` file.
- If the Liferay Home is in the Patching Tool's tree, create a `.liferay-home` file in the Liferay Home folder and re-run the  auto-discovery process. 

## Conclusion 

Congratulations! The Patching Tool is ready to install patches. 

## Additional Information 

- [Comparing Patch Levels](../08-reference/06-comparing-patch-levels.md) 

- [The Patching Process](./05-the-patching-process.md)

- [Patching a DXP WAR](./06-patching-a-dxp-war.md)

- [Installing the Patching Tool](./07-installing-the-patching-tool.md)

- [Keeping Up With Fix Packs and Service Packs](./11-keeping-up-with-fix-packs.md)
