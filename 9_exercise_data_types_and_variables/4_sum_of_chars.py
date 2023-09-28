num_of_chars = int(input())
sum = int(0)

for x in range (0, num_of_chars):
    current_char = str(input())
    sum += ord(current_char)

print(f"The sum equals: {sum}")