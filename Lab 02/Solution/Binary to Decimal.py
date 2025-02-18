#Write a program that convert a binary number into its decimal equivalent
'''Taking binary input'''
bin_INPUT = (input("Enter a binary number:"))
# checking a valid binary number
if not all (i=="0" or i == "1" for i in bin_INPUT):
    print("Please enter a valid binary number")
else:
    decimal_num = 0
    power = len(bin_INPUT)-1
    #conversion formula
    for i in bin_INPUT:
        decimal_num  += (int(i)) * (2**power)
        power-=1
    print(f"The decimal equilent  of given binary number is {decimal_num}")





