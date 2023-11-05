text = input()
text_dict = {}

for char in text:
    if char != " ":
        if char not in text_dict.keys():
            text_dict[char] = 1
        else:
            text_dict[char] += 1

for key in text_dict:
    print(f"{key} -> {text_dict[key]}")