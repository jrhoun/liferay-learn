# Command-line Tool

Liferay DXP's command-line interface (CLI) is a tool that helps you use and 
manage DXP Cloud. For example, you can use the CLI to create, manage, and scale 
applications. 

* [Installing the CLI](#installing-the-cli)
* [Changing the CLI Remote](#changing-the-cli-remote)
* [Showing the Service Logs](#showing-the-service-logs)
* [Manage Custom Domains](#manage-custom-domains)
* [Manage Environment Variables](#manage-environment-variables)
* [Change the number of service instances](#change-the-number-of-service-instances)
* [List Projects or Services](#list-projects-or-services)
* [Restart a Service](#restart-a-service)
* [Execute Commands in a Service Container](#execute-commands-in-a-service-container)
* [Access a Service's Shell](#access-a-services-shell)
* [Open Console](#open-console)
* [Uninstalling the CLI](#uninstalling-the-cli)

## Installing the CLI

**\*nix Systems**

Open a terminal and run this command: 

```bash
curl https://cdn.liferay.cloud/lcp/stable/latest/install.sh -fsSL | bash
```

If you get a permissions error, try running the same command with `sudo`. 

**Windows Systems**

Download the latest version of the 
[Windows installer](https://cdn.liferay.cloud/lcp/stable/latest/lcp-install.exe) and follow the steps in the wizard. 


## Changing the CLI Remote

To access DXP Cloud services via the CLI, the CLI must be pointed to the right 
DXP Cloud. The remote URL for DXP Cloud is `liferay.cloud`. To list the CLI's 
remotes, run this command: 

```shell
lcp remote
```

Follow these steps to change the default remote: 

1. Add a new remote if necessary: 

    ```shell
    lcp remote set <remote-alias> <remote-url>
    ```

1. Run this command to set the default remote: 

    ```shell
    lcp remote default <remote-alias>
    ```

Alternatively, specify the remote inline via this command: 

```shell
lcp shell --project <project-id> --service <service-id> --remote <remote-alias>
```

## Showing the Service Logs

The `lcp log` command displays the DXP Cloud project's service logs. Here are 
some common examples. 

Check an entire project's logs: 

```shell
lcp log --project <projectID>
```

View the logs of a specific service in a project: 

```shell
lcp log --project <projectID> --service <serviceID>
```

View the logs of a specific period of time: 

```shell
lcp log --project <projectID> --since <timestamp>
```

Alternatively, view a service's logs by passing the service's full URL to 
`lcp log`: 

```shell
lcp log --url <serviceID>-<projectID>.lfr.cloud
```

## Manage Custom Domains

Use the `lcp domain` command to manage custom domains in DXP Cloud projects. 
Here are some common examples. 

Get the list of custom domains for a particular service: 

```shell
lcp domain --project <projectID> --service <serviceID>
```

Add a custom domain to a service: 

```shell
lcp domain add example.com --project <projectID> --service <serviceID>
```

Remove a custom domain from a service:

```shell
lcp domain delete example.com --project <projectID> --service <serviceID>
```

Alternatively, run the same commands by passing the service's full URL to 
`lcp domain`: 

```shell
lcp domain --url <serviceID>-<projectID>.lfr.cloud
```

## Manage Environment Variables

Use the `lcp env-var` command to manage environment variables. Here are some common examples. 

Get the list of environment variables for a particular service: 

```shell
lcp env-var --project <projectID> --service <serviceID>
```

Add an environment variable to a service: 

```shell
lcp env-var set SOME_KEY somevalue --project <projectID> --service <serviceID>
```

Remove an environment variable from a service: 

```shell
lcp env-var rm SOME_KEY --project <projectID> --service <serviceID>
```

Alternatively, pass a service's full URL to `lcp env`: 

```shell
lcp env-var --url <serviceID>-<projectID>.lfr.cloud
```

## Change the number of service instances

Use the `lcp scale` command to change the number of instances. Here are some common examples. 

```shell
lcp scale --project <projectID> <instances>
```

Scale instances of a specific service in a project: 

```shell
lcp scale --project <projectID> --service <serviceID> <instances>
```

Alternatively, scale instances by passing its full URL to `lcp restart`: 

```shell
lcp scale --url <serviceID>-<projectID>.lfr.cloud <instances>
```

## List Projects or Services

Use the `lcp list` command to list projects and services. Here are some common 
examples. 

See the full list of projects, services, and instances you own or collaborate on: 

```shell
lcp list
```

List a project's services: 

```shell
lcp list --project <projectID>
```

Check a specific service in a project: 

```shell
lcp list --project <projectID> --service <serviceID>
```

Alternatively, check a service by passing its full URL to `lcp list`: 

```shell
lcp list --url <serviceID>-<projectID>.lfr.cloud
```

## Restart a Service

Use the `lcp restart` command to restart a service. Here are some common 
examples. 

Restart a project's services: 

```shell
lcp restart --project <projectID>
```

Restart a specific service in a project: 

```shell
lcp restart --project <projectID> --service <serviceID>
```

Alternatively, restart a service by passing its full URL to `lcp restart`: 

```shell
lcp restart --url <serviceID>-<projectID>.lfr.cloud
```

## Execute Commands in a Service Container

Use the CLI to run commands in a service container. For example, this runs a 
command in a specific service instance: 

```shell
lcp exec --project <projectID> --service <serviceID> --instance <abc123> -- mkdir foo
```

This runs a command in any instance of a service: 

```shell
lcp exec --project <projectID> --service <serviceID> --instance any -- mkdir foo
```

## Access a Service's Shell

To access a service container's shell, run this command: 

```shell
lcp shell
```

This lists all the services in the container and lets administrators choose 
which one to access. 

Alternatively, access the shell of a specific service's container by adding the 
service's project ID and service ID to the `lcp shell` command: 

```shell
lcp shell --project <projectID> --service <serviceID>
```

## Open Console

Use the CLI to open the console anytime. For example, this opens the console: 

```shell
lcp console
```

This opens a specific service on the console:

```shell
lcp open --project <projectID> --service <serviceID>
```

This opens DXP Cloud documentation:

```shell
lcp docs
```

## Uninstalling the CLI

For Mac and Linux, run this command:

```bash
curl https://cdn.liferay.cloud/lcp/stable/latest/uninstall.sh -fsSL | bash
```

For Windows, navigate to `Control Panel -> Add or Remove Programs`. Find "LCP CLI" in the list of programs, select it, and click "Uninstall". Follow the steps in the wizard.



