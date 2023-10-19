pirate_ship_status_list = input().split(">")
for x in range(0, len(pirate_ship_status_list)):
    pirate_ship_status_list[x] = int(pirate_ship_status_list[x])
warship_status_list = input().split(">")
for x in range(0, len(warship_status_list)):
    warship_status_list[x] = int(warship_status_list[x])
max_health_capacity = int(input())

command = str(input())

while command != "Retire":
    command_list = command.split(" ")
    current_command = command_list[0]

    if current_command == "Fire":
        index = int(command_list[1])
        damage = int(command_list[2])
        if index >= 0 and index < len(warship_status_list):
            warship_status_list[index] -= damage
            if warship_status_list[index] <= 0:
                print("You won! The enemy ship has sunken.")
                quit()
    elif current_command == "Defend":
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        damage = int(command_list[3])
        if start_index >= 0 and start_index < len(pirate_ship_status_list) \
            and end_index >= 0 and end_index < len(pirate_ship_status_list):
            for x in range(start_index, end_index + 1):
                pirate_ship_status_list[x] -= damage
                if pirate_ship_status_list[x] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    quit()
    elif current_command == "Repair":
        index = int(command_list[1])
        health = int(command_list[2])
        if index >= 0 and index < len(pirate_ship_status_list):
            pirate_ship_status_list[index] += health
            if pirate_ship_status_list[index] > max_health_capacity:
                pirate_ship_status_list[index] = max_health_capacity
    elif current_command == "Status":
        count_of_sections_for_repair = 0
        for x in range(0, len(pirate_ship_status_list)):
            if float(int(pirate_ship_status_list[x])) < float(max_health_capacity * 0.2):
                count_of_sections_for_repair += 1
        print(f"{count_of_sections_for_repair} sections need repair.")

    command = str(input())

pirate_ship_sum = 0
warship_sum = 0

for x in range(0, len(pirate_ship_status_list)):
    pirate_ship_sum += pirate_ship_status_list[x]
for x in range(0, len(warship_status_list)):
    warship_sum += warship_status_list[x]

print(f"Pirate ship status: {pirate_ship_sum}")
print(f"Warship status: {warship_sum}")