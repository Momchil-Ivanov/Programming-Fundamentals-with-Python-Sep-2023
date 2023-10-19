sequence_of_elements = str(input()).split(" ")
# print(sequence_of_elements)
command = str(input())
number_of_moves = int(1)

while command != "end":
    command_list = command.split(" ")
    first_index = int(command_list[0])
    second_index = int(command_list[1])

    if first_index == second_index or first_index < 0 or first_index > len(sequence_of_elements) - 1 \
        or second_index < 0 or second_index > len(sequence_of_elements) - 1:
        index_on_half = int(len(sequence_of_elements) / 2)
        sequence_of_elements.insert(index_on_half, f"-{number_of_moves}a")
        sequence_of_elements.insert(index_on_half, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
            print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
            if first_index < second_index:
                sequence_of_elements.pop(first_index)
                sequence_of_elements.pop(second_index - 1)
            else:
                sequence_of_elements.pop(second_index)
                sequence_of_elements.pop(first_index - 1)
            if len(sequence_of_elements) == 0:
                print(f"You have won in {number_of_moves} turns!")
                quit()
        else:
            print("Try again!")

    # print(sequence_of_elements)
    number_of_moves += 1
    command = str(input())

print("Sorry you lose :(")
print(" ".join(sequence_of_elements))