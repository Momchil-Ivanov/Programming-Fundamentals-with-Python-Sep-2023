def trains(number_of_wagons: int):
    wagon_list = [0] * number_of_wagons
    command = str(input())
    while command != "End":
        command_list = command.split(" ")
        current_command = command_list[0]
        if current_command == "add":
            people_to_add = int(command_list[1])
            wagon_list[len(wagon_list)-1] += people_to_add
        elif current_command == "insert":
            people_to_insert_index = int(command_list[1])
            people_to_insert_num = int(command_list[2])
            wagon_list[people_to_insert_index] += people_to_insert_num
        elif current_command == "leave":
            people_to_leave_index = int(command_list[1])
            people_to_leave_num = int(command_list[2])
            wagon_list[people_to_leave_index] -= people_to_leave_num
        command = str(input())

    print(wagon_list)

real_input = int(input())
result = trains(real_input)
result