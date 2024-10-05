<style>
    r { color: Red; }
</style>

# Project Plan

## Project Name: FoodDB

## Group Number: 049

### Team members

| Student No. | Full Name   | GitHub Username | Contribution (sum to 100%) |
|-------------|-------------|-----------------|----------------------------|
| S5384822    | Kane Bebb   | Groogi          | 33.3% or Equal             |
| S5350818    | Nick Bland  | NickBland       | 33.3% or Equal             |
| s5403634    | Cameron Cassar  | Camcassar   | 33.3% or Equal             |

### Brief Description of Contribution

Please Describe what you have accomplished in this group project.

- S5384822, Kane Bebb
  - Accomplishments: In the project plan section, I created the [Project Objectives](#11-project-objectives) and [Project Scope](#13-project-scope) sections. In the software design doc I created the [Problem Background](./Software%20Design%20Document.md#11-problem-background), [System Capabilities/Overview](./Software%20Design%20Document.md#12-system-capabilitiesoverview), [Benefit Analysis](./Software%20Design%20Document.md#13-benefit-analysis), and [Visual Design](./Software%20Design%20Document.md#42-visual-design) sections. I also collaborated with Nick to complete the [Structural Design](./Software%20Design%20Document.md#41-structural-design).
  - <r> For Milestone 2, I worked on the implementation of the search features, including all the filters required to display results. I also worked on updating the User Interface to reflect the requirements of these filters from what Nick had already created.</r>
- s5350818, Nick Bland
  - In the project plan section, I created the [WBS](#2-work-breakdown-structure), [Activity Definitions](#3-activity-definition-estimation), and [Gantt Chart](#4-gantt-chart).
  - In the software design section, I created the [Software Design and System Components](./Software%20Design%20Document.md#3-software-design-and-system-components) as well as collaborating on the [Structural Design](./Software%20Design%20Document.md#41-structural-design) for the project. 
  - <r>For Milestone 2, I created the User interface for most components. I also worked on implementing the food screen and comparison panel to display more in-depth information about foods selected.</r>
- s5403634, Cameron Cassar
  - In the software design section, I created the [Requirements](./Software%20Design%20Document.md#2-requirements), [User Requirements](./Software%20Design%20Document.md#21-user-requirements), [Software Requirements](./Software%20Design%20Document.md#22-software-requirements), [Use Case Diagrams](./Software%20Design%20Document.md#23-use-case-diagram), [Use Cases](./Software%20Design%20Document.md#24-use-cases),
  - In the project plan section, I created the [Project Stakeholders](#12-project-stakeholders).
  - <r>For Milestone 2, I worked on documentation and updates to previously made documentation in Milestone 1.</r>
  
## Table of Contents

- [Project Plan](#project-plan)
  - [1. Project Overview](#1-project-overview)
    - [1.1 Project Objectives](#11-project-objectives)
    - [1.2 Project Stakeholders](#12-project-stakeholders)
    - [1.3 Project Scope](#13-project-scope)
  - [2. Work Breakdown Structure](#2-work-breakdown-structure)
  - [3. Activity Definition Estimation](#3-activity-definition-estimation)
  - [4. Gantt Chart](#4-gantt-chart)

## 1. Project Overview

<!-- Kane -->
### 1.1 Project Objectives  

**'Project Objectives'** refers to the **goals** that we will attempt to achieve during the life-cycle of the project. These **goals** include meeting quality standards and stakeholder satisfaction; paired alongside are **objectives** such as "Intuitive UI design" which speaks a goal of setting and consistently meeting our high quality standards.

<ins>_General Project Objectives/Needs_: </ins>

- Create an innovative and invaluable tool that satisfies the standards set by stakeholders.
- Complete the project with minimal delay and within the pre-planned schedule.
- Create an intuitive UI (user interface) that feels natural and comfortable for users to interact with.
- Adhere to stakeholder specifications and meet expectations of both the stakeholders and our customers/users.
- Maintain the scope of the project throughout it's lifecycle; paying close attention to stay within bounds.
- Create an application that meets the needs of a user base interested in analysing data, specifically food-based data. Such as: Dietitians, Nutritionists, Health-conscious individuals, and Meal Planners.

<ins>_Stakeholder Objectives/Needs_: </ins>

- Create an app that fulfills the required specifications I.E: Input database **&rarr;** manipulate data **&rarr;** output/display data in interesting ways (graphs etc.)
- The app will meet the following stakeholder requirements/specifications (functionally): Food Search, Nutrition Breakdown, Nutrition Range Filter, Nutrition Level Filter, and one extra additional feature chosen by developers (Food Comparison).

<!---->

<!-- Cam -->
### 1.2 Project Stakeholders

Internal Teams:

1. Project Management Team (Cameron Cassar, Nick Bland and Kane Bebb)
    - Role: Responsible for planning, coordinating, and overseeing the project from inception to completion. They ensure the project stays on schedule, within scope, and meets quality standards.
    - Involvement: Defining project goals, timelines, and deliverables; managing resources and addressing any risks or issues that arise during the project.
2. Development Team (Cameron Cassar, Nick Bland and Kane Bebb)
    - Role: Comprising software developers, database administrators, and UI/UX designers, this team is responsible for the actual development and implementation of the tool.
    - Involvement: Writing code, designing the user interface, integrating the Nutritional Food Database, and ensuring the tool's functionality aligns with the project requirements.
3. Documentation Team (Cameron Cassar, Nick Bland and Kane Bebb)
    - Role: Responsible for creating user manuals, help guides, and technical documentation that detail how the tool works.
    - Involvement: Preparing comprehensive documentation that assists end-users and developers in understanding and using the tool effectively.

Potential End-Users:

1. Dietitians
    - Role: Health professionals who provide dietary advice and nutrition plans to individuals and groups.
    - Involvement: Using the tool to analyse and recommend foods based on nutritional content for their patients or clients.
2. Nutritionists
    - Role: Anyone who studies food related subjects to provide advice on how food affects health.
    - Involvement: Using the tool to research, analyse, and present nutritional information in various settings such as clinics, educational institutions, or wellness programs.
3. Health-Conscious Individuals
    - Role: Individuals who are proactive about their health and diet that are seeking to optimize their nutrition for personal wellness.
    - Involvement: Using the tool to track and analyse the nutritional content of foods they eat or plan to eat.
4. Meal Planners
    - Role: Individuals responsible for planning meals this could include personal chefs, parents or anyone managing the dietary needs of a group or family.
    - Involvement: Leveraging the tool to create balanced and nutritionally sound meal plans by filtering and selecting foods based on their nutritional content.
5. Healthcare Providers
    - Role: Medical professionals such as doctors or nurses who might use the tool to provide dietary recommendations to patients.
    - Involvement: Recommending or using the tool as part of a plan for patients needing nutritional guidance.
6. Educational purposes
    - Role: Schools, colleges, or universities where the tool could be used as a teaching tool in courses related to nutrition and health.
    - Involvement: Instructors and students could use the tool to explore and analyse nutritional data as part of their curriculum.

Additional Stakeholders:

1. Regulatory Agencys
    - Role: Organizations that set standards and regulations for nutritional information and public health.
    - Involvement: May provide guidelines that the tool needs to adhere to in terms of data accuracy and presentation.
2. Investors/Sponsors
    - Role: Individuals or entities funding the project.
    - Involvement: Providing financial resources and expecting a return on investment through the successful deployment and adoption of the tool.
3. Marketing and Sales Team (Cameron Cassar, Nick Bland and Kane Bebb)
    - Role: Responsible for promoting and selling the tool once it is developed.
    - Involvement: Developing strategies to reach potential users and ensuring that the tool’s benefits are clearly communicated to the target market.

<!-- Kane -->
### 1.3 Project Scope

#### Scope Overview

The **'Scope'** of the project refers to the **features** and **goals** that we will include and feel is reasonable to complete within the **projects time-frame**. By outlining these **tasks** and **goals** ahead of time we enable ourselves to stay on track and focus on core features and set clear expectations for stakeholders.  

#### Scope Inclusions

**What are Inclusions?**

Inclusions encompass the tasks of the project that are included in the **scope** and are key aspects of the project that are to be completed within the agreed upon **time-frame**.

- Data Input - <r>The application should be able to accept data from a csv file
- Data manipulation - <r> The application should be able to manipulate the data to a more human-readable format
- Data output / display - <r> The application should be able to display the data in interesting ways (graphs etc.)
- Food search - <r> The user should be able to search for foods using keywords
- Nutrition Breakdown - <r> The user should be able to see a breakdown of the nutritional information of a food
- Nutrition Range Filter - <r> The user should be able to filter foods based on a range of nutritional values (e.g. calories: 50-100)
- Nutrition Level Filter - <r> The user should be able to filter foods based on a nutritional level (e.g. high protein)
- Food Comparison - <r> The user should be able to compare the nutritional information of two foods

##### Scope Exclusions

**What are Exclusions?**

Exclusions encompass possible tasks and goals of the project that are **not** main **objectives/tasks** to be completed within the projects **time-frame**.

- Data share feature - <r> The application will not have a feature to share data with other users
- Online cloud data storage/hosting - <r> The application will not have a feature to store data online
- Customisable UI - <r> The application will not have a feature to customise the UI
- Persistent User account - <r> The application will not have a feature to store user data, or save associated information
- Persistent data storage - <r> The application will not have a feature to store data between sessions

<!-- Nick -->
## 2. Work Breakdown Structure

The following is a Work Breakdown Structure diagram, showcasing the five different process groups of which the FoodDB Project has been planned around. Although the timings and details have not yet been established, this diagram serves to show the overall structure and flow of how the FoodDB Project will be developed.

![Hierarchical WBS Diagram](./WBS.png)

<!-- Nick -->
## 3. Activity Definition Estimation

The following table defines the activities planned out in the [WBS](#2-work-breakdown-structure). The table will serve to show the estimated duration, and the team members to be assigned for each activities.

| **Activity #No** | **Activity Name** | **Brief Description** | **Duration** | **Responsible Team Members** |
|:-:|---|---|---|---|
| **1.0** | Initiation Process Group |  |  |  |
| **1.1** | Draw Project Charter | Define the high-level objectives that the FoodDB project aims to solve. | 1 | Nick, Cam, & Kane |
| **1.1.1** | Problem Background | Define the issues at present. | 1 | Kane |
| **1.1.2** | High-level System Capabilities | Define what the FoodDB project should do | 1 | Kane |
| **1.1.3** | Benefit Analysis | Analyse the benefits that implementing the project will create. | 1 | Kane |
| **1.2** | Identify Stakeholders | Identifty the parties to be involved both during development and implementation of the FoodDB project. | 1 | Kane & Cam |
| **2.0** | Planing Process Group |  |  |  |
| **2.1** | Gather Requirements | Collect and define what each stakeholder requires the project to accomplish | 3 | Cam |
| **2.2** | Establish Scope | Clearly define what the project should and should not do during development. | 2 | Cam |
| **2.2.1** | Functional Requirements | The tangible requirements to be developed off of. | 5 |  |
| **2.2.1.1** | User Requirements | What stakeholders require from the project. | 1 | Cam |
| **2.2.1.2** | Software Requirements | Decide and plan what the software itself will accomplish, with regards to the user requirements, and use cases. | 2 | Cam |
| **2.2.1.3** | Use Cases and Use Case Diagrams | Defining the flow of interaction between the users and the software. | 1 | Cam |
| **2.2.1.4** | Software Design Choices | Other design choices such as frameworks, languages, etc. to be used in developing the software. | 1 | Cam |
| **2.2.2** | Non-Functional Requirements | These are the non-tangible requirements to be developed off of. | 3 |  |
| **2.2.2.1** | Structural Design | Designing the layout of the codebase and data structures the software will use. | 1 | Nick & Kane |
| **2.2.2.2** | Visual Design Choices | Designing elements of the GUI, including the 'look and feel' of the application. | 2 | Kane |
| **2.3** | Create Project Management Plan | Create a plan to show the overall sequence of activities, and resources each activity requires. | 5 | Nick |
| **2.3.1** | Define and Sequence Activities | Define what activities need to take place, and the sequence these activities need to be undertaken. | 2 | Nick |
| **2.3.2** | Estimate Activity Resources | This table to define time-estimates, and also create estimates on costs and any other resources (computers, etc.) that are required. | 1 | Nick |
| **2.3.3** | Create WBS | Work Breakdown Structure (WBS): To break down the large project in to smaller pieces and organisational processes. This table is one part of that process. | 1 | Nick |
| **2.3.4** | Create Gantt Chart | Organise the WBS and activity resource definitions into a flowchart, which can be updated to show progress on development. | 1 | Nick |
| **3.0** | Executing Process Group |  |  |  |
| **3.1** | Assign Work Based Off Plan | Designate work based off the WBS to group members | 1 | Nick, Cam, & Kane |
| **3.2** | Develop Project | Develop the application in line with the plan set out. | 7 | Nick, Cam, & Kane |
| **3.2.1** | Test Project During Development | Ensure that tests are conducted during development to prevent issues early on. | 2 | Nick, Cam, & Kane |
| **3.3** | Conduct Meetings | Ensure developers meet with stakeholders and project managers to frequently document progress, and ensure the project is in line with the planned vision. | 2 | Nick, Cam, & Kane |
| **3.4** | Monitor Risks | Monitor and implement risk management strategies. | 1 | Nick, Cam, & Kane |
| **3.5** | Frequently Update Plan Based Off Events and Progress | Update the plan and Gantt chart to show progress of development | 1 | Nick, Cam, & Kane |
| **4.0** | Monitoring and Controlling Process Group |  |  |  |
| **4.1** | Monitor Development of Project | Identify development issues, performance issues, and variances to the vision and take corrective actions. | 3 | Nick, Cam, & Kane |
| **4.1.1** | Control Scope | Ensure that the scope of the project is kept in check during development. | 1 | Nick, Cam, & Kane |
| **4.1.2** | Control Quality | Ensure that the quality of the project is kept in check during development. | 1 | Nick, Cam, & Kane |
| **4.1.3** | Control Resources | Ensure that resources are being utilised correctly, and kept in check during development. | 1 | Nick, Cam, & Kane |
| **4.2** | Assess Risks Over Time | Assess risks during development, implement responses. | 2 | Nick, Cam, & Kane |
| **4.3** | Update Plans | Frequently update the plans as development occurs, including risks, communication events, etc. to document progress. | 2 | Nick, Cam, & Kane |
| **4.4** | Report Progress to Relevant Stakeholders | Report on the developmental progress of the project to stakeholders, and update the plans from these meetings - issues, removal of features, etc. | 2 | Nick, Cam, & Kane |
| **5.0** | Closing Process Group |  |  |  |
| **5.1** | Review Performance | Review the performance of each team member, and the work that they put in to the project. | 1 | Nick, Cam, & Kane |
| **5.2** | Create Final Report | Generate a final report based off the development process, and how the project aligns with initial plan and vision of the stakeholders. | 2 | Nick, Cam, & Kane |

<!-- Nick -->
## 4. Gantt Chart

The Gantt Chart is used to show current developmental progress on the project. It uses the planned activities from [Section 3](#3-activity-definition-estimation), which in turn were developed in [Section 2](#2-work-breakdown-structure).

![Gantt Chart](./Gantt_chart.png)
<r>Updated Gantt Chart to reflex activities that have been completed in both Milestone 1 and Milestone 2. Importantly, the closing process was not a part of this assessment</r>
