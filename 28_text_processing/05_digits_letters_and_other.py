current_string = input()
numbers = ""
letters = ""
symbols = ""

for char in current_string:
    char_to_ascii = ord(char)
    if 48 <= char_to_ascii <= 57:
        numbers += char
    elif 65 <= char_to_ascii <= 90 or 97 <= char_to_ascii <= 122:
        letters += char
    else:
        symbols += char

print(numbers)
print(letters)
print(symbols)