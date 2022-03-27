"""This is the 4th iteration of my 4th component of my project. I have added a
profit calculator
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
TICKET_COST_PRICE = 5.00
profit = 0
name = input("Name >> ")
age = int(input("Age >> "))
ticket_price = calc_ticket_price(age)
profit += (ticket_price - TICKET_COST_PRICE)
print(f"The price of your ticket is ${calc_ticket_price(age):,.2f} \nHope you "
      f"enjoy the movie!")
print(f"The profit for this sale is ${profit:,.2f}")
