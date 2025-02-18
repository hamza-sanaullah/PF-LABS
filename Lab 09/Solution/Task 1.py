"""class Students():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        print(f"The studemt {self.name} whose age is {self.age} and his grade is {self.grade}")
student = Students("hamza",18,"A")"""
LIST_1 = ["hAMZA","SIR","sample","saleem"]
a = lambda i: False if i.startswith("s") else True
for i in LIST_1:
    new = list(filter(a,LIST_1))
    print(new)
    break
n  = [1,2,3,4,5,6,7,8,9,10]
s = [x**2 for x in n if x % 2!=0]
print(s)