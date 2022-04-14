"""This component asks the user if they would like instructions for the program
If they do, it shows them, if they don't the program launches
Made by Daniel Fraser
14/04/22"""


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
        print("Program launches...")


def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


def blank_check(ask_name):
    while True:
        response = input(ask_name).title()
        if not response:
            print("Please do not leave this blank!")
        else:
            return response


valid_yes_no = [["y", "yes"], ["n", "no"]]
show_instructions(valid_yes_no)
