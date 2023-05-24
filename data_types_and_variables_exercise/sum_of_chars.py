data = int(input())

total = 0

for char in range(data):
    simbols = input()

    total+= ord(simbols)

print(f"The sum equals: {total}")