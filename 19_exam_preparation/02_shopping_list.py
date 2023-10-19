products_list = input().split("!")

command = str(input())

while command != "Go Shopping!":
    command_list = command.split(" ")
    current_command = command_list[0]
    current_item = command_list[1]

    if current_command == "Urgent":
        if current_item not in products_list:
            products_list.insert(0, current_item)
    elif current_command == "Unnecessary":
        if current_item in products_list:
            products_list.remove(current_item)
    elif current_command == "Correct":
        new_item = command_list[2]
        if current_item in products_list:
            products_list = [new_item if item == current_item else item for item in products_list]
    elif current_command == "Rearrange":
        if current_item in products_list:
            temporary_item = current_item
            products_list.remove(current_item)
            products_list.append(temporary_item)
    command = str(input())

print((", ").join(products_list))