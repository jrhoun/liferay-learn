# Installing DXP 7.2 on WebLogic 12c R2

Although DXP 7.2 can be installed on a WebLogic Admin Server, _this is not recommended_. It's a best practice to install web apps, including DXP 7.2, in a WebLogic Managed server. Deploying to a Managed Server lets administrators to start or shut down DXP 7.2 more quickly and facilitates transitioning into a cluster configuration. This article therefore focuses on installing DXP 7.2 in a Managed Server.

Before getting started, create the Admin and Managed Servers. See [WebLogic's documentation](http://www.oracle.com/technetwork/middleware/weblogic/documentation/index.html) for instructions on setting up and configuring Admin and Managed Servers.

See [Optimizing the Application Server]() and [Preparing the Database](./preparing-the-database.md).

Now, [download the DXP 7.2 WAR and Dependency JARs](/docs/7-2/deploy/-/knowledge_base/d/obtaining-product#downloading-the-liferay-war-and-dependency-jars):

* DXP 7.2 WAR file
* Dependencies ZIP file
* OSGi Dependencies ZIP file

**Checkpoint:**

The following jars should be present within the `liferay-dxp-dependencies-[version].zip`:

* `com.liferay.petra.concurrent.jar`
* `com.liferay.petra.executor.jar`
* `com.liferay.petra.function.jar`
* `com.liferay.petra.io.jar`
* `com.liferay.petra.lang.jar`
* `com.liferay.petra.memory.jar`
* `com.liferay.petra.nio.jar`
* `com.liferay.petra.process.jar`
* `com.liferay.petra.reflect.jar`
* `com.liferay.petra.string.jar`
* `com.liferay.registry.api.jar`
* `hsql.jar`
* `portal-kernel.jar`
* `portlet.jar`

The following folders should be present within the `/liferay/osgi` folder:

* `Configs`
* `Core`
* `Marketplace`
* `War`

## Configuring WebLogic's Node Manager

WebLogic requires a Node Manager to start and stop managed servers. Before installing DXP 7.2, configure the Node Manager included with the WebLogic installation. This is set in the `domains/your_domain_name/nodemanager/nodemanager.properties` file. Open this file and set the `SecureListener` property to `false`:

```properties
SecureListener=false
```

This setting disables the encryption (SSL) requirement for the Node Manager, allowing it to accept unencrypted connections. Although it's possible to run DXP 7.2 with this property set to `true`, there may be some difficulties doing so. And because `SecureListener` set to `true`, administrators then must configure the machine in the Admin Server's console to accept unencrypted connections from the Node Manager. To do this:

1. Log in to the Admin Server and select *Environment* &rarr; *Machines* from the *Domain Structure* box on the left.
1. Click the corresponding machine in the table and then select the *Configuration* &rarr; *Node Manager* tab. 
1. Select *Plain* from the selector menu in the *Type* field.
1. Click *Save*.
1. Restart the Admin Server for this change to take effect.

If running WebLogic on Mac or Linux, administrators may also need to set the `NativeVersionEnabled` property to `false`:

```properties
NativeVersionEnabled=false
```

This tells the Node Manager to start in non-native mode. This is required for the platforms where WebLogic does not provide native Node Manager libraries.

## Configuring WebLogic

Set the following variables in the two respective WebLogic startup scripts. These variables and scripts are as follows. Be sure to use `set` instead of `export` if you're on Windows.

1. `your-domain/startWebLogic.[cmd|sh]`: This is the Admin Server's startup
    script.

1. `your-domain/bin/startWebLogic.[cmd|sh]`: This is the startup script for
    Managed Servers.

    Add the following variables to both `startWebLogic.[cmd|sh]` scripts:

    ```bash
    export DERBY_FLAG="false"
    export JAVA_OPTIONS="${JAVA_OPTIONS} -Dfile.encoding=UTF-8 -Duser.timezone=GMT -da:org.apache.lucene... -da:org.aspectj..."
    export MW_HOME="/your/weblogic/directory"
    export USER_MEM_ARGS="-Xmx2560m -Xms2560m"
    ```

    | **Important:** For DXP 7.2 to work properly, the application server JVM must use the `GMT` time zone and `UTF-8` file encoding.

    The `DERBY_FLAG` setting disables the Derby server built in to WebLogic, as DXP 7.2 does not require this server. The remaining settings support DXP 7.2's  memory requirements, UTF-8 requirement, Lucene usage, and Aspect Oriented Programming via AspectJ. Also make sure to set `MW_HOME` to the directory containing the WebLogic server on the machine. For example:

    ```bash
    export MW_HOME="/Users/ray/Oracle/wls12210"
    ```

1. Some of the settings are also found in the `your-domain/bin/SetDomainEnv.[cmd|sh]` . Add the following variables (Windows):

    ```bash
    set WLS_MEM_ARGS_64BIT=-Xms2560m -Xmx2560m
    set WLS_MEM_ARGS_32BIT=-Xms2560m -Xmx2560m
    ```

    or on Mac or Linux:

    ```bash
    WLS_MEM_ARGS_64BIT="-Xms2560m -Xmx2560m"
    export WLS_MEM_ARGS_64BIT

    WLS_MEM_ARGS_32BIT="-Xms2560m -Xmx2560m"
    export WLS_MEM_ARGS_32BIT
    ```

1. Set the Java file encoding to UTF-8 in `your-domain/bin/SetDomainEnv.[cmd|sh]` by appending `-Dfile.encoding=UTF-8` ahead of the other Java properties:  

    ```bash
    JAVA_PROPERTIES="-Dfile.encoding=UTF-8 ${JAVA_PROPERTIES} ${CLUSTER_PROPERTIES}"
    ```

1. Ensure that the Node Manager sets DXP 7.2's memory requirements when starting the Managed Server. In the Admin Server's console UI, navigate to the Managed Server where DXP 7.2 is to be deployed and select the *Server Start* tab. Enter the following parameters into the *Arguments* field:

    ```bash
    -Xmx2560m -Xms2560m -XX:MaxMetaspaceSize=512m
    ```

1. Click *Save* when finished.

## Setting DXP 7.2 Properties

Before installing DXP 7.2, administrator must set the [*Liferay Home*]https://help.liferay.com/hc/articles/360028712272-Liferay-Home) folder's location via the `liferay.home` property in a [`portal-ext.properties`](https://help.liferay.com/hc/articles/360028712292-Portal-Properties) file. (Use this file to override [other DXP 7.2 properties](@platform-ref@/7.2-latest/propertiesdoc/portal.properties.html) as needed.)

> 1. Designate a folder that serves as Liferay Home. In WebLogic, the user domain's folder is generally Liferay Home, but administrators can choose any other folder on the machine.
> 1. Create the `portal-ext.properties` file and add the `liferay.home` property:

```properties
liferay.home=/full/path/to/your/liferay/home/folder
```

Remember to change this file path to the location on your machine that serving as Liferay Home.

Put the updated `portal-ext.properties` inside the DXP 7.2 WAR file. Expand the DXP 7.2 WAR file and place `portal-ext.properties` in the `WEB-INF/classes` folder. Later, administrators will deploy the expanded archive to WebLogic. Alternatively, administrators can re-WAR the expanded archive for later deployment. In either case, DXP 7.2 reads the property settings once it starts up.

If administrators need to make any changes to `portal-ext.properties` after DXP 7.2 deploys, the file is found in the user domain's `autodeploy/ROOT/WEB-INF/classes` folder. Note that the `autodeploy/ROOT` folder contains the DXP 7.2 deployment.

## Installing DXP 7.2 Dependencies

1. Unzip the Dependencies ZIP file and place its contents in the WebLogic domain's `lib` folder.
1. Unzip the OSGi Dependencies ZIP file and place its contents in the `Liferay_Home/osgi` folder (create this folder if it doesn't exist).
1. Add the database's driver JAR file to the user domain's `lib` folder. Note that although Hypersonic is fine for testing purposes, **do not** use it for production DXP 7.2 instances.

**Checkpoint:**

The domain `lib` folder has these jars:

* `com.liferay.petra.concurrent.jar`
* `com.liferay.petra.executor.jar`
* `com.liferay.petra.function.jar`
* `com.liferay.petra.io.jar`
* `com.liferay.petra.lang.jar`
* `com.liferay.petra.memory.jar`
* `com.liferay.petra.nio.jar`
* `com.liferay.petra.process.jar`
* `com.liferay.petra.reflect.jar`
* `com.liferay.petra.string.jar`
* `com.liferay.registry.api.jar`
* `hsql.jar`
* `portal-kernel.jar`
* `portlet.jar`

A JDBC driver for the database has been added to the user domain's `lib` folder. Here are some common JDBC drivers:

* [`mariadb.jar`](https://downloads.mariadb.org/)
* [`mysql.jar`](http://dev.mysql.com/downloads/connector/j)
* [`postgres.jar`](https://jdbc.postgresql.org/download/postgresql-42.0.0.jar)

The `[Liferay Home]/osgi` folder has these subfolders:

* `Configs`
* `Core`
* `Marketplace`
* `War`

## Database Configuration

Use the following procedure if using WebLogic to manage the [database](./preparing-the-database.md) for DXP 7.2. Otherwise skip this section if using DXP 7.2's built-in Hypersonic database.

1. Log in to the AdminServer console.
1. In the *Domain Structure* tree, find the domain and navigate to *Services* &rarr; *JDBC* &rarr; *Data Sources*.
1. To create a new data source, click *New*. 
1. Enter the *Name* field with `Liferay Data Source` and the *JNDI Name* field with `jdbc/LiferayPool`.
1. Select the database type and driver. For example, MySQL is *MySQL's Driver (Type 4) Versions:using com.mysql.jdbc.Driver*.
1. Click *Next* to continue.
1. Accept the default settings on this page and click *Next* to move on.
1. Fill in the database information for the MySQL database.
1. If using MySQL, add the text `?useUnicode=true&characterEncoding=UTF-8&\useFastDateParsing=false` to the URL line and test the connection. If it works, click *Next*.
1. Select the target for the data source and click *Finish*.
1. Connect DXP 7.2 to the JDBC data source: in the `portal-ext.properties` file (see above) in the Liferay Home directory, enter the following line:

    ```propreties
    jdbc.default.jndi.name=jdbc/LiferayPool
    ```

Alternatively, administrators can make the above configuration strictly via properties in the `portal-ext.properties` file. To do so, place the following properties and values in the file. Be sure to change the `your*` values with the values appropriate for the database's configuration (if using MySQL): 

```propreties
jdbc.default.driverClassName=com.mysql.jdbc.Driver
jdbc.default.url=jdbc:mysql://your.db.ip.address/yourdbname?useUnicode?useUnicode=true&characterEncoding=UTF-8&useFastDateParsing=false
jdbc.default.username=yourdbuser
jdbc.default.password=yourdbpassword
```

## Mail Configuration

If using WebLogic to manage the [mail session](https://help.liferay.com/hc/articles/360029031591-Configuring-Mail), use the following procedure. Otherwise, skip this section if using Liferay's built-in mail session (recommended).

1. Start WebLogic and log in to the Admin Server's console.
1. Select *Services* &rarr; *Mail Sessions* from the *Domain Structure* box on the left hand side of the Admin Server's console UI.
1. Click *New* to begin creating a new mail session.
1. Name the session *LiferayMail* and give it the JNDI name `mail/MailSession`.
1. Enter the *Session Username*, *Session Password*, *Confirm Session Password*, and *JavaMail Properties* fields as necessary for the mail server. See the [WebLogic documentation](http://docs.oracle.com/middleware/1221/wls/FMWCH/pagehelp/Mailcreatemailsessiontitle.html) for more information on these fields.
1. Click *Next*.
1. Choose the Managed Server where DXP 7.2 is to be installed on, and click *Finish*. 
1. Shut down the Managed and Admin Servers.
1. With the Managed and Admin servers shut down, add the following property to the `portal-ext.properties` file in Liferay Home:

    ```propreties
    mail.session.jndi.name=mail/MailSession
    ```

DXP 7.2 references the WebLogic mail session via this property setting. If DXP 7.2 has already been deployed, the `portal-ext.properties` file can be found in the domain's `autodeploy/ROOT/WEB-INF/classes` folder.

The changes take effect upon restarting the Managed and Admin servers.

## Deploying DXP 7.2

As mentioned earlier, although DXP 7.2 can be deployed to a WebLogic Admin Server, administrators should instead deploy it to a WebLogic Managed Server. Dedicating the Admin Server to managing other servers that run the apps is a best practice.

Follow these steps to deploy DXP 7.2 to a Managed Server:

1. Verify that the designated Managed Server where DXP 7.2 is to be deployed on is shut down.
1. In the Admin Server's console UI, select *Deployments* from the *Domain Structure* box on the left hand side. 
1. Click *Install* to start a new deployment.
1. Select the DXP 7.2 WAR file or its expanded contents on the machine. Alternatively, administrators can upload the WAR file by clicking the *Upload your file(s)* link. Click *Next*.
1. Select *Install this deployment as an application* and click *Next*.
1. Select the designated Managed Server where DXP 7.2 is to be deployed and click *Next*.
1. If the default name is appropriate for the installation, keep it. Otherwise, enter a different name and click *Next*.
1. Click *Finish*.
1. After the deployment finishes, click *Save* if the configuration is correct.
1. Start the Managed Server where DXP 7.2 is deployed on. DXP 7.2 precompiles all the JSPs and then launches.

| After deploying DXP 7.2, there may be excessive warnings and log messages, such as the ones below, involving `PhaseOptimizer`. These are benign and can be ignored. Adjust the application server's logging level or log filters to avoid excessive benign log messages.

```log
     May 02, 2018 9:12:27 PM com.google.javascript.jscomp.PhaseOptimizer$NamedPass process
     WARNING: Skipping pass gatherExternProperties
     May 02, 2018 9:12:27 PM com.google.javascript.jscomp.PhaseOptimizer$NamedPass process
     WARNING: Skipping pass checkControlFlow
    May 02, 2018 9:12:27 PM com.google.javascript.jscomp.PhaseOptimizer$NamedPass process
     INFO: pass supports: [ES3 keywords as identifiers, getters, reserved words as properties, setters, string continuation, trailing comma, array pattern rest, arrow function, binary literal, block-scoped function declaration, class, computed property, const declaration, default parameter, destructuring, extended object literal, for-of loop, generator, let declaration, member declaration, new.target, octal literal, RegExp flag 'u', RegExp flag 'y', rest parameter, spread expression, super, template literal, modules, exponent operator (**), async function, trailing comma in param list]
     current AST contains: [ES3 keywords as identifiers, getters, reserved words as properties, setters, string continuation, trailing comma, array pattern rest, arrow function, binary literal, block-scoped function declaration, class, computed property, const declaration, default parameter, destructuring, extended object literal, for-of loop, generator, let declaration, member declaration, new.target, octal literal, RegExp flag 'u', RegExp flag 'y', rest parameter, spread expression, super, template literal, exponent operator (**), async function, trailing comma in param list, object literals with spread, object pattern rest]
```
