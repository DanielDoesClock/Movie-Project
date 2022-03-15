"""This small bit of code is the first component in my project
This will ask the user for their name, if this is left blank it will ask again
Created by Daniel Fraser
14/03/22"""


def blank_check(ask_name):
    valid = ""
    while not valid:
        response = input(ask_name)
        if not response:
            print("Please do not leave this blank!")
        else:
            return response


# ******* Main routine *******
name = blank_check("What is your name? >> ")
