two_strings_list = input().split()

first_string = two_strings_list[0]
second_string = two_strings_list[1]
first_string_list = []
second_string_list = []
for char in first_string:
    first_string_list.append(char)
for char in second_string:
    second_string_list.append(char)

sum = 0

if len(first_string) >= len(second_string):
    for x in range(0, len(second_string)):
        sum += ord(first_string_list[x]) * ord(second_string_list[x])
    for y in range(len(second_string), len(first_string)):
        sum += ord(first_string_list[y])
else:
    for x in range(0, len(first_string)):
        sum += ord(first_string_list[x]) * ord(second_string_list[x])
    for y in range(len(first_string), len(second_string)):
        sum += ord(second_string[y])

print(sum)