count_of_strings = int(input())
searched_word = str(input())

full_list = []
filtered_list = []

for x in range (0, count_of_strings):
    current_string = str(input())
    full_list.append(current_string)
    if searched_word in current_string:
        filtered_list.append(current_string)

print(full_list)
print(filtered_list)