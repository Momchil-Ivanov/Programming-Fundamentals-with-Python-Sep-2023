command = str(input())
total_products = 0
total_quantity = 0
products_dictionary = {}

while command != "statistics":
    command_to_list = command.split(": ")
    product = command_to_list[0]
    quantity = int(command_to_list[1])
    if product in products_dictionary.keys():
        products_dictionary[product] += quantity
    else:
        products_dictionary[product] = quantity
        total_products += 1
    total_quantity += quantity
    command = str(input())

print("Products in stock:")

for key in products_dictionary:
    print(f"- {key}: {products_dictionary[key]}")

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")