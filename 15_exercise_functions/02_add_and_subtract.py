def sum_numbers(first_num: int, second_num: int):
    return first_num + second_num
def subtract(result_num, third_num):
    return result_num - third_num

def add_and_subtract(first_num, second_num, third_num):
    added = sum_numbers(first_num, second_num)
    subtracted = subtract(added, third_num)
    return subtracted

first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)
