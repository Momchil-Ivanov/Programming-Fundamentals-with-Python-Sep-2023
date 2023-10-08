def factorial_divider(first_num: int, second_num: int):
    first_factorial = 1
    second_factorial = 1
    for x in range(1, first_num + 1):
        first_factorial *= x
    for y in range(1, second_num + 1):
        second_factorial *= y

    factorial_result = first_factorial / second_factorial
    print(f"{factorial_result:.2f}")

first_number_argument = int(input())
second_number_argument = int(input())
result = factorial_divider(first_number_argument, second_number_argument)
result