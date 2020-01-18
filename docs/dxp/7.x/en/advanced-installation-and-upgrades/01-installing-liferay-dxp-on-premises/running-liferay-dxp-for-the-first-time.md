# Running Liferay DXP for the First Time

Once you've [installed Liferay DXP](./installing-liferay-dxp-on-premises.md#installing) and [configured a database](configuring-a-database.md) for it, Liferay DXP is ready to run using the startup script bundled with the application server.

Run the startup script. Tomcat bundle example:

```bash
./liferay-dxp-version/tomcat-version/bin/startup.sh
```

> **Note:** By default, DXP writes log files to `[LIFERAY_HOME]/logs`.

The [Setup Wizard](./using-the-setup-wizard.md) appears in your web browser at `http://localhost:8080`.

![On completing startup, DXP launches a web browser that displays the Basic Configuration page.](./running-liferay-dxp-for-the-first-time/images/01.png)

You've launched Liferay DXP. Complete basic configuration next [using the Setup Wizard](./using-the-setup-wizard.md).

> **Note:** You'll want to continue with using the Setup Wizard. But whenever you want to stop your server, you can use the shutdown script bundled with your application server. Tomcat bundle example: `./liferay-dxp-version/tomcat-version/bin/shutdown.sh`

## Next Steps 

[Use the Setup Wizard](./using-the-setup-wizard.md).
