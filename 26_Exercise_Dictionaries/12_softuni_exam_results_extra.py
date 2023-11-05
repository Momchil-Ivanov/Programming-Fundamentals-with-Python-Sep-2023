command = input()
courses_dict = {}
students_dict = {}
while command != "exam finished":
    command_list = command.split('-')
    name = command_list[0]
    course = command_list[1]
    if course == "banned":
        del students_dict[name]
        command = input()
        continue
    else:
        score = int(command_list[2])
        if name not in students_dict.keys():
            students_dict[name] = score
        else:
            if score > students_dict[name]:
                students_dict[name] = score
    if course not in courses_dict.keys():
        courses_dict[course] = 1
    else:
        courses_dict[course] += 1
    command = input()
print("Results:")
for student in students_dict:
    print(f"{student} | {students_dict[student]}")
print("Submissions:")
for each_course in courses_dict:
    print(f"{each_course} - {courses_dict[each_course]}")