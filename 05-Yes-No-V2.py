"""This is the 5th component and is used to check if a user is answering a
Yes/No questions appropriately. In this 2nd version, I have added a function
Made By Daniel Fraser
27/03/22"""


def y_n_response(question):
    error = "Please answer with 'Yes' or 'No'"
    valid_response = ["YES", "Y", "NO", "N"]
    response = question.upper()
    while response not in valid_response:
        print(error)
        response = input(question).upper()
    if response == "N" or response == "NO":
        return False
    else:
        return True


snacks_required = y_n_response("Would you like to purchase some snacks?"
                               " >> ")
if not snacks_required:
    print("Valid answer. No snacks wanted")
else:
    print("Valid answer. You would like snacks")



