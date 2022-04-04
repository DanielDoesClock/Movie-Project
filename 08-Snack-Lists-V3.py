"""This is component 8 of MMF and will create lists of all of the snacks
that have been ordered and adds a 'sub total' block.
Made by Daniel Fraser
04/04/22"""

import pandas

names = ["Blue", "Red", "Green", "Yellow", "Orange"]
tickets = [7.5, 10.5, 10.5, 10.5, 6.5]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

movie_data_dict = {
    "Name": names,
    "Ticket": tickets,
    "popcorn": popcorn,
    "M&Ms": mms,
    "Pita Chips": pita_chips,
    "water": water,
    "Orange Juice": orange_juice
}

price_dict = {
    "popcorn": 2.5,
    "M&Ms": 3,
    "Pita Chips": 4.5,
    "water": 2,
    "Orange Juice": 3.25
}

test_data = [
    [[2, 'popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'water']],
    [[1, 'popcorn'], [1, 'Orange Juice']],
    [[1, "M&Ms"], [1, "Pita Chips"], [3, "Orange Juice"]]
]

count = 0
for client_order in test_data:
    for item in snack_lists:
        item.append(0)

    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = item[1]
            amount = item[0]
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

print()
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")

movie_frame["Sub Total"] = \
    movie_frame["Ticket"] + \
    movie_frame["popcorn"] * price_dict["popcorn"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["water"] * price_dict["water"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips"})
print(movie_frame)

