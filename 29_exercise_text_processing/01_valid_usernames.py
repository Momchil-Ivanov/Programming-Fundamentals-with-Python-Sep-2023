usernames_list = input().split(', ')
valid_usernames_list = []

for username in usernames_list:
    if len(username) < 3 or len(username) > 16:
        continue
    current_username = username
    current_username = current_username.replace("_","")
    current_username = current_username.replace("-","")
    if current_username.isalnum():
        valid_usernames_list.append(username)

for username in valid_usernames_list:
    print(username)