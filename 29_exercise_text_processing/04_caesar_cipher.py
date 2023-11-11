input_text = input()
new_text = ""
for char in input_text:
    char_ascii = ord(char)
    new_char = chr(char_ascii + 3)
    new_text += new_char

print(new_text)