# Using the DBStore

You can store Documents and Media files in Liferay DXP 7.2 database using DBStore. DBStore's maximum file (stored as a blob) size is 1 gigabyte. To store files larger than that, use [Simple File System Store](./using-the-simple-file-system-store.md) or [Advanced File System Store]().

Here are the DBStore configuration steps:

1. Set the following property in a [`portal-ext.properties`](https://help.liferay.com/hc/articles/360028712292-Portal-Properties) file in your [Liferay Home](https://help.liferay.com/hc/articles/360028712272-Liferay-Home) folder:

    ```
    dl.store.impl=com.liferay.portal.store.db.DBStore
    ```

1. Restart DXP 7.2.

Documents and Media now uses DXP 7.2's database via DBStore.

## Additional Information

* [Document Repository Reference](./document-repository-reference.md)
