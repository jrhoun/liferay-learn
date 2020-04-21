# Example: Creating a DXP Cluster 

An easy way to learn DXP clustering is to set up a cluster environment on a single machine using Docker containers. Here you'll prepare each required server and each DXP app server node in their own containers. The containers will refer to each other by container name over a Docker bridge network. This is a fast way to set up a DXP cluster development environment.

Here are the server's you'll create:

| Server type | Implementation | Server Name |
| :---------- | :------- | :---------- |
| Database | MariaDB  | `some-mariadb` |
| Search Engine | Elasticsearch | `elasticsearch` |
| File Store | DBStore | `some-mariadb` |
| App Server | Tomcat | `dxp-1` |
| App Server | Tomcat | `dxp-2` |

Here are the steps:

1. Configure a network for the containers (Optional; it facilitates this example)
1. Prepare a database server
1. Prepare a search engine server
1. Prepare a File Store
1. Configure DXP servers

```note::
   DXP cluster environments can also be set up using on-premises DXP Tomcat bundles, using DXP installed to other app servers on-premises, or using any combination of Docker containers and DXP installations.
```

## Configure a Network for the Containers

Since the server containers in this example run on the same machine, a [Docker bridge network](TODO) enables containers to refer to each other by container name, rather than IP address. Outside of this kind of environment, you would use IP addresses.

Create an arbitrarily named Docker bridge network for the containers to use on your host machine.

```bash
docker network create --driver=bridge my-bridge
```

A bridged network called `my-bridge` is available.

## Prepare a Database Server

A DXP cluster requires a data source that's accessible to all of the app server nodes. The data source can be a JNDI data source, a database server, or a database server cluster. See the [compatibility matrix](TODO) for the database servers your DXP version supports.

<!-- TODO how to look up an old version's matrix? -->

Create a database server container based on a MariaDB Docker image:

1. Create a MariaDB database server container on the Docker bridge network you created. 

    ```bash
    docker pull mariadb:10.2
    docker run --name some-mariadb --network=my-bridge -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mariadb:10.2
    ```

    The `pull` command downloads the MariaDB version 10.2 Docker image. The `run` command creates a MariaDB server Docker container called `some-mariadb` on the `my-bridge` Docker network. The database server's `root` user password is `my-secret-pw`. See the [MariaDB Docker Hub page](TODO) for more information.

1. In a shell on the container, [create a database](TODO/installation-and-upgrades/reference/database-configurations.html) for DXP.

    ```bash
    docker exec -it some-mariadb bash

    mysql -uroot -pmy-secret-pw

    MariaDB [(none)]> create database dxp_db character set utf8;
    MariaDB [(none)]> quit 
    exit
    ```

Your database server is running and ready for DXP.

## Prepare a Search Engine Server

A DXP cluster requires a search engine that's accessible to all of the app server nodes. You can optionally create a search engine server cluster. See [Configuring a Search Engine in a Cluster](TODO) for more information.

Create a search engine server container based on an Elasticsearch Docker image:

1. Download the Elasticsearch Docker image that's compatible with your DXP version.

    ```bash
    docker pull elasticsearch:6.8.7
    ```

1.  Start an Elasticsearch server container, mounting the container's data folder to a host machine folder.

    ```bash
    mkdir -p ~/elasticsearch/es_data_volume

    docker run -it -p 9200:9200 -p 9300:9300  -e cluster.name=LiferayElasticsearchCluster -e ES_JAVA_OPTS="-Xms512m -Xmx512m" --network my-bridge --name elasticsearch -v ~/elasticsearch/es_data_volume:/usr/share/elasticsearch/data elasticsearch:6.8.7
    ```
    
    The first command creates a local folder to hold search indexes from the container. The `run` command creates an Elasticsearch Docker container that publishes on ports `9200` and `9300`, and has an Elasticsearch cluster called `LiferayElasticsearchCluster`. The command allocates `512m` memory to the server. The `-v ...` option maps the container's data folder to the host machine folder. 

1. In a shell on the container, install the required Elasticsearch plugins.

    ```bash
    docker exec -it elasticsearch bash 

    cd /usr/share/elasticsearch

    ./bin/elasticsearch-plugin install analysis-icu

    ./bin/elasticsearch-plugin install analysis-kuromoji

    ./bin/elasticsearch-plugin install analysis-smartcn

    ./bin/elasticsearch-plugin install analysis-stempel

    exit
    ```

Your search engine server is running and ready to store and retrieve search indexes for DXP.

## Prepare a Remote File Store 

A DXP cluster can use any File Store that's accessible to all of the app server nodes. For convenience, this example uses a [DBStore File Store](TODO) configured on the DXP database. It's configured on the app server nodes (described next). See [File Store](TODO) for other file store types.

## Configure the DXP Server Cluster

Each DXP server cluster node must be configured with the following things:

| Item | Configuration Method | More Information |
| :--- | :---------- | :--------------- |
| Data source connection | `portal-ext.properties` file | See [Database Templates](TODO) |
| Search engine connection | System configuration (OSGi config) file | See [System Configuration Files](TODO) |
| File Store connection | `portal-ext.properties` file and in some cases a System configuration file | See [Configuring a File Store](TODO) |
| Cluster Link | `portal-ext.properties` file | See [Configuring Cluster Link](TODO) |

All except the search engine connection are configured using portal properties. The portal properties can be specified using Docker environment variables or a `portal-ext.properties` file. Since there are several properties, we'll use a properties file in this example. 

Keep your server node configurations separate, by creating a folder for each node:

```bash
mkdir dxp-1 dxp-2
```

### Configure DXP with the Search Engine 

1. Create a search engine configuration file:

    ```bash
    mkdir -p dxp-1/files/osgi/configs
    touch dxp-1/files/osgi/configs/com.liferay.portal.search.elasticsearch6.configuration.ElasticsearchConfiguration.config
    ```

1. Add this content to the `.config` file:

    ```properties
    operationMode="REMOTE"
    transportAddresses="elasticsearch:9300"
    clusterName="LiferayElasticsearchCluster"
    ```

1. Copy the configuration to your other node(s).

    ```bash
    mkdir -p dxp-2/files/osgi/configs
    cp dxp-1/files/osgi/configs/com.liferay.portal.search.elasticsearch6.configuration.ElasticsearchConfiguration.config dxp-2/files/osgi/configs/
    ```

### Configure the Server Connections and Enable Cluster Link

Use portal properties to configure the DXP servers with the database server and file store, and to enable Cluster Link.

1. Create a `portal-ext.properties` file for each node:

    ```bash
    touch dxp-1/files/portal-ext.properties
    touch dxp-2/files/portal-ext.properties
    ```

1. Add this to the `dxp-1/files/portal-ext.properties` file:

    ```properties
    jdbc.default.jndi.name=

    jdbc.default.driverClassName=org.mariadb.jdbc.Driver
    jdbc.default.url=jdbc:mariadb://some-mariadb:3306/dxp_db?useUnicode=true&characterEncoding=UTF-8&useFastDateParsing=false
    jdbc.default.username=root
    jdbc.default.password=my-secret-pw

    dl.store.impl=com.liferay.portal.store.db.DBStore

    virtual.hosts.default.site.name=

    com.liferay.portal.servlet.filters.strip.StripFilter=true

    cluster.link.enabled=true

    cluster.link.autodetect.address=some-mariadb:3306

    cluster.link.channel.logic.name.control=control-channel-logic-name-1
    cluster.link.channel.logic.name.transport.0=transport-channel-logic-name-1

    module.framework.properties.osgi.console=11312

    web.server.http.port=8080

    web.server.display.node=true
    ```

1. Add this to the `dxp-2/files/portal-ext.properties` file:

    ```properties
    jdbc.default.jndi.name=

    jdbc.default.driverClassName=org.mariadb.jdbc.Driver
    jdbc.default.url=jdbc:mariadb://some-mariadb:3306/dxp_db?useUnicode=true&characterEncoding=UTF-8&useFastDateParsing=false
    jdbc.default.username=root
    jdbc.default.password=my-secret-pw

    dl.store.impl=com.liferay.portal.store.db.DBStore

    virtual.hosts.default.site.name=

    com.liferay.portal.servlet.filters.strip.StripFilter=true

    cluster.link.enabled=true

    cluster.link.autodetect.address=some-mariadb:3306

    cluster.link.channel.logic.name.control=control-channel-logic-name-2
    cluster.link.channel.logic.name.transport.0=transport-channel-logic-name-2

    module.framework.properties.osgi.console=11313

    web.server.http.port=9080

    web.server.display.node=true
    ```


Examine the unique values each node uses for the ports and cluster logic names.

| Property | dxp-1 | dxp-2 |
| :------- | :---- | :---- |
| cluster.link.channel.logic.name.control | control-channel-logic-name-1 | control-channel-logic-name-2 |
| cluster.link.channel.logic.name.transport.0 | transport-channel-logic-name-1 | transport-channel-logic-name-2 |
| module.framework.properties.osgi.console | 11312 | 11313 |
| web.server.http.port | 8080 | 9080 |

### Start Both Nodes 

Start `dxp-1`:

```bash
docker run -it --name dxp-1 --network my-bridge -p 8080:8080 -v ${PWD}/dxp-1/files:/mnt/liferay liferay/portal:7.3.1-ga2
```

Start `dxp-2`:

```bash
docker run -it --name dxp-2 --network my-bridge -p 9080:8080 -v ${PWD}/dxp-2/files:/mnt/liferay liferay/portal:7.3.1-ga2
```

As the `dxp-2` node starts, the `dxp-1` node notices that it's joined the cluster view.

```
2020-04-15 19:25:53.926 INFO  [jgroups-32,liferay-channel-control,control-channel-logic-name-1][JGroupsReceiver:93] Accepte
d view [control-channel-logic-name-1|1] (2) [control-channel-logic-name-1, control-channel-logic-name-2]
2020-04-15 19:25:54.275 INFO  [jgroups-34,liferay-channel-transport-0,transport-channel-logic-name-1][JGroupsReceiver:93] A
ccepted view [transport-channel-logic-name-1|1] (2) [transport-channel-logic-name-1, transport-channel-logic-name-2]
```

```
2020-04-15 19:28:11.500 INFO  [default-27][ClusterExecutorImpl:544] Updated cluster node {bindInetAddress=/172.18.0.4, clus
terNodeId=67d85000-28f8-c3fd-c3c1-e6277e3e3294, portalInetSocketAddress=/127.0.0.1:8080, portalProtocol=http}
```

TODO conclusion
