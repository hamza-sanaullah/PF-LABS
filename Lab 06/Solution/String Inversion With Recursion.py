def invert_string(string):
    if len(string) == 1:
        return string
    else:
        return  string[-1] + invert_string(string[:-1])
string = input("Enter the string")
print(invert_string(string))