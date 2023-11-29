command = input()
cities_dict = {}

while command != "Sail":
    command_to_list = command.split("||")
    city = command_to_list[0]
    population = int(command_to_list[1])
    gold = int(command_to_list[2])

    if city in cities_dict.keys():
        cities_dict[city][0] += population
        cities_dict[city][1] += gold
    else:
        cities_dict[city] = [int(population), int(gold)]

    command = input()

event = input()

while event != "End":
    event_to_list = event.split("=>")
    current_event = event_to_list[0]
    current_town = event_to_list[1]
    if current_event == "Plunder":
        current_people = int(event_to_list[2])
        current_gold = int(event_to_list[3])
        cities_dict[current_town][0] -= current_people
        cities_dict[current_town][1] -= current_gold
        print(f"{current_town} plundered! {current_gold} gold stolen, {current_people} citizens killed.")
        if cities_dict[current_town][0] == 0 or cities_dict[current_town][1] == 0:
            cities_dict.pop(current_town)
            print(f"{current_town} has been wiped off the map!")

    elif current_event == "Prosper":
        gold_to_be_added = int(event_to_list[2])
        if gold_to_be_added < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[current_town][1] += gold_to_be_added
            print(f"{gold_to_be_added} gold added to the city treasury. {current_town} now has {cities_dict[current_town][1]} gold.")
    event = input()

if len(cities_dict) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for city in cities_dict:
        print(f"{city} -> Population: {cities_dict[city][0]} citizens, Gold: {cities_dict[city][1]} kg")