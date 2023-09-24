count_of_orders = int(input())
total_price = float()

for x in range (0, count_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= capsule_price <= 100 and \
        1 <= days <= 31 and \
        1 <= capsules_per_day <= 2000:
        current_price = capsule_price * days * capsules_per_day
        print(f"The price for the coffee is: ${current_price:.2f}")
    else:
        current_price = 0
    total_price += current_price

print(f"Total: ${total_price:.2f}")