import re

password = input()

command = input()

while command != "Complete":
    command_to_list = command.split()
    current_command = command_to_list[0]
    if current_command == "Make":
        upper_or_lower = command_to_list[1]
        index = int(command_to_list[2])
        if upper_or_lower == "Upper":
            if 0 <= index < len(password):
                upper_case = password[index].upper()
                string_list_upper = list(password)
                string_list_upper[index] = upper_case
                password = "".join(string_list_upper)
            print(password)
        elif upper_or_lower == "Lower":
            if 0 <= index < len(password):
                lower_case = password[index].lower()
                string_list_lower = list(password)
                string_list_lower[index] = lower_case
                password = "".join(string_list_lower)
            print(password)
    elif current_command == "Insert":
        index = int(command_to_list[1])
        if 0 <= index < len(password):
            symbol = command_to_list[2]
            password = password[:index] + symbol + password[index:]
            print(password)
    elif current_command == "Replace":
        current_char = command_to_list[1]
        char_to_ascii = ord(current_char)
        current_value = int(command_to_list[2])
        sum = char_to_ascii + current_value
        sum_to_char = chr(sum)
        password = password.replace(current_char, sum_to_char)
        print(password)
    elif current_command == "Validation":

        if len(password) < 8:
            print(f"Password must be at least 8 characters long!")

        password_wihtout_underscore = ""

        for element in password:
            if not element == "_":
                password_wihtout_underscore += element

        if not password_wihtout_underscore.isalnum():
            print(f"Password must consist only of letters, digits and _!")

        contains_uppercase = any(char.isupper() for char in password)

        if not contains_uppercase:
            print("Password must consist at least one uppercase letter!")

        contains_lowercase = any(char.islower() for char in password)

        if not contains_lowercase:
            print("Password must consist at least one lowercase letter!")

        has_digit = False

        for char in password:

            if char.isdigit():
                has_digit = True

        if has_digit == False:
            print(f"Password must consist at least one digit!")

    command = input()