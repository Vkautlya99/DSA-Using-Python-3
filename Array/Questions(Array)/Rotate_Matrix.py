# Write a Programm to Rotate a Matrix


def RotateMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for rows in matrix:
        rows.reverse()


matrix = [[1, 2], [3, 4]]
print("Original Matrix")
for rows in matrix:
    print(rows)
RotateMatrix(matrix)

print("\nRotated Matrix:")
for rows in matrix:
    print(rows)
