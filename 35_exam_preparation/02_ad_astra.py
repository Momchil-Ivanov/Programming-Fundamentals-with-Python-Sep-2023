import re

raw_string = input()
pattern = r"#([A-Za-z\s]+)#([0-9]{2}/[0-9]{2}/[0-9]{2})#(\d{1,5})#|\|([A-Za-z\s]+)\|([0-9]{2}/[0-9]{2}/[0-9]{2})\|(\d{1,5})\|"
total_calories = 0

matches = re.findall(pattern, raw_string)

for match in matches:
    if match[0] == "":
        total_calories += int(match[5])
    else:
        total_calories += int(match[2])

number_of_days = int(total_calories / 2000)

print(f"You have food to last you for: {number_of_days} days!")

for match in matches:
    if match[0] == "":
        print(f"Item: {match[3]}, Best before: {match[4]}, Nutrition: {match[5]}")
    else:
        print(f"Item: {match[0]}, Best before: {match[1]}, Nutrition: {match[2]}")