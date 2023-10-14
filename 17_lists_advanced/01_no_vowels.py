def vowel_remover (text_to_edit: str):
    text_to_list = []
    for symbol in text_to_edit:
        text_to_list.append(symbol)
    text_without_vowels = [symbol for symbol in text_to_list if symbol != "a" and\
                           symbol != "A" and symbol != "o" and symbol != "O" and\
                           symbol != "u" and symbol != "U" and symbol != "e" and\
                           symbol != "E" and symbol != "i" and symbol != "I"]
    print("".join(text_without_vowels))

real_input = str(input())
result = vowel_remover(real_input)
result