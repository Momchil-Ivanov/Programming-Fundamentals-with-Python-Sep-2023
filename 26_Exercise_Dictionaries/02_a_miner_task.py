command = input()
metrics_dict = {}

while command != "stop":

    item = command
    quantity = int(input())
    if item not in metrics_dict.keys():
        metrics_dict[item] = quantity
    else:
        metrics_dict[item] += quantity

    command = input()

for key in metrics_dict:
    print(f"{key} -> {metrics_dict[key]}")