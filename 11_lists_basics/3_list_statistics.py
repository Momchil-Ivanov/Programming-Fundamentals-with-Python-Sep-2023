count_of_nums = int(input())

positive_list = []
negative_list = []
count_of_positives = int(0)
sum_of_negatives = int(0)

for x in range (0, count_of_nums):
    current_num = int(input())
    if current_num >= 0:
        positive_list.append(current_num)
        count_of_positives += 1
    else:
        negative_list.append(current_num)
        sum_of_negatives += current_num

print(positive_list)
print(negative_list)
print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {sum_of_negatives}")