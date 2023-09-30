budget = int(input())

while budget >= 0:
    current_item_price = str(input())
    if current_item_price == "End":
        print("You bought everything needed.")
        quit()
    budget = budget - int(current_item_price)

if budget < 0:
    print("You went in overdraft!")