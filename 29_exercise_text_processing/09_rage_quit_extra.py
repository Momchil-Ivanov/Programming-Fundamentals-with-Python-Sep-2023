text_input = input()
text_input_list = []
rage_text_list = []
sequence = ""
multiplier = ""

for char in text_input:
    text_input_list.append(char)

for x in range(0, len(text_input_list)):
    if not text_input_list[x].isnumeric():
        sequence += text_input_list[x]

    else:
        multiplier += text_input_list[x]
        if x == len(text_input_list) - 1 or not text_input_list[x + 1].isnumeric():
            sequence = sequence.upper()
            sequence = sequence * int(multiplier)
            rage_text_list.append(sequence)
            sequence = ""
            multiplier = ""

rage_text_string = "".join(rage_text_list)
unique_chars = len(set(rage_text_string))

print(f"Unique symbols used: {unique_chars}")
print(rage_text_string)