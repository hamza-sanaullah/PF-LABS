with open("input.txt","w") as fileptr:
    for i in range(5):
        line = input("Enter a line")
        fileptr.write(line + "\n")
with open("input.txt","r") as fileptr:
    with open("output.txt", "w") as fileptr1:
        for i in fileptr.readlines():
            x = i.rstrip()
            rev = x[::-1]
            fileptr1.write(rev+ "\n")