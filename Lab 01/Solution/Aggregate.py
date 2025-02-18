#Write a program that takes your ECAT Marks, Intermediate Part 1 Marks and Matric Marks from user and calculate the
# aggregate according to given formula
#ECAT 33% Intermediate 50% Matric 17%
#First method with f string

Ecat_marks = int(input("Enter your Ecat marks:"))
Matric_marks = int(input("Enter your Matric marks:"))
Inter_program = input("Enter your Inter program:")
Inter_Marks = int(input("Enter your Inter Part 1 marks:"))
if Inter_program == "fsc":
    m = (Inter_Marks/520)*50
    Aggregate = Ecat_marks / 400 * 33 + Matric_marks / 1100 * 17 + m
    print(f"Your aggregate is {Aggregate:.2f}")
elif Inter_program == "ics":
    m  =  (Inter_Marks/510)*50
    Aggregate = Ecat_marks / 400 * 33 + Matric_marks / 1100 * 17 + m
    print(f"Your aggregate is {Aggregate:.2f}")
elif Inter_program == "biology":
    m = (Inter_Marks/505)*50
    Aggregate = Ecat_marks / 400 * 33 + Matric_marks / 1100 * 17 + m
    print(f"Your aggregate is {Aggregate:.2f}")

#second methos with format string
#The other method with format method
#takingg inputs
Ecat_marks = int(input("Enter your Ecat marks:"))
Matric_marks = int(input("Enter your Matric marks:"))
Inter_program = input("Enter your Inter program:")
Inter_Marks = int(input("Enter your Inter part 1 marks:"))
def discipline_check(program,marks):
    if program == "fsc":
        m = (marks/520)*50
        Aggregate = Ecat_marks / 400 * 33 + Matric_marks / 1100 * 17 + m
        print("Aggregate: {:.2f}".format(Aggregate))
    elif program == "ics":
        m  =  (marks/510)*50
        Aggregate = Ecat_marks / 400 * 33 + Matric_marks / 1100 * 17 + m
        print("Aggregate: {:.2f}".format(Aggregate))
    elif program == "biology":
        m = (marks/505)*50
        Aggregate = Ecat_marks / 400 * 33 + Matric_marks / 1100 * 17 + m
        print("Aggregate: {:.2f}".format(Aggregate))
discipline_check(Inter_program,Inter_Marks)





