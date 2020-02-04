## Reactivating Liferay DXP

If you have a new DXP activation key and your DXP instance is currently activated by an activation key or by Liferay Connected Services (LCS), it's best to remove remnants of the former activation method before deploying your new activation key. This removes any ambiguity as to which activation key you're using.

Here are the steps for reactivating DXP with your new key:

1. Stop the application server.

1. If you've been using LCS to activate DXP, remove the Liferay Connected Services Client LPKG file (`.lpkg`) from your `osgi/marketplace` folder in your [Liferay Home](../14-reference/01-liferay-home.md).

1. Delete the _contents_ of your `[Liferay Home]/data/license` folder but preserve the folder.

1. Remove all `activation-key-[...].xml` files from your `[Liferay Home]/osgi/modules` folder.

1. Start the application server.

1. Copy your new activation key file to your `[Liferay Home]/deploy` folder.

A DXP console message confirms the registration.

```
License registered ...
```

DXP is reactivated and ready to use.
