def to_do_list(command: str):
    initial_list = []
    while command != "End":
        initial_list.append(command)
        command = str(input())

    initial_list.sort(reverse=True)
    final_list = []

    for sequence in initial_list:
        sequence_list = sequence.split("-")
        if int(sequence_list[0]) == 10:
            final_list.insert(0, sequence_list[1])
        else:
            final_list.append(sequence_list[1])

    final_final_list = []
    count_final_final_list = int(len(final_list)) - 1
    for x in range(count_final_final_list, -1, -1):
        final_final_list.append(final_list[x])

    print(final_final_list)

real_input = str(input())
result = to_do_list(real_input)
result