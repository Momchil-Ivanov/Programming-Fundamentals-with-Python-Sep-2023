def all_ascii_chars_between_two(first_char: str, second_char: str):
    first_char_ascii = ord(first_char)
    second_char_ascii = ord(second_char)
    char_list = []

    for x in range(first_char_ascii + 1, second_char_ascii):
        current_char = chr(x)
        char_list.append(current_char)
    return char_list

first_character = str(input())
second_character = str(input())
result = all_ascii_chars_between_two(first_character, second_character)
print(" ".join(result))