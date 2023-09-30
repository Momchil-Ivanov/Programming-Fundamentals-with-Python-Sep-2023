nums_count = int(input())

my_list = []
filtered_list = []

for x in range (0, nums_count):
    current_num = int(input())
    my_list.append(current_num)

filter = str(input())

if filter == "even":
    for y in range (0, len(my_list)):
        if my_list[y] % 2 == 0:
            filtered_list.append(my_list[y])
elif filter == "odd":
    for y in range (0, len(my_list)):
        if my_list[y] % 2 != 0:
            filtered_list.append(my_list[y])
elif filter == "negative":
    for y in range (0, len(my_list)):
        if my_list[y] < 0:
            filtered_list.append(my_list[y])
elif filter == "positive":
    for y in range (0, len(my_list)):
        if my_list[y] >= 0:
            filtered_list.append(my_list[y])

print(filtered_list)