import csv

class HotelManagementSystem:
    def __init__(self):
        self.customers = []
        self.rooms = []
        self.bookings = []
    
    def load_data(self):
        with open('customer_details.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.customers.append(row)
                
    def save_data(self):
        with open('customer_details.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for customer in self.customers:
                writer.writerow(customer)
                
    def display_main_menu(self):
        print("Main Menu:")
        print("1. Personal details")
        print("2. Hotel room details")
        print("3. Bookings")
        print("4. Billing and payments")
        print("5. Record keeping")
        print("6. Exit")
    
    def add_customer(self, customer_info):
        self.customers.append(customer_info)
    
    def add_room(self, room_info):
        self.rooms.append(room_info)
    
    def make_booking(self, booking_info):
        self.bookings.append(booking_info)
    
    def display_customers(self):
        for customer in self.customers:
            print(customer)
    
    def display_rooms(self):
        for room in self.rooms:
            print(room)
    
    def display_bookings(self):
        for booking in self.bookings:
            print(booking)
    
    def run(self):
        self.load_data()
        while True:
            self.display_main_menu()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                customer_info = input("Enter customer details (name, email, phone number, etc.): ")
                self.add_customer(customer_info)
            elif choice == 2:
                room_info = input("Enter room details (type, number of persons, number of beds, etc.): ")
                self.add_room(room_info)
            elif choice == 3:
                booking_info = input("Enter booking details (customer name, room type, dates, etc.): ")
                self.make_booking(booking_info)
            elif choice == 4:
                # Implement billing and payment functionality
                pass
            elif choice == 5:
                print("Customer details:")
                self.display_customers()
                print("Room details:")
                self.display_rooms()
                print("Booking details:")
                self.display_bookings()
            elif choice == 6:
                self.save_data()
                break
            else:
                print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    system = HotelManagementSystem()
    system.run()
