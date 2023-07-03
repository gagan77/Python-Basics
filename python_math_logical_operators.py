# Logical Operators are used to combine conditional statements.
# and - BOTH NEED TO BE TRUE
# or - ONE OF THEM MUST BE TRUE
# not - REVERSE THE CONDITION
# Examples:
x = 10

# The following statement will be true and print out the message below
if x > 5 and x < 15:
    print("x is greater than 5 and less than 15")

a = True
b = True

if a and b:
    print("Both a and b are true")

if a or b:
    print("Either a or b is true")

if not a:
    print("a is false")
# Check out more about logical operators here: https://docs.python.org/3/library/stdtypes.html#boolean-operations

#Math Operators are used to perform mathematical operations.
# + - Addition
# - - Subtraction
# * - Multiplication
# / - Division
# % - Modulus (Remainder)
# ** - Exponentiation
# // - Floor Division

# Examples:
# Addition
print(2 + 3)
# Subtraction
print(2 - 3)
# Multiplication
print(2 * 3)
# Division
print(2 / 3)
# Modulus (Remainder)
print(2 % 3)
# Exponentiation
print(2 ** 3)
# Floor Division
print(2 // 3)

# Check out more about math operators here: https://docs.python.org/3/library/math.html