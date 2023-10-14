def sorting_names():
    the_list = input().split(", ")
    the_list.sort() # sorts normally by alphabetical order
    the_list.sort(key=len, reverse=True) # sorts by descending length
    print(the_list)

result = sorting_names()
result