"""This code loops the code to sell all available tickets
The loop will stop when break code 'xxx' is entered or all tickets are sold
Made by Daniel Fraser
15/03/22"""


# Initialize loop so that it can do 1 loop
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    # Get details
    name = input("What is your name? >> ").title()
    count += 1
