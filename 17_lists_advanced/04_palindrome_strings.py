def palindrome_finder():
    words_list = input().split(" ")
    palindrome_list = []
    counter = 1
    for word in words_list:
        is_palindrome = True
        for char in word:
            if not char == word[len(word) - counter]:
                is_palindrome = False
            counter += 1
        counter = 1
        if is_palindrome:
            palindrome_list.append(word)
        else:
            is_palindrome = True
    print(palindrome_list)
    checked_palindrome = str(input())
    count_of_searched_palindrome = palindrome_list.count(checked_palindrome)
    print(f"Found palindrome {count_of_searched_palindrome} times")

result = palindrome_finder()
result