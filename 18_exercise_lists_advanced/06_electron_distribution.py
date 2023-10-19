def electron_distributer(electron_num: int):
    electron_list = []
    n = 1
    while electron_num > 0:
        if electron_num >= 2 * n ** 2:
            current_electron_count = 2 * n ** 2
        else:
            current_electron_count = electron_num
        electron_list.append(current_electron_count)
        electron_num -= current_electron_count
        n += 1
    print(electron_list)

current_electron_num = int(input())
result = electron_distributer(current_electron_num)
result