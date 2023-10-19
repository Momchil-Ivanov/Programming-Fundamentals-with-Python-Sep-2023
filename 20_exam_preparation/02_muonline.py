health = 100
bitcoins = 0
dead = False
best_room = 1

dungeon_rooms_list = input().split("|")
for x in range(0, len(dungeon_rooms_list)):
    current_command = dungeon_rooms_list[x].split(" ")
    current_item = current_command[0]
    current_value = int(current_command[1])
    if current_item == "potion":
        initial_health = health
        health += current_value
        if health > 100:
            health = 100
        healed_amount = health - initial_health
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")
    elif current_item == "chest":
        bitcoins += current_value
        print(f"You found {current_value} bitcoins.")
    else:
        health -= current_value
        if health <= 0:
            print(f"You died! Killed by {current_item}.")
            print(f"Best room: {best_room}")
            quit()
        else:
            print(f"You slayed {current_item}.")
    best_room += 1

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")