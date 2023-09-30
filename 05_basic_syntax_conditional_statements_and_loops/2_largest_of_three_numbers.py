first_num = int(input())
second_num = int(input())
third_num = int(input())

largest_number = int(0)

if first_num > second_num and first_num > third_num:
    largest_number = first_num
elif second_num > first_num and second_num > third_num:
    largest_number = second_num
else:
    largest_number = third_num

print(largest_number)