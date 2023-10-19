def next_version_finder(version: str):
    version_list = version.split(".")
    primary_index = int(version_list[0])
    secondary_index = int(version_list[1])
    third_index = int(version_list[2])

    if third_index < 9:
        third_index += 1
    else:
        third_index = 0
        if secondary_index < 9:
            secondary_index += 1
        else:
            secondary_index = 0
            primary_index += 1

    print(f"{primary_index}.{secondary_index}.{third_index}")

index = str(input())
result = next_version_finder(index)
result