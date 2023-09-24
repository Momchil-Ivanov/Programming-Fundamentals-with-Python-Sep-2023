quantity = int(input())
days = int(input())

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17
total_cost = int(0)
total_spirit = int(0)

for current_day in range (1, days + 1):
    if current_day % 11 == 0:
        quantity += 2

    if current_day % 2 == 0:
        total_cost += quantity * ornament_set_price
        total_spirit += ornament_set_points

    if current_day % 3 == 0:
        total_cost += quantity * tree_skirt_price
        total_spirit += tree_skirt_points
        total_cost += quantity * tree_garland_price
        total_spirit += tree_garland_points

    if current_day % 5 == 0:
        total_cost += quantity * tree_lights_price
        total_spirit += tree_lights_points
        if current_day % 3 == 0:
            total_spirit += 30

    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")