import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = float(0)
max_attendances = float(0)
max_attendances = math.ceil(max_attendances)
total_bonus = float(0)

if number_of_lectures > 0:
    for x in range(0, number_of_students):
        current_count_of_attendances = int(input())
        total_bonus = (current_count_of_attendances / number_of_lectures) * (5 + additional_bonus)
        if total_bonus > max_bonus and current_count_of_attendances > max_attendances:
            max_bonus = total_bonus
            max_attendances = current_count_of_attendances

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")