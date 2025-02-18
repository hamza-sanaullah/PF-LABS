def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter the value of n:"))
r = int(input("Enter the value of r:"))
per = factorial(n)//factorial(n-r)
com = factorial(n)//factorial(r) * factorial(n-r)
print("The permutation for given values of n and r is {}".format(per))
print("The permutation for given values of n and r is {}".format(com))