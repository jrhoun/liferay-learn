# Enabling Search Suggestions

Search terms can be suggested to users when their initial queries can be improved. Spell check settings allow administrators to configure the Search application so that if a user types a search term that doesn't return many results (for example, a slightly misspelled word), the user can be prompted to improve the search.

To configure the spell check settings:

1. You must first reindex the spell check indexes. Go to _Control Panel_ &rarr; _Configuration_ &rarr; _Search_, and open the Index Actions screen.

    Click _Execute_ next to _Reindex all spell check indexes_.

1. Add the _Suggestions_ widget to the search page.

1. Open the _Suggestions_ widget configuration screen. Click the widget Options button (![Options](../../../images/icon-widget-options.png)) and select _Configuration_.

    ![Configure the suggestion settings to allow for user input mistakes and help lead users to results.](./enabling-search-suggestions/images/01.png)

1. Configure as desired and click _Save_.

## Suggestions Configuration Reference

There are three main settings available for the Suggestions widget:

**Display "Did you mean..." if the number of search results does not meet the threshold:** Present users alternate, spell checked search queries if their search did not return a minimum number of results (50 by default).

**Display Related Queries:** If the number of search results doesn't meet the specified threshold (50 by default), display up to a maximum number of alternative queries (10 by default).

**Add New Related Queries Based on Successful Queries:** Index a user's search query if it produces a minimum number of results (50 by default), so it can be displayed to users as a suggestion. If the Display Related Queries setting is enabled, it's used as a related query for similar search queries that don't produce enough results.
