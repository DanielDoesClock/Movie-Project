"""This code will ask for an age. If it does not meet the criteria, it will
give an appropriate error message and ask again.
This version is changed to be more simple than the more simpler one
Made By Daniel Fraser
18/03/22"""


def int_check(question):
    number = ""
    while not number:
        # Asking for a number and checking if it is valid
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer (whole number)")


# Main routine
# Check for valid age, 12-110
AGE_RANGE = range(12, 111)    # Includes numbers 12-110
age = int_check("\nPlease enter age of ticket-holder >> ")
while age not in AGE_RANGE:    # Age must be 12-110
    age = int_check("\nPlease enter an age between 12-110 >> ")
print(f"Age = {age}")
