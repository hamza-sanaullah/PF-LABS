def hexadecimal(decimal):
    decimal_number = hex(decimal)
    return decimal_number
try:
    number = int(input("Enter a number: "))
    print(f"The hexadecimal equivalent is {hexadecimal(number)}")
except ValueError:
    print("Please enter a valid input")

else:
    print("THE FUNCTION IS RUNNING SUCCESSFULLY")



