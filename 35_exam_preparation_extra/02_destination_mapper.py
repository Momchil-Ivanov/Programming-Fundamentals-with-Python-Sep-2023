import re

raw_string = input()
pattern = r"=[A-Z][A-Za-z]{2,}=|/[A-Z][A-Za-z]{2,}/"
points = 0
destinations = []
matches = re.findall(pattern, raw_string)

for match in matches:
    destinations.append(match[1:-1])
    points += len(match[1:-1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")