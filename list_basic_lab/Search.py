number = int(input())
word = input()

lst = []

for i in range(number):
    text = input()
    lst.append(text)
print(lst)

for i in range(len(lst) -1,-1,-1):
    element = lst[i]
    if word  not in element:
        lst.remove(element)
print(lst)