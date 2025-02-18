class Circle:
    def __init__(self,radius):
        print("hamza")

        self.radius = radius
    def area(self):
        import math
        ar = math.pi * self.radius**2
        return ar
class Cylinder(Circle):
    def Volume(self):
        # vol = self.area() * self.height
        # return vol
        pass
height = int(input("Enter the value of radius"))
radius = int(input("enter the height"))
d = Cylinder(height)
print(d.area())
print(d.Volume())