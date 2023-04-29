number = input() .split(' ')

lst_number = []

for num in number:
     lst_number.append(abs(float(num)))

print(lst_number)