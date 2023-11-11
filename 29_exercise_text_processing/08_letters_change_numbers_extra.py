text_input_list = input().split()
sum = 0

for part in text_input_list:
    first_letter = part[0]
    second_letter = part[len(part) - 1]
    number = int(part[1:len(part) - 1])
    # Using ASCII values to determine if first and second letters are upper- or lower-case
    # If ASCII value is smaller than 91 then letter is uppercase, else it is lowercase
    if ord(first_letter) < 91:
        first_letter_position = ord(first_letter) - 64
        number /= first_letter_position
    else:
        first_letter_position = ord(first_letter) - 96
        number *= first_letter_position

    if ord(second_letter) < 91:
        second_letter_position = ord(second_letter) - 64
        number -= second_letter_position
    else:
        second_letter_position = ord(second_letter) - 96
        number += second_letter_position

    sum += number


print(f"{sum:.2f}")