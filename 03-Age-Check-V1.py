"""This code will ask for an age. If it does not meet the criteria, it will
give an appropriate error message and ask again.
Made By Daniel Fraser
18/03/22"""


def int_check(question, min_age, max_age):
    error = f"\nPlease enter an age between {min_age}-{max_age}"
    valid = False
    while not valid:
        # Asking for a number and checking if it is valid
        try:
            num_to_check = int(input(question))
            if min_age <= num_to_check <= max_age:
                return num_to_check
            else:
                print(error)
        except ValueError:
            print("\nPlease enter an integer (whole number)")


# Main routine
# Check for valid age, 12-110
age = int_check("\nPlease enter age of ticket-holder >> ", 12, 110)
print(f"Age = {age}")

