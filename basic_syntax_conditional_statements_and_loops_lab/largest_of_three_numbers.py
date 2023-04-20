number = int(input())
second_number = int(input())
third_number = int(input())

if number > second_number and second_number> third_number:
    print(number)
elif second_number > number and second_number > third_number:
    print(second_number)
else:
    print(third_number)