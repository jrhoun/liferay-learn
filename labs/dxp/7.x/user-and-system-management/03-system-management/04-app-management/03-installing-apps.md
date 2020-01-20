# Installing Apps

After [purchasing an app](./02-using-the-liferay-marketplace.md), you can install it. It's typical to try an app before deploying it to a formal environment (e.g., production server or a cluster). For casual purposes, DXP supports "auto deploying" apps---installing them while the server is running. This allows DXP to provide these UIs for installing apps:

- [Marketplace in the Control Panel](#using-marketplace-in-the-control-panel): Connects to the Marketplace to support purchasing and installing an apps simultaneously. It also provides screens for managing Marketplace apps.

- [App Manager](#using-the-app-manager): Installs apps you've downloaded as `.lpkg` files and apps via URLs.

You can also [install apps via the File System](#using-the-file-system) on the DXP server, which can be running or stopped.

> **Important:** Installing apps while the server is running is NOT recommended for production and other formal environments. This is because not all apps are designed to be auto deployed. Deploying such apps that way can cause instabilities, such as class loading leaks and memory leaks.

Since installing apps in production is the end goal, it's discussed first. [Installing apps in casual environments](#installing-apps-in-casual-environments) is demonstrated afterwards.

## Installing Apps in Production

Installing an app while the server is stopped is a sure-fire way to install an app to any environment, no matter how casual your environment might be. Here are the steps:

1. Stop your DXP server.

1. Copy your app (LPKG, module JAR, or plugin WAR) to your `[Liferay Home]/deploy` folder. The [Liferay Home](../../../installation-and-upgrades/14-reference/01-liferay-home.md) folder is typically the app server's parent folder.

1. Start your DXP server.

The app installation commences. If the app's dependencies resolve, it installs.

> **Note:** [OSGi component configurations](https://help.liferay.com/hc/en-us/articles/360029131591-System-Settings#exporting-and-importing-configurations) are also best installed while the DXP server is stopped. If you're installing a component configuration, copy its `.config` file to your `[Liferay Home]/osgi/configs` folder. 

> **Note:** If you're running in cluster, follow the instructions for [updating a cluster](../../../installation-and-upgrades/10-maintaining-clusters/01-maintaining-clustered-installations.md).

If it's not feasible to stop your server or you're app *is* designed for auto deployment, DXP provides several "auto deployment" conveniences. They're demonstrated next.

## Installing Apps in Casual Environments

There are several convenient ways to deploy apps and configurations in informal, non-production environments.

- [Marketplace via the Control Panel](#installing-apps-via-marketplace-in-the-control-panel)
- [App Manager](#installing-apps-via-the-app-manager)
- [File system](#installing-apps-via-the-file-system)

They use auto deployment, copies the app or configuration file to the appropriate subfolder in `[Liferay Home]/osgi`, converts it to an OSGi bundle (LPKGs and WARs need converting), and deploys the bundle to the OSGi container. By default, the following `[Liferay Home]/osgi` subfolders are used per type:

- `marketplace`: Marketplace LPKG packages
- `modules`: OSGi module JAR files
- `war`: WAR files
- `configs`: [Configuration files](https://help.liferay.com/hc/en-us/articles/360029131591-System-Settings#exporting-and-importing-configurations)

> **Warning:** Avoid repeatedly auto deploying new versions of apps that aren't designed for auto deployment.

> **Note:** LPKG packages that have the `restart-required=true` property in their `liferay-marketplace.properties` file (inside the LPKG file) require a server restart to complete installation. If you inadvertently auto deploy such an LPKG package, the installation hangs and reports a message like this: `14:00:15,789 INFO  [com.liferay.portal.kernel.deploy.auto.AutoDeployScanner][AutoDeployDir:252] Processing Liferay Push 2.1.0.lpkg`

> **Note:** An app server doesn't need to support "hot deploy" for auto deploy to work. DXP's module framework (OSGi) enables auto deploy. Any app server running DXP therefore also supports this auto deploy mechanism.

The Control Panel's Marketplace interface immediately installs apps on purchase.

### Installing Apps via Marketplace in the Control Panel

The Control Panel provides a purchased apps page for installing apps.

1. Open the Control Panel.

1. Navigate to *Apps* &rarr; *Purchased* to see your purchased apps.

1. An button (install or uninstall) next to each app lets you install or uninstall the app. If the app isn't compatible with your DXP version, *Not Compatible* is displayed in place of the button. Additional compatibility notes are also shown, such as whether a newer version of the app is available. You can also search for an app here by project, category, and title. Clicking the app takes you to its Marketplace entry.

    ![Figure 1: The Control Panel's purchased apps lets you manage your purchased apps from within a running Liferay instance.](./installing-apps/images/marketplace-purchased-apps.png)

1. Click *Install* to install the app to DXP.

> **Note:** Using Marketplace in the Control Panel requires the Marketplace plugin. It is built-in to DXP bundles (e.g., the DXP Tomcat bundle). If you installed DXP on to an existing app server, you must [set up the Marketplace plugin](..\..\..\installation-and-upgrades\01-installing-liferay-dxp\09-setting-up-marketplace.md).

If you downloaded an app from the Marketplace website, you can install it via the App Manager (discussed next).

### Installing Apps via the App Manager

The App Manager is a convenient way to install an app from your local machine to a remote and local DXP server.

1. Navigate to *Control Panel* &rarr; *Apps* &rarr; *App Manager*.

1. Select *Upload* from the options button (![Options](./installing-apps/images/icon-options.png)). The Upload dialog appears.

1. Browse for the app on your machine and then click *Install*.

The app installs via auto deploy. When the install completes, close the dialog and you're ready to roll!

> **Note:** To uninstall an app installed with the App Manager, use [Blacklisting](./05-blacklisting-modules-and-osgi-components.md).

### Installing Apps via the File System

To install an app or configuration via the DXP server's local file system, put the app file in the `[Liferay Home]/deploy` folder (the [Liferay Home](../../../installation-and-upgrades/14-reference/01-liferay-home.md)). The auto deploy mechanism copies the app to the appropriate subfolder in `[Liferay Home]/osgi`, converts it to an OSGi bundle, and deploys the bundle to the OSGi container.

## Conclusion

Now you know how to install apps for formal environments and informal environments. The steps for installing to formal environments requires stopping the server and restarting it. There are several convenient mechanisms for installing apps to informal environments too.

## Additional Information

- [Using the Liferay Marketplace](./02-using-the-liferay-marketplace.md)

- [Maintaining a Clustered Installation](../../../installation-and-upgrades/10-maintaining-clusters/01-maintaining-clustered-installations.md)

- [Managing Apps and App Components](./04-managing-apps-and-app-components.md)

- [Blacklisting Modules and OSGi Components](./05-blacklisting-modules-and-osgi-components.md)

- [OSGi component configurations](https://help.liferay.com/hc/en-us/articles/360029131591-System-Settings#exporting-and-importing-configurations)
