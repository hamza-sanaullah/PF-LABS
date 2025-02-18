#Write a program to check whether the given number is palindrome or not.

palin = input("Enter a number to check it whether a palindrome or not:")
rev_num = palin[::-1]
if palin==rev_num:
    print(f"The given number {palin} is a palindrome ")
else:
    print(f"The given number {palin} is not a  palindrome ")


