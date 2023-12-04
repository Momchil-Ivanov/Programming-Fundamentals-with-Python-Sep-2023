command = input()

customers_dict = {}

total_count_of_unliked_meals = 0

while command != "Stop":
    command_to_list = command.split("-")
    current_command = command_to_list[0]
    current_customer = command_to_list[1]
    current_meal = command_to_list[2]

    if current_command == "Like":
        if current_customer in customers_dict.keys():
            if not current_meal in customers_dict[current_customer]:
                customers_dict[current_customer].append(current_meal)
        else:
            customers_dict[current_customer] = [current_meal]
    elif current_command == "Dislike":
        if current_customer in customers_dict.keys():
            if current_meal in customers_dict[current_customer]:
                customers_dict[current_customer].remove(current_meal)
                total_count_of_unliked_meals += 1
                print(f"{current_customer} doesn't like the {current_meal}.")
            else:
                print(f"{current_customer} doesn't have the {current_meal} in his/her collection.")
        else:
            print(f"{current_customer} is not at the party.")

    command = input()

for key in customers_dict.keys():
    final_output = f"{key}: "
    meals = ', '.join(customers_dict[key])
    final_output += meals
    print(final_output)

print(f"Unliked meals: {total_count_of_unliked_meals}")