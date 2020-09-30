# Warehouse Reference Guide

Warehouses represent physical locations where product inventory is managed and shipped for order fulfillment. Product inventory quantities can be managed per warehouse. Available inventory is then calculated by Liferay Commerce to determine the total available inventory for sale across warehouses. Channels must have a warehouse associated with it in order to source product inventory. Multiple warehouses can be created and associated with a given channel.

To manage your warehouses, navigate to the _Global Applications_ → _Commerce_ → _Settings_. Click the _Warehouses_ tab.

```note::
   Warehouse settings are located in the _Control Panel_ if using Commerce 2.0 or 2.1.
```

## Warehouse Name

![Adding a Warehouse](./warehouse-reference-guide/images/01.png)

| Field | Description |
| --- | --- |
| Name | Name of the Warehouse |
| Description | Additional Information |
| Active | Toggle to designate warehouse as active |

## Channels

![Selecting a Channel](./warehouse-reference-guide/images/02.png)

| Field | Description |
| --- | --- |
| Channels | List of checkboxes for all channels this warehouse serves |

## Address Fields

![Adding the Warehouse's Address](./warehouse-reference-guide/images/03.png)

| Field | Description |
| --- | --- |
| Street 1 | Address's first line |
| Street 2 | Address's second line |
| Street 3 | Address's third line |
| Country | Dropdown menu to select a country |
| Region | Dropdown menu to select the state or province |
| Postal Code | Field to enter the postal code |
| City | City where the warehouse is located |

## Geolocation

![Setting the warehouse's geolocation](./warehouse-reference-guide/images/04.png)

| Field | Description |
| --- | --- |
| Latitude | Warehouse's Latitude |
| Longitude | Warehouse's Longitude |

A warehouse's geolocation is used to calculate shipping costs based on distance. See [Using the Variable Rate Shipping Method](../../store-administration/configuring-shipping-methods/using-the-variable-rate-shipping-method.md) for more information.

## Additional Information

* [Introduction to Shipments](../../orders-and-fulfillment/shipments/introduction-to-shipments.md)
* [Adding a New Warehouse](./adding-a-new-warehouse.md)
* [Setting Inventory by Warehouse](./setting-inventory-by-warehouse.md)
