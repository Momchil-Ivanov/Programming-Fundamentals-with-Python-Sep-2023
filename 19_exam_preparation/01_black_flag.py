days_pirating_lasts = int(input())
plunder_amount_per_day =  int(input())
expected_plunder = float(input())
total_plunder = float(0)

for x in range(1, days_pirating_lasts + 1):
    if x % 3 == 0:
        total_plunder += plunder_amount_per_day * 1.50
    else:
        total_plunder += plunder_amount_per_day
    if x % 5 == 0:
        total_plunder -= total_plunder * 0.30

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage_of_total_plunder = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage_of_total_plunder:.2f}% of the plunder.")