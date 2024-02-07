# GYM MANAGMENT SYSTEM DATABASE PROJECT

## Project Description:
The Gym Management System appears as a crucial tool designed exclusively for gyms in today's quickly changing digital world. This system overcomes traditional record-keeping since it was created to handle activities, memberships, and member interactions effectively. It includes automation, analytics, increased member engagement, and quick access to member, trainer, and equipment data. This technology will have a significant influence on how fitness facilities run, making it the management system of the future for gyms.

What it does: It provides an integrated approach to gym administration, from monitoring scheduled maintenance for equipment to allowing participation by members.

Technologies: Built by using Visual Studio Code, Quarto(qmd -> html), Mermaid Editor, Graphviz editor, Lucid chart, Zoom, Kaltura.

Challenges and Future Plans: Creating a Gantt chart for milestones and scheduling meetings was one of the main difficulties encountered. Future revisions plan to include integrations with virtual exercise classes, and more.

## How to install and run the project
## Installation Steps:
### 1. Pre-requisites:
Ensure all the required software and libraries are installed.
### 2. Download Visual Studio Code:
If you haven't already, download Visual Studio Code and install it.
### 3. Install Quarto Extension in VS Code:
Open Visual Studio Code.
Go to Extensions or press Ctrl+Shift+X.
Search for "Quarto" and install the appropriate extension.
### 4. Clone the Repository:
Clone the Gym Management System repository to your local machine.
### 5. Setup:
Navigate to the directory where you've cloned the repository.

## Viewing the Report:
Using a Web Browser:
* Navigate to the directory where you've cloned the repository on your local desktop.
* Double-click on the report.html file. This will open the report in your default web browser.

Using Visual Studio Code (with Quarto Extension):
* Open the Visual Studio Code.
* Navigate to the directory where you've cloned the repository.
* Open the report.qmd file.
* Click on the "Preview HTML" button (usually located at the top right corner of the VS Code interface) to view the report.

## How to Use the Project
### Employees:
* Login with your credentials.
* Access your timesheet, check assigned sessions, report equipment maintenance needs.

### Members/Customers:
* Sign up or Login.
* Browse and book available sessions, view payment history, access promotions.

### Authority/Owners:
* Admin access is provided to control the entirety of the system.
* Generate payment sheet, manage staff, control finances, and oversee gym activities.

### Suppliers:
* Check due dates, update product availability.

### API Definition:
Base URL: https://github.com/cmsc-vcu/cmsc508-fa2023-prj-gymmanagementsystem

### Gym Information:
● Endpoint: /gyms
● Method: GET
● Description: Retrieve a list of all gyms.
● Response: JSON array of gym objects.
● Endpoint: /gyms/{gymID}
● Method: GET
● Description: Retrieve details of a specific gym.

### Employee Information:
● Endpoint: /employees
● Method: GET
● Description: Retrieve a list of all employees.
● Response: JSON array of employee objects.
● Endpoint: /employees/{employeeID}
● Method: GET
● Description: Retrieve details of a specific employee.

### Member Information:
● Endpoint: /members
● Method: GET
● Description: Retrieve a list of all members.
● Response: JSON array of member objects.
● Endpoint: /members/{memberID}
● Method: GET
● Description: Retrieve details of a specific member.

### Session Information:
● Endpoint: /sessions
● Method: GET
● Description: Retrieve a list of all sessions.
● Response: JSON array of session objects.
● Endpoint: /sessions/{sessionID}
● Method: GET
● Description: Retrieve details of a specific session.

### Payment Information:
● Endpoint: /payments
● Method: GET

● Description: Retrieve a list of all payments.
● Response: JSON array of payment objects.
● Endpoint: /payments/{paymentID}
● Method: GET
● Description: Retrieve details of a specific payment.

### Owner Information:
● Endpoint: /owners
● Method: GET
● Description: Retrieve a list of all owners.
● Response: JSON array of owner objects.
● Endpoint: /owners/{ownerID}
● Method: GET
● Description: Retrieve details of a specific owner.

### Supplier Information:
● Endpoint: /suppliers
● Method: GET
● Description: Retrieve a list of all suppliers.
● Response: JSON array of supplier objects.
● Endpoint: /suppliers/{supplierID}
● Method: GET

● Description: Retrieve details of a specific supplier.

### Equipment Information:
● Endpoint: /equipments
● Method: GET
● Description: Retrieve a list of all equipment.
● Response: JSON array of equipment objects.
● Endpoint: /equipments/{equipmentID}
● Method: GET
● Description: Retrieve details of specific equipment.


### Future Consideration:-

Authentication and Authorization:
Implement a secure authentication mechanism, such as OAuth or JWT, to protect the API
endpoints.
Set up role-based access control (RBAC) to manage permissions for different user roles (admin,
employee, member).

Data Validation and Error Handling:
Enhance input validation to ensure that the API handles invalid requests gracefully.

Implement a robust error-handling mechanism and provide meaningful error messages to users.

Caching:
Integrate caching mechanisms to reduce the load on the database, especially for frequently
accessed or static data.

Testing:
Provide test coverage by implementing unit tests, integration tests, and end-to-end tests.

### Reflections:-

I've found the overall journey to be both challenging and rewarding. We successfully
implemented key features and established a functional API, meeting several milestones.
However, challenges such as working together with the same code and connecting to the sql
database and working on the code others have implemented was a little challenging. required
adjustments to the initial timeline. Feedback from each other helped us solve almost everything.
One notable reflection is the importance of effective collaboration. Our team's ability to
communicate and adapt to unforeseen circumstances proved essential.
In conclusion, this group project has been a valuable experience, reinforcing the significance of
effective teamwork, adaptability, and continuous improvement. I am grateful for the opportunity
to work with such a dedicated team, and I look forward to applying these lessons in future
collaborative endeavors.
## Credits
This project is a result of collaborative efforts by:
* Emil Baez - Database Designer - https://github.com/EmilSalazar
* Harita Agarwal - Database Designer - https://github.com/hpa179
* Anisha Vijaykumar - Database Designer - https://github.com/Anisha2608
