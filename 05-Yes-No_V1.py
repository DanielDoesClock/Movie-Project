"""This is the 5th component and is used to check if a user is answering a
Yes/No questions appropriately.
Made By Daniel Fraser
27/03/22"""

error = "Please answer with 'Yes' or 'No'"
valid_response = ["YES", "Y", "NO", "N"]
response = input("Would you like to purchase some snacks? >> ").upper()
while response not in valid_response:
    print(error)
    response = input("Would you like to purchase some snacks? >>" ).upper()

if response == "N" or response == "NO":
    print("Valid answer. No snacks wanted")
else:
    print("Valid answer. You would like snacks")
