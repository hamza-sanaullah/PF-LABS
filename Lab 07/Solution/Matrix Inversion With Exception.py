try:
    matrix1 = eval(input("Please Enter a List: "))
    matrix2 = eval(input("Please Enter a List: "))
except ValueError as e:
    print("Enter Valid input")


# Swap elements
(matrix1[0], matrix2[1]) = (matrix2[1], matrix1[0])
(matrix1[1], matrix2[0]) = (-matrix1[1], -matrix2[0])

# Calculate determinant
determinant = (matrix1[0] * matrix2[1]) - (matrix1[1] * matrix2[0])

# Check if matrix is invertible
if determinant == 0:
    raise ZeroDivisionError("The inverse of the matrix is not possible")
else:
    # Calculate inverse
    inverse_matrix = [[matrix2[1] / determinant, -matrix1[1] / determinant],
                      [-matrix2[0] / determinant, matrix1[0] / determinant]]

    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)
    print("Determinant:", determinant)
    print("Inverse Matrix:")
    for row in inverse_matrix:
        print(row)


