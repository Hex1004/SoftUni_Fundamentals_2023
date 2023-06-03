text = input().split(" ")
number = int(input())

for element in range(number):
    card_deck = []
    middle_of_the_deck = len(text) // 2
    left_part = text[0:middle_of_the_deck]
    right_part = text[middle_of_the_deck:]


    for card in range(len(right_part)):
        card_deck.append(left_part[card])
        card_deck.append(right_part[card])
        text = card_deck
print(card_deck)

