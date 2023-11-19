import re

input_string = input()

regex = r'[0-9]{2}/[A-Z][a-z]{2}/[0-9]{4}|[0-9]{2}\.[A-Z][a-z]{2}\.[0-9]{4}|[0-9]{2}-[A-Z][a-z]{2}-[0-9]{4}'

matches = re.findall(regex, input_string)

for match in matches:
    print(f"Day: {match[0:2]}, Month: {match[3:6]}, Year: {match[7:11]}")