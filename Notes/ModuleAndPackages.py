# MODULES
# a module is a file with some python code
# we use modules to help organize our code into multiple files and aids in reusability
# Usually broken in with related classes and functions

# Put weight converter functions into the a module file (Projects/Modules/converters.py)
# import the entire module file into the current file
 
import converters 
print(converters.kg_to_lbs(70))

# if you just want to import a specific function from a module, use the following:
# if you want to add more functions, separate it by a comma
from converters import kg_to_lbs       # kg_to_lbs, lbs_to_kg
print(kg_to_lbs(60))


# Problem: create a function 'find_max()' that returns the largest number in a given list.
# place the function in a file called utils and cal the function in this file

import utils

print(utils.find_max([23,45,67,1,0,-100]))

# PACKAGES
# another way that our code can be organized.
# Packages are containers that contain related modules

'''Packages are new directories so to make one, 
 create a new folder
 add '__init__.py' to the folder
 add a module file
 '''

# you can import this way but you have to keep typing ecommerce.shipping.method
# import ecommerce.shipping
# ecommerce.shipping.calculate_shipping()

# if you use this import style, you only call the specific method itself
from ecommerce.shipping import calculate_shipping
calculate_shipping()