# Configuring Your Site's Friendly URL

Friendly URLs are used for both Public and Private Pages. The public Site base URL is `https://localhost:8080/web`, and the private one is `https://localhost:8080/group`. This helps Users quickly access their Site without having to recall an extended URL. Each friendly URL must be unique. The URL path is appended to the `https://localhost:8080/` URL (i.e. `https://localhost:8080/web/my-site/`).

## Setting a Site's Friendly URL

To update your site's friendly URL, follow these steps:

1. From the Site Menu on the left side of the screen, navigate to _Configuration_ &rarr; _Settings_.

1. Scroll down and expand the _Site URL_ panel.

1. Enter a new URL in the _Friendly URL_ input and click _Save_ to apply the changes.

![You can configure a friendly URL for your Site.](./configuring-your-sites-friendly-url/images/01.png)

If you add a friendly URL for your Site's Home Page, follow the additional steps in the next section.

## Updating Your Instance's Home URL

If you add a friendly URL for your instance's Home Page, you should update your instance's Home URL field so that page requests to `http://localhost:8080` redirect properly: <!-- What is a Home URL? Do I HAVE to do this? What does it impact? -->

1. Open the [Global Menu](../../../getting-started/navigating-dxp.md) ( ![Global Menu icon](../../../images/icon-applications-menu.png) ) and go to _Control Panel_ &rarr; _Instance Settings_.

1. Select _Instance Configuration_ under the _Platform_ heading and click the _General_ link.

1. Under _Navigation_, enter your new friendly home URL into the _Home URL_ field. For example, setting the friendly URL of your default Site to `/my-site` makes your Site's public Home Page's URL `https://localhost:8080/web/my-site/home`. So, you would enter `/web/my-site/home`.

![Enter the updated home URL to redirect to your new friendly URL.](./configuring-your-sites-friendly-url/images/02.png)

Once you've entered this setting, page requests to `localhost:8080` redirect to the friendly URL of your Liferay DXP instance's new Home Page.
