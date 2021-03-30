# Staging Overview

You can use Liferay DXP's *Staging* tool to make changes to your Site behind the scenes in a *Staging environment* and then publish your changes to a local or remote *Live environment*, while the Live environment handles incoming User traffic.

As part of Staging configuration, determine whether to host your environments on the same server or separate servers connected by a network. You can also enable Page versioning and customize which Site content and application data is staged.

* [Configuration Options](#staging-configuration-options)
* [Understanding the Publishing Process](#understanding-the-publishing-process)

## Configuration Options

There are two options for configuring Staging on your Site: *Local Live Staging* and *Remote Live Staging*.

**Local Live Staging**: You can host both your Staging and Live environments on the same Liferay server. When enabled, Liferay DXP creates a local clone of your Site that serves as the Staging environment, while your original DXP instance becomes your Live environment.

**Remote Live Staging**: You can host your Staging and Live environments on separate Liferay servers. When enabled, the Site used to configure Staging becomes your Staging environment, while the configured remote server becomes your Live environment.

While both options use the same interface for managing and publishing staged Pages, applications, and content, they differ in their setup. Once you've chosen the configuration option that best suits your needs, see [Configuring Local Live Staging](./configuring-local-live-staging.md) or [Configuring Remote Live Staging](./configuring-remote-live-staging.md) for more information and setup instructions.

### Page Versioning

As part of Staging, you can enable the *Page versioning* feature. With this, you and your team can simultaneously develop and work in variations of both your Private and Public Pages. You can see the complete history of Page versions and revert Pages to an earlier version if needed. See [Page Versioning](./page-versioning.md) to learn how to create and manage variations and [Managing Staging Permissions](./managing-staging-permissions.md) to learn about managing permissions for each variation.

```note::
   Starting Liferay DXP 7.4, 7.3 Fix Pack 1, and 7.2 Fix Pack 11, you can use page versioning in Widget Pages and Content Pages. In previous Liferay DXP versions, you can create variations only in Widget Pages. To learn more about variations in these type of pages, see [Types of Variations](./page-versioning.md/#types-of-variations).
```

### Staged Data and Content Types

As part of Staging configuration, you can select which content groups and application data is staged. If staged, the selected data and content are managed by your Staging environment. Also, when an application or content group is selected, all contained entities (e.g., application folders) are staged as well. See [Managing Data and Content Types in Staging](./managing-data-and-content-types-in-staging.md) for more information.

## Understanding the Publishing Process

From a low level perspective, staging is an equivalence relation where entities are mirrored to a different location. From a high level perspective, the staging process is executed in three sequential phases: Export, Validation, and Import.

Understanding this process can improve efficiency and help you plan ahead to achieve a seamless publishing experience. See [Understanding the Publishing Process](./understanding-the-publishing-process.md) for more information.

## Additional Information

* [Understanding the Publishing Process](./understanding-the-publishing-process.md)
* [Configuring Local Live Staging](./configuring-local-live-staging.md)
* [Configuring Remote Live Staging](./configuring-remote-live-staging.md)
* [Staging UI Reference](./staging-ui-reference.md)
