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


def does_user_want_numbers():
    """Checks whether a user wants to include numbers in their password"""
    while True:
        does_user_want_numbers = input("Do you want to have numbers in your password? Please type in 'y' or 'n'.").lower()
        if does_user_want_numbers == "y":
            return True
        elif does_user_want_numbers == "n":
            return False
        else:
            continue


def does_user_want_special_characters():
    """Checks whether a user wants to include special characters in their password"""
    while True:
        does_user_want_special_characters = input("Do you want to have special characters in your password? Please type in 'y' or 'n'.").lower()
        if does_user_want_special_characters == "y":
            return True
        elif does_user_want_special_characters == "n":
            return False
        else:
            continue


def get_characters_source(has_numbers, has_special_chars):
    """Specifies the characters set from which a password can be generated"""
    characters_source = string.ascii_letters
    if has_numbers == True:
        characters_source += string.digits
    if has_special_chars == True:
        characters_source += string.punctuation
    return characters_source


def generate_password(minimum_length, characters_source, has_numbers, has_special_chars):
    password = ""
    while True:
        for _ in range(minimum_length):
            character_to_add = random.choice(characters_source) 
            password += character_to_add
        contains_digits = any(char.isdigit() for char in password)
        if has_numbers == True and contains_digits == False: 
            continue
        contains_special_characters = any(char in string.punctuation for char in password)
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
    print(f"Your requested password is: {password}")


main()