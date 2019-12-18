# Migrating From Audience Targeting

While the Audience Targeting app has been removed from Liferay DXP as of 7.2, the same features are integrated into Liferay's core as Segmentation and Personalization. This enables better integration with other applications and provides developers with easier access to Segmentation and Personalization features.

Audience Targeting Users must migrate their user segments into the new Segments application. There are three steps to the migration process:

1.  **Upgrade to DXP 7.2.** Follow the steps in the [upgrade guide](../01-introduction-to-upgrading-to-liferay-dxp-7-2.md). Most prior Audience Targeting configuration is automatically transferred with the upgrade.

2.  **Evaluate Audience Targeting rules.** Any custom rules that were created in Audience Targeting must be re-evaluated after the upgrade. Some rules have a direct equivalent in Segmentation and Personalization and may be migrated automatically with the upgrade. See [Migrating User Segments](./02-migrating-user-segments.md) for a list of which features are migrated automatically.

3.  **Manually migrate rules and widgets.** See the [overview on manually migrating from Audience Targeting](./03-manually-migrating-from-audience-targeting.md) for help with evaluating rules or widgets that are not automatically migrated. If a rule must be re-implemented, see the [Segmentation and Personalization development guide](https://help.liferay.com/hc/en-us/articles/360028721372-Introduction-to-Segmentation-and-Personalization).

4.  **Migrate behavior-based features.** Since Audience Targeting's analytics features are now part of Analytics Cloud, there is no direct path to upgrade like other features. See the [Analytics Cloud documentation](https://help.liferay.com/hc/en-us/articles/360006947671-Creating-Segments) for more information.
