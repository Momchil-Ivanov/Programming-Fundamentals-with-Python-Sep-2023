def sort_numbers(text: str):
    list_of_numbers = text.split(" ")
    list_of_numbers = list(map(int, list_of_numbers))
    list_of_numbers = sorted(list_of_numbers)
    return list_of_numbers

real_input = str(input())
result = sort_numbers(real_input)
print(result)