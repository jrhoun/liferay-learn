# Running Liferay DXP for the First Time

Once you've [installed Liferay DXP](./03-downloading-liferay-dxp.md#installing) and [configured a database](./04-connecting-a-database.md) for it, Liferay DXP is ready to run using the startup script bundled with the application server. 

Run the startup script. Tomcat bundle example:

```bash
./liferay-dxp-version/tomcat-version/bin/startup.sh
```

> **Note:** By default, DXP writes log files to `[LIFERAY_HOME]/logs`.


The [Setup Wizard](./06-using-the-setup-wizard.md) in a web browser at `http://localhost:8080`.

![On completing startup, DXP launches a web browser that displays the Basic Configuration page.](./running-liferay-dxp-for-the-first-time/images/01.png)

Congratulations! You've launched Liferay DXP. 

## Next Steps 

[Use the Setup Wizard](./06-using-the-setup-wizard.md) to configure DXP.
