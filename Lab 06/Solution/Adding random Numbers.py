import random
number = []
for j in range(10):
    randoms = random.randint(1,1000)
    number.append(randoms)
print(number)
def add_list(numbers,index):
    if index == len(numbers):
        return 0
    else:
       return numbers[index] + add_list(numbers,index+1)
print(f"The sum of the random numbers of the  list is {add_list(number,0)}")



