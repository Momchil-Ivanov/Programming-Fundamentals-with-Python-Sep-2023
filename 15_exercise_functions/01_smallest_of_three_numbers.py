def return_smallest_of_three (first_num: int, second_num: int, third_num: int):
    list_three_nums = (first_num, second_num, third_num)
    smallest_num = min(list_three_nums)
    return smallest_num

first_number = int(input())
second_number = int(input())
third_number = int(input())

smallest_number = return_smallest_of_three(first_number, second_number, third_number)
print(smallest_number)