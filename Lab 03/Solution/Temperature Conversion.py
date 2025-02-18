def fen_to_cel(temp):
    cel = (temp-32) * 5//9
    return cel
temp = int(input("Enter the temperature in fahrenheit:"))
print(f"The EQUILENT of FAHRENHEIT IN CELCIUS is {fen_to_cel(temp)}")

def cel_to_fen(temp):
    fen = (temp * 9//5) + 32
    return fen
temp = int(input("Enter the temperature in celcius:"))
print(f"The EQUILENT OF CELCIUS IN FAHRENHIET IN CELCIUS is {cel_to_fen(temp)}")