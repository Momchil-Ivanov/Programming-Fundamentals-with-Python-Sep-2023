def office_chairs_counter():
    number_of_rooms = int(input())
    free_chairs = 0
    game_on = True

    for x in range(0, number_of_rooms):
        command_list = input().split(" ")
        chairs = command_list[0]
        chairs_num = int(len(chairs))
        visitors = int(command_list[1])
        if chairs_num > visitors:
            free_chairs += chairs_num - visitors
        elif chairs_num < visitors:
            print(f"{visitors - chairs_num} more chairs needed in room {x + 1}")
            game_on = False

    if game_on:
        print(f"Game On, {free_chairs} free chairs left")

result = office_chairs_counter()
result