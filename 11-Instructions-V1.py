"""This component asks the user if they would like instructions for the program
If they do, it shows them, if they don't the program launches
Made by Daniel Fraser
14/04/22"""


def show_instructions():
    print("******* Mega Movie Fundraiser Instructions *******\n"
          "When asked a question, please type in a proper response\nCapitals "
          "and punctuation are not needed.")


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

instructions = ""
while not instructions:
    instructions = blank_check("Would you like to read the"
                               " instructions? >> ").lower()
    instructions = (get_choice(instructions, valid_yes_no))

if instructions == "Y":
    show_instructions()

print("Program launches...")

