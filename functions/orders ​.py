text = input()
numbers = int(input())

name = ["coffee","water","coke","snacks"]

price = [1.50,1.00,1.40,2.00]

def oder(sum_1):
    if text == name[0]:
        sum_1 = numbers * price[0]
    elif text == name[1]:
        sum_1 = numbers * price[1]
    elif text == name[2]:
        sum_1 = numbers * price[2]
    elif text == name[3]:
        sum_1 = numbers * price[3]
    return f"{sum_1:.2f}"

print(oder(numbers))