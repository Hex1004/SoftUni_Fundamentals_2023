numbers = int(input())

positive = []
negative = []

for n in range(numbers):
    current_number = int(input())
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}\nSum of negatives: {sum(negative)}")