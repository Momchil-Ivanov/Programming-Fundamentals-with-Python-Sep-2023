distances = [int(x) for x in input().split(" ")]
sum = int(0)

while len(distances) > 0:
    current_index = int(input())
    first_index_value = int(distances[0])
    last_index_value = int(distances[len(distances) - 1])
    if current_index < 0:
        current_value = first_index_value
        del distances[0]
        distances.insert(0, last_index_value)
    elif current_index > len(distances) - 1:
        current_value = last_index_value
        distances.insert(len(distances)-1, first_index_value)
        del distances[len(distances)-1]
    else:
        current_value = int(distances[current_index])
        del distances[current_index]
    sum += current_value
    for x in range(0, len(distances)):
        if distances[x] <= current_value:
            distances[x] += current_value
        else:
            distances[x] -= current_value

print(sum)