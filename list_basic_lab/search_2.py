number = int(input())
word = input()

lst_string = []

for i in range(number):
    text = input()
    lst_string.append(text)
print(lst_string)

for i in range(len(lst_string)-1,-1,-1):
    element_2 = lst_string[i]
    if word not in element_2:
        lst_string.remove(element_2)
print(lst_string)
