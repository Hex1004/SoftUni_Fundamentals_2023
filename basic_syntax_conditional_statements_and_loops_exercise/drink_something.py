age = int(input())

drink = ["drink toddy","drink coke","drink beer","drink whisky"]

if age <=14:
    print(drink[0])
elif age <= 18:
    print(drink[1])
elif age<=21:
    print(drink[2])
elif age > 21:
    print(drink[3])

