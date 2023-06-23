"""
Import random and string modules to be able to construct a password randomly using letters, 
numbers, and special characters
"""
import random
import string


def get_password_minimum_length():
    """Gets a user's desired minimum number of characters of their password"""
    while True:
        minimum_length_user_input = input("Enter a number that represents the minimum length of the password that you want; the number must be greater than 5: ")
        if minimum_length_user_input.isdigit() == False:
            continue
        desired_minimum_length = int(minimum_length_user_input)
        if desired_minimum_length < 6:
            continue
        return desired_minimum_length

