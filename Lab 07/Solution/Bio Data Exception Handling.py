biodata = {}

while True:
    try:
        name = input("Enter your Name: ")
        for char in name:
            if char.isdigit():
                raise ValueError("There must be no digit in a name")
        biodata["Name"] = name

        address = input("Enter your address: ")
        if len(address) < 3:
            raise ValueError("The address must be at least 3 characters long")
        biodata["Address"] = address

        contact_no = input("Please enter your contact number: ")
        if any(char.isalpha() for char in contact_no):
            raise ValueError("The contact number should not contain any alphabets")
        biodata["Contact Number"] = contact_no

        age = int(input("Enter your age: "))
        if age < 0 or age > 150:
            raise ValueError("Please enter a correct age")
        biodata["Age"] = age

        gender = input("Enter your gender: ")
        if gender.lower() not in ["male", "female"]:
            raise ValueError("Please enter an appropriate gender (male or female)")
        biodata["Gender"] = gender

        break
    except ValueError as e:
        print(str(e))

# Print the collected biodata
print("Biodata:")
for key, value in biodata.items():
    print(f"{key}: {value}")




