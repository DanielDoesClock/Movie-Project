"""This is V16 of my final project file. I am adding the instruction function
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
    valid_snacks = [["popcorn", "p", "pop", "corn", "(1"],
                    ["m&ms", "mms", "mm", "m", "(2"],
                    ["pita chips", "chips", "pc", "pita", "c", "(3"],
                    ["water", "h2o", "w", "(4"],
                    ["orange juice", "oj", "o", "juice", "(5"],
                    ["x", "exit", "(6"]]
    snacks_order = []
    max_snacks = 4
    option = ""
    while option != "X":
        snack = input("What snack do you want? - qty then item"
                      "\n e.g. '2 Popcorn' OR 'x' "
                      "To stop ordering >> ").lower()
        snack = split_order(snack)
        quantity = snack[0]

        if quantity > max_snacks:
            print("Sorry, the max number of snacks is 4")
        else:
            snack = snack[1]
            option = get_choice(snack, valid_snacks)
            if option == "X":
                break
            elif option is not None:
                snacks_order.append([quantity, option])
    return snacks_order


# Calculates the ticket price based on age
def calc_ticket_price(age_):
    child_age = range(12, 16)
    standard_age = range(16, 65)
    child_price = 7.50
    standard_price = 10.50
    retired_price = 6.50

    if age_ in child_age:
        ticket_price_ = child_price
    elif age in standard_age:
        ticket_price_ = standard_price
    else:
        ticket_price_ = retired_price
    return ticket_price_


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
    valid_age = int_check(f"Please enter {name}'s age >> ")
    if valid_age < minimum:
        print(f"{name} is young to watch this move.")
        return None
    elif valid_age >= maximum:
        print(f"There is no way {name} could be that old!")
        return None
    else:
        return valid_age


def check_valid_payment_method():
    ask_payment_method = input("How would you like to pay? >> ").lower()
    valid_payment_method = [["credit card", "card", "credit", "cc", "cr", "1"],
                            ["eftpos", "eft", "pos", "ep", "e", "2"],
                            ["cash", "ca", "money", "notes", "coins", "c",
                             "3"]]
    payment_method_ = get_choice(ask_payment_method, valid_payment_method)
    return payment_method_


def ticket_counting(tickets_sold, maximum):
    if ticket_count < MAX_TICKETS:
        if ticket_count > 1:
            print(f"\n{ticket_count} tickets have been sold")
        else:
            print("1 ticket has been sold")
        if MAX_TICKETS - ticket_count > 1:
            print(f"{MAX_TICKETS - ticket_count} tickets are still "
                  f"available\n")
        else:
            print("1 ticket is still available\n")
    else:
        print("!!!!! ALL TICKETS HAVE BEEN SOLD !!!!!")
        print("*" * 60)


def currency(number):
    return f"${number:,.2f}"


def show_instructions(valid_responses):
    instructions = ""
    while not instructions:
        instructions = blank_check("Would you like to read the"
                                   " instructions? >> ").lower()
        instructions = (get_choice(instructions, valid_yes_no))

    if instructions == "Y":
        print("\n**********************************************************\n"
              "\n\t******* Mega Movie Fundraiser Instructions *******\n"
              "\nYou will be shown how many tickets are still available\n"
              "for sale and asked for the first ticket-purchaser's name.\n"
              "You will then be asked to input the ticket-purchaser's age\n"
              "\nThis is because:\n"
              "\t-The minimum age for entry is 12; and\n"
              "\t-There is a standard price for adults; but\n"
              "\t-Different prices for students and retired people.\n"
              "\nThe program will then ask you for the snacks you would like\n"
              "and once these are entered you will need to provide a valid\n"
              "payment method\n"
              "\nThis process keeps repeating until either all the tickets\n"
              "are sold or you choose to exit the program.\n"
              "\nOn exit, a summary of sales and profits will be printed to\n"
              "the screen. Full details of all sales and profits are also\n"
              "output to .csv files. These can be found in the same\n"
              "directory in which the program is stored.\n"
              "\n**********************************************************\n")


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
MAXIMUM_AGE = 111
MINIMUM_AGE = 12
MAX_TICKETS = 150
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
ticket_profit = 0
surcharge = 0
# Ask user if they have used program before
# Tell instructions if necessary
print("*** Welcome to Mega Movie ***")

valid_yes_no = [["y", "yes"], ["n", "no"]]
show_instructions(valid_yes_no)

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

        ticket_profit += (ticket_price - TICKET_COST_PRICE)

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
        while not payment_method:
            payment_method = check_valid_payment_method()

        if payment_method == "Credit Card":
            surcharge_multiplier = SURCHARGE_RATE

        else:
            surcharge_multiplier = 0

        surcharge_mult_list.append(surcharge_multiplier)

        ticket_counting(ticket_count, MAX_TICKETS)
# Calculate total sales and profit

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
    summary_data.append(sum(item))

snack_total = movie_frame["Snack Cost"].sum()
snack_profit = snack_total * SNACK_PROFIT_MARGIN
total_profit = snack_profit + ticket_profit
currency_amounts = [snack_profit, ticket_profit, total_profit]
for amount in currency_amounts:
    amount = currency(amount)
    summary_data.append(amount)

summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index("Item")

pandas.set_option("display.max_columns", None)

currency_amounts = ["Ticket", "Snack Cost", "Sub Total", "Surcharge", "Total"]
for amount in currency_amounts:
    movie_frame[amount] = movie_frame[amount].apply(currency)

movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")

print()
print("******* Ticket/Snack Information *******")
print("Note: For full details please see Exel file named 'ticket_summary.csv'"
      " and 'snack_summary.csv")
print()
print(movie_frame[["Ticket", "Snack Cost", "Sub Total", "Surcharge", "Total"]])
print()
print("******* Snack/Profit Summary *******")
print()
print(summary_frame)

ticket_counting(ticket_count, MAX_TICKETS)
# Output data to text file
