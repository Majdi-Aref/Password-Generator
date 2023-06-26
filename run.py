"""
Import random and string modules to be able to construct a
password randomly using letters, numbers, and special characters
"""
import random
import string

import colorama
from colorama import Fore, Back, Style
colorama.init()


def get_password_minimum_length():
    """Gets a user's desired minimum number of characters of their password"""
    while True:
        minimum_length_user_input = (
            input(Fore.CYAN + "Enter a number "
                  "that represents the minimum length of the password that "
                  "you want; the number must be greater than 5.\n")
        )
        if minimum_length_user_input.isdigit() == False:
            print(Fore.RED + "Error! You entered letters "
                             "and/or special characters.")
            continue
        desired_minimum_length = int(minimum_length_user_input)
        if desired_minimum_length < 6:
            print(Fore.RED + "Error! You entered a number that "
                             "is not greater than 5.")
            continue
        return desired_minimum_length


def does_user_want_numbers():
    """Checks whether a user wants to include numbers in their password"""
    while True:
        does_user_want_numbers = (
            input(Fore.CYAN + "Do you want to "
                  "have numbers in your password? "
                  "Please type in 'y' or 'n'.\n").lower()
        )
        if does_user_want_numbers == "y":
            return True
        elif does_user_want_numbers == "n":
            return False
        else:
            print(Fore.RED + "Error! You entered neither 'y' nor 'n'.")
            continue


def does_user_want_special_characters():
    """Checks whether a user wants to include
       special characters in their password"""
    while True:
        does_user_want_special_characters = (
            input(Fore.CYAN + "Do you want to have "
                  "special characters in your password? "
                  "Please type in 'y' or 'n'.\n").lower()
        )
        if does_user_want_special_characters == "y":
            return True
        elif does_user_want_special_characters == "n":
            return False
        else:
            print(Fore.RED + "Error! You entered neither 'y' nor 'n'.")
            continue


def get_characters_source(has_numbers, has_special_chars):
    """Specifies the characters set from which a password can be generated"""
    characters_source = string.ascii_letters
    if has_numbers == True:
        characters_source += string.digits
    if has_special_chars == True:
        characters_source += string.punctuation
    return characters_source


def generate_password(minimum_length, characters_source,
                      has_numbers, has_special_chars):
    password = ""
    while True:
        for _ in range(minimum_length):
            character_to_add = random.choice(characters_source)
            password += character_to_add
        contains_digits = any(char.isdigit() for char in password)
        if has_numbers == True and contains_digits == False:
            continue
        contains_special_characters = any(char in string.punctuation
                                          for char in password)
        if has_special_chars == True and contains_special_characters == False:
            continue
        return password


def main():
    """The main function that runs the whole programme"""
    minimum_length = get_password_minimum_length()
    has_numbers = does_user_want_numbers()
    has_special_chars = does_user_want_special_characters()
    characters_source = get_characters_source(has_numbers, has_special_chars)
    password = generate_password(minimum_length, characters_source, has_numbers, has_special_chars)
    print(Fore.GREEN + "Your requested password is:\n" + Fore.YELLOW + password)


main()