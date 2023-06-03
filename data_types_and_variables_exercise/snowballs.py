number_of_snowballs = int(input())

max_weight = 0
max_time = 0
max_value = 0
max_quality = 0

for snowballs in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    highest = (weight / time) ** quality
    if highest > max_value:
        max_weight = weight
        max_time = time
        max_quality = quality
        max_value = highest

print(f"{max_weight} : {max_time} = {max_value:.0f} ({max_quality})")