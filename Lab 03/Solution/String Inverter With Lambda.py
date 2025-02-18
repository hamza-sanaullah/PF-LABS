string = input("Enter the string:")

t = lambda string:string.upper() if string == string.lower() else string
print(f"{(t(string))}")

def invert(v= t(string)):
    q = v[::-1]
    return q
print(invert())

#Another Method
upper_string = lambda str:str.upper() if str.lower() else str
string = input("Enter the string:")
ham = upper_string(string)
print(ham)
def inverter_string(str):
    return str[::-1]
print(inverter_string(ham))


