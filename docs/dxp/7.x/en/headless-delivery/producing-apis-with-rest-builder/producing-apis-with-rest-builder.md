# Producing APIs with REST Builder

REST Builder is a code generation tool that makes it easy for you to take your local APIs and make them available on the web. 
It uses the [OpenAPI Specification](https://www.openapis.org/) to generate REST and [GraphQL](https://graphql.org/) APIs.

REST Builder uses the configuration you define in `rest-config.yaml` and `rest-openapi.yaml` files to generate most of the code necessary for your API to work all at once. You configure class names and where to put the code, and REST Builder generates all of the necessary files. Then you add your implementation logic. 

You run REST Builder using the Gradle task `buildREST` from your `impl` module in a Liferay workspace. Once configured, it generates all the scaffolding code, interfaces, and even resource classes ready for implementation. 

In general, you can use the `@generated` annotation above the class name in each Java file to distinguish whether it's something you've modified, or if it should be re-generated the next time REST Builder runs. If the annotation is not present, the file is meant for you to add your own code to and is not overwritten.

## Generated Code Structure

REST Builder generates the boilerplate, so you can focus on just your implementation class. However, you must start by defining the locations for each of your modules. In a conventional Liferay workspace, create the folders for each module and each of their `bnd.bnd` and `build.gradle` files.

After you create the initial configuration for your modules and the [REST Builder configuration files](#adding-your-api-configurations) (`rest-config.yaml` and `rest-openapi.yaml`), running REST Builder generates the following API structure:

```
api root
├── bnd.bnd
├── build.gradle
└── src
    └── main
        └── java
            └── <apiPackagePath>
                ├── dto
                │   └── <version>
                │       └── Schema object classes
                └── resource
                    └── <version>
                        └── Schema object resource interfaces
```

The API module contains the Java classes for any custom objects you have defined (as [object schemas](#defining-schemas) in ``rest-openapi.yaml``) within the `dto` package. Reference these classes to work with your custom objects when you are adding your implementation logic.

```note::
   The path ``src/main/java/`` may vary if you defined a different path in the ``apiDir`` property. The ``apiPackagePath`` is defined in your project's ``rest-config.yaml`` file. Finally, the ``version`` path is configured in the ``rest-openapi.yaml`` file.
```

REST Builder generates the following structure for `impl` modules:

```
impl root
├── bnd.bnd
├── build.gradle
├── rest-config.yaml
├── rest-openapi.yaml
└── src
    └── main
        ├── resources
        │   └── OSGI-INF
        │       └── liferay
        │           └── rest
        │               └── <version>
        │                   └── Generated properties files
        └── java
            └── <apiPackagePath>
                └── internal
                    ├── graphql
                    │   └── GraphQL endpoint code
                    ├── jaxrs
                    │   └── application
                    │       └── JAX-RS application code
                    └── resource
                        └── <version>
                            └── *ResourceImpl classes
```

GraphQL endpoint code and JAX-RS application code are both generated in the `graphql` and `jaxrs` packages, respectively. Your own API implementation is added into the appropriate `*ResourceImpl` class in the `resource` package.

You can also configure a `client` and `test` module for REST Builder to generate client and test code, respectively. Define a `clientDir` or `testDir` path in your `rest-config.yaml` to generate them. 

As with the `api` and `impl` modules, REST Builder uses the directory paths, `apiPackagePath` values, and `version` value to define the folders that it will add classes into.

For `test` modules, you can define the implementation of your tests to the appropriate `*ResourceTest` Java class. Generated test classes follow the [JUnit](https://junit.org/junit5/docs/current/user-guide/) testing framework.

## Adding Your API Configurations

The details of the API you intend to add are configured in your project's `rest-openapi.yaml`. There are three main sections of this file that you can define: an `info` section, a `components` section, and a `paths` section.

### Defining Basic API Information

The `info` section of your `rest-openapi.yaml` file defines information about your APIs that is used by the JAX-RS application when it becomes available, as well as the OpenAPI version beneath it.

Here is an example of an `info` section: 

```
info:
    description:
        "This is an example API."
    license:
        name: "Apache 2.0"
        url: "http://www.apache.org/licenses/LICENSE-2.0.html"
    title: "Journal Article API Expansion"
    version: v1.0
openapi: 3.0.1
```

### Defining Schemas

If you need REST Builder to create a new entity or data structure to use as a return type or parameter for your APIs, you must define it as an object with its own _schema_ in the `components` section of your `rest-openapi.yaml` file.

Objects are defined with a name, a `type` (usually `object`, unless it only represents a basic type), and then a list of `properties` (fields in Java code) they contain. Each property also has a `type` and a `description` that are used to generate Java documentation.

Here is an example of a `components` section that defines one schema for a `BasicUser` object, containing only a name and ID:

```
components:
    schemas:
        BasicUser:
            description:
                A basic user with only a name and ID.
            properties:
                name:
                    description:
                        The user's name as a string.
                    type:
                        string
                id:
                    description:
                        The user's ID as an integer.
                    type:
                        integer
            type:
                object
```

The schema also defines the prefix REST Builder uses when generating the resource files for your implementation. In the above example, the API implementation belongs in the `BasicUserResourceImpl` file.

See the [OpenAPI specification](https://swagger.io/docs/specification/data-models/data-types/) for a list of all the supported basic data types that you can use for schemas.

```tip::
   If your API only returns one of the basic data types, you may not need to define any schemas in your ``rest-openapi.yaml`` file.
```

### Defining the APIs

The last section, `paths`, specifies the details of the APIs themselves. Each API must be defined within its own path, which is added to the end of the base URL. Making a request to the full URL including the path calls the API you've defined. APIs can take several types of requests, including `get`, `post`, `put`, `patch`, and `delete`.

Each API contains an `operationId` (which becomes the name of the method in the Java code), a list of `parameters`, a tag, and a list of possible `responses` that the API returns when it is called. At least a `200` response (indicating a successful request) is required for the API to work.

```
paths:
    "/entities/{userId}":
        get:
            operationId: getBasicUser
            parameters:
                - in: path
                  name: userId
                  required: true
                  schema:
                      type: integer
            responses:
                200:
                    content:
                        application/json:
                            schema:
                                $ref: "#/components/schemas/BasicUser"
                        application/xml:
                            schema:
                                $ref: "#/components/schemas/BasicUser"
                    description:
                        "The BasicUser object"
            tags: ["BasicUser"]
```

The `parameters` each have a `name` (used for the request as well as in the Java method call), whether it is required, and a `schema` (which may be either a basic data type or a schema for a custom object you have defined).

The `responses` must each have `content` defined for JSON or XML responses (or both). Each possible response must also define a `schema`, just like the parameters.

```note::
   If you want to use an object you have defined in the ``components`` section for either your API's parameters or return type, then you can reference it with ``$ref: "#/components/schemas/<ObjectName>"``.
```

The tag determines what name to use when generating documentation when your code is annotated.

## Create Your Own APIs with REST Builder

Now that you understand how REST Builder works, you can use it to create APIs for your own applications. See [Implementing a New API with REST Builder](./implementing-a-new-api-with-rest-builder.md) to walk through this process with an example.
