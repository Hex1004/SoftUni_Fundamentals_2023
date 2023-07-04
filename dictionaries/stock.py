elements = input().split(" ")

bakery = {}

for  i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

searched_for_product = input().split(" ")

for products in searched_for_product:
    if products in bakery:
        print(f"We have {bakery[products]} of {products} left")
    else:
        print(f"Sorry, we don't have {products}")