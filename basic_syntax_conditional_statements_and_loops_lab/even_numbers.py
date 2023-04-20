number = int(input())

for i in range(number):
    number_1 = int(input())
    if not number_1 % 2 == 0:
        print(f"{number_1} is odd!")
        break
else:
    print("All numbers are even.")