def word_filter_by_even_lenght(words: str):
    words_list = words.split(" ")
    words_list_even = [x for x in words_list if len(x) % 2 == 0]
    for x in words_list_even:
        print(x)

current_words = str(input())
result = word_filter_by_even_lenght(current_words)
result