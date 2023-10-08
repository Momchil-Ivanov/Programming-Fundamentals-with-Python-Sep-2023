def sum_odd_and_even_digits(input: str):
    even_sum = int(0)
    odd_sum = int(0)
    for x in range(0, len(input)):
        current_number = int(input[x])
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number

    return odd_sum, even_sum

practical_input = str(input())
result = sum_odd_and_even_digits(practical_input)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")