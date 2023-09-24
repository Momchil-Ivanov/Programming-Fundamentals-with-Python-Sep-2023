number_of_nums = int(input())

for x in range (0,number_of_nums):
    current_num = int(input())
    if current_num % 2 == 1:
        print(f"{current_num} is odd!")
        quit()

print("All numbers are even.")