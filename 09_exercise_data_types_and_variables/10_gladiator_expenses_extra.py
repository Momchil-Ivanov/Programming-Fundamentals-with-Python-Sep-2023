lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

all_expenses = float(0)

for x in range (1, lost_fights_count + 1):
    if x % 2 == 0:
        all_expenses += helmet_price
    if x % 3 == 0:
        all_expenses += sword_price
    if x % 6 == 0:
        all_expenses += shield_price
    if x % 12 == 0:
        all_expenses += armor_price

print(f"Gladiator expenses: {all_expenses:.2f} aureus")