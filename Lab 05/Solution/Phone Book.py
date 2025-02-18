Phone_Book = {"waleed":"03452562290","hamza":"03138635661","afeef obaid":"03234104522","dad":"03004169582","bahauddin":"03154155779","samia":"03344201696",
              "salman":"03484569123","zain":"03174846585","huzaifa":"03493434677","ali hassan": "03234133785"}
PURPOSE = input("WHAT DO YOU WANT?\nEnter S for search contact by name:\nEnter N for names of all contacts:\nEnter C for all contacts:\nEnter R to delete any contact number:\nEnter U to update any number:\nEnter CL to clear phone book:\nEnter AD to add contact number:\n").lower()


if PURPOSE == "S".lower():
    name = input("Enter a name:")
    if name in Phone_Book.keys():
        print(Phone_Book.get(name))
if  PURPOSE == "N".lower():
    print(Phone_Book.keys())
if  PURPOSE == "C".lower():
    print(Phone_Book.values())
if  PURPOSE == "R".lower():
    imp = input("Enter key of which you want to delete number: ")
    print(Phone_Book.pop(imp))
    print(Phone_Book.items())
if PURPOSE == "U".lower():
    key = input("which key you want to update number:")
    UPdate = Phone_Book.update({key : "03456712340"})
    print(Phone_Book)
if PURPOSE == "CL".lower():
    Phone_Book.clear()
    print(Phone_Book)
if PURPOSE == "AD".lower():
    key = input("Enter the name of contact")
    value = input("Enter the contact number")
    Phone_Book[key] = value
    print(Phone_Book)