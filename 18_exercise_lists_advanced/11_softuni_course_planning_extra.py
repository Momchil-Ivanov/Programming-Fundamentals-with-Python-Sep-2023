def softuni_planner():
    lessons_list = input().split(", ")

    command = str(input())
    while command != "course start":
        command_list = command.split(":")
        current_command = command_list[0]
        lesson_name = command_list[1]
        exercise_name = f"{command_list[1]}-Exercise"
        if current_command == "Add":
            if not lesson_name in lessons_list:
                lessons_list.append(command_list[1])
        elif current_command == "Insert":
            if not lesson_name in lessons_list:
                lessons_list.insert(int(command_list[2]), command_list[1])
        elif current_command == "Remove":
            if lesson_name in lessons_list:
                lessons_list.remove(command_list[1])
                if exercise_name in lessons_list:
                    lessons_list.remove(exercise_name)
        elif current_command == "Swap":
            exercise_name_second = f"{command_list[2]}-Exercise"
            lesson_name_second = command_list[2]
            if lesson_name in lessons_list and lesson_name_second in lessons_list:
                first_lesson_index = lessons_list.index(lesson_name)
                second_lesson_index = lessons_list.index(lesson_name_second)
                lessons_list[first_lesson_index], lessons_list[second_lesson_index] = \
                        lessons_list[second_lesson_index], lessons_list[first_lesson_index]
                if exercise_name in lessons_list:
                    exercise_name_index = lessons_list.index(exercise_name)
                    element = lessons_list.pop(exercise_name_index)
                    lessons_list.insert(second_lesson_index + 1, element)
                if exercise_name_second in lessons_list:
                    exercise_name_index = lessons_list.index(exercise_name_second)
                    element = lessons_list.pop(exercise_name_index)
                    lessons_list.insert(first_lesson_index + 1, element)
        elif current_command == "Exercise":
            if lesson_name in lessons_list:
                if exercise_name not in lessons_list:
                    lesson_index = lessons_list.index(lesson_name)
                    lesson_exercise_index = lesson_index + 1
                    lessons_list.insert(lesson_exercise_index, exercise_name)
            else:
                lessons_list.append(lesson_name)
                lessons_list.append(exercise_name)

        command = str(input())
    counter = 1

    for x in lessons_list:
        print(f"{counter}.{x}")
        counter += 1

result = softuni_planner()
result