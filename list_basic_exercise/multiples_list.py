first_number = int(input())
second_number = int(input())

lst_number = []

for current_number in range(1, second_number + 1):
    lst_number.append(first_number * current_number)
print(lst_number)