import re

number_of_strings = int(input())
pattern = r"@#+([A-Z][A-Za-z0-9]{4}[A-Za-z0-9]*[A-Z])@#+"
number_pattern = r"[0-9]*"
for x in range(0, number_of_strings):
    current_string = input()
    match_list = re.findall(pattern, current_string)
    if len(match_list) == 0:
        print("Invalid barcode")
    else:
        valid_string = match_list[0]
        match_number_list = re.findall(number_pattern, valid_string)
        while "" in match_number_list:
            match_number_list.remove("")
        if len(match_number_list) == 0:
            print("Product group: 00")
        else:
            result = ""
            for digit in match_number_list:
                result += digit
            print(f"Product group: {result}")