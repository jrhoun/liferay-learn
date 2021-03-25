# Building an Intranet Overview

In the modern digital workplace, it's important to connect, inform, and equip members of your organization wherever they are. With Liferay DXP, you can use out-of-the-box features to quickly build and deploy modern intranet solutions on a single platform. <!--Provide a functional/dynamic, secure, and reliable access point to content and resources... Create/provide seamless, content-rich experiences for users across your organization, regardless of device and location... -->

The following articles lead you through the process of building your own intranet solution. This process includes creating its Site, determining its appearance, importing digital assets, and more. <!-- First will provide an overview of DXP features that are useful for building a modern intranet. Then note any prerequisites or advice for before starting to build the intranet. Then provides an outline of the steps we'll go through in subsequent articles.-->

* [Overview of Liferay Features](#overview-of-liferay-features)
* [Before Getting Started](#before-getting-started)
* [Outline for Building an Intranet](#outline-for-building-an-intranet)

## Overview of Liferay Features

<!-- Statements regarding Liferay's specific features and how they contribute to building a modern intranet. Keep sections very short, and only address how each application meets an intranet need... -->
Liferay DXP provides an extensive library of flexible, out-of-the-box features that you can use for building a modern intranet solution. These include tools for Site design, collaboration, content creation/management, and more. Each feature is extensible, so both backend and frontend developers can customize your intranet solution to meet your specific needs.

### Site Building and Design

With Liferay's convenient, user-friendly interface, you can create and design intranet [Sites]() and [Pages]() with minimal technical knowledge<!--W/Cs-->. Quickly add pages using [Page Templates](), and then organize them to create the desired [Site structure]()<!--W/C...hierarchy?-->. When building a Content Page or Page Template, use configurable<!--W/C...modular?--> drag-and-drop page elements to determine its layout and functionalities. Using DXP's [Site versioning](), you can make your changes in an editing environment before they go live.

As part of this process, you can standardize your Site's appearance using [Style Books](). These customizations sit on top of a base theme ([Classic Theme]() by default), which you can change if desired. With dynamic, [responsive design](), you can also determine how your Pages are displayed on different devices. Personalize appearance and create visually engaging and unified experiences across your intranet.

<!-- WHAT ABOUT USERS? Add users, define and assign roles and permissions, manage user access through roles and permissions, organize them into [User Groups]() and [Organizations](). Connect to an active directory.
User [Segments]() are dynamically assigned user collections based on a common set of properties (e.g., job title, group, language, etc). Once you've created a user segment, you can use it to design personalized experiences for your users--determining how pages appear for each segment. Toggle through different user experiences.-->

### Collaboration and Social

Use Liferay DXP's wide suite of flexible and extensible applications to build intranets that foster communication and collaboration. Use [Message Boards]() along with the [Questions]() app to help users find answers to questions and to facilitate discussions. Draft and display articles and for your Site with the [Wiki]() app.<!--add custom workflow...--> Publish engaging [Blogs] that __.<!--add custom workflow...--> Use [Activities] to follow user activity. Use [Contacts Center]() to provide contact information to users. Implement a [Ratings] system for Site content. Further connect your site users using [Comments], [Mentions], and [Notifications].
Other social tools, including [Activities]() and [Contacts Center](). User Profiles.

You can use these tools to build company-wide awareness (major announcements, job openings, etc.), promote team building/connectivity, highlight success stories, spotlight employees.
Create channels for employee announcements, questions, feedback, and dialogue.
Empower your employees with tools that support knowledge sharing.

In addition to work related events, keep a calendar with local community events (). Gamify your intranet to encourage employee adoption (e.g., badges, ranks, points). Sharing community photos (e.g., from company events, etc.--something that focused on shared experiences and demonstrates care). Promote collaboration, providing opportunities for employees to create intranet content. Communicate clear focus on all elements of the company's mission, while highlighting stories that reflect the company's commitment to its core values.

### Creating and Managing Digital Assets and Resources

Liferay DXP provides out of the box tools for creating, managing, and searching/navigating your intranet's digital assets. These applications include [Web Content](), [Documents and Media](), [Collections](), and more. These applications can be used directly in a specific Site, or at the instance level in [Asset Libraries](). DXP's [file storage]().

Use [Web Content]() to __. Can add custom [workflows] to guide content creation, revision, and publishing.

Use [Documents and Media]() to store and organize files of any kind on the Liferay server, serving as a virtual shared drive, accessible via [WebDAV](). Can be integrated with [Microsoft Office 365&trade;](), [Google Drive]().

Categorize content to reduce search time, improve visibility, and make it easier to display (e.g., [tags and categories](), [content ratings]()).

Create [Collections]() to manually or dynamically group and filter content, making it easier to display.

Use [Knowledge Base]() to display professional product documentation or form complete books or guides.

Provide your employees with timely, well-curated information to do their jobs in line with up-to-date policies and information, as well as provide employee onboarding and growth resources.

With enterprize [search]() features, ensure your users can find the most relevant and up to date material/information. <!--Search: Content and metadata search, filters and facets, smart recommendations.--> 

Liferay DXP also supports [localization]() by language and time zone, which can be scoped site-wide or for individual users to provide an enhanced employee experience. Engage your global team members.

Creating [Forms](). [Kaleo Forms]() integrates form building with additional workflow tools to create form-based business processes (e.g., Conference Room Checkout Form, Support Ticket Process, etc.)

<!-- Data Integration: Leverage and connect existing data and systems on a unified platform to easily transition off legacy tools. Doing so, streamlines day-to-day business tool usage and supports an omnichannel experience no matter where your employee is. -->

### Platform Integration and Customization

Liferay offers out-of-the-box connectors for Liferay DXP and [Sharepoint](), [Documentum](), and [Google Drive]().

With platform integration, you can "create Document Library files that link to Google Drive™ files and Google Photos™ so you can access your Google files from the Document Library."

Integrate essential tools to equip your teams. (e.g., Microsoft Office)

Empower users by giving them access to the tools and resources they need via your intranet.

The Liferay UI tag library makes it easier for developers to implement commonly used UI components, with tags that make your markup consistent, responsive, and accessible.

## Before Getting Started

Before building your first intranet Site with Liferay DXP, ensure your DXP instance is up and running. May want to take time to determine your Site and User Hierarchies. Also gather your organization's digital assets for import.

### Determining Site Hierarchy

Determine the __ .

### Determining User Hierarchy

Determine the user roles and responsibilities you want reflected in your intranet's user hierarchy  categories of user who will use your intranet.

By default, ___.

### Preparing Your Digital Assets

If applicable, prepare your digital assets to be imported into Liferay DXP. 

## Outline for Building an Intranet

Outline of the Intranet creation process (e.g., To build an intranet, create an organization. Create an organization Site. Personalize your Site's appearance. Add and design intranet pages to implement your desired page hierarchy. You can then define user roles and permissions in the organization to achieve the desired user hierarchy. Personalize your intranet's appearance.)

### Setting Up a New Intranet Site

This step covers the creation of an organization Site.
Multiple options for creating Sites. Can create standalone Sites, arrange them in a parent-child relation.
For an intranet, we'll be building an Organization Site to reflect<!--aligns with/conforms to--> your real-world organizational hierarchy.
Create an Organization.
Create Organization Site.
Can add sub-organizations and child sites later, if desired.

### Managing Your Intranet's Users and Roles
<!-- ALT: Adding Intranet Users and Assigning Roles -->

This step covers the general intranet roles you'll be using in your intranet
User Groups and Organizations.
Intranet personas (Specific User profiles).
connecting to active directory. Set up [LDAP]() on the instance level, and [configure import]() of users. <!--mapping fields for attributes and groups to match users between your two systems.-->
Setting up single sign on and authentication

### Adding Digital Assets to Your Intranet

This step covers the the considerations relevant for determining how to import your digital assets to your new Intranet, as well as tagging and categorizing assets to optimize Search and asset visibility.
Question of Scope (e.g., instance, Site)--determines the accessibility of assets within and across your Sites.
This walk-through recommends using Asset Libraries for accessibility of assets across instance, or importing assets to the Parent Site so they're accessible in child Sites.
Integrating tools (.e.g, [Google Drive](), [Microsoft 365]()).

### Personalizing Your Intranet's Appearance

Designing your intranet's appearance.
Building on the default theme base, using Style Books (general, color system, spacing, layout, buttons).
Setting Organization's logo, favicon

### Adding and Designing Your Intranet's Pages

Page Templates.
Master Page Templates for determining headers and footers.
General/Other Page Templates.
Suggest specific Pages to use.

### Further Customization Options

Can develop Intranet Customizations beyond these out-of-the-box features.
e.g., develop a vacation SPA, Liferay JS Toolkit + React, Data Engine API.
