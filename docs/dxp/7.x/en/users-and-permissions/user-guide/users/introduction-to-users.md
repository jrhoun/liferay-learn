# Users and Organizations

*Users* and *Organizations* are fundamental entities. If your site requires people (even just a set of site administrators) to have accounts to do anything, you need to know about Users. If your Users are at all divided hierarchically, like into departments, you'll find that Organizations are helpful. 

![Users and Organizations are managed from the same place in the Control Panel](./intro/images/01.png)

Users and Organizations are managed in the Control Panel's *Users and Organizations* section.

These are just a few examples of activities executed from the Users and Organizations section of the Control Panel: 

- An employee leaves the company, requiring account deletion

- An employee joins the company and must be added to the portal, and to a specific department.

- An employee is promoted to a new role and needs additional permissions within the portal.

- Organize the Users by department with Organizations.

- Add new departments (as Organizations, most likely) and give the department's employees their own internal website.

- An employee gets married and changes her name.

## What are Users?

A User is an entity that can sign into Liferay DXP and do something. A User has more privileges, called Permissions, than a Guest of your site who does not sign in. Users are assigned Roles, and Roles define the User's privileges.

## What are Organizations? 

An *Organization* groups [*Users*](./02-managing-users.md) hierarchically. For example, you can model a company's departments (i.e., Human Resources and Customer Support) with Organizations. Organizations often have their own Sites. 

Many simple portal designs don't use Organizations at all; they only use Sites. The main purpose of Organizations is to enable distributed User management. Portal administrators can delegate some User management responsibilities to Organization administrators. If you don't anticipate needing to delegate User management responsibilities, your portal design may not need Organizations. 

**User Groups and Organizations:** It's easy to confuse User Groups with Organizations since they both collect Users. User Groups are an ad hoc collection of Users, organized for a specific function. If you wanted a group of bloggers, for example, it wouldn't make sense to assign the Sales Department the Role of blogging. Instead, creating a User Group containing one individual from each department who is responsible for blogging would make more sense. 

To decide whether your portal design should include Organizations, think about its function. A photo-sharing website could be powered by Sites only. On the other hand, Organizations are useful for corporations, educational institutions, governments, or any other large entity since their Users can be placed into a hierarchical structure. 

Don't think that Organizations are only for large enterprises, though. Any group hierarchy, from large government agencies all the way down to small clubs, can be modeled with Organizations. Also, don't think that you must decide between an Organization-based structure or a Site-based structure for assembling your portal's Users. Users can belong both to Organizations and to independent Sites. For example, a corporation or educational institution could create a social networking site open to all Users, even ones from separate Organizations. 

Users and Organizations are two of the most common ways to administer Liferay DXP and model your use case. Read on to learn how to manage them. 
