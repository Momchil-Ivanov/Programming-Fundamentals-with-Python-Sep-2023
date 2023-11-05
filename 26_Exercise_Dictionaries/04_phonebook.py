command = input()
phone_dict = {}

while "-" in command:
    command_list = command.split("-")
    name = command_list[0]
    phone_number = command_list[1]
    phone_dict[name] = phone_number
    command = input()

count_of_checks = int(command)

for check in range(count_of_checks):
    checked_name = input()
    if checked_name not in phone_dict.keys():
        print(f"Contact {checked_name} does not exist.")
    else:
        print(f"{checked_name} -> {phone_dict[checked_name]}")