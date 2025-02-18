import random
def password(length,upper,lower,special_characters,digit):
    password = ""
    all_characters  = ""
    if upper == "yes":
       all_characters += "ABCDEFGHIJKLMNOPQRSWXYZ"

    if lower == "yes":
        all_characters += "abcdefghijklmnopqrswxyz"

    if digit== "yes":
        all_characters  += "0123456789"

    if special_characters == 'yes':
        all_characters += "!@#$%^&*()<>?{}|`~"

    if length<0:
        print("Error! Length should be a positive integer")

    if not all_characters:
        print("You have to select a particular of character to generate a password")

    for i in range(length):
        password += random.choice(all_characters)

    return password
length = int(input("Please enter the length of password:"))
upper = input("Do you want upper case letters in your password(yes,no):")
lower = input("Do you want lower case letters in yor password(yes,no):")
special_characters = input("Do you want speacial case characters(yes,no):")
digit = input("Do you want digit in yout password(yes,no):")
generated_password = password(length,upper,lower,special_characters,digit)
print(f"The generasted password is {generated_password}")






