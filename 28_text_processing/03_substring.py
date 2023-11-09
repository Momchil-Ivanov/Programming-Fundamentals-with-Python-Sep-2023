string_to_remove = input()
string_to_check = input()

while string_to_remove in string_to_check:
    string_to_check = string_to_check.replace(string_to_remove,"")

print(string_to_check)