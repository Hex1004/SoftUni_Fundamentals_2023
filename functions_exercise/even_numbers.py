number_string = input().split()

even_lst = []


for number in number_string:
    even_lst.append(int(number))

even = lambda number: number % 2 == 0

total = list(filter(even, even_lst))

print(total)





