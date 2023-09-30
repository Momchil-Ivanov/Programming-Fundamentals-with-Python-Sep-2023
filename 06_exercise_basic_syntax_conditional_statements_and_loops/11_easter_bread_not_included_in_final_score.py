budget = float(input())
flour_price_per_kilo = float(input())
price_of_eggs_pack = 0.75 * flour_price_per_kilo
milk_price_per_liter = 1.25 * flour_price_per_kilo
price_per_loave = flour_price_per_kilo + price_of_eggs_pack + (milk_price_per_liter / 4)
colored_eggs_count = int(0)
loave_count = int(0)

while budget >= price_per_loave:
    budget -= price_per_loave
    loave_count += 1
    colored_eggs_count += 3
    if loave_count % 3 == 0:
        colored_eggs_count -= loave_count - 2

print(f"You made {loave_count} loaves of Easter bread! \
Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")