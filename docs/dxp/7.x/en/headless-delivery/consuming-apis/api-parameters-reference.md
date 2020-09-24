# API Parameters Reference

This article documents the available parameters you can use when making Headless API requests:

* [`fields`](#fields)
* [`filter`](#filter)
* [`flatten`](#flatten)
* [`page`](#page)
* [`pageSize`](#pagesize)
* [`restrictFields`](#restrictfields)
* [`search`](#search)
* [`sort`](#sort)

## `fields`

Reduces the amount of information included in each returned item – only the indicated fields are included. (See also [`restrictFields`](#restrictfields) for the opposite functionality.)

### Example Request

<div class="toggle headless">
OpenAPI Example | <a href="#" onclick="return toggleVisible('graphql');">GraphQL Example</a>

```
curl --user test@liferay.com:test 'example.com/o/headless-admin-user/v1.0/organizations?fields=id,name,organizationContactInformation.emailAddresses'
```
</div>

<div class="toggle graphql d-none">
<a href="#" onclick="return toggleVisible('headless');">OpenAPI Example</a> | GraphQL Example

```
query {
  organizations {
    actions
    items {
      id
      name
      organizationContactInformation {
        emailAddresses {
          emailAddress
          id
          primary
          type
        }
      }
    }
    lastPage
    page
    pageSize
    totalCount
  }
}
```

```note::
The desired fields are always specified in GraphQL, so there's no specific "fields" or "restrictFields" parameter to pass.
```
</div>

### Example Response

```
{
  "actions" : {
    ...
  },
  "items" : [ {
    "id" : "35562",
    "name" : "The Earth",
    "organizationContactInformation" : {
      "emailAddresses" : [ ]
    }
  } ],
  "lastPage" : 1,
  "page" : 1,
  "pageSize" : 20,
  "totalCount" : 1
}
```

## `filter`

Reduces the number of items returned, by faceted search.

### Example Request

<div class="toggle headless">
OpenAPI Example | <a href="#" onclick="return toggleVisible('graphql');">GraphQL Example</a>

```
curl --user test@liferay.com:test 'example.com/o/headless-admin-user/v1.0/organizations?fields=id,name&flatten=true&filter=contains(name,%27America%27)'
```
</div>

<div class="toggle graphql d-none">
<a href="#" onclick="return toggleVisible('headless');">OpenAPI Example</a> | GraphQL Example

```
query {
  organizations (flatten: true, filter: "contains(name, 'America')") {
    actions
    items {
      id
      name
    }
    lastPage
    page
    pageSize
    totalCount
  }
}
```
</div>

### Example Response

```
{
  "actions" : {
    ...
  },
  "items" : [ {
    "id" : "35575",
    "name" : "The United States of America"
  }, {
    "id" : "35567",
    "name" : "North America"
  } ],
  "lastPage" : 1,
  "page" : 1,
  "pageSize" : 20,
  "totalCount" : 2
}
```

## `flatten`

Allows retrieving items outside of their hierarchical structure.

### Example Request

<div class="toggle headless">
OpenAPI Example | <a href="#" onclick="return toggleVisible('graphql');">GraphQL Example</a>

```
curl --user test@liferay.com:test 'example.com/o/headless-admin-user/v1.0/organizations?fields=id,name&flatten=true'
```
</div>

<div class="toggle graphql d-none">
  <a href="#" onclick="return toggleVisible('headless');">OpenAPI Example</a> | GraphQL Example

```
query {
  organizations (flatten: true) {
    actions
    items {
      id
      name
    }
    lastPage
    page
    pageSize
    totalCount
  }
}
```
</div>

### Example Response

```
{
  "actions" : {
    ...
  },
  "items" : [ {
    "id" : "35575",
    "name" : "The United States of America"
  }, {
    "id" : "35579",
    "name" : "Canada"
  }, {
    "id" : "35583",
    "name" : "Germany"
  }, {
    "id" : "35567",
    "name" : "North America"
  }, {
    "id" : "35571",
    "name" : "Europe"
  }, {
    "id" : "35562",
    "name" : "The Earth"
  }, {
    "id" : "35587",
    "name" : "France"
  } ],
  "lastPage" : 1,
  "page" : 1,
  "pageSize" : 20,
  "totalCount" : 7
}
```

## `page`

Selects which subset of items should be returned, by page number. For example, for 20 total elements and `pageSize=5`, passing `page=3` would yield the 11th through 15th elements.

### Example Request

<div class="toggle headless">
OpenAPI Example | <a href="#" onclick="return toggleVisible('graphql');">GraphQL Example</a>

```
curl --user test@liferay.com:test 'example.com/o/headless-admin-user/v1.0/organizations?fields=id,name&flatten=true&page=2&pageSize=5'
```
</div>

<div class="toggle graphql d-none">
<a href="#" onclick="return toggleVisible('headless');">OpenAPI Example</a> | GraphQL Example

```
query {
  organizations (flatten: true, page: 2, pageSize: 5) {
    actions
    items {
      id
      name
    }
    lastPage
    page
    pageSize
    totalCount
  }
}
```
</div>

### Example Response

```
{
  "actions" : {
    ...
  },
  "items" : [ {
    "id" : "35562",
    "name" : "The Earth"
  }, {
    "id" : "35587",
    "name" : "France"
  } ],
  "lastPage" : 2,
  "page" : 2,
  "pageSize" : 5,
  "totalCount" : 7
}
```

## `pageSize`

Selects how many items should be returned in a single response, that is, the number of elements in each page.

### Example Request

<div class="toggle headless">
OpenAPI Example | <a href="#" onclick="return toggleVisible('graphql');">GraphQL Example</a>

```
curl --user test@liferay.com:test 'example.com/o/headless-admin-user/v1.0/organizations?fields=id,name&flatten=true&pageSize=5'
```
</div>

<div class="toggle graphql d-none">
<a href="#" onclick="return toggleVisible('headless');">OpenAPI Example</a> | GraphQL Example


```
query {
  organizations (flatten: true, pageSize: 5) {
    actions
    items {
      id
      name
    }
    lastPage
    page
    pageSize
    totalCount
  }
}
```
</div>

### Example Response

```
{
  "actions" : {
    ...
  },
  "items" : [ {
    "id" : "35575",
    "name" : "The United States of America"
  }, {
    "id" : "35579",
    "name" : "Canada"
  }, {
    "id" : "35583",
    "name" : "Germany"
  }, {
    "id" : "35567",
    "name" : "North America"
  }, {
    "id" : "35571",
    "name" : "Europe"
  } ],
  "lastPage" : 2,
  "page" : 1,
  "pageSize" : 5,
  "totalCount" : 7
}
```

## `restrictFields`

Reduces the amount of information included in each returned item – the indicated fields are excluded. (See also [`fields`](#fields) for the opposite functionality.)

### Example Request

<div class="toggle headless">
OpenAPI Example | <a href="#" onclick="return toggleVisible('graphql');">GraphQL Example</a>

```
curl --user test@liferay.com:test 'example.com/o/headless-admin-user/v1.0/organizations?restrictFields=actions,comment,customFields,dateCreated,dateModified,keywords,location,numberOfOrganizations,organizationContactInformation.telephones,services'
```
</div>

<div class="toggle graphql d-none">
<a href="#" onclick="return toggleVisible('headless');">OpenAPI Example</a> | GraphQL Example

```
query {
  organizations {
    actions
    items {
      id
      name
      organizationContactInformation {
        emailAddresses {
          emailAddress
          id
          primary
          type
        }
        postalAddresses {
          addressCountry
          addressLocality
          addressRegion
          addressType
          id
          postalCode
          primary
          streetAddressLine1
          streetAddressLine2
          streetAddressLine3
        }
        webUrls {
          id
          url
          urlType
        }
      }
    }
    lastPage
    page
    pageSize
    totalCount
  }
}
```

```note::
The desired fields are always specified in GraphQL, so there's no specific "fields" or "restrictFields" parameter to pass.
```
</div>

### Example Response

```
{
  "actions" : {
    ...
  },
  "items" : [ {
    "id" : "35920",
    "name" : "The Earth",
    "organizationContactInformation" : {
      "emailAddresses" : [ ],
      "postalAddresses" : [ ],
      "webUrls" : [ ]
    }
  } ],
  "lastPage" : 1,
  "page" : 1,
  "pageSize" : 20,
  "totalCount" : 1
}
```

## `search`

Reduces the number of items returned, by simple keyword search.

### Example Request

<div class="toggle headless">
OpenAPI Example | <a href="#" onclick="return toggleVisible('graphql');">GraphQL Example</a>

```
curl --user test@liferay.com:test 'example.com/o/headless-admin-user/v1.0/organizations?fields=id,name&flatten=true&search=America'
```
</div>

<div class="toggle graphql d-none">
<a href="#" onclick="return toggleVisible('headless');">OpenAPI Example</a> | GraphQL Example

```
query {
  organizations (flatten: true, search: "America") {
    actions
    items {
      id
      name
    }
    lastPage
    page
    pageSize
    totalCount
  }
}
```
</div>

### Example Response

```
{
  "actions" : {
    ...
  },
  "items" : [ {
    "id" : "35575",
    "name" : "The United States of America"
  }, {
    "id" : "35567",
    "name" : "North America"
  } ],
  "lastPage" : 1,
  "page" : 1,
  "pageSize" : 20,
  "totalCount" : 2
}
```

## `sort`

Modifies the order in which items are returned (and, if more than [`pageSize`](#pagesize) items exist, determines which items are returned in a given page).

### Example Request

<div class="toggle headless">
OpenAPI Example | <a href="#" onclick="return toggleVisible('graphql');">GraphQL Example</a>

```
curl --user test@liferay.com:test 'example.com/o/headless-admin-user/v1.0/organizations?fields=id,name&flatten=true&sort=name:asc'
```
</div>

<div class="toggle graphql d-none">
<a href="#" onclick="return toggleVisible('headless');">OpenAPI Example</a> | GraphQL Example

```
query {
  organizations (flatten: true, sort: "name:asc") {
    actions
    items {
      id
      name
    }
    lastPage
    page
    pageSize
    totalCount
  }
}
```
</div>

### Example Response

```
{
  "actions" : {
    ...
  },
  "items" : [ {
    "id" : "35579",
    "name" : "Canada"
  }, {
    "id" : "35571",
    "name" : "Europe"
  }, {
    "id" : "35587",
    "name" : "France"
  }, {
    "id" : "35583",
    "name" : "Germany"
  }, {
    "id" : "35567",
    "name" : "North America"
  }, {
    "id" : "35562",
    "name" : "The Earth"
  }, {
    "id" : "35575",
    "name" : "The United States of America"
  } ],
  "lastPage" : 1,
  "page" : 1,
  "pageSize" : 20,
  "totalCount" : 7
}
```

<script>
  function toggleVisible(showClass) {
    var hideElements = document.getElementsByClassName('toggle');

    for (var i = 0, len = hideElements.length; i < len; i++) {
      hideElements[i].classList.add('d-none');
    }

    var showElements = document.getElementsByClassName(showClass);

    for (var i = 0, len = showElements.length; i < len; i++) {
      showElements[i].classList.remove('d-none');
    }

    return false;
  }
</script>