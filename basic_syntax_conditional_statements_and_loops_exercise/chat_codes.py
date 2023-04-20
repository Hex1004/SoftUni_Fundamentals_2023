number_of_message = int(input())
message_lst = ["Hello","How are you?","GREAT!","Bye."]

for _ in range(number_of_message):
    number = int(input())

    if number == 88:
       print(message_lst[0])

    elif number == 86:
       print(message_lst[1])

    elif number < 88:
       print(message_lst[2])

    else:
      print(message_lst[3])

