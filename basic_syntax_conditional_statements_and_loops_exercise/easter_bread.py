budget = float(input())
price_for_1_kilogram = float(input())

eggs_price = price_for_1_kilogram * 0.75
milk_one = (price_for_1_kilogram * 1.25) / 4
colored_egg = 0

for bread in range(1, int(budget) +1):
    if eggs_price + milk_one + price_for_1_kilogram <= budget:
        budget -= (eggs_price + milk_one + price_for_1_kilogram)
        colored_egg += 3
        if bread % 3 == 0:
            colored_egg -= (bread - 2)
    else:
        print(f"You made {bread - 1} loaves of Easter bread! Now you have {colored_egg} eggs and {budget:.2f}BGN left.")
        break