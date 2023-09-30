pours_count = int(input())
capacity = int(0)

for x in range (0, pours_count):
    current_pour = int(input())
    if current_pour + capacity > 255:
        print("Insufficient capacity!")
    else:
        capacity += current_pour

print(capacity)