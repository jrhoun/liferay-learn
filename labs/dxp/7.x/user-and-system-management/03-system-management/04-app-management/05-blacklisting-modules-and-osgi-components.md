# Blacklisting Modules and OSGi Components

Blacklists are a convenient way to manage multiple OSGi bundle (module) and [OSGi Declarative Service Component](https://help.liferay.com/hc/en-us/articles/360028846452-Declarative-Services) (component) installations. You can set these lists in the Control Panel and using config files. These lists save you the trouble of modifying them individually with the [Application Manager](./04-managing-apps-and-app-components.md) or [Gogo shell](https://help.liferay.com/hc/en-us/articles/360029070351-Using-the-Felix-Gogo-Shell). Here's how the lists work:

- Adding modules to the module blacklist uninstalls them. 
- Adding components to the component blacklist disables them.

The blacklists can be exported from the Control Panel. Modifying the files and deploying them to DXP has these additional effects:

- Persists the changes across DXP server startups
- Propagates the changes from a local cluster node to all the other nodes.

Blacklisting modules and components using the UI and config files is demonstrated. Start with blacklisting modules.

## Blacklisting Modules

DXP removes any installed module on the blacklist. Blacklisted modules can't be installed. The log reports each module uninstallation.

Follow these steps to blacklist modules:

1.  In the Control Panel, navigate to *Configuration* &rarr; *System Settings* &rarr; *Module Container*.

1.  In the Bundle Blacklist screen, add the bundle symbolic names (see the table below) for the [module](https://help.liferay.com/hc/en-us/articles/360035467532-OSGi-and-Modularity#modules) JARs, LPKG files, or WARs to uninstall. Click the *Save* button when you're finished. DXP uninstalls the blacklisted modules immediately.
 
    ![Figure 1: This blacklist uninstalls the `com.liferay.docs.greeting.api` module, Liferay Marketplace LPKG, and `classic-theme` WAR.](./blacklisting-modules-and-osgi-components/images/bundle-blacklist-configuration.png)

1.  To export the blacklist, click its Actions button (![Actions](./blacklisting-modules-and-osgi-components/images/icon-actions.png)) and then click *Export*. The blacklist config file then downloads (`com.liferay.portal.bundle.blacklist.internal.BundleBlacklistConfiguration.config`). Here are contents from an example file:

    ```properties
    blacklistBundleSymbolicNames=["com.liferay.docs.greeting.api","Liferay\ Marketplace","classic-theme"]
    ```

1.  Add the bundle symbolic names of any modules not already listed that you want to uninstall and prevent from installing in subsequent DXP server startups.

    **Important**: Configuration values can't contain extra spaces. Extra spaces can short-circuit lists or invalidate the configuration entry.

1.  To deploy the configuration file, copy it into the folder `[Liferay Home]/osgi/configs`. The [Liferay Home](../../../installation-and-upgrades/14-reference/01-liferay-home.md) folder is typically the app server's parent folder.

**Note**: Blacklisting an LPKG uninstalls all of its internal modules.

**Blacklist Bundle Symbolic Names**

| Type       | Bundle Symbolic Name |
| ---------- | --------------|
| Bundle/Module JAR | `Bundle-SymbolicName` in `bnd.bnd` or `MANIFEST.MF` file |
| LPKG       | LPKG file name without the `.lpkg` extension |
| WAR        | Servlet context name in `liferay-plugin-package.properties` file or the WAR file name (minus `.war`), if there is no servlet context name property |

## Reinstalling Blacklisted Modules

To reinstall blacklisted modules, follow these steps:

1.  Open the configuration file `com.liferay.portal.bundle.blacklist.internal.BundleBlacklistConfiguration.config`.

1.  Remove the symbolic names of the module JARs, LPKGs, or WARs from the `blacklistBundleSymbolicNames` list and save the file.

To reinstall *all* the blacklisted modules execute one of these options:

- Remove the configuration file.
- Uninstall the module `com.liferay.portal.bundle.blacklist` using the [Application Manager](./04-managing-apps-and-app-components.md#using-the-app-manager) or [Felix Gogo Shell](https://help.liferay.com/hc/en-us/articles/360029070351-Using-the-Felix-Gogo-Shell).

> **Note**: To temporarily reinstall a module that's been blacklisted, you can remove its symbolic name from the Bundle Blacklist module in *System Settings* and click the *Update* button. If you're using a module blacklist config file (in the `[Liferay Home]/osgi/configs` folder) and want the module to install on subsequent server startup, make sure to remove the module's symbolic name from the file.

The log reports each module installation.

## Blacklisting Components

Follow these steps to disable OSGi components:

1.  In the Control Panel, navigate to *Configuration* &rarr; *System Settings* &rarr; *Module Container*.

1.  In the Component Blacklist screen, add the names of components to disable, and click the *Save* button. The components disable immediately.

    ![Figure 2: This blacklist disables the components `com.liferay.portal.security.ldap.internal.authenticator.LDAPAuth` and `com.liferay.ip.geocoder.sample.web.internal.portlet.IPGeocoderSamplePortlet`.](./blacklisting-modules-and-osgi-components/images/component-blacklist-configuration.png)

1.  To export the blacklist, click on the Component Blacklist module's Actions button (![Actions](./blacklisting-modules-and-osgi-components/images/icon-actions.png)) and then click *Export*. The blacklist configuration file then downloads (`com.liferay.portal.component.blacklist.internal.ComponentBlacklistConfiguration.config`). Here are contents from an example file:

    ```properties
    blacklistComponentNames=["com.liferay.portal.security.ldap.internal.authenticator.LDAPAuth","com.liferay.ip.geocoder.sample.web.internal.portlet.IPGeocoderSamplePortlet "]
    ```

1.  Add the names of any components not already listed (e.g., components of modules not yet installed) that you want to prevent from enabling.

    **Important**: Configuration values can't contain extra spaces. Extra spaces can short-circuit lists or invalidate the configuration entry.

1.  To deploy the configuration file, copy it into the folder `[Liferay Home]/osgi/configs`. The Liferay Home folder is typically the app server's parent folder.

## Re-enabling Blacklisted Components

To re-enable and permit enabling of blacklisted OSGi components, follow these steps:

1.  Open the configuration file `[Liferay Home]/osgi/configs/com.liferay.portal.component.blacklist.internal.ComponentBlacklistConfiguration.config`.

1.  Remove the names of the components from the `blacklistComponentNames` list and save the file.

To enable *all* the blacklisted components, remove the configuration file.

> **Note**: To temporarily re-enable a blacklisted component, remove its name from the Component Blacklist Configuration module in System Settings and click *Update*. If you're using a component blacklist config file (in the `[Liferay Home]/osgi/configs` folder) and want the component to enable on subsequent server startup, make sure to remove the component's name from the file.

Congratulations! Now you can manage multiple module and component installations using two simple lists.

## Additional Information

[Managing Apps and App Components](./04-managing-apps-and-app-components.md)

[Using the Felix Gogo shell](https://help.liferay.com/hc/en-us/articles/360029070351-Using-the-Felix-Gogo-Shell)
