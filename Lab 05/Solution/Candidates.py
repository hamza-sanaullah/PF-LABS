engineering = {"Hamza","Salman","Bilal","Sajjad","Saad","Zain","Ahmad","Adeel","Shahbaz","Hammad"}
Non_engineering = {"Umer","Anas","Hamza","Sajjad","Zain","Adeel","Saad","Abdul Rehman","Usman","shafiq"}
both_programs = engineering.intersection(Non_engineering)
#print(both_programs)
count = 0
print(f"CANDIDATES APPLIED IN BOTH PROGRAMS ARE GIVEN BELOW:")
for item in both_programs:

    print(item)
    count+=1
print(f"The NUMBER OF STUDENTS APLIED IN BOTH PROGRAMS ARE {count}")
list1 = list(engineering)
List2 = list(Non_engineering)
list_ = list1 + List2
count = 0
for item in list_:
    count+=1
print(f"The TOTAL NUMBER OF STUDENTS APPLIED IN UET ARE  {count}")










