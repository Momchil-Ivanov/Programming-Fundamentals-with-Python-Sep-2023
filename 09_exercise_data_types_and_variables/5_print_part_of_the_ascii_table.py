start_index = int(input())
end_index = int(input())

result = str()

for x in range (start_index, end_index + 1):
    result += chr(x) + " "

print(result)