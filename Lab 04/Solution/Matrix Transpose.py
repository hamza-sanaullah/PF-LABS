#converting rows into integer by getting each element into a separere string  by list comprehension
row1 = [int(x) for x in input("Enter the row 1 separated by spaces:").split()]
row2 = [int(x) for x in input("Enter the row 2 separated by spaces:").split()]
row3 = [int(x) for x in input("Enterthe row 3 separated by spaces:").split()]
matrix = [row1,row2,row3]
print("The matrix is:")
for row in matrix:
    print(row)
new_matrix = []
an_matrix = []
f_matrix = []
for row in matrix:
     new_matrix.append((row[0]))
     an_matrix.append((row[1]))
     f_matrix.append((row[2]))
Transpose = [new_matrix,an_matrix,f_matrix]
print("The Transpose matrix is")
for row in Transpose:

    print(row)




