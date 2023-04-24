text_1 = input()
text_2 = input()
text_3 = input()

lst = [text_1,text_2,text_3]

lst[0], lst[2] = lst[2], lst[0]

print(lst)