"""This code asks the user what snack they want and gives them a valid answer
Made By Daniel Fraser
27/03/22"""


def get_snacks():
    snack_error = "Sorry, that is not a valid choice"
    valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                    ["pita chips", "chips", "pc", "pita", "c", "3"],
                    ["water", "w", "4"]]
    snack_choice = input("Snack >> ").lower()
    for snack in valid_snacks:
        if snack_choice in snack:
            snack_choice = snack[0].title()
            return snack_choice
    print(snack_error)
    return get_snacks()


for test in range(6):
    print(f"You want {get_snacks()}")
