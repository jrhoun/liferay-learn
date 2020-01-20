# Using the Liferay Marketplace 

Liferay Marketplace is a hub for sharing, browsing, and downloading apps. Marketplace leverages the entire Liferay ecosystem to release and share apps in a user-friendly, one-stop shop.

![Figure 1: The Liferay Marketplace home page lets you browse and search for apps.](./using-the-liferay-marketplace/images/marketplace-homepage.png)

There are two ways to access the Marketplace.

1. **Marketplace website ([web.liferay.com/marketplace](https://web.liferay.com/marketplace)):** Open your browser [https://web.liferay.com/marketplace](https://web.liferay.com/marketplace). The website is the recommended way to download apps for production use.

2. **Control Panel:** In the Control Panel, navigate to *Apps* &rarr; *Store*. Sign in with your liferay.com account to view Marketplace.

    > **Note:** Using Marketplace in the Control Panel requires the Marketplace plugin. It is built-in to DXP bundles (e.g., the DXP Tomcat bundle). If you installed DXP on to an existing app server, you must [set up the Marketplace plugin](..\..\..\installation-and-upgrades\01-installing-liferay-dxp\09-setting-up-marketplace.md).

    > **Warning:** In production environments, purchase apps via the Marketplace website only---do not use Liferay Marketplace from the Control Panel. Clicking an app's *Purchase* button downloads and installs it immediately, which can cause problems if the app does not support auto-deploy.

No matter how you access Marketplace, you'll see the same app store content. Here are the Marketplace app topics:

- [Finding and purchasing apps](#finding-and-purchasing-apps)

- [Downloading apps](#downloading-apps)

- [Renewing apps](#renewing-apps)

Start with finding and purchasing the apps you want.

## Finding and Purchasing Apps

Marketplace provides a familiar app store experience. Apps are in the center of the page, in the following sections:

- Featured Apps: Liferay features a different set of apps each month.

- New and Interesting: The latest apps added to Marketplace.

- Most Viewed in the Past Month: The top 5 most viewed apps in the last month.

- Liferay Subscription Apps: Apps available to enterprise subscribers only.

- Templates and Themes: Apps for organizing site content and changing your site's look and feel.

- App categories: Communication, Productivity, Security, and more.

Each section's *See All* link lists all the apps for that section.

![Figure 2: Each app category page, such as the Communication app page, lists the apps published to that category.](./using-the-liferay-marketplace/images/marketplace-category-see-all.png)

At the top of the page, you can search Marketplace in these ways:

- Keywords
- Category
- Liferay (DXP) version
- Price (free or paid)

At the bottom of the page, Weekly Stats lists the newest apps and latest updated apps, and shows a trend chart for app downloads and views.

Click an app to view its details page. Each app's page includes these details:

- Description
- Screenshots
- Purchase button (labeled Free or Buy, depending on the price)
- Latest version
- Number of downloads
- Developer website link
- Documentation website link
- Support website link
- License agreement link
- Current requirements
- Past DXP versions the app works with
- Latest changes list
- Reviews 
- Version history 
- Access control 
- Installation instructions

![Figure 3: Click an app to see screenshots and app details.](./using-the-liferay-marketplace/images/marketplace-app-details.png)

> **Important:** Purchasing apps requires that you have a [liferay.com](https://www.liferay.com) account and agree to the Marketplace Terms of Use.

The purchase steps are the same via the Marketplace website and Marketplace in the Control Panel, **however**, completing the purchase via Marketplace in the Control Panel downloads the app and installs it to DXP immediately on the running DXP server. The best practice in production is to stop the DXP server,  and install the app during DXP server startup.

> **Warning:** In production, do not purchase apps in Marketplace via the Control Panel---only purchase apps via the [Marketplace website](https://web.liferay.com/marketplace).

Here are the app purchase steps:

1. Click the *Purchase* (Free or Paid) button. You're prompted to choose a purchase type.

1. Choose a purchase type. You can purchase an app for your personal account, or for a Liferay project associated with your company.

    A *Liferay project* is a space where teammates shares apps they have purchased or developed. If you have the necessary permissions, you can also create a new project for your company.

1. Accept the EULA and Terms of Service.

1. Complete the purchase.

On purchasing an app via the Marketplace website, your receipt is displayed immediately. 

The next section explains how to download purchased apps.

## Downloading Apps

You can download a purchased app via its receipt or via your account on Marketplace and liferay.com. 

Each Marketplace app is distributed as an LPKG package. The LPKG package contains Marketplace metadata and the files the app needs to run. Note that it's possible for an LPKG package to contain multiple app components (e.g., portlets, layout templates, and APIs). For example, a single LPKG package can contain several [portlets](https://help.liferay.com/hc/en-us/articles/360029046351-Introduction-to-Portlets). This is common in cases where an app requires a Control Panel portlet for administrators, and another portlet for end users.

### Downloading via the Purchase Receipt

The receipt displayed immediately on an app purchase links to a page for downloading that app.

1. In the receipt, click *See Purchased*. The *Purchased App* page for that app.

1. Click *App* to download the app.

### Downloading via the Purchased Apps Page 

The *Purchased Apps* page lets you download your purchased apps any time. It shows the apps you purchased, organized by project.

![Figure 4: You can manage your purchased apps from your Marketplace and liferay.com account home page.](./using-the-liferay-marketplace/images/marketplace-purchased-apps.png)

Here are the steps:

1. Navigate to the Purchased Apps page via the Marketplace website or liferay.com. 

    **Marketplace website:** Go to https://web.liferay.com/marketplace and sign in. Click on your profile picture in the top right corner and select *Purchased Apps*. 

    **Liferay.com:** Go to [liferay.com](https://www.liferay.com) and sign in. Click on your profile picture in the top right corner, select *Account Home* from the menu, and select *Apps* in the navigation panel on the left.

1. Select a project to view its registered apps.

1. Click a app's icon. A listing for the purchased app version appears. 

1. Click on *Past Versions* to view past versions. (Optional)

1.  Click *App* for the app version you want to download .

The app downloads as an LPKG file. You can use this file to [install the app](./03-installing-apps.md).

## Renewing Apps

To continue using a purchased app whose license terms are not perpetual, you must renew your app subscription, register your server to use the app, and generate a new activation key to use on your server. Here are the steps:

1. Go to [https://web.liferay.com/marketplace](https://web.liferay.com/marketplace). 

1. Click your profile picture in the upper right corner and select *Purchased Apps*. The Purchased Apps page appears and shows your app icons organized by project.

1. Click your app's icon. Your app's details page appears.

1. Click *Manage Licenses*.

1. Select *Register New Server*.

1. Select the most recent *Order ID* (typically the order that has no registered servers).

1. Fill in your server details.

1. Click *Register*.

1. Click *Download*. The new app activation key for your server downloads.

1. Copy the activation key file to your `deploy/` folder in your [`[Liferay Home]`](../../../installation-and-upgrades/14-reference/01-liferay-home.md).

You can continue using the application on your server.

Congratulations! You know how to find, purchase, download, and renew Liferay Marketplace apps.

## Additional information

- [Installing Apps](./03-installing-apps.md)

- [Managing Apps and App Components](./04-managing-apps-and-app-components.md)

- [Liferay Marketplace Developer Portal](https://marketplace.liferay.dev/)
