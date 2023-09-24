count_of_strings = int(input())

for x in range (0, count_of_strings):
    current_string = str(input())

    if "," in current_string or \
            "." in current_string or \
            "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")