# Calculate a user's age 
""" 
birth_year = input('Birth year: ')
age = 2024 - birth_year
print(age)
"""
# Though this is pretty straight forward, it will not work 
# 2024 is an integer and birth_year is type string. ( 2024 - '1994')
# Python deems these two to be incompatible and there for cannot perform mathematical operations
# we must do a type conversion on the birth year (string to int) so that they are compatible (see below)

# int() - this function converts a string to an integer: '2000' -> 2000
# float() - this function converts a string to a float or number with a decimal: '1.5' -> 1.5
# bool() - this function converts a string to a boolean value: 'true' -> True
# type() - this is a function that returns the type of the passed variable: type('test') -> <class 'str'>,  type(14) -> <class 'int'>
birth_year = input('Birth year: ')
age = 2024 - int(birth_year)

print(age)


#Example: Ask a user their weight( in pounds), convert it to kilograms and prinnt to terminal
lbs_weight = input("what is you weight (in pounds)? ")
kg_weight = 0.45 * float(lbs_weight)
print(kg_weight)