import os
from datetime import datetime, timedelta
from math import ceil

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class ParkingGarage():
    PARKING_RATE = 2

    def __init__(self):
        self.tickets_available = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10"]
        self.parking_spaces_open = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.current_ticket_paid = {}

    def take_ticket(self):
        clear_screen()
        if self.tickets_available == []:
            print("Sorry, we're full. Please wait for a ticket and space to become available.")
        else:
            ticket_id = self.tickets_available.pop(0)
            space_taken = self.parking_spaces_open.pop(0)
            self.enter = datetime.now()
            self.current_ticket_paid[ticket_id] = {
                "paid?": False, 
                "parking_space": space_taken,
                "entered_at": self.enter,
                }
            print(f"Your ticket ID is {ticket_id}. Park in space {space_taken}. Be sure to write down your ticket ID and parking space.")

    def pay_for_parking(self):
        self.user_ticket = input("\nPlease enter your ticket ID to process payment: ").upper().strip()
        exit = datetime.now()
        parked_total = (exit - self.enter).total_seconds()
        amt_owed = ParkingGarage.PARKING_RATE * ceil(parked_total / 3600)
        if self.user_ticket.upper().strip() in self.current_ticket_paid.keys():
            while self.current_ticket_paid[self.user_ticket]["paid?"] == False:
                self.user_payment = int(input(f"\nYou owe ${str(amt_owed)}. Please enter your payment [enter amount owed WITHOUT dollar sign]. "))
                if self.user_payment == amt_owed:
                    self.current_ticket_paid[self.user_ticket]["paid?"] = True
                    print("\nThank you for your payment. You have 15 minutes to leave.")
                elif self.user_payment < amt_owed:
                    self.remaining_payment = int(input(f"\nYou still owe ${str(amt_owed - self.user_payment)}. Please enter your remaining payment [enter amount owed WITHOUT dollar sign]. "))
                    if self.remaining_payment == amt_owed - self.user_payment:
                        self.current_ticket_paid[self.user_ticket]["paid?"] = True
                        print("\nThank you for your payment. You have 15 minutes to leave.")
                    else: 
                        print("\nPlease see a parking attendant.")
                        break
                elif self.user_payment > amt_owed:
                    self.current_ticket_paid[self.user_ticket]["paid?"] = True
                    print(f"\nThank you for your payment. Please take your change totaling ${str(self.user_payment - amt_owed)}. You have 15 minutes to leave.")
                else:
                    print("\nInvalid payment method. Please try again.")
        else:
            print("\nInvalid ticket entry. Please enter a valid ticket ID.")

    def leave_garage(self):
        clear_screen()
        self.user_ticket = input("Please enter your PAID ticket ID to leave: ").upper().strip()
        if self.current_ticket_paid[self.user_ticket]["paid?"] == True:
                print("\nHave a nice day! Drive safely!")
                self.tickets_available.insert(0, self.user_ticket)
                self.parking_spaces_open.insert(0, self.current_ticket_paid[self.user_ticket]["parking_space"])
                del self.current_ticket_paid[self.user_ticket]
        else:
            print("\nPlease pay your ticket before leaving. Once paid, you may try leaving again.")
            self.pay_for_parking()

    def show_available(self):
        clear_screen()
        print("\nThe available tickets are:")
        print(*self.tickets_available, sep = ", ")
        print("\nThe available parking spaces are:")
        print(*self.parking_spaces_open, sep = ", ")

class UI(ParkingGarage):
    def __init__(self):
        super().__init__()

    def user_interface():
        new_garage = ParkingGarage()
        clear_screen()
        print("Welcome to Patrick\'s Premier Parking!")
        while True:
            action = input("\nPlease select one of the following options: \n- Take a ticket to park ['ticket']\n- Pay your ticket prior to leaving ['pay']\n- Leave the garage after paying ['leave']\n- Show available tickets & spaces['show']\n- Quit ['quit']\n\nYour selection: ")
            if action.lower().strip() == "quit":
                break
            elif action.lower().strip() == "ticket":
                new_garage.take_ticket()
            elif action.lower().strip() == "pay":
                new_garage.pay_for_parking()
            elif action.lower().strip() == "leave":
                new_garage.leave_garage()
            elif action.lower().strip() == "show":
                new_garage.show_available()
            else:
                print("\nInvalid entry. Please select a valid option.")

def main():
    UI.user_interface()

if __name__ == "__main__":
    main()