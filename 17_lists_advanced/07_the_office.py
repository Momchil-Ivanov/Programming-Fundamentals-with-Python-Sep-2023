def happiness_meter():
    employees_list = input().split(" ")
    factor = int(input())
    new_list = []
    total_score = 0
    for x in employees_list:
        current_score = factor * int(x)
        new_list.append(current_score)
        total_score +=  current_score

    average_score = total_score / len(new_list)
    happy = 0
    not_happy = 0
    for x in new_list:
        if int(x) >= average_score:
            happy += 1
        else:
            not_happy += 1
    if happy >= not_happy:
        print(f"Score: {happy}/{len(new_list)}. Employees are happy!")
    else:
        print(f"Score: {happy}/{len(new_list)}. Employees are not happy!")

result = happiness_meter()
result