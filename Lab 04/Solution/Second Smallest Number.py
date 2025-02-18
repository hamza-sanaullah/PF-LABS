def distinct(x):
    l = []
    for i in x:
        if i not in l:
            l.append(i)
    return l
def second_smallest(List):
    s = distinct(List)
    sort_list = sorted(s)
    if len(sort_list) == 1:
        print(f"The second smallest element in the list is {sort_list[0]}")
    else:
        print(f"The second smallest element in the list is {sort_list[1]}")
list = eval(input("Enter a list to find smallest:"))
second_smallest(list)





