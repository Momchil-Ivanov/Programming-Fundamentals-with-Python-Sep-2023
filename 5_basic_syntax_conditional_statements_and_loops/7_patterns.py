num = int(input())
stars = str()

for x in range (0, num):
    stars = stars + "*"
    print(stars)
for x in range (1, num):
    stars = stars[:-1]
    print(stars)