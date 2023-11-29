encrypted_message = input()
encrypted_command = input()

while encrypted_command != "Decode":

    encrypted_command_to_list = encrypted_command.split("|")
    command = encrypted_command_to_list[0]

    if command == "Move":
        number_of_letters = int(encrypted_command_to_list[1])
        encrypted_message += encrypted_message[0:number_of_letters]
        encrypted_message = encrypted_message[number_of_letters:]

    elif command == "Insert":
        index = int(encrypted_command_to_list[1])
        value = encrypted_command_to_list[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif command == "ChangeAll":
        substring = encrypted_command_to_list[1]
        replacement = encrypted_command_to_list[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    encrypted_command = input()

print(f"The decrypted message is: {encrypted_message}")