price_ratings = [int(x) for x in input().split(", ")]
entry_point = int(input())
type_of_items = input()

left_side = sum(price_ratings[:entry_point])
right_side = sum(price_ratings[entry_point + 1:])

if type_of_items == "cheap":
    left_side = sum(x for x in price_ratings[:entry_point] if x < price_ratings[entry_point])
    right_side = sum(x for x in price_ratings[entry_point + 1:] if x < price_ratings[entry_point])
elif type_of_items == "expensive":
    left_side = sum(x for x in price_ratings[:entry_point] if x >= price_ratings[entry_point])
    right_side = sum(x for x in price_ratings[entry_point + 1:] if x >= price_ratings[entry_point])

if left_side >= right_side:
    print(f"Left - {left_side}")
else:
    print(f"Right - {right_side}")






