event = str(input())
coffee_count = int()

while event != "END":
    if event.isupper():
        if event == "CODING" or \
            event == "DOG" or \
            event == "CAT" or \
            event == "MOVIE":
            coffee_count += 2
    else:
        if event == "coding" or \
            event == "dog" or \
            event == "cat" or \
            event == "movie":
            coffee_count += 1
    if coffee_count > 5:
        print("You need extra sleep")
        quit()
    event = str(input())
print(coffee_count)