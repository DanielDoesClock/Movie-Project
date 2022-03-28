"""This is V7 of my final project file. I am adding a profit calculator and
yes/no checker
Made By Daniel Fraser
27/03/22"""

# Import statements


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

# ******* Main Routine *******

# Set up dictionaries / lists to hold data

# Ask user if they have used program before
# Tell instructions if necessary

# Loop to get ticket details


# Get name (cant be blank)
TICKET_COST_PRICE = 5
MAX_TICKETS = 5
tickets = MAX_TICKETS
name = ""
ticket_count = 0
profit = 0

while name != "Xxx" and ticket_count != MAX_TICKETS:
    if MAX_TICKETS - ticket_count > 1:
        print(f"\nThere are {tickets} tickets left")

    # Get details
    else:
        print("\n******* THERE IS ONLY 1 TICKET LEFT *******")
    name = blank_check("Please enter ticket-holder's name >> ")
    ticket_count += 1
    tickets -= 1
    if name == "Xxx":
        break
    else:
        MAX_AGE = 110
        MIN_AGE = 12
        age = int_check("Please enter age of ticket-holder >> ")
        if age < MIN_AGE:
            print(f"{name} is young to watch this move.")
            ticket_count -= 1
            tickets += 1
        elif age > MAX_AGE:
            print(f"There is no way {name} could be that old!")
            ticket_count -= 1
            tickets += 1
        else:
            # Calculate ticket price
            ticket_price = calc_ticket_price(age)
            print(f"For {name} the price is ${ticket_price:,.2f}")
            profit += (ticket_price - TICKET_COST_PRICE)

# Calculate total sales and profit
if tickets == 0:
    print("All tickets have been sold")

if name == "Xxx":
    print(f"You have sold {ticket_count - 1} tickets")

print(f"Total profit is ${profit:,.2f}")
# Get age (12-130)

# Loop to ask for snacks

# Calculate snack price

# Ask for payment method (add surcharge if needed)

# Output data to text file
