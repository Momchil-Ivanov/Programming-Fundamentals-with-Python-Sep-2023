phones_list = input().split(", ")

command = str(input())

while command != "End":
    current_command = command.split(" - ")
    current_action = str(current_command[0])
    current_phone_model = str(current_command[1])

    if current_action == "Add":
        if current_phone_model not in phones_list:
            phones_list.append(current_phone_model)
    elif current_action == "Remove":
        if current_phone_model in phones_list:
            phones_list.remove(current_phone_model)
    elif current_action == "Bonus phone":
        current_phones_models_list = current_phone_model.split(":")
        old_phone = str(current_phones_models_list[0])
        new_phone = str(current_phones_models_list[1])

        if old_phone in phones_list:
            index_of_old_phone = phones_list.index(old_phone)
            phones_list.insert(index_of_old_phone + 1, new_phone)
    elif current_action == "Last":
        if current_phone_model in phones_list:
            temporary_current_phone_model = current_phone_model
            phones_list.remove(current_phone_model)
            phones_list.append(temporary_current_phone_model)

    command = str(input())

print(", ".join(phones_list))