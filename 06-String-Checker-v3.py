"""This code asks the user what snack they want and gives them a valid answer
this iteration adds the yes-no thing
Made By Daniel Fraser
27/03/22"""


def get_choice(question, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    choice = input(question).lower()
    for item in valid_choices:
        if choice in item:
            choice = item[0].title()
            return choice

    print(choice_error)
    return get_choice(question, valid_choices)


ask_for_snacks = "What snack do you want? ('x' to stop ordering) >> "
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                ["pita chips", "chips", "pc", "pita", "c", "3"],
                ["water", "w", "4"], ["x", "exit", "5"]]
check_snacks = "Do you want snacks? >> "
valid_yes_no = [["y", "yes"], ["n", "no"]]

getting_snacks = True
snacks_required = get_choice(check_snacks, valid_yes_no)
while getting_snacks:
    if snacks_required == "N":
        print("You do not want snacks")
        getting_snacks = False
    else:
        option = get_choice(ask_for_snacks, valid_snacks)
        if option != "X":
            print(f"You have chosen {option}")
        else:
            getting_snacks = False
            print("Thank you for ordering some snacks!")
