first_number = int(input())
second_number = int(input())

lst = []

for char in range(1, second_number + 1):
    lst.append(first_number * char)
print(lst)