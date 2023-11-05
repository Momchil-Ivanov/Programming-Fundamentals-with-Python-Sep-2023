command = input()
products_info_dict = {}

while command != "buy":
    command_to_list = command.split()
    item = command_to_list[0]
    price = float(command_to_list[1])
    quantity = int(command_to_list[2])
    if item not in products_info_dict.keys():
        products_info_dict[item] = [price, quantity]
    else:
        products_info_dict[item][0] = price
        products_info_dict[item][1] += quantity

    command = input()

for key in products_info_dict.keys():
    price = products_info_dict[key][0] * products_info_dict[key][1]
    print(f"{key} -> {price:.2f}")