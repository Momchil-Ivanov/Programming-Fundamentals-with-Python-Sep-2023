filepath_list = input().split("\\")
file = ""
for part in filepath_list:
    if "." in part:
        file = part
file_list = file.split(".")
file_name = file_list[0]
file_extension = file_list[1]
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")