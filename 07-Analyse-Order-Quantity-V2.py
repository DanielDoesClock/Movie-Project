"""This is the 7th component in my project. This version uses the RE method
of finding positions and snacks
Made by Daniel Fraser
31/03/22"""

import re

test_strings = [
    "Popcorn",
    "2 pc",
    "1.50J",
    "40J"
    ]

for item in test_strings:
    number_regex = "^[1-9]"

    if re.match(number_regex, item):
        amount = int(item[0])
        snack = item[1:]

    else:
        amount = 1
        snack = item

    snack = snack.strip()

    print(f"Amount: {amount}")
    print(f"Snack: {snack}")
    print(f"length of snack: {len(snack)}")
