"""
PYTHON OPERATORS

Operators are symbols used to perform operations on variables and values.

Main types of operators:

1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators
5. Membership Operators
6. Identity Operators
7. Bitwise Operators
"""



# 1. ARITHMETIC OPERATORS


a = 10
b = 3

print(a + b)   # Addition -> 13
print(a - b)   # Subtraction -> 7
print(a * b)   # Multiplication -> 30
print(a / b)   # Division -> 3.333...
print(a // b)  # Floor Division -> 3
print(a % b)   # Modulus/Remainder -> 1
print(a ** b)  # Exponent -> 10^3 = 1000



# 2. COMPARISON OPERATORS


x = 10
y = 20

print(x == y)  # Equal to -> False
print(x != y)  # Not equal to -> True
print(x > y)   # Greater than -> False
print(x < y)   # Less than -> True
print(x >= y)  # Greater than or equal to -> False
print(x <= y)  # Less than or equal to -> True



# 3. ASSIGNMENT OPERATORS


num = 10       # Assign value

num += 5       # num = num + 5
print(num)     # 15

num -= 3       # num = num - 3
print(num)     # 12

num *= 2       # num = num * 2
print(num)     # 24

num /= 4       # num = num / 4
print(num)     # 6.0

num %= 4       # num = num % 4
print(num)     # 2.0



# 4. LOGICAL OPERATORS


age = 20
has_id = True

# and -> Both conditions must be True
print(age >= 18 and has_id)   # True

# or -> At least one condition must be True
print(age < 18 or has_id)     # True

# not -> Reverses True/False
print(not has_id)             # False



# 5. MEMBERSHIP OPERATORS


languages = ["Python", "Java", "C++"]

# in -> Checks if value exists
print("Python" in languages)       # True

# not in -> Checks if value does not exist
print("JavaScript" not in languages)  # True



# 6. IDENTITY OPERATORS


a = [1, 2, 3]
b = a
c = [1, 2, 3]

# is -> Checks if both variables refer to same object
print(a is b)      # True

# Same values but different objects
print(a is c)      # False

# is not -> Checks if objects are different
print(a is not c)  # True

# == compares VALUES
print(a == c)      # True



# 7. BITWISE OPERATORS


a = 5   # Binary: 0101
b = 3   # Binary: 0011

print(a & b)   # AND -> 1
print(a | b)   # OR -> 7
print(a ^ b)   # XOR -> 6
print(~a)      # NOT -> -6
print(a << 1)  # Left Shift -> 10
print(a >> 1)  # Right Shift -> 2