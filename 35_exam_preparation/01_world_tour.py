stops_string = input()

command = input()

while command != "Travel":
    command_to_list = command.split(":")
    current_command = command_to_list[0]
    if current_command == "Add Stop":
        index = int(command_to_list[1])
        string_to_add = command_to_list[2]
        if 0 <= index < len(stops_string):
            stops_string = stops_string[:index] + string_to_add + stops_string[index:]
    elif current_command == "Remove Stop":
        start_index = int(command_to_list[1])
        end_index = int(command_to_list[2])
        if 0 <= start_index < len(stops_string) and 0 <= end_index < len(stops_string):
            stops_string = stops_string[:start_index] + stops_string[end_index + 1:]
    elif current_command == "Switch":
        old_string = command_to_list[1]
        new_string = command_to_list[2]
        if old_string in stops_string:
            stops_string = stops_string.replace(old_string, new_string)
    print(stops_string)
    command = input()

print(f"Ready for world tour! Planned stops: {stops_string}")