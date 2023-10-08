def password_validator(password: str):
    valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        valid = False
    for digit in password:
        value = ord(digit)
        if value < 48 or 57 < value < 65 or 90 < value < 97 or value > 122:
            print("Password must consist only of letters and digits")
            valid = False
            break
    digit_counter = 0
    for digit in password:
        value = ord(digit)
        if 48 <= value <= 57:
            digit_counter += 1
    if digit_counter < 2:
        valid = False
        print("Password must have at least 2 digits")
    if valid:
        print("Password is valid")

real_input = str(input())
result = password_validator(real_input)
result