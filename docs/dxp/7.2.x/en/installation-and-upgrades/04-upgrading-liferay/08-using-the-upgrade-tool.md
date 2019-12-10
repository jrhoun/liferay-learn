# Using the Upgrade Tool

<!-- this article feels written like a reference, for being the culminating milestone of the upgrade process - perhaps performing the upgrade should play a stronger role in the structure -->
This article provides an overview of how to use the upgrade tool within your application server.

## Upgrade Tool Usage

Start the upgrade tool using the `db_upgrade.sh` script in the `[LIFERAY_HOME]/tools/portal-tools-db-upgrade-client` folder (`db_upgrade.bat` on Windows). Here are the core upgrade stages:

1. Show the upgrade patch level
1. Execute the core upgrade processes
1. Execute the core verifiers

If you configured the upgrade tool to upgrade non-core modules, the tool opens a Gogo shell and starts upgrading them after the core upgrade processes are complete. The Gogo shell lets you upgrade modules, check module upgrade status, verify upgrades, and restart module upgrades. See [Upgrading Modules Using Gogo Shell](./09-upgrading-modules-using-gogo-shell.md) for more information.

This command prints the upgrade tool usage:

```bash
db_upgrade.sh --help
```

Here are the tool's default Java parameters:

```bash
-Dfile.encoding=UTF-8 -Duser.country=US -Duser.language=en -Duser.timezone=GMT -Xmx2048m
```

The `-j` option overrides the JVM parameters. For example, these options set the
JVM memory to 10GB, which is a good starting point for this process type:

```bash
db_upgrade.sh -j "-Dfile.encoding=UTF-8 -Duser.country=US -Duser.language=en -Duser.timezone=GMT -Xmx10240m"
```

The `-l` option specifies the tool's log file name:

```bash
db_upgrade.sh -l "output.log"
```

### Upgrade Tool Options

Here are all the upgrade tool command line options:

**--help** or **-h**: Prints the tool's help message.

**--jvm-opts** or **-j** + **[arg]**: Sets any JVM options for the upgrade
process.

**--log-file** or **-l** + **[arg]**: Specifies the tool's log file name---the
default name is `upgrade.log`.

**--shell** or **-s**: Automatically connects you to the Gogo shell after
finishing the upgrade process.

### Ensuring the Upgrade Runs Smoothly

Only execute the upgrade process on a server with ideal memory, CPU, and database connection configurations. If executing an upgrade remotely using `ssh`, make sure to guard against interruptions:

* If you're executing the upgrade using `ssh` and connection is lost, connect again and check the upgrade logs since the process will continue running.
* If execution stopped during an upgrade process for DXP 7.1 or higher, restart the upgrade tool to continue the upgrade from that point. You can also use Gogo shell to [check module upgrade status](./09-upgrading-modules-using-gogo-shell.md#checking-upgrade-status) and continue non-core module upgrades, as long as the core upgrade processes have completed.
* If execution stopped during a core upgrade process for DXP 7.0 or lower, you must [restore the data from a backup](https://help.liferay.com/hc/en-us/articles/360029124271-Backing-up-a-Liferay-DXP-Installation) and start the upgrade again.

**Warning:** To prevent the tool's expanded command from growing too large for Windows, execute the upgrade tool script from the `[LIFERAY_HOME]/tools/portal-tools-db-upgrade-client` folder.

<!-- additional information -->