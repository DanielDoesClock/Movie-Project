"""This is v2 of the loop sales code
I have added a seat counter so the user knows how many possible sales are left
Made by Daniel Fraser
15/03/22"""


# Initialize loop so that it can do 1 loop
name = ""
count = 0
MAX_TICKETS = 5
seats = MAX_TICKETS

while name != "Xxx" and count != MAX_TICKETS:
    # Get details
    print(f"There are {seats} seats left")
    name = input("What is your name? >> ").title()
    count += 1
    seats -= 1

if seats == 0:
    print("All tickets have been sold")

if name == "Xxx":
    print(f"You have sold {count - 1} tickets")
