number = int(input())

for x in range (1, number + 1):
    current_sum = sum(int(digit) for digit in str(x))
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        print(f"{x} -> True")
    else:
        print(f"{x} -> False")