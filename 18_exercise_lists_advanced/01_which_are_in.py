def sub_string_finder (sub_string_line: str, string_line: str):
    sub_string_list = sub_string_line.split(", ")

    found_sub_strings_list = [x for x in sub_string_list if x in string_line]
    print(found_sub_strings_list)

current_sub_string_input = str(input())
current_string_input = str(input())
result = sub_string_finder(current_sub_string_input, current_string_input)
result