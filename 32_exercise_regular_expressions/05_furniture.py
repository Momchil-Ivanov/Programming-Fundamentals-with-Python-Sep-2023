import re
money_spend = 0
furniture = []

command = input()
pattern = r">>([A-Za-z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)"

while command != "Purchase":
    match = re.findall(pattern, command)
    if len(match) > 0:
        for item in match:
            furniture.append(item[0])
            money_spend += float(item[1]) * int(item[2])

    command = input()

print("Bought furniture:")
for current_furniture in furniture:
    print(current_furniture)
print(f"Total money spend: {money_spend:.2f}")