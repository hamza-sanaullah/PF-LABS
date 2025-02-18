list_inp = eval(input("Enter a list with a duplicate elemnts"))
new_list = []
for item in list_inp:
    if item not in new_list:
        new_list.append(item)
print(new_list)

#TASK 1 BY LIST COMPREHENSON METHOD
list_inp = eval(input("Enter a list with a duplicate numbers"))
new_list = []
[new_list.append(item) for item in list_inp if item not in new_list]
print(new_list)






