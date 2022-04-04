"""This is the 7th component in my project. It will ask user if they want a
snack, if they do, it will ask for amount and type. I will keep track of the
inventory to make sure we do not sell more than we have.
Made by Daniel Fraser
31/03/22"""

test_strings = [
    "Popcorn"
    "2 pc"
    "1.50J"
    "40J"
    "12Chips"
    ]

for item in test_strings:
    if item[0].isdigit():
        if item[1].isdigit():
            quantity = int(item[0]+item[1])
            snack = item[2:]
        else:
            quantity = int(item[0])
            snack = item[1:]
    else:
        quantity = 1
        snack = item
    print(f"Quantity: {quantity}")
    print(f"Snack: {snack}")
