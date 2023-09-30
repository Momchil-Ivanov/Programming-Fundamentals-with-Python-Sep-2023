number = float(input())
size = str("")
value = str("")

if number == 0:
    value = "zero"
elif number > 0:
    value = "positive"
else:
    value = "negative"

if 0 < abs(number) < 1:
    size = "small"
elif abs(number) > 1000000:
    size = "large"

result = size + " " + value
print(result.strip())