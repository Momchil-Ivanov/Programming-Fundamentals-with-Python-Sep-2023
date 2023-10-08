def palindrome_checker(numbers: str):
    numbers_list = numbers.split(", ")
    for number in numbers_list:
        current_number = int(number)
        reversed_number = int(number[::-1])
        if current_number == reversed_number:
            print("True")
        else:
            print("False")

real_input = str(input())
result = palindrome_checker(real_input)
result