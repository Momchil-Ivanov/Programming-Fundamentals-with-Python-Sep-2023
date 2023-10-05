def rounder (numbers: str):
    number_list = numbers.split()
    rounded_list = []
    for x in number_list:
        rounded_list.append(round(float(x)))
    return rounded_list
string_input = str(input())
result = rounder(string_input)
print(result)