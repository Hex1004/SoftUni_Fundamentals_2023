budget = int(input())
command = input()

lst = ["You went in overdraft!", "You bought everything needed.", "End"]

while command != lst[2]:
    price_for_product = int(command)
    budget -= price_for_product
    if budget < 0:
        print(lst[0])
        break
    command = input()
else:
    print(lst[1])
