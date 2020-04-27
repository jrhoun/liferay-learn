# Configuring The Commerce Notification Queue

When an event triggers an notification (for example, an order is placed), the notification is placed temporarily in the _Notification Queue_ tab. By default, the Liferay Commerce instance checks for unsent any unsent notification every 15 minutes and deletes any unsent notifications after 43200 minutes (30 days).

To change the intervals for when Liferay Commerce checks for unsent notifications and the Delete Interval:

1. Navigate to the _Control Panel_ → _Configuration_ → _System Settings_.
1. Click _Orders_ then the _Commerce Notification Queue_. The default values are listed in minutes. Change the values for the Check Interval and the Delete Interval if necessary.

    ![Changing Intervals](./configuring-the-commerce-notification-queue/images/01.png)

1. Click _Save_ when finished.

## Additional Information

* [Using Notification Templates](./using-notification-templates.md)
