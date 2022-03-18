"""This is v3 of the loop sales code
I have added nice spacing and a clear warning when 1 ticket is left
Made by Daniel Fraser
15/03/22"""


# Initialize loop so that it can do 1 loop
name = ""
count = 0
MAX_TICKETS = 5
seats = MAX_TICKETS

while name != "Xxx" and count != MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nThere are {seats} seats left")

    # Get details
    else:
        print("\n******* THERE IS ONLY 1 SEAT LEFT *******")
    name = input("What is your name? >> ").title()
    count += 1
    seats -= 1

if seats == 0:
    print("All tickets have been sold")

if name == "Xxx":
    print(f"You have sold {count - 1} tickets")
