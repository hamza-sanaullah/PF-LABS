class Calculator():
    def __init__(self):
        self.num1 = int(input("Enter the fisrt number: "))
        self.num2 = int(input("Entr the second number: "))
    def addition(self):
        add = self.num1 + self.num2
        print(f"The addition of givn numbers is {add}")
    def subtract(self):
        sub = self.num1 - self.num2
        print(f"The subtraction of the given numbers is {sub}")
    def multiplication(self):
        mul = self.num1 * self.num2
        print(f"The multiplication of the given numbers is {mul}")
    def division(self):
        div = self.num1/self.num2
        print(f"The division of the given numbers is {div}")
cal = Calculator()

cal.addition()
cal.subtract()
cal.multiplication()
cal.division()