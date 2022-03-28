"""This code asks the user what snack they want and gives them a valid answer
this iteration makes it more generic
Made By Daniel Fraser
27/03/22"""


def get_choice(question, valid_choices):
    choice_error = "Sorry, that is not a valid choice"

    choice = input(question).lower()
    for item in valid_snacks:
        if choice in item:
            choice = item[0].title()
            return choice

    print(choice_error)
    return get_choice(question, valid_choices)


ask_for_snacks = "What snack do you want? >> "
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                ["pita chips", "chips", "pc", "pita", "c", "3"],
                ["water", "w", "4"]]
for test in range(6):
    print(f"You want {get_choice(ask_for_snacks, valid_snacks)}")
