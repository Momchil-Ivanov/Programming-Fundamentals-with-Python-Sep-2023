input_text = input()
input_text_list = []
emoticon_list = []

for char in input_text:
    input_text_list.append(char)

for x in range(0, len(input_text_list)):
    if input_text_list[x] == ":":
        current_emoticon = "".join(input_text_list[x:x + 2])
        emoticon_list.append(current_emoticon)

for emoticon in emoticon_list:
    print(emoticon)