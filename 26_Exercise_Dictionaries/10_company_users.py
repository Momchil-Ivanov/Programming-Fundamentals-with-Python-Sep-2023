command = input()
companies_dict = {}

while command != "End":
    command_list = command.split(" -> ")
    company = command_list[0]
    id = command_list[1]
    if company not in companies_dict.keys():
        companies_dict[company] = [id]
    else:
        if id not in companies_dict[company]:
            companies_dict[company].append(id)
    command = input()

for key in companies_dict.keys():
    print(f"{key}")
    for current_id in companies_dict[key]:
        print(f"-- {current_id}")