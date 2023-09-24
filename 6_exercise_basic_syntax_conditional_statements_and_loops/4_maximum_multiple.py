divisor = int(input())
bound_num = int(input())

while bound_num > 0:
    if bound_num % divisor == 0:
        print(bound_num)
        quit()
    bound_num -= 1