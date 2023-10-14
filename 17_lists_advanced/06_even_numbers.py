def even_numbers_index_finder(numbers: str):
    num_list = numbers.split(", ")
    even_num_indexes_list = []
    current_index = 0
    for num in num_list:
        if int(num) % 2 == 0:
            even_num_indexes_list.append(current_index)
        current_index += 1

    print(even_num_indexes_list)

real_input = str(input())
result = even_numbers_index_finder(real_input)
result