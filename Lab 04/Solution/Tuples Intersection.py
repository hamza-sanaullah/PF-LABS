def intersect(t1,t2):
    d = list()
    for i in (t1):
        for j in (t2):
            if i==j:
                d.append(i)

    return tuple(d)
Tuple_1 = eval(input("ENTER THE TUPLE ONE:"))
Tuple_2= eval(input("ENTER THE TUPLE TWO:"))
print(intersect(Tuple_1,Tuple_2))