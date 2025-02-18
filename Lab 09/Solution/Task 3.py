class Rectngle():
    def __init__(self,length,width):
        self.length  = length
        self.width = width
    def perimeter(self):
        per = 2 * (self.length + self.width)
        print(f"The perimeter of the rectngle is {per}")
    def area(self):
        area = (self.length) * (self.width)
        print(f"The area of the rectangle is {area}")
rec = Rectngle(3,9).perimeter()
re = Rectngle(3,9).area()