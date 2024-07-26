# Addition
print(10 + 3)  # -> 13

# Subtraction
print(10 - 3)  # -> 7

# Multiplication
print(10 * 3)  # -> 30

# Division
# / - single slash means regular divion returns a float
# // - double slash returns the whole number without the decimal. javascript equivalent is Math.floor()
print(10 / 3)  # -> 3.3333333333 (float)
print(10 // 3)  # -> 3 (int)

# Modulo - returns the remainder of the division
print(10 % 3)  # -> 1

# Exponent - returns the base raised to a power
print(10**3)  # -> 1000  (10^3)

# Augmented/Enhanced Assignment Operator
# this is a shorter way to write out operations
"""
x=10
x = x + 3
print(x) -> 13
"""
x = 10
# Addition
x += 3
print(x)  # -> 13

# Subtraction
x -= 3
print(x)  # -> 10

# Multiplication
x *= 3
print(x)  # -> 30

# OPERATION PRECEDENCE (PEMDAS / Order of Operations)
# this is the order in which math operations are executed

"""
parenthesis: ()
exponentiation: 2 ** 3
multiplication OR division: * OR / OR //
addition OR subtraction: + OR -
"""

x = 10 + 3 * 2**2
#   10 + 3 *   4
#   10 +   12
#      22
print(x)  # -> 22

x = (10 + 3) * 2**2
#       13   * 2**2
#       13   *   4
#            52
print(x)  # -> 52

x = (2 + 3) * 10 - 3
#      5    * 10 - 3
#          50    - 3
#              47

print(x) # -> 47


# MATH FUUNCTIONS
# round(int) - rounds a number to the nearest int. 4-(round down), 5+ round up
# abs(int) - returns the positive value of the int. (just the distance away from 0)

print(round(2.9)) # -> 3
print(round(2.2)) # -> 2
print(abs(1)) # -> 1
print(abs(-10)) # -> 10

# MATH METHODS - in order to use these, you have to import the math package
# here is documentation of all the math methods: https://docs.python.org/3/library/math.html
import math
# .ceil(int) - always rounds a number UP to the nearest integer
# .floor(int) - always rounds a number DOWN to the nearest integer
# .sqrt(int) - returns the square root of a number as a float



print(math.ceil(2.1)) # -> 3
print(math.floor(2.9)) # -> 2
print(math.sqrt(4)) # -> 2.0
