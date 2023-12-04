password_string = input()

command = input()

while command != "Done":
    command_to_list = command.split()
    current_command = command_to_list[0]
    if current_command == "TakeOdd":
        temporary_password = ""
        for x in range(0, len(password_string)):
            if x % 2 != 0:
                temporary_password += password_string[x]
        password_string = temporary_password
        print(password_string)
    elif current_command == "Cut":
        start_index = int(command_to_list[1])
        length = int(command_to_list[2])
        end_index = start_index + length
        password_string = password_string[:start_index] + password_string[end_index:]
        print(password_string)
    elif current_command == "Substitute":
        substring = command_to_list[1]
        substitute = command_to_list[2]
        if substring in password_string:
            password_string = password_string.replace(substring, substitute)
            print(password_string)
        else:
            print(f"Nothing to replace!")
    command = input()

print(f"Your password is: {password_string}")