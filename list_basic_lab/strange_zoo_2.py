head = input()
body = input()
tail = input()

lst = [head, body, tail]

lst[0], lst[2] = lst[2], lst[0]

print(lst)