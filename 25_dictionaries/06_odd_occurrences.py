sequence_of_words = input().split()
words_dict = {}

for word in sequence_of_words:
    word = word.lower()
    if word not in words_dict.keys():
        words_dict[word] = 1
    else:
        words_dict[word] += 1
result = ""
for key in words_dict:
    if words_dict[key] % 2 != 0:
        result += f"{key} "

result.strip()
print(result)