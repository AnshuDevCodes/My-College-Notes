# Practical 3: Gaussian Elimination
# Mathematics for Computing

# System of equations:
# 2x + y - z = 8
# -3x + y + 2z = -11
# -2x + y + 2z = -3

# Augmented matrix [A | b]
matrix = [
    [2.0, 1.0, -1.0, 8.0],
    [-3.0, 1.0, 2.0, -11.0],
    [-2.0, 1.0, 2.0, -3.0]
]

print("=" * 50)
print("PRACTICAL 3 - GAUSSIAN ELIMINATION")
print("=" * 50)

print("\nOriginal Augmented Matrix [A | b]:")
for row in matrix:
    print(row)

# --------------------------------------------------
# Step 1: Eliminate x
# --------------------------------------------------

factor = matrix[1][0] / matrix[0][0]

for j in range(4):
    matrix[1][j] = matrix[1][j] - factor * matrix[0][j]

factor = matrix[2][0] / matrix[0][0]

for j in range(4):
    matrix[2][j] = matrix[2][j] - factor * matrix[0][j]

print("\nAfter eliminating x:")
for row in matrix:
    print(row)

# --------------------------------------------------
# Step 2: Eliminate y
# --------------------------------------------------

factor = matrix[2][1] / matrix[1][1]

for j in range(4):
    matrix[2][j] = matrix[2][j] - factor * matrix[1][j]

print("\nAfter eliminating y:")
for row in matrix:
    print(row)

# --------------------------------------------------
# Step 3: Back Substitution
# --------------------------------------------------

z = matrix[2][3] / matrix[2][2]

y = (matrix[1][3] - matrix[1][2] * z) / matrix[1][1]

x = (matrix[0][3] - matrix[0][1] * y - matrix[0][2] * z) / matrix[0][0]

print("\nSolution:")
print(f"x = {x:.2f}")
print(f"y = {y:.2f}")
print(f"z = {z:.2f}")

# --------------------------------------------------
# Step 4: Verification
# --------------------------------------------------

equation1 = 2 * x + y - z
equation2 = -3 * x + y + 2 * z
equation3 = -2 * x + y + 2 * z

print("\nVerification:")
print(f"Equation 1: 2x + y - z = {equation1:.2f}")
print(f"Equation 2: -3x + y + 2z = {equation2:.2f}")
print(f"Equation 3: -2x + y + 2z = {equation3:.2f}")

if (abs(equation1 - 8) < 1e-9 and
        abs(equation2 + 11) < 1e-9 and
        abs(equation3 + 3) < 1e-9):
    print("\nVerification successful.")
else:
    print("\nVerification failed.")