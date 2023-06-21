## Gym Management System

Your local Gym needs a system to track memberships. This system should handle memberships, membership types, locker allocation, group classes, professional trainer subscriptions, etc.

Scenarios
Your app should handle the following scenarios:

A person wants to join the gym. They visit the gym and the Gym Admin gets them registered. There are multiple plans to choose from. They subscribe to one of them.
A customer can book lockers in the store room. There are a limited number of lockers.
A customer should be able to subscribe to a professional trainer plan. They can also give ratings to the trainers.
A way to keep track of metrics that will make it easy for each customer to track improvements in their fitness journey. For e.g., weight, calories intake, etc
The Gym Admin should be able to create and edit workout plans (Beginner, Intermediate, and Advanced) and publish these plans on the Gym website portal.
Customers should be able to book group classes (dance fitness, boxing, etc). Customers should get a weekly summary of the classes they attended in the gym via email.
Create a Profile page (custom page) for customers that shows: 
Active Plan
Remaining days in the subscription 
Allocated Trainer (with contact info) Past Plans
   DocTypes
Gym Member
Gym Membership
Gym Trainer
Gym Trainer Subscription Gym Locker Booking Gym Class Booking
Gym Workout Plan
Gym Workout Plan Exercise (Child Table) Gym Settings
These doctypes are only for reference, you should add any additional doctypes that are necessary. Make sure that your system has at least one of each type of doctype:

Standard DocType
 Child DocType 
Submittable DocType 
Single DocType
Roles
Gym Admin
Should be able to do all possible actions
Gym Member
Should be able to book a cardio machine, and subscribe to a trainer plan.
Gym Trainer
Should be able to create a process sheet and track it for all trainees
Reports
A report that shows the fitness journey of a customer. Show tracked weight, calories, etc in a report and also show a chart. The report should have a filter to select a customer.
A report to see which group classes are being booked the most and are the most popular.
Revenue report by month
Other
Write at least 2 tests for at least one doctype. 
You are free to write more tests. 
Write client scripts for at least 2 doctypes.
Write 1 patch to fix old data or set values for a new field in the database.
Override the 404 page from the framework, and create your own version.
If you have an idea that you think should be there in this system instead of the ones suggested here, feel free to implement it.

#### License

MIT
