
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Create an empty matrix
C = [[0, 0],
     [0, 0]]

# Add the matrices
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]

print("First Matrix:")
for row in A:
    print(row)

print("Second Matrix:")
for row in B:
    print(row)

print("Sum of Matrices:")
for row in C:
    print(row)