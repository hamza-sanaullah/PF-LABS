while True:
    try:
        number = int(input("Enter number to find Factorial:"))
        assert number>=0,"Number cannot be negative"
        factorial = 1
        for i in range(1,number+1):
            factorial *=i
        print(f"The factorial of the given number is {factorial}")
        break
    except ValueError :
        print("Invalid input! Please enter a positive integer")
    except AssertionError:
        print("Please enter a positive integer")
    finally:
        print("Thanks for using this program")



