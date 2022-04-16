import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class ParkingGarage():
    def __init__(self):
        self.tickets_available = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10"]
        self.parking_spaces_open = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.current_ticket_paid = {}

    def take_ticket(self):
        clear_screen()
        ticket_id = self.tickets_available.pop(0)
        space_taken = self.parking_spaces_open.pop(0)
        self.current_ticket_paid[ticket_id] = [False, space_taken]
        print(f"Your ticket ID is {ticket_id}. Park in space {space_taken}. Be sure to write down your ticket ID and parking space.")

    def pay_for_parking(self):
        self.user_ticket = input("\nPlease enter your ticket ID to process payment: ").upper().strip()
        if self.user_ticket.upper().strip() in self.current_ticket_paid.keys():
            while self.current_ticket_paid[self.user_ticket][0] == False:
                self.user_payment = int(input("\nYou owe $5. Please enter your payment [enter amount owed WITHOUT dollar sign]. "))
                if self.user_payment == 5:
                    self.current_ticket_paid[self.user_ticket][0] = True
                    print("\nThank you for your payment. You have 15 minutes to leave.")
                elif self.user_payment < 5:
                    self.remaining_payment = int(input(f"\nYou still owe ${str(5 - self.user_payment)}. Please enter your remaining payment [enter amount owed WITHOUT dollar sign]. "))
                    if self.remaining_payment == (5 - self.user_payment):
                        self.current_ticket_paid[self.user_ticket][0] = True
                        print("\nThank you for your payment. You have 15 minutes to leave.")
                    else: 
                        print("\nPlease see a parking attendant.")
                        break
                elif self.user_payment > 5:
                    self.current_ticket_paid[self.user_ticket][0] = True
                    print(f"\nThank you for your payment. Please take your change totaling ${str(self.user_payment - 5)}. You have 15 minutes to leave.")
                else:
                    print("\nInvalid payment method. Please try again.")
        else:
            print("\nInvalid ticket entry. Please enter a valid ticket ID.")

    def leave_garage(self):
        clear_screen()
        self.user_ticket = input("Please enter your PAID ticket ID to leave: ").upper().strip()
        if self.current_ticket_paid[self.user_ticket][0] == True:
                print("\nHave a nice day! Drive safely!")
                self.tickets_available.insert(0, self.user_ticket)
                self.parking_spaces_open.insert(0, self.current_ticket_paid[self.user_ticket][1])
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