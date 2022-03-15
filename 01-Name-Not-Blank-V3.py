"""This is the third iteration of the first component
This is modified to be less over-kill and make a space and invalid name
Created by Daniel Fraser
14/03/22"""


def blank_check(ask_name):
    while True:
        response = input(ask_name)
        if not response.isalpha():
            print("Please do not leave this blank!")
        else:
            return response


# ******* Main routine *******
name = blank_check("What is your name? >> ")
