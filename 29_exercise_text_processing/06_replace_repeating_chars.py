input_text = input()
input_text_list = []
for char in input_text:
    input_text_list.append(char)

for x in range(1, len(input_text_list)):
    try:
        while input_text_list[x - 1] == input_text_list[x]:
            del input_text_list[x]
    except:
        break

print("".join(input_text_list))