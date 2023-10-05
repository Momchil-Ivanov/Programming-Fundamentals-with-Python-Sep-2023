def rectangle_area_calculator (width: int, height: int):
    result = int(width * height)
    return result

width_input = int(input())
height_input = int(input())

result_output = rectangle_area_calculator(width_input, height_input)
print(result_output)