def min_max_sum(input: str):
    num_list = input.split()
    num_list = list(map(int, num_list))
    mins = min(num_list)
    maxs = max(num_list)
    sums = sum(num_list)

    return mins, maxs, sums

real_input = str(input())
result = min_max_sum(real_input)
print(f"The minimum number is {result[0]}")
print(f"The maximum number is {result[1]}")
print(f"The sum number is: {result[2]}")