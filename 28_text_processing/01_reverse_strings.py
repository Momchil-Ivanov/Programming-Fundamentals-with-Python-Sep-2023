current_word = input()
words_list = []
while current_word != "end":
    words_list.append(current_word)
    current_word = input()

for word in words_list:
    print(f"{word} = {word[::-1]}")