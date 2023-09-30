current_name = str(input())

while current_name != "Welcome!":
    if current_name == "Voldemort":
        print("You must not speak of that name!")
        quit()

    if len(current_name) < 5:
        print(f"{current_name} goes to Gryffindor.")
    elif len(current_name) == 5:
        print(f"{current_name} goes to Slytherin.")
    elif len(current_name) == 6:
        print(f"{current_name} goes to Ravenclaw.")
    elif len(current_name) > 6:
        print(f"{current_name} goes to Hufflepuff.")

    current_name = str(input())

print("Welcome to Hogwarts.")