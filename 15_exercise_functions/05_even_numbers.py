def even_numbers_identificator(numbers: str):
    list_numbers = numbers.split(" ")
    result_list = []
    for x in range(0, len(list_numbers)):
        current_number = int(list_numbers[x])
        if current_number % 2 == 0:
            result_list.append(current_number)

    return result_list

numbers_input = str(input())
result = even_numbers_identificator(numbers_input)
print(result)