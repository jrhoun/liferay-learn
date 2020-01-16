# Running Liferay DXP for the First Time

Once you've installed Liferay DXP (see the Installation Overview and Downloading Liferay DXP)  and [configured a new database](./04-connecting-a-database.md) for it, Liferay DXP is ready to run. Start Liferay DXP's application server (the server) using the startup script bundled with the application server. For example, here's the path to a Tomcat bundle startup script:

```bash
./liferay-dxp-version/tomcat-version/bin/startup.sh
```

> **Note:** By default, DXP writes log files to `[LIFERAY_HOME]/logs`.

On completing startup, DXP launches the Basic Configuration page (the [Setup Wizard](./05-using-the-setup-wizard.md)) in a web browser. If the page isn't launched, open a browser to the server's URL (for example, `http://localhost:8080`).

![On completing startup, DXP launches a web browser that displays the Basic Configuration page.](./running-liferay-dxp-for-the-first-time/images/01.png)

## Next Steps 

Congratulations! You've launched Liferay DXP. You're ready to configure DXP's basic settings [using the Setup Wizard](./05-using-the-setup-wizard.md).
