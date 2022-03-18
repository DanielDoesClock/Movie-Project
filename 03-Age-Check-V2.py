"""This code will ask for an age. If it does not meet the criteria, it will
give an appropriate error message and ask again.
This version is changed to be more simple
Made By Daniel Fraser
18/03/22"""


def int_check(text):
    valid = False
    while not valid:
        # Asking for a number and checking if it is valid
        try:
            num_to_check = int(input(text))
            if isinstance(num_to_check, int):
                valid = True
                return num_to_check
        except ValueError:
            print("\nPlease enter an integer (whole number)")


# Main routine
# Check for valid age, 12-110
age = int_check("\nPlease enter age of ticket-holder >> ")
while not 12 <= age <= 110:
    age = int_check("\nPlease enter an age between 12-110 >> ")
print(f"Age = {age}")

