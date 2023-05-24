from math import ceil

number_of_elevate_person = int(input())
number_of_capacity_person = int(input())

total = ceil(number_of_elevate_person/ number_of_capacity_person)

print(total)