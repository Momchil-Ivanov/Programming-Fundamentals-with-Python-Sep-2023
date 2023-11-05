items_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
crafted = False

while crafted == False:

    description_list = input().split()
    for x in range(0, len(description_list), 2):
        current_quantity = int(description_list[x])
        current_material = description_list[x + 1]
        current_material= current_material.lower()
        if current_material not in items_dict.keys():
            items_dict[current_material] = current_quantity
        else:
            items_dict[current_material] += current_quantity

        if current_material == "shards":
            if items_dict[current_material] >= 250:
                print("Shadowmourne obtained!")
                items_dict[current_material] -= 250
                crafted = True
                break
        elif current_material == "fragments":
            if items_dict[current_material] >= 250:
                print("Valanyr obtained!")
                items_dict[current_material] -= 250
                crafted = True
                break
        elif current_material == "motes":
            if items_dict[current_material] >= 250:
                print("Dragonwrath obtained!")
                items_dict[current_material] -= 250
                crafted = True
                break

for key in items_dict.keys():
    print(f"{key}: {items_dict[key]}")