def is_perfect(random_number: int) -> str:
   divisor_sum = 0
   for divisor in range(1, random_number):
       if random_number % divisor == 0:
           divisor_sum += divisor

   if random_number == divisor_sum:
        return "We have a perfect number!"

   return "It's not so perfect."



number = int(input())
print(is_perfect(number))
