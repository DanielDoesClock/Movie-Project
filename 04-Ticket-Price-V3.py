"""This is the 3rd iteration of my 4th component of my project. I have removed
the constants because there should not be any in a function.
Made by Daniel Fraser
26/03/22"""


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


# Main Routine
# Temp inputs for component testing
name = input("Name >> ")
age = int(input("Age >> "))

print(f"The price of your ticket is ${calc_ticket_price(age):,.2f} \nHope you "
      f"enjoy the movie!")
