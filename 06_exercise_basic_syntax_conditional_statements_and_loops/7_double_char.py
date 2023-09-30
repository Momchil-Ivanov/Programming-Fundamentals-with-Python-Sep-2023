current_string = str(input())
result = str()

while current_string != "End":
    if current_string != "SoftUni":
        for x in range(0, len(current_string)):
            result += current_string[x] + current_string[x]
        print(result)
        result = str()

    current_string = str(input())