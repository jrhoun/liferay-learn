# Consuming REST Services

Liferay DXP contains REST services for most of the applications shipped with it. These services are fully [OpenAPI](https://app.swaggerhub.com/apis/liferayinc/headless-delivery) compliant. Here, you'll learn how to consume them. This takes only three steps: 

1. Identify the service you wish to consume. 
1. Identify the site containing the data you need. 
1. Make the service call using credentials that have access to the data. 

This example uses Docker image with a fresh install of Liferay DXP. 

## Identify the Service to Consume

Liferay DXP's REST services are published on [Swagger Hub](https://app.swaggerhub.com/apis/liferayinc/headless-delivery). This example uses the `BlogPosting` service to retrieve blog posts from the Blogs widget, but you can use this procedure with any of the services listed on Swagger Hub. The documentation there shows all the parameters necessary for performing the call and includes example JSON or XML that the service returns. 

## Identify the Site Containing the Data

You need a running Liferay DXP website to call its REST services. To obtain one using Docker, run this command: 

```bash
docker run -it -p 8080:8080 liferay/portal:7.3.0-ga1
```

After Liferay DXP initializes, visit it with your browser at `http://localhost:8080`. 

You'll need to create a blog entry:

1. Sign in using the default credentials: 
   **User Name:** `test@liferay.com`
   **Password:** `test`
1. Click *Content & Data* &rarr; *Blogs*. 
1. Click the blue Plus button to add a blog entry. 
1. When finished typing your blog entry, click *Publish*. 

Now that you have your blog entry in your site, you need only find the site ID: 

1. Go to Control Panel &rarr; Sites &rarr; Sites. 
1. Click the Actions button, and then choose *Go to Site Settings*. 

The Site ID appears at the top of the Details section. It's an Integer, like `20119`.

## Make the Service Call Using Credentials with Access to the Data


