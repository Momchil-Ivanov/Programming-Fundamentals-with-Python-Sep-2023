input_text = input()
input_text_list = []
for char in input_text:
    input_text_list.append(char)
chars_for_deletion = 0

for x in range(1, len(input_text_list) + 1):
    try:
        if input_text_list[x - 1] == ">" and input_text_list[x] != ">":
                chars_for_deletion += int(input_text_list[x])
                while chars_for_deletion > 0 and input_text_list[x] != ">":
                    del input_text_list[x]
                    chars_for_deletion -= 1
    except:
        break

print("".join(input_text_list))