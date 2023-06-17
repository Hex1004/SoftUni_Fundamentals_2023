
lst_tasks = []

while True:
   to_do = input()
   if to_do == "End":
     break

   lst_tasks.append(to_do)

sorted_notes = sorted(lst_tasks, key=lambda x: int(x.split("-")[0]))
result_sorted_notes = [to_do.split("-")[1] for to_do in sorted_notes]



print(result_sorted_notes)

# def process_todo_notes():
#    lst_tasks = []
#
#    while True:
#      to_do = input()
#      if to_do == "End":
#        break
#
#      lst_tasks.append(to_do)
#
#    sorted_notes = sorted(lst_tasks, key=lambda x: int(x.split("-")[0]))
#    result_sorted_notes = [to_do.split("-")[1] for to_do in sorted_notes]
#    return result_sorted_notes
#
# result  = process_todo_notes()
# print(result)