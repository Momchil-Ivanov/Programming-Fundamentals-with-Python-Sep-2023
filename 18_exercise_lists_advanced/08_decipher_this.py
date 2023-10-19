text = input().split(" ")
result = ""

for word in text:
    current_num_char = ""
    index_counter = 0
    word_remainer = ""
    word_list = []
    for char in word:
        if 48 <= ord(char) <= 57:
            current_num_char += char
            index_counter += 1
        else:
            current_num_to_string = chr(int(current_num_char))
            for x in range (index_counter, len(word)):
                word_list.append(word[x])
            if len(word_list) > 1:
                first = word_list.pop(0)
                last = word_list.pop(-1)
                word_list.insert(0, last)
                word_list.append(first)
            word_list_to_string = "".join(word_list)
            final_string = current_num_to_string + word_list_to_string
            result += f"{final_string} "
            break
print(result.strip())