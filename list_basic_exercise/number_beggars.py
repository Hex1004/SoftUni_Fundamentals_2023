money_as_string = input().split(", ")
number_of_beggar = int(input())

money_as_diggit = []

for element in money_as_string :
    money_as_diggit.append(int(element))

final_result = []
start_index = 0

while start_index < number_of_beggar:
    sum_of_current_beggar = 0
    for current_index in range(start_index, len(money_as_diggit), number_of_beggar):
          sum_of_current_beggar += money_as_diggit[current_index]
    final_result.append(sum_of_current_beggar)
    start_index += 1
print(final_result)