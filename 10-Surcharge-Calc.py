"""This is my 10th component for the MMF. This will ask the user if they want
to use cash or credit to pay, and add a surcharge if needed.
Created by Daniel Fraser
05/04/22"""


def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


SURCHARGE_RATE = 0.05
name = input("What is your name? >> ").title()
while name != "X":
    surcharge = 0
    sub_total = float(input("Sub-total: $"))
    ask_payment_method = input("How would you like to pay? >> ").lower()
    valid_payment_method = [["credit card", "card", "credit", "cc", "cr", "1"],
                            ["eftpos", "eft", "pos", "ep", "e", "2"],
                            ["cash", "ca", "money", "notes", "coins", "c", "3"]]
    payment_method = get_choice(ask_payment_method, valid_payment_method)
    if not payment_method:
        name = input("What is your name? >> ").title()
        continue

    elif payment_method == "Credit Card":
        surcharge = (sub_total * SURCHARGE_RATE)

    total_payable = sub_total + surcharge

    print(f"{name} | Subtotal: ${sub_total:,.2f} | Surcharge: ${surcharge:,.2f}"
          f" | The total payable is ${total_payable:,.2f}")
    name = input("What is your name? >> ").title()
