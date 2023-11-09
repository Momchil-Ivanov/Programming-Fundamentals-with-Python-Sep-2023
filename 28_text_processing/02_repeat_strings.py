string_list = input().split()
final_string = ""
for word in string_list:
    for x in range(len(word)):
        final_string += word
print(final_string)