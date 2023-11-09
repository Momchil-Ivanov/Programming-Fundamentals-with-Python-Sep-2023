pairs_num = int(input())
students_dict = {}

for _ in range(pairs_num):
    name = input()
    grade = float(input())

    if name not in students_dict.keys():
        students_dict[name] = [grade]
    else:
        students_dict[name].append(grade)

for student in students_dict.keys():
    average_grade = sum(students_dict[student]) / len(students_dict[student])
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")