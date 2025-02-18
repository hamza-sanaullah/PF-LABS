def cal_power(number,power):
    if power == 1:
        return number
    else:
       return number * cal_power(number,power-1)
number = int(input("Enter the number:"))
power = int(input("Enter the power of the number:"))
print(f"The  answer for the given power of the number is {cal_power(number,power)}")