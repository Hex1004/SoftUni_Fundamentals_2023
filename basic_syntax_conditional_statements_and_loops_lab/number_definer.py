number = float(input())

number_lst = ["zero", "positive", "negative", "small", "large", "small positive", "large positive", "small negative", "large negative"]

if number == 0:
 print(number_lst[0])
elif number > 0:
  if number < 1:
   print(number_lst[5])
  elif number > 1_000_000:
      print(number_lst[6])
  else:
      print(number_lst[1])
else:
    if abs(number) < 1:
      print(number_lst[7])
    elif abs(number) > 1_000_000:
      print(number_lst[8])
    else:
      print(number_lst[2])

