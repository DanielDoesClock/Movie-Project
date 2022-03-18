# Import statements

# Functions go here
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
name = ""
count = 0
MAX_TICKETS = 5
seats = MAX_TICKETS

while name != "Xxx" and count != MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nThere are {seats} seats left")

    # Get details
    else:
        print("\n******* THERE IS ONLY 1 SEAT LEFT *******")
    name = blank_check("What is your name? >> ")
    count += 1
    seats -= 1
    if name == "Xxx":
        break
    else:
        MAX_AGE = 110
        MIN_AGE = 12
        age = int_check("\nPlease enter age of ticket-holder >> ")
        if age < MIN_AGE:
            print("You are too young to watch this move.")
            count -= 1
            seats += 1
        elif age > MAX_AGE:
            print("There is no way you are that old!")
            count -= 1
            seats += 1


if seats == 0:
    print("All tickets have been sold")

if name == "Xxx":
    print(f"You have sold {count - 1} tickets")
# Get age (12-130)

# Calculate ticket price


# Loop to ask for snacks

# Calculate snack price

# Ask for payment method (add surcharge if needed)

# Calculate total sales and profit

# Output data to text file
