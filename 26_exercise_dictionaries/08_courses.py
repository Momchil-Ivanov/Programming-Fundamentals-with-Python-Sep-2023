command = input()
courses_dict = {}

while command != "end":
    command_list = command.split(' : ')
    course = command_list[0]
    student = command_list[1]
    if course not in courses_dict.keys():
        courses_dict[course] = [student]
    else:
        courses_dict[course].append(student)
    command = input()

for key in courses_dict.keys():
    print(f"{key}: {len(courses_dict[key])}")
    for student_name in courses_dict[key]:
        print(f"-- {student_name}")