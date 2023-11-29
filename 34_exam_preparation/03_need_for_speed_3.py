number_of_cars = int(input())
cars_dict = {}

for x in range(0, number_of_cars):
    car_info = input().split("|")
    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    cars_dict[car] = [mileage, fuel]

command_input = input()

while command_input != "Stop":
    command_to_list = command_input.split(" : ")
    command = command_to_list[0]
    car_command = command_to_list[1]
    if command == "Drive":
        distance_command = int(command_to_list[2])
        fuel_command = int(command_to_list[3])
        if cars_dict[car_command][1] < fuel_command:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car_command][1] -= fuel_command
            cars_dict[car_command][0] += distance_command
            print(f"{car_command} driven for {distance_command} kilometers. {fuel_command} liters of fuel consumed.")
            if cars_dict[car_command][0] >= 100000:
                print(f"Time to sell the {car_command}!")
                cars_dict.pop(car_command)
    elif command == "Refuel":
        refueled_fuel = 0
        fuel_to_refuel = int(command_to_list[2])
        fuel_before_refuel = cars_dict[car_command][1]
        cars_dict[car_command][1] += fuel_to_refuel
        if cars_dict[car_command][1] > 75:
            cars_dict[car_command][1] = 75
            refueled_fuel = 75 - fuel_before_refuel
        else:
            refueled_fuel = fuel_to_refuel
        print(f"{car_command} refueled with {refueled_fuel} liters")
    elif command == "Revert":
        car_kilometers_to_revert = int(command_to_list[2])
        cars_dict[car_command][0] -= car_kilometers_to_revert
        if cars_dict[car_command][0] < 10000:
            cars_dict[car_command][0] = 10000
        else:
            print(f"{car_command} mileage decreased by {car_kilometers_to_revert} kilometers")
    command_input = input()

for car in cars_dict:
    print(f"{car} -> Mileage: {cars_dict[car][0]} kms, Fuel in the tank: {cars_dict[car][1]} lt.")