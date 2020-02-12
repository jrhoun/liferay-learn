# Installing DXP on WebLogic

Installing Liferay DXP on WebLogic requires deploying the DXP WAR file, deploying DXP's dependencies, and configuring WebLogic Server for DXP.

It is **highly recommended** to install DXP to a WebLogic Managed server. Deploying to a Managed Server lets you start or shut down DXP more quickly and facilitates transitioning into a cluster configuration. This article therefore focuses on installing DXP to a Managed Server.

Before installing DXP, configure an Admin Server and a Managed Server following [WebLogic's documentation](http://www.oracle.com/technetwork/middleware/weblogic/documentation/index.html).

Liferay DXP requires a **Java JDK 8 or 11**. See [www.java.com](https://www.java.com/) to install a JDK.

```note::
   The [Liferay DXP Compatibility Matrix](https://web.liferay.com/documents/14/21598941/Liferay+DXP+7.2+Compatibility+Matrix/b6e0f064-db31-49b4-8317-a29d1d76abf7?) specifies supported databases and environments.
```

Download these files from the [Help Center](https://customer.liferay.com/downloads) (Subscribers) or from [Liferay Community Downloads](https://www.liferay.com/downloads-community):

* DXP WAR file
* Dependencies ZIP file
* OSGi Dependencies ZIP file

Here are the basic steps for installing DXP on WebLogic:

1. [Configuring WebLogic for DXP](#configuring-weblogic)
1. [Declaring the `Liferay Home` folder](#declaring-the-liferay-home-folder)
1. [Installing the dependencies](#installing-dxp-dependencies)
1. [Database Configuration](#database-configuration)
1. [Mail Configuration](#mail-configuration)
1. [Deploying the WAR](#deploying-dxp)

## Configuring WebLogic

### Configuring WebLogic's Node Manager

WebLogic's Node Manager starts and stops managed servers.

To avoid difficulties running DXP with the encryption requirement enabled in the Node Manager, it's recommended to disable the requirement by setting the following property in the `domains/your_domain_name/nodemanager/nodemanager.properties` file:

```properties
SecureListener=false
```

This disables the encryption (SSL) requirement for the Node Manager, allowing it to accept unencrypted connections. With the encryption requirement disabled, configure the machine in the Admin Server's console to accept unencrypted connections from the Node Manager:

1. Log in to the Admin Server and select *Environment* &rarr; *Machines* from the *Domain Structure* box on the left.
1. Click the corresponding machine in the table and then select the *Configuration* &rarr; *Node Manager* tab.
1. Select *Plain* from the selector menu in the *Type* field.
1. Click *Save*.
1. Restart the Admin Server for this change to take effect.

If you're running WebLogic on a UNIX system other than Solaris or Linux, use the Java Node Manager, instead of the native version of the Node Manager, by configuring these Node Manager properties in the `domains/your_domain_name/nodemanager/nodemanager.properties` file:

```properties
NativeVersionEnabled=false

StartScriptEnabled=true
```

See Oracle's [Configuring Java Node Manager](https://docs.oracle.com/middleware/1212/wls/NODEM/java_nodemgr.htm#NODEM173) documentation for details.

### Configuring WebLogic's JVM

Configure the JVM using variables and options in the WebLogic scripts and Managed Server.

1. Add the following variables to both your Admin Server startup script (`your-domain/startWebLogic.sh`) and Managed Server startup script (`your-domain/bin/startWebLogic.sh`)

    ```bash
    export DERBY_FLAG="false"
    export JAVA_OPTIONS="${JAVA_OPTIONS} -Dfile.encoding=UTF-8 -Duser.timezone=GMT -da:org.apache.lucene... -da:org.aspectj..."
    export MW_HOME="/your/weblogic/directory"
    export USER_MEM_ARGS="-Xmx2560m -Xms2560m"
    ```

    The `DERBY_FLAG` setting disables the Derby server built in to WebLogic, as DXP does not require this server. The remaining settings support DXP's memory requirements, UTF-8 requirement, Lucene usage, and Aspect Oriented Programming via AspectJ.

    ```important::
       For DXP to work properly, the application server JVM must use the `GMT` time zone and `UTF-8` file encoding.
    ```

    Also make sure to set `MW_HOME` to the directory containing the WebLogic server on the machine. For example:

    ```bash
    export MW_HOME="/Users/ray/Oracle/wls12210"
    ```

1. Make sure `your-domain/bin/SetDomainEnv.sh` uses these memory settings:

    ```bash
    WLS_MEM_ARGS_64BIT="-Xms2560m -Xmx2560m"
    export WLS_MEM_ARGS_64BIT

    WLS_MEM_ARGS_32BIT="-Xms2560m -Xmx2560m"
    export WLS_MEM_ARGS_32BIT
    ```

1. Set the Java file encoding to UTF-8 in `your-domain/bin/SetDomainEnv.sh` by appending `-Dfile.encoding=UTF-8` ahead of the other Java properties:

    ```bash
    JAVA_PROPERTIES="-Dfile.encoding=UTF-8 ${JAVA_PROPERTIES} ${CLUSTER_PROPERTIES}"
    ```

1. Ensure that the Node Manager sets DXP's memory requirements when starting the Managed Server. In the Admin Server's console UI, navigate to the Managed Server where DXP is to be deployed and select the *Server Start* tab. Enter the following parameters into the *Arguments* field:

    ```bash
    -Xmx2560m -Xms2560m -XX:MaxMetaspaceSize=512m
    ```

1. Click *Save*.

## Declaring the Liferay Home Folder

Before installing DXP, set your [*Liferay Home*](../../14-reference/01-liferay-home.md) folder location.

1. Create a file called [`portal-ext.properties`](../../14-reference/03-portal-properties.md). (It overrides [DXP properties](https://docs.liferay.com/dxp/portal/7.2-latest/propertiesdoc/portal.properties.html).) 

1. In the `portal-ext.properties` file, set the `liferay.home` property to your Liferay Home folder path. In WebLogic, the user domain's folder is generally Liferay Home, but any other folder on the machine can be used:

```properties
liferay.home=/full/path/to/your/liferay/home/folder
```

1. Package the `portal-ext.properties` in your DXP WAR file by expanding the DXP WAR file and copying the `portal-ext.properties` file into the `WEB-INF/classes` folder. 

1. Optionally, you can re-WAR the expanded DXP WAR. When you're ready to deploy DXP, you can deploy it as an expanded archive or WAR file. In both cases, DXP reads the property settings once it starts up.

```note::
   If you need to update `portal-ext.properties` after DXP deploys, it is in the user domain's `autodeploy/ROOT/WEB-INF/classes` folder. Note that the `autodeploy/ROOT` folder contains the DXP deployment.
```

## Installing DXP Dependencies

DXP depends on libraries (Dependencies ZIP) and OSGi modules (OSGi Dependencies ZIP).

1. Unzip the Dependencies ZIP file contents in the WebLogic domain's `lib` folder.
1. Unzip the OSGi Dependencies ZIP file\ contents in the `Liferay_Home/osgi` folder (create this folder if it doesn't exist).

DXP communicates with your database via JDBC. Add your database JDBC driver JAR file to the user domain's `lib` folder. Here are some common JDBC drivers:

* [`mariadb.jar`](https://downloads.mariadb.org/)
* [`mysql.jar`](http://dev.mysql.com/downloads/connector/j)
* [`postgres.jar`](https://jdbc.postgresql.org/download/postgresql-42.0.0.jar)

Note that although a Hypersonic database is bundled with DXP and is fine for testing purposes, **do not** use it for production DXP instances.

## Database Configuration

DXP contains a built-in Hypersonic database which is great for demonstration purposes but _should not be used in production_. Beyond demonstration purposes, we recommend using a full-featured, supported RDBMS. See [Configure a Database](../configuring-a-database.md) to set up your database. 

Liferay DXP can connect with your database using DXP's built-in data source (recommended) or using a data source you create on your app server. 

To configure DXP's built-in data source with your database when you run DXP for the first time, you can use the [Setup Wizard](../../../getting-started/using-the-setup-wizard.md). Or you can configure the data source in your `portal-ext.properties` file based on the [Database Template](../../14-reference/05-database-templates.md) for your database.

Otherwise, you can configure the data source in WebLogic.

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
1. Connect DXP to the JDBC data source: in the `portal-ext.properties` file (see above) in the Liferay Home directory, enter the following line:

    ```properties
    jdbc.default.jndi.name=jdbc/LiferayPool
    ```

## Mail Configuration

Liferay DXP can be [connected to a mail server](../../02-setting-up-liferay-dxp/connecting-to-a-mail-server.md) of your choice. Another option is WebLogic's mail session:

1. Start WebLogic and log in to the Admin Server's console.
1. Select *Services* &rarr; *Mail Sessions* from the *Domain Structure* box on the left hand side of the Admin Server's console UI.
1. Click *New* to begin creating a new mail session.
1. Name the session *LiferayMail* and give it the JNDI name `mail/MailSession`.
1. Enter the *Session Username*, *Session Password*, *Confirm Session Password*, and *JavaMail Properties* fields as necessary for the mail server. See the [WebLogic documentation](http://docs.oracle.com/middleware/1221/wls/FMWCH/pagehelp/Mailcreatemailsessiontitle.html) for more information on these fields.
1. Click *Next*.
1. Choose the Managed Server where DXP is to be installed on, and click *Finish*.
1. Shut down the Managed and Admin Servers.
1. With the Managed and Admin servers shut down, add the following property to the `portal-ext.properties` file in Liferay Home:

    ```properties
    mail.session.jndi.name=mail/MailSession
    ```

DXP references the WebLogic mail session via this property setting. If DXP has already been deployed, the `portal-ext.properties` file can be found in the domain's `autodeploy/ROOT/WEB-INF/classes` folder.

The changes take effect upon restarting the Managed and Admin servers.

## Deploying DXP on a Managed Server

Follow these steps to deploy DXP:

1. Verify that the designated Managed Server where DXP is to be deployed on is shut down.
1. In the Admin Server's console UI, select *Deployments* from the *Domain Structure* box on the left hand side.
1. Click *Install* to start a new deployment.
1. Select the DXP WAR file or its expanded contents on the machine. Alternatively, upload the WAR file by clicking the *Upload your file(s)* link. Click *Next*.
1. Select *Install this deployment as an application* and click *Next*.
1. Select the designated Managed Server where DXP is to be deployed and click *Next*.
1. If the default name is appropriate for the installation, keep it. Otherwise, enter a different name and click *Next*.
1. Click *Finish*.
1. After the deployment finishes, click *Save* if the configuration is correct.
1. Start the Managed Server where DXP is deployed on. DXP precompiles all the JSPs and then launches.

If you have a Liferay DXP Enterprise subscription, DXP requests your activation key. See [Activating Liferay DXP](../../02-setting-up-liferay-dxp/activating-liferay-dxp.md).

Congratulations! You're running DXP on WebLogic.

```note::
     Adjust the application server's logging level or log filters to avoid excessive benign log messages such as the ones below involving `PhaseOptimizer`.
```

```
 May 02, 2018 9:12:27 PM com.google.javascript.jscomp.PhaseOptimizer$NamedPass process
     WARNING: Skipping pass gatherExternProperties
May 02, 2018 9:12:27 PM com.google.javascript.jscomp.PhaseOptimizer$NamedPass process
     WARNING: Skipping pass checkControlFlow
May 02, 2018 9:12:27 PM com.google.javascript.jscomp.PhaseOptimizer$NamedPass process
     INFO: pass supports: [ES3 keywords as identifiers, getters, reserved words as properties, setters, string continuation, trailing comma, array pattern rest, arrow function, binary literal, block-scoped function declaration, class, computed property, const declaration, default parameter, destructuring, extended object literal, for-of loop, generator, let declaration, member declaration, new.target, octal literal, RegExp flag 'u', RegExp flag 'y', rest parameter, spread expression, super, template literal, modules, exponent operator (**), async function, trailing comma in param list]
     current AST contains: [ES3 keywords as identifiers, getters, reserved words as properties, setters, string continuation, trailing comma, array pattern rest, arrow function, binary literal, block-scoped function declaration, class, computed property, const declaration, default parameter, destructuring, extended object literal, for-of loop, generator, let declaration, member declaration, new.target, octal literal, RegExp flag 'u', RegExp flag 'y', rest parameter, spread expression, super, template literal, exponent operator (**), async function, trailing comma in param list, object literals with spread, object pattern rest]
```

## Next Steps

You can [sign in as your administrator user](../../../getting-started/introduction-to-the-admin-account.md) and start [building a solution on DXP](../../../building-solutions-on-dxp/README.md). Or you can explore [additional Liferay DXP setup](../../02-setting-up-liferay-dxp/setting-up-liferay-dxp.md) topics:

* [Setting up Marketplace](../../02-setting-up-liferay-dxp/setting-up-marketplace.md)
* [Trial Plugin Installation](../../02-setting-up-liferay-dxp/trial-plugin-installation.md)
* Installing and Configuring a Search Engine
* [Securing Liferay DXP](../../05-securing-liferay/01-securing-liferay.md)
* [Introduction to Clustering Liferay DXP](../../02-setting-up-liferay-dxp/configuring-clustering-for-high-availability/01-introduction-to-clustering-liferay-dxp.md)
