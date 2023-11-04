data = input().split()

stock = {}

for x in range(0, len(data), 2):
    item = data[x]
    quantity = int(data[x + 1])
    stock[item] = quantity

products_to_search = input().split()

for x in range(0, len(products_to_search)):
    searched_product = products_to_search[x]
    if searched_product in stock:
        print(f"We have {stock[searched_product]} of {searched_product} left")
    else:
        print(f"Sorry, we don't have {searched_product}")