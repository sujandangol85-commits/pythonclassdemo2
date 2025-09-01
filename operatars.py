# Python program demonstrating major operators

# 1. Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print("a + b =", a + b)      # Addition
print("a - b =", a - b)      # Subtraction
print("a * b =", a * b)      # Multiplication
print("a / b =", a / b)      # Division
print("a // b =", a // b)    # Floor Division
print("a % b =", a % b)      # Modulus
print("a ** b =", a ** b)    # Exponentiation

# 2. Comparison Operators/relational
print("\nComparison Operators:")
print("a == b:", a == b)     # Equal
print("a != b:", a != b)     # Not Equal
print("a > b:", a > b)       # Greater than
print("a < b:", a < b)       # Less than
print("a >= b:", a >= b)     # Greater than or equal to
print("a <= b:", a <= b)     # Less than or equal to

# 3. Assignment Operators
print("\nAssignment Operators:")
c = a       # Simple assignment
print("c =", c)
c += 5      # Add and assign
print("c += 5 →", c)
c *= 2      # Multiply and assign
print("c *= 2 →", c)
c //= 3     # Floor divide and assign
print("c //= 3 →", c)

# 4. Logical Operators
print("\nLogical Operators:")
x = True
y = False
print("x and y:", x and y)   # Logical AND
print("x or y:", x or y)     # Logical OR
print("not x:", not x)       # Logical NOT

# 5. Bitwise Operators
print("\nBitwise Operators:")
print("a & b =", a & b)      # Bitwise AND
print("a | b =", a | b)      # Bitwise OR
print("a ^ b =", a ^ b)      # Bitwise XOR
print("~a =", ~a)            # Bitwise NOT
print("a << 1 =", a << 1)    # Left Shift
print("a >> 1 =", a >> 1)    # Right Shift

# 6. Membership Operators
print("\nMembership Operators:")
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits:", "apple" in fruits)       # True
print("'mango' not in fruits:", "mango" not in fruits)  # True

# 7. Identity Operators
print("\nIdentity Operators:")
m = 5
n = 5
print("m is n:", m is n)         # True (same object for small integers)
print("m is not n:", m is not n) # False

# End of program
