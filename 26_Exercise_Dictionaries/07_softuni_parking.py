num_of_operations = int(input())
registrations_dict = {}
for _ in range(num_of_operations):
    command_list = input().split()
    operation = command_list[0]
    username = command_list[1]

    if operation == "register":
        if username not in registrations_dict.keys():
            license_plate_number = command_list[2]
            registrations_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {registrations_dict[username]}")
    elif operation == "unregister":
        if username not in registrations_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            registrations_dict.pop(username)
            print(f"{username} unregistered successfully")

for key in registrations_dict.keys():
    print(f"{key} => {registrations_dict[key]}")