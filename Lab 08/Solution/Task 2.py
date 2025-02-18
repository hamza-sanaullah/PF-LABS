with open("ATTENDENCE", "w") as fileptr:
    name = input("Please Enter the names of students separated by spaces")
    roll_no = input("Please enter the roll no of students respectively")
    fileptr.write(name + "\n")
    fileptr.write(roll_no + "\n")
    weeks = ["week_1", "week_2", "week_3", "week_4", "week_5"]
    attendance_weeks = []

    for week in weeks:
        attendance = input(f"Please enter the attendance for {week} separated by spaces: ")
        fileptr.write(attendance + "\n")
        attendance_weeks.append(attendance.split())
with open("ATTENDENCE", "r") as fileptr:
    lines = fileptr.readlines()
    students = lines[0].rstrip().split()

    roll_no = lines[1].rstrip().split()

    attendance_weeks = [line.rstrip().split() for line in lines[2:]]

with open("ATTENDENCE", "w") as fileptr:
    for i in range(len(students)):
        fileptr.write(f"The student {students[i]} whose roll no is {roll_no[i]}\n")
        for j in range(len(attendance_weeks)):
            fileptr.write(f"Week {j + 1} attendance: {attendance_weeks[j][i]}\n")

        if any("p" in attendance_weeks[j][i] for j in range(len(attendance_weeks))):
            fileptr.write(f"*********** {students[i]} is eligible to sit in the exam ***********\n")
        else:
            fileptr.write(f"*********** {students[i]} is not eligible to sit in the exam ***********\n")

        fileptr.write("\n")