number_of_snowballs = int(input())
best_value = 0

for x in range (0, number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())

    current_value = (current_weight / current_time) ** current_quality
    if current_value > best_value:
        best_value = int(current_value)
        best_weight = current_weight
        best_time = current_time
        best_quality = current_quality

print(f"{best_weight} : {best_time} = {best_value} ({best_quality})")