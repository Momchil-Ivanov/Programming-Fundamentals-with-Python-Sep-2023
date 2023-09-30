from math import ceil

people_count = int(input())
capacity_of_elevator = int(input())

num_of_courses = people_count / capacity_of_elevator

print(ceil(num_of_courses))