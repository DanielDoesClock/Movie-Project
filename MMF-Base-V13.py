"""This is V13 of my final project file. I am getting some feedback from and
end user and implementing that feedback into the code.
Made By Daniel Fraser
10/04/22"""

# Import statements
import re
import pandas


# Functions go here
def split_order(choice):
    number_regex = "^[1-9]"

    if re.match(number_regex, choice):
        quantity_required = int(choice[0])
        snack_name = choice[1:]

    else:
        quantity_required = 1
        snack_name = choice

    snack_name = snack_name.strip()
    return quantity_required, snack_name


def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


def collate_order():
    valid_snacks = [["popcorn", "p", "corn", "(1"], ["m&ms", "mms", "m", "(2"],
                    ["pita chips", "chips", "pc", "pita", "c", "(3"],
                    ["water", "w", "(4"], ["orange juice", "oj", "(5"],
                    ["x", "exit", "(6"]]
    valid_yes_no = [["y", "yes"], ["n", "no"]]
    snack_order = []
    max_snacks = 4
    getting_snacks = True
    while getting_snacks:
        snacks_required = ""
        while snacks_required != "N" and snacks_required != "Y":
            check_snacks = input("Do you want snacks? (Y/N) >> ").lower()
            snacks_required = get_choice(check_snacks, valid_yes_no)
        if snacks_required == "N":
            getting_snacks = False
            break
        else:
            option = ""
            while option != "X":
                snack = input("Please choose a snack 'x' to exit >> ").lower()
                snack = split_order(snack)
                quantity = snack[0]
                if quantity > max_snacks:
                    snack = None
                    print("Sorry, the maximum number of snacks is 4")
                else:
                    snack = snack[1]
                    option = get_choice(snack, valid_snacks)
                    if option == "X":
                        getting_snacks = False
                    elif option is not None:
                        snack_order.append([quantity, option])
    return snack_order


# Calculates the ticket price based on age
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


def check_max_tickets(maximum, sold):
    if maximum - sold > 1:
        print(f"There are {maximum - sold} tickets left")
    else:
        print("*****THERE IS ONLY ONE TICKET LEFT! *****")


def check_valid_age(minimum, maximum):
    age = int_check(f"Please enter {name}'s age >> ")
    if age < minimum:
        print(f"{name} is young to watch this move.")
        return None
    else:
        while not age <= MAXIMUM_AGE:
            print(f"There is no way {name} could be that old!")
        return age


def check_valid_payment_method():
    ask_payment_method = input("How would you like to pay? >> ").lower()
    valid_payment_method = [["credit card", "card", "credit", "cc", "cr", "1"],
                            ["eftpos", "eft", "pos", "ep", "e", "2"],
                            ["cash", "ca", "money", "notes", "coins", "c", "3"]]
    payment_method = get_choice(ask_payment_method, valid_payment_method)
    return payment_method


# ******* Main Routine *******
# Set up dictionaries / lists to hold data
surcharge_mult_list = []
summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Water", "Orange Juice",
                    "Snack Profit", "Ticket Profit", "Total Profit"]
all_names = []
all_tickets = []

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
summary_data = []
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Data frame dictionary
summary_data_dict = {
    "Item": summary_headings,
    "Amount": summary_data
}

movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    "Popcorn": popcorn,
    "M&Ms": mms,
    "Pita Chips": pita_chips,
    "Water": water,
    "Orange Juice": orange_juice,
    'Surcharge Multiplier': surcharge_mult_list
}

price_dict = {
    "Popcorn": 2.5,
    "M&Ms": 3,
    "Pita Chips": 4.5,
    "Water": 2,
    "Orange Juice": 3.25
}

SNACK_PROFIT_MARGIN = 0.2
SURCHARGE_RATE = 0.05
MAXIMUM_AGE = 110
MINIMUM_AGE = 12
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
ticket_profit = 0
surcharge = 0
# Ask user if they have used program before
# Tell instructions if necessary

# Loop to get ticket details


# Get name (cant be blank)


while name != "X" and ticket_count < MAX_TICKETS:
    check_max_tickets(MAX_TICKETS, ticket_count)

    name = blank_check("Enter ticket holder's name >> ").title()
    if name == "X":
        break
    else:
        age = check_valid_age(MINIMUM_AGE, MAXIMUM_AGE)
        if not age:
            continue
        else:
            ticket_count += 1

        ticket_price = calc_ticket_price(age)
        print(f"For {name}, the price is ${ticket_price:,.2f}")

        all_names.append(name)
        all_tickets.append(ticket_price)

        # Get snacks
        snack_order = collate_order()

        for item in snack_lists:
            item.append(0)

        for item in snack_order:
            if len(item) > 0:
                to_find = item[1]
                amount = item[0]
                add_list = movie_data_dict[to_find]
                add_list[-1] = amount

        if len(snack_order) > 0:
            print("\nYour order is currently:")
            for item in snack_order:
                print(f"\t{item[0]} {item[1]}")
        else:
            print("No snacks ordered")

        payment_method = check_valid_payment_method()
        if not payment_method:
            continue

        elif payment_method == "Credit Card":
            surcharge_multiplier = SURCHARGE_RATE

        else:
            surcharge_multiplier = 0

        surcharge_mult_list.append(surcharge_multiplier)

# Calculate total sales and profit
if ticket_count < MAX_TICKETS:
    if ticket_count > 1:
        print(f"\n{ticket_count} tickets have been sold")
    else:
        print("1 ticket has been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available\n")
    else:
        print("1 ticket is still available\n")
else:
    print("!!!!! ALL TICKETS HAVE BEEN SOLD !!!!!")
    print("*" * 60)

print()
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")

movie_frame["Snack Cost"] = \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

movie_frame["Sub Total"] = movie_frame["Snack Cost"] + movie_frame["Ticket"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + movie_frame["Surcharge"]

movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips",
                                          "Surcharge Multiplier": "SM"})

for item in snack_lists:
    summary_data.appent(sum(item))

snack_total = movie_frame["Snack Cost"].sum()
snack_profit = snack_total * SNACK_PROFIT_MARGIN
summary_data.append(snack_profit)

total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

pandas.set_option("display.max_columns", None)

pandas.set_option("display.precision", 2)

print(movie_frame)
print()

print_all = input("Print all columns? (Y for yes) >> ").upper()
if print_all == "Y":
    print(movie_frame)
else:
    print(movie_frame[["Ticket", "Snack Cost", "Sub Total", "Surcharge",
                       "Total"]])
print()

# Output data to text file
