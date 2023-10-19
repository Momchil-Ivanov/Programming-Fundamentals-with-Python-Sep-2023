from textwrap import wrap

data_list = input().split(" ")

command = str(input())
while command != "3:1":
    command_to_list = command.split(" ")
    current_command = command_to_list[0]
    first_index = int(command_to_list[1])
    last_index = int(command_to_list[2])
    if current_command == "merge":
        if first_index < 0:
            first_index = 0
        if first_index > len(data_list) - 1:
            first_index = len(data_list) - 1
        if last_index < 0:
            last_index = 0
        if last_index > len(data_list) - 1:
            last_index = len(data_list) - 1
        data_list[first_index:last_index+1] = [''.join(data_list[first_index:last_index+1])]
    elif current_command == "divide":
        new_data_list = data_list[first_index]
        data_list.pop(first_index)
        substring_len = len(new_data_list) // last_index
        remainder = len(new_data_list) % last_index
        substrings_added = 0
        start_part = 0
        end_part = substring_len
        while substrings_added < last_index:
            data_list.insert(first_index, new_data_list[start_part:end_part])
            first_index += 1
            substrings_added += 1
            if substrings_added + 1 == last_index:
                start_part += substring_len
                end_part +=  substring_len + remainder
            else:
                start_part += substring_len
                end_part += substring_len
    command = str(input())

print(" ".join(data_list))