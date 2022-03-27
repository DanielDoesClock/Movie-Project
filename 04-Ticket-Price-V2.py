"""This is the 2nd iteration 4th component of my project. I have removed the
redundant line talking about retired age, as this is not used because we use
an 'else' command.
Made by Daniel Fraser
26/03/22"""


def ticket_price(age):
    CHILD_AGE = range(12, 16)
    STANDARD_AGE = range(16, 65)
    CHILD_PRICE = 7.50
    STANDARD_PRICE = 10.50
    RETIRED_PRICE = 6.50

    if age in CHILD_AGE:
        ticket_price = CHILD_PRICE
    elif age in STANDARD_AGE:
        ticket_price = STANDARD_PRICE
    else:
        ticket_price = RETIRED_PRICE
    return(ticket_price)


# Main Routine
# Temp inputs for component testing
name = input("Name >> ")
age = int(input("Age >> "))

print(f"The price of your ticket is ${ticket_price(age):,.2f} \nHope you "
      f"enjoy the movie!")
