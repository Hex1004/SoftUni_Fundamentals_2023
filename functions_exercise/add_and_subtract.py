def sum_numbers(first,second):
    return first_number + second_number

def subtract(sum, third):
    return sum - third

def add_and_subtract(number_1, number_2, number_3):
    sum_of_first_two_numbers = sum_numbers(number_1,number_2)
    total = subtract(sum_of_first_two_numbers,number_3)
    print(total)


first_number = int(input())
second_number = int(input())
third_number = int(input())

add_and_subtract(first_number, second_number, third_number)