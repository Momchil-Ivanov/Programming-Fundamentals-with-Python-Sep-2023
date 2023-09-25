year = int(input())

year_in_text = str(year)
unique_count = 0

while len(set(year_in_text)) == len(year_in_text) and unique_count < 1:
    year += 1
    unique_count += 1
    year_in_text = str(year)

while len(set(year_in_text)) != len(year_in_text):
    year += 1
    year_in_text = str(year)

print(year)