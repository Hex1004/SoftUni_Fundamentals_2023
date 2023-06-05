number_string = input().split()

sorted_numbers = []

for number in number_string:
    sorted_numbers.append(int(number))

sorted_n = sorted(sorted_numbers)

print(sorted_n)