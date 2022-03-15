"""This is the second iteration of the first component
This is modified to make it more versatile
Created by Daniel Fraser
14/03/22"""


def blank_check(ask_name, error_message):
    valid = ""
    while not valid:
        response = input(ask_name)
        if not response:
            print(error_message)
        else:
            return response


# ******* Main routine *******
name = blank_check("What is your name? >> ", "Please do not leave this blank!")
