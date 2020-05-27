# Workflow Designer Nodes Reference

> Subscribers

A Workflow Node represents a specific point in an approval process, whether it is starting the review process, approving or rejecting the asset, or reassigning the task.

This article details the different types of nodes and the possible actions associated with each node.

## Types of Nodes

| Node | Description |
| --- | --- |
| Task |_Task_ nodes indicate the workflow task and its assignee. |
| Fork and Join | _Fork_ and _Join_ are paired nodes that allow users to spilt the review process to concurrent reviewers then rejoin for the next step. |
| Join XOR| The _Join XOR_ node allows the workflow to proceed as long as the transition from one of the parallel executions is invoked. |
| Condition | The _Condition_ node establishes a condition before the review process can proceed. |
| Start | The _Start_ node is the starting point. |
| End | The default _End_ node is a pre-configured state node that sets the workflow status to _Approved_. |
| State | _State_ nodes describe the status of the review process; they can be used for "created" (start) or "approved". |

### Start and End Nodes

Start and end nodes kick off the workflow processing and bring the asset to its final, approved state. Often you can use the default start and end nodes without modification. However, you can still configuring a start node, such as notifying users that the review process has begun.

End nodes have a default action that sets the workflow status to Approved using the Groovy scripting language:

```java
    import com.liferay.portal.kernel.workflow.WorkflowStatusManagerUtil;
    import com.liferay.portal.kernel.workflow.WorkflowConstants;

    WorkflowStatusManagerUtil.updateStatus(WorkflowConstants.getLabelStatus("approved"), workflowContext);
```

### State Nodes

State nodes can have [Actions and Notifications](./configuring-workflow-actions-and-notifications.md). For example, users can create a node that sets the status to _Expired_. Here is a Groovy script that sets the workflow status as Expired:

```java
    import com.liferay.portal.kernel.workflow.WorkflowStatusManagerUtil;
    import com.liferay.portal.kernel.workflow.WorkflowConstants;

    WorkflowStatusManagerUtil.updateStatus(WorkflowConstants.getLabelStatus("expired"), workflowContext);
```

## Additional Information

* [Creating Workflow Tasks](./creating-workflow-tasks.md)
* [Kaleo Forms](../../../user-guide/advanced-forms-usage/kaleo-forms/kaleo-forms.md)
* [Activating Workflow](../activating-workflow.md)
* [Introduction to the Workflow Framework](https://help.liferay.com/hc/en-us/articles/360028727112-Introduction-to-The-Workflow-Framework)
* [Dynamic Data Lists](../../../user-guide/advanced-forms-usage/dynamic-data-lists/getting-started-with-dynamic-data-lists.md)
