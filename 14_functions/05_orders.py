def calculate_order(product: str, quantity: int):
    product_price = float(0)
    if product == "coffee":
        product_price = 1.50
    elif product == "water":
        product_price = 1.00
    elif product == "coke":
        product_price = 1.40
    elif product == "snacks":
        product_price = 2.00
    final_price = product_price * quantity
    return final_price

product_input = str(input())
quantity_input = int(input())

result = calculate_order(product_input, quantity_input)
print(f"{result:.2f}")