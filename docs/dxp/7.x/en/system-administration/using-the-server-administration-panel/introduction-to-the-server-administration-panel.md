# Introduction to the Server Administration Panel

Server Administration is a system-scoped administration panel holding a variety of low-level Liferay DXP configurations. In Server Administration you can manage and monitor system memory usage, low-level properties, some third-party integrations, document repository migration, logging, scripting, mail server configuration, and portal shutdown.

Access Server Administration by clicking *Control Panel* &rarr; *Configuration* &rarr; *Server Administration*.

![The Resources tab of Server Administration shows a graph of your server's memory usage.](./introduction-to-the-server-administration-panel/images/02.png)

Server Administration's functionality is segmented into tabs:

| Server Admin Tab   | Description                     | Documentation Link       |
| ------------------ | ------------------------------- | ------------------------ |
| Resources          | Monitor the system and perform management tasks (run the garbage collector, clear the database cache, etc.) | [Managing System Resources in Server Administration](./managing-system-resources-in-server-administration.md) |
| Log Levels         | View and set logging levels. Modify log levels for Liferay DXP classes and packages. Add custom objects to the logging configuration. | [Configuring Logging in Server Administration](./configuring-logging-in-server-administration.md) |
| Properties         | View System and Portal properties. System Properties shows the system properties for the JVM and Liferay DXP, and is used for debugging or checking the running configuration. Portal Properties shows the current portal property values. See the [portal properties reference documentation](https://docs.liferay.com/portal/7.3-latest/propertiesdoc/portal.properties.html) for more details. | [Portal Properties](./../../installation-and-upgrades/reference/portal-properties.md) |
| Data Migration     | Migrate documents from one repository to another. For example, you can migrate your documents to a new repository on a different disk or in a new format. |  [File Storage Migration](./../file-storage/file-store-migration.md) |
| Mail               | Instead of a [Portal Properties file](../../installation-and-upgrades/setting-up-liferay-dxp/configuring-mail/alternative-email-configuration-methods.md#configuring-the-built-in-mail-session-using-portal-properties) configure a mail server from this tab. These settings override any mail server settings in your `portal-ext.properties` file. | [Connecting to a Mail Server](../../installation-and-upgrades/setting-up-liferay-dxp/configuring-mail/connecting-to-a-mail-server.md) |
| External Services  | Configure external services for generating file previews for images, audio files, and video files. | [Configuring External Services in Server Administration](./configuring-external-services-in-server-administration.md) |
| Script             | Write Groovy scripts in a scripting console for executing migration or management code. | [Using the Script Engine](./../using-the-script-engine/using-the-script-engine.md) |
| Shutdown           | Schedule a shutdown (in _x_ minutes from now) that warns logged-in users of the impending shutdown. | [Configuring a Shutdown Event in Server Administration](./configuring-a-shutdown-event-in-server-administration.md) |

