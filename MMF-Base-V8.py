"""This is V8 of my final project file. I am adding the 6th and 7th component
which asks for the snack and amount.
Made By Daniel Fraser
04/04/22"""

# Import statements
import re
import pandas


# Functions go here
# Calculates the ticket price based on age
def calc_ticket_price(age):
    child_age = range(12, 16)
    standard_age = range(16, 65)
    child_price = 7.50
    standard_price = 10.50
    retired_price = 6.50

    if age in child_age:
        ticket_price = child_price
    elif age in standard_age:
        ticket_price = standard_price
    else:
        ticket_price = retired_price
    return ticket_price


def blank_check(ask_name):
    while True:
        response = input(ask_name).title()
        if not response:    # Checks if name has at least 1 letter
            print("Please do not leave this blank!")    # Error message if not
        else:
            return response    # Returns name


# Check for valid integer (for age)
def int_check(question):
    number = ""
    while not number:
        # Asking for a number and checking if it is valid
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer (whole number)")


def check_max_tickets(maximum, sold):
    if maximum - sold > 1:
        print(f"There are {maximum - sold} tickets left")
    else:
        print("*****THERE IS ONLY ONE TICKET LEFT! *****")


def check_valid_age(minimum, maximum):
    age = int_check(f"Please enter {name}'s age >> ")
    if age < minimum:
        print(f"{name} is young to watch this move.")
        return None
    else:
        while not age <= MAXIMUM_AGE:
            print(f"There is no way {name} could be that old!")
        return age


# ******* Main Routine *******
# Set up dictionaries / lists to hold data
all_names = []
all_tickets = []
# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

MAXIMUM_AGE = 110
MINIMUM_AGE = 12
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0
# Ask user if they have used program before
# Tell instructions if necessary

# Loop to get ticket details


# Get name (cant be blank)


while name != "Xxx" and ticket_count < MAX_TICKETS:
    check_max_tickets(MAX_TICKETS, ticket_count)

    name = blank_check("Enter ticket holder's name >> ").title()
    if name == "Xxx":
        break
    else:
        age = check_valid_age(MINIMUM_AGE, MAXIMUM_AGE)
        if not age:
            continue
        else:
            ticket_count += 1

    ticket_price = calc_ticket_price(age)
    print(f"For {name}, the price is {ticket_price:,.2f}")
    profit += (ticket_price - TICKET_COST_PRICE)

    all_names.append(name)
    all_tickets.append(ticket_price)

# Calculate total sales and profit
if ticket_count < MAX_TICKETS:
    if ticket_count > 1:
        print(f"\n{ticket_count} tickets have been sold")
    else:
        print("1 ticket has been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available\n")
    else:
        print ("1 ticket is still available\n")
else:
    print("!!!!! ALL TICKETS HAVE BEEN SOLD !!!!!")
    print("*" * 60)

movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)
print(f"Ticket profit is ${profit:,.2f}")
# Get age (12-130)

# Loop to ask for snacks

# Calculate snack price

# Ask for payment method (add surcharge if needed)

# Output data to text file
