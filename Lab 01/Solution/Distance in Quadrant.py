#Write a program that takes two points from the user in the form of(x1, y1)and (x2, y2) and tell their quadrants and
# distance between them by using distance formula as given below
import math
first_point = input("Enter the fisrt point in the form of (x,y):")
second_point = input("Enter the second point in the form of (x,y):")
"""To get the values of x1 and y1"""
s = first_point.find(",")
x1 = (first_point[1:s])
j = len(first_point)
y1 = (first_point[s+1:j-1])
print(f"The Values of x1 and y1 are (x1,y1) {x1,y1}")
"""To get the values of x2 and y2"""
h = second_point.find(",")
x2 = (second_point [1:h])
i = len(second_point)
y2 = (second_point[h+1:i-1])
print(f"The Values of x2 and y2 are (x2,y2) {x2,y2}")
#Quadrant checking
def quad_check(x,y):
    if int(x)>0 and int(y)>0 :
        return "1st quadrant"
    elif int(x)<0 and int(y)>0 :
        return "2nd quadrant"
    elif int(x)<0 and int(y)<0 :
        return "3rd quadrant"
    elif int(x)>0 and int(y)<0:
        return "4th quadrant"
print("The first point is in ",quad_check(x1,y1))
print("The second point is in ",quad_check(x2,y2))
"""calculating distance"""
x = (int(x2)-int(x1))**2
y = (int(y2)-int(y1))**2
d = math.sqrt(x+y)
print(f"The distanc between these two points is {d:.2f}")