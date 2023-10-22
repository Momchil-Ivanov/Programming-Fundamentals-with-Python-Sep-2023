vehicles_list = input().split(">>")
total_taxes = 0

for index_of_vehicle in range(0, len(vehicles_list)):
    initial_tax = 0
    modified_tax = 0
    current_command = vehicles_list[index_of_vehicle].split(" ")
    current_car_type = str(current_command[0])
    years_to_pay_tax = int(current_command[1])
    kilometers_traveled = int(current_command[2])

    if current_car_type == "family":
        initial_tax = 50
        times_3000_kilometers_reached = kilometers_traveled // 3000
        modified_tax = times_3000_kilometers_reached * 12 + initial_tax - years_to_pay_tax * 5
    elif current_car_type == "heavyDuty":
        initial_tax = 80
        times_9000_kilometers_reached = kilometers_traveled // 9000
        modified_tax = times_9000_kilometers_reached * 14 + initial_tax - years_to_pay_tax * 8
    elif current_car_type == "sports":
        initial_tax = 100
        times_2000_kilometers_reached = kilometers_traveled // 2000
        modified_tax = times_2000_kilometers_reached * 18 + initial_tax - years_to_pay_tax * 9
    else:
        print("Invalid car type.")
        continue

    print(f"A {current_car_type} car will pay {modified_tax:.2f} euros in taxes.")
    total_taxes += modified_tax

print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")