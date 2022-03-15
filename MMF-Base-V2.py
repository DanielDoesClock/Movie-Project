# Import statements

# Functions go here
def blank_check(ask_name):
    while True:
        response = input(ask_name)
        if not response.isalpha():    # Checks if name has at least 1 letter
            print("Please do not leave this blank!")    # Error message if not
        else:
            return response    # Returns name


# ******* Main Routine *******

# Set up dictionaries / lists to hold data

# Ask user if they have used program before
# Tell instructions if necessary

# Loop to get ticket details

    # Get name (cant be blank)
    name = blank_check("What is your name? >> ")
    # Get age (12-130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (add surcharge if needed)

# Calculate total sales and profit

# Output data to text file
