#TASK 1 OF LAB 3
def fac_find(num):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
    return factorial

def permutation(num,r):
    per = fac_find(num) // (fac_find((num-r)))
    return per
def combination(num,r):
    com = fac_find(num)//(fac_find(r) * fac_find((num-r)))
    return com
num = int(input("Enter the value of n:"))
r = int(input("Enter the value of r:"))
if r > num:
    print("The value of r must be less than n")
    quit()
print(f"The Permutation for Given values of n and r  is {permutation(num,r)}")
print(f"The Combination for Given values of n and r  is {combination(num,r)}")