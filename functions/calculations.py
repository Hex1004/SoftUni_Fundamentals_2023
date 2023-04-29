text = input()
number_1 = int(input())
number_2 = int(input())

def calculation(a,b,operator):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a/b
    elif operator== "add":
        return a + b
    elif operator == "subtract":
        return a - b
print(f"{calculation(number_1 , number_2 , text):.0f}")