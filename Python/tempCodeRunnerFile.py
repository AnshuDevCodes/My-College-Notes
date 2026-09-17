import numpy as np

# Practical 1: Creation and Transformation of Vectors and Matrices

# Row vector
row_vector = np.array([1, 2, 3], dtype=complex)

# Column vector
column_vector = np.array([[1], [2], [3]], dtype=complex)

# Matrix containing complex numbers
matrix = np.array([
    [1 + 2j, 2 - 1j],
    [3 + 0j, 4 + 3j]
])

print("Original Row Vector:")
print(row_vector)

print("\nOriginal Column Vector:")
print(column_vector)

print("\nOriginal Matrix:")
print(matrix)

# Transpose
print("\nTranspose of Row Vector:")
print(row_vector.T)

print("\nTranspose of Matrix:")
print(matrix.T)

# Conjugate
print("\nConjugate of Row Vector:")
print(np.conjugate(row_vector))

print("\nConjugate of Matrix:")
print(np.conjugate(matrix))

# Conjugate Transpose (Hermitian Transpose)
print("\nConjugate Transpose of Row Vector:")
print(np.conjugate(row_vector).T)

print("\nConjugate Transpose of Matrix:")
print(np.conjugate(matrix).T)