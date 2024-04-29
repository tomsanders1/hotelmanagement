# Hotel Management

## Scenario
You have been hired by the Artemis Hotel to create a hotel management system.  The system will be used by the hotel for managing customers bookings and their details.
The program system must be capable of providing the following information:
Hotel Booking, Provide you with Hotel Rooms Info, Room Service, Billing and Record-Keeping.

## Methods
Analyse the detailed requirements using suitable methods, i.e. analysis by decomposition of requirements (breaking down the tasks into manageable parts). 
Elements and functions table. 
Algorithms / pseudocode or flow diagram .
Show the iterative development of the individual solutions with suitable testing throughout the process. 
Test the final product with an appropriate test table and evaluate your solution against the detailed requirements you identified in the analysis.
## System Requirements
Main Menu options.
Personal details: including type of room and service booked.
Hotel room details: Type of room, number of persons, number of beds, what is included in the room i.e. on-suite, couch, TV etc.
Bookings.
Billing and payments.
Record keeping guest records, guests and allocated rooms, vacancy of rooms, room services
Database CSV document for customer / guests’ details.
Test table to show that the system works.
## Example of Functions Required:
Home()- Function to display the project’s main screen i.e. the home page of the project or you can say the main menu for selecting the desired operation to perform. 
Date(str)- Function to validate date entered by the user/customer. 
Booking()- Function for booking room in hotel by entering user/customer details. 
Room_Info()- Function to provide users/customers with hotel rooms information(i.e. about room amenities). 
Restaurant()- Function for room service which provides user/customer with the restaurant’s menu card to order food at the room. 
Payment()- Function for payment of hotel room and restaurant bill generation at the time of check-out. 
Record()- Function for keeping records of customers stayed in the hotel. 

## Client Requirements
Login Page,
Create booking,
Hotel Room Info,
Billing Payments,
Record Keeping,
Room service.

## Installation
``import csv``
If csv is not found:
``pip install csv``
## Task Table
| Requirement ID  | Description |
| ------------- | ------------- |
| 1  | Username and password stored.  |
| 1  | Checkuser details when entered.  |
| 2  | Check if any rooms are available.  |
| 2  | Create a booking.  |
| 3  | Check the number of rooms.  |
| 3  | Check how many rooms are taken.  |
| 3  | Check how many people per room.  |
| 3  | Check facilities per room.  |
| 3  | Get price of room.  |
| 4  | Calculate price by multiplying the price of the room * days.  |
| 4  | Make them pay for the room.  |
| 4  | Remove them from the room.  |
| 5  | Keep records of everyone who has booked in.  |
| 6  | Keep a record of room service and charge them when they are done with their room.  |
