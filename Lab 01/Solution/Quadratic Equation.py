#Write a program that determine the nature of the roots of the Quadratic Equation ax2 + bx + c = 0 by calculating the
# Discriminant

import math
#Taking  inputs
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
"""Calculating discriminant"""
disc = b**2-4*a*c
#Checkinf different conditions
if disc == 0:
    print("Roots are real,Equal and Rational")
    x = (-b+math.sqrt(disc))/(2*a)
    print(f"Roots are{x:.2f}")
elif disc>0:
    print("Roots are real,unequal and irrational")
    root_1 = (-b+math.sqrt(disc))/(2*a)
    root_2 = (-b-math.sqrt(disc))/(2*a)
    print(f"The Roots are {root_1:.2f} and {root_2:.2f}")
elif disc<0:
    print("Roots are imaginry")
    new_disc = abs(disc)
    real_roots = -b/(2*a)
    img = math.sqrt(new_disc)/(2*a)
    print(f"The real and imaginary parts of roots ars  {real_roots:.2f}+{img:.2f}j")
    print(f"The real and imaginary parts of roots ars  {real_roots:.2f}-{img:.2f}j")




