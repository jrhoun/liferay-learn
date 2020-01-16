# Getting Started with Liferay DXP

Follow these steps to quickly take Liferay DXP for a test drive and tour its features on your own Linux, macOS, or Windows machine.

> For Liferay DXP CE 7.3 GA1, visit [Community Downloads page](https://www.liferay.com/downloads-community) and see the [Installation Overview](./02-installation-overview.md).

## Run Liferay DXP locally on Linux, macOS, or Windows

> JAVA JDK 8 or 11 are required to run Liferay DXP. Learn more by visiting [www.java.com](https://www.java.com/).

1. Download

    `curl -L -O https://github.com/liferay/liferay-portal/releases/download/7.2.1-ga2/liferay-ce-portal-tomcat-7.2.1-ga2-20191111141448326.tar.gz`

1. Extract

    `tar -xzf liferay-ce-portal-tomcat-7.2.1-ga2-20191111141448326.tar.gz`

1. Run

    `./liferay-ce-portal-7.2.1-ga2/tomcat-9.0.17/bin/startup.sh`

    > `INFO: Server startup in x milliseconds` indicates server startup completion.

1. Go to `http://localhost:8080/`. Follow the prompts to complete [basic configuration](./06-using-the-setup-wizard.md)!

    ![Follow the Setup Wizard Prompts to Log In](./getting-started-with-liferay-dxp/images/01.png)

1. Stop DXP

    `Ctrl + c`
    
    Rerun

    `./liferay-ce-portal-7.2.1-ga2/tomcat-9.0.17/bin/startup.sh`

The Liferay DXP home page appears at `http://localhost:8080/`. Sign in and get started!

![Liferay DXP is ready to explore!](./getting-started-with-liferay-dxp/images/02.png)

## Next Steps

Now you're ready to explore Liferay DXP! To learn more about what you can build with Liferay DXP see [Building Solutions on DXP](../../building-solutions-on-dxp/README.rst). To learn more about installing Liferay see the [Installation Overview](./02-installation-overview.md).
