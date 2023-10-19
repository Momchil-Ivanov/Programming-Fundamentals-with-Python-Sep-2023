def ten_grouper(numbers: str):
    numbers_list = numbers.split(", ")
    numbers_list_int = list(map(int, numbers_list))
    decimal_num = 1
    decimal_num_prev = 0
    current_ten = str(decimal_num) + str(0)
    previous_ten = str(decimal_num_prev) + str(0)
    while int(max(numbers_list_int)) + 9 >= int(current_ten):
        current_list = [x for x in numbers_list_int if int(previous_ten) < x <= int(current_ten)]
        print(f"Group of {current_ten}'s: {current_list}")
        decimal_num += 1
        decimal_num_prev += 1
        current_ten = str(decimal_num) + str(0)
        previous_ten = str(decimal_num_prev) + str(0)

current_numbers = str(input())
result = ten_grouper(current_numbers)
result