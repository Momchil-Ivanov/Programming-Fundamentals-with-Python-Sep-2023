def perfect_number_checker(checked_number: int):
    perfect_sum = int(0)
    for x in range(1, checked_number):
        if checked_number % x == 0:
            perfect_sum += x

    if perfect_sum == checked_number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

real_input = int(input())
result = perfect_number_checker(real_input)
result