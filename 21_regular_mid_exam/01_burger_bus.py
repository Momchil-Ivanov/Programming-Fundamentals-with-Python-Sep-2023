number_of_cities = int(input())
total_profit = float(0)

for day in range(1, number_of_cities + 1):
    name_of_city = str(input())
    money_earned = float(input())
    owners_expenses = float(input())

    if day % 5 == 0:
        money_earned -= money_earned * 0.10

    if day % 3 == 0 and day % 5 != 0:
        owners_expenses += owners_expenses * 0.50

    profit = money_earned - owners_expenses
    total_profit += profit
    print(f"In {name_of_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")