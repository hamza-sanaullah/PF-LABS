larger_number= lambda x,y: x  if (x>y) else y
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print(f"{larger_number(x,y)} is greater")
def Table(d = larger_number(x,y)):
    start = int(input("Enter the starting range for table:"))
    end = int(input("Enter the ending range for the table:"))
    for i in range(start,end+1):
        print(f"{d} * {i} = {d*i}")

Table()

#ANOTHER METHOD
q = lambda x,y: x  if (x>y) else y
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print(f"{q(x,y)} is greater")
def Table(NUM,START,END):

    for i in range(START,END+1):
        print(f"{NUM} * {i} = {NUM*i}")
LARGEST_NUMBER = q(x,y)
start = int(input("Enter the starting value for the table:"))
end = int(input("Enter the ending vlaue for the table:"))
Table(LARGEST_NUMBER,start,end)
print("The table of the greater number is shown above")