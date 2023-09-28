n = int(input())
symbol_x = 97
symbol_y = 97
symbol_z = 97

for x in range (0, n):
    for y in range (0, n):
        for z in range (0, n):
            print(chr(symbol_x)+chr(symbol_y)+chr(symbol_z))
            symbol_z += 1
        symbol_z = 97
        symbol_y += 1
    symbol_y = 97
    symbol_x += 1