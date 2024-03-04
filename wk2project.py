class ParkingGarage:
    # Constructor
    def __init__(self):
        self.available_Parking = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.available_Tickets = ['11', '12', '13', '14', '15', '16', '17', '18', '19']

    # Take Ticket
    def take_ticket(self):
        # Decrease the amount of tickets available by 1
        ticket_number = input("Enter your ticket number: ")
        parking_spot = input("Enter your parking spot number: ")

        if ticket_number in self.available_Tickets:
            self.available_Tickets.remove(ticket_number)
            self.available_Parking.remove(parking_spot)
            print(f"{ticket_number} has parked in {parking_spot}.")
        else:
            print(f"Sorry, parking spot {parking_spot} is not available.")

    # Pay for Parking
    def pay_for_parking(self, ticket_number):
        if ticket_number in self.available_Tickets:
            cost = 10
            ticket_paid = int(input("Enter the amount paid: "))
            if ticket_paid >= cost:
                self.available_Tickets.append(ticket_number)
                print(f"{ticket_number} has been paid. You have 15 minutes to leave.")
            else:
                print("Payment not accepted. Please try again.")
        else:
            print(f"{ticket_number} is not found.")

    # Leave Garage
    def leave_garage(self, ticket_number):
        if ticket_number in self.available_Tickets:
            print("Thank you, have a nice day!")
            self.available_Tickets.remove(ticket_number)
            self.available_Parking.append(f"parking {ticket_number[-1]}")  # Assuming ticket_number and parking_spot have a similar naming convention
        else:
            print("Please pay for your parking before leaving.")

# Testing the class
if __name__ == '__main__':
    garage = ParkingGarage()
    garage.take_ticket()

    ticket_number = ("enter your ticket number to pay:")
    garage.pay_for_parking(ticket_number)
    print ("Thanks for your Payment")
    