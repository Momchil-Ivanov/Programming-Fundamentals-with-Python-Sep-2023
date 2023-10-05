def calculator (command: str, first_num: float, second_num: float):
    result = float(0)

    if command == "multiply":
        result = first_num * second_num
    elif command == "divide":
        if second_num == 0:
            result = str("Error")
        else:
            result = first_num / second_num
    elif command == "add":
        result = first_num + second_num
    elif command == "subtract":
        result = first_num - second_num
    else:
        result = str("N/A")

    return result

command_input = str(input())
first_num_input = float(input())
second_num_input = float(input())

result_output = calculator(command_input, first_num_input, second_num_input)
print(int(result_output))