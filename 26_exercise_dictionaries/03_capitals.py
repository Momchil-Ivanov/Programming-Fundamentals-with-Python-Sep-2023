countries = input().split(', ')
capitals = input().split(', ')
countries_dict = {}

for x in range(0, len(countries)):
    countries_dict[countries[x]] = capitals[x]

for key in countries_dict:
    print(f"{key} -> {countries_dict[key]}")