def factorial_divisor(numbers):
    for current_number in range(1, numbers):
        numbers *= current_number
    return numbers



first_number = int(input())
second_number = int(input())
first_number_factorial = factorial_divisor(first_number)
second_number_factorial = factorial_divisor(second_number)

result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")