# Cluster Link Overview

Enabling Cluster Link automatically activates distributed caching. The cache is distributed across multiple Liferay DXP nodes running concurrently. Cluster Link uses [Ehcache](http://www.ehcache.org) replication. The Ehcache global settings are in the [`portal.properties` file](https://docs.liferay.com/portal/7.2-latest/propertiesdoc/portal.properties.html#Ehcache).

By default Liferay does not copy cached entities between nodes. If an entity is deleted or changed, for example, Cluster Link sends a *remove* message to the other nodes to invalidate this entity in their local caches. Requesting that entity on another node results in a cache *miss*; the entity is then retrieved from the database and put into the local cache. Entities added to one node's local cache are not copied to local caches of the other nodes. An attempt to retrieve a new entity on a node which doesn't have that entity cached results in a cache *miss*. The miss triggers the node to retrieve the entity from the database and store it in its local cache.

![Figure 1: Liferay DXP's cache algorithm is extremely efficient.](./cluster-link-overview/images/01.png)

Clustering in DXP may be configured in different ways depending on your network and the location of your cluster nodes. The following topics concerning cluster link are covered in this article:

**Contents:**

* [Enabling Cluster Link](#enabling-cluster-link)
* [Configuring Cluster Link](#configuring-cluster-link)
* [Optimizing Cluster Cache Performance](#optimizing-cluster-cache-performance)
* [Conclusion](#conclusion)

## Enabling Cluster Link

To enable Cluster Link, add this [portal property](https://help.liferay.com/hc/en-us/articles/360028712292-Portal-Properties) to a `portal-ext.properties` file:

```properties
cluster.link.enabled=true
```

The [Cluster Link portal properties](https://docs.liferay.com/dxp/portal/7.2-latest/propertiesdoc/portal.properties.html#Cluster%20Link) provide a default configuration that you can override to fit your needs.

Many of the defaults use `localhost`, instead of a real address. In some configurations, however, `localhost` is bound to the internal loopback network (`127.0.0.1` or `::1`), rather than the host's real address. If you still need this configuration, you can make DXP auto detect the real address with this property:

```properties
cluster.link.autodetect.address=www.google.com:80
```

Set it to connect to some other host that's contactable by your server. By default, it points to Google, but this may not work if your server is behind a firewall. If you use each host's real address, you don't need to set the auto-detect address.

Cluster Link depends on [JGroups](http://www.jgroups.org) and provides an API for nodes to communicate. It can:

* Send messages to all nodes in a cluster
* Send messages to a specific node
* Invoke methods and retrieve values from all, some, or specific nodes
* Detect membership and notify when nodes join or leave

Cluster Link contains an enhanced algorithm that provides one-to-many type communication between the nodes. This is implemented by default with JGroups's UDP multicast, but unicast and TCP are also available.

## Configuring Cluster Link

When you enable Cluster Link, DXP's default clustering configuration is enabled. This configuration defines *IP multicast over UDP*. If you cannot use multicast for your own nodes (for example, because they are separated geographically or by a firewall), then you can instead configure a unicast implementation. See [Configuring Unicast Over TCP](./06-configuring-unicast-over-tcp.md) for more information.

DXP uses two groups of [channels from JGroups](http://www.jgroups.org/manual4/index.html#_channel) to implement multicast over UDP: a control group and a transport group. If you want to customize the [channel properties](https://docs.liferay.com/portal/7.2-latest/propertiesdoc/portal.properties.html#Cluster%20Link), you can do so by adding the following to `portal-ext.properties`:

```properties
cluster.link.channel.name.control=[your control channel name]
cluster.link.channel.properties.control=[your control channel properties]
cluster.link.channel.name.transport.0=[your transport channel name]
cluster.link.channel.properties.transport.0=[your transport channel properties]
```

Please see [JGroups's documentation](http://www.jgroups.org/manual4/index.html#protlist) for channel properties. The default configuration sets many properties whose settings are discussed there.

Multicast broadcasts to all devices on the network. Clustered environments on the same network communicate with each other by default. Messages and information (e.g., scheduled tasks) sent between them can lead to unintended consequences. Isolate such cluster environments by either separating them logically or physically on the network, or by configuring each cluster's `portal-ext.properties` to use different sets of [multicast group address and port values](https://docs.liferay.com/portal/7.2-latest/propertiesdoc/portal.properties.html#Multicast).

JGroups sets a bind address automatically, using `localhost` by default. If you want to set a manual address, you can set it in `portal-ext.properties`:

```properties
cluster.link.bind.addr["cluster-link-control"]=localhost
cluster.link.bind.addr["cluster-link-udp"]=localhost
```

Your network configuration may preclude the use of multicast over TCP, so below are some other ways you can get your cluster communicating. Note that these methods are provided by JGroups.

## Optimizing Cluster Cache Performance

It's recommended to test your system under a load that best simulates the kind of traffic your system must handle. For example, if you serve a lot of message board messages, your script should reflect that. If web content is the core of your Site, your script should reflect that too.

As a result of a load test, you may find that the default distributed cache settings aren't optimized for your Site. In this case, tweak the settings using a module. Follow instructions for [Overriding Cache](https://help.liferay.com/hc/en-us/articles/360035581471-Overriding-Cache).

You can install the module on each node and change the settings without taking down the cluster. Be aware that Ehcache doesn't allow for changes to cache settings while the cache is active. Therefore, reconfiguring a cache while the server is running flushes the cache.

## Conclusion

Once you've configured your cluster, you can start it. A log file message shows your cluster's name (e.g., `cluster=liferay-channel-control`):

```bash
-------------------------------------------------------------------
GMS: address=oz-52865, cluster=liferay-channel-control, physical address=192.168.1.10:50643
-------------------------------------------------------------------
```

Congratulations! Your cluster is using Cluster Link.

## Additional Information

* [Configuring Unicast over TCP](./06-configuring-unicast-over-tcp.md)
* [Introduction to Clustering Liferay DXP](./01-introduction-to-clustering-liferay-dxp.md)
