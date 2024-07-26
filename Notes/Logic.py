# IF STATEMENTS

# how can we turn the following statement into written code
# that a program can read and tell us what kind of day it is?

"""
if it's hot
    It's a hot day
    Drink plenty of water
otherwise if it's cold
    Ti's a cold day
    Wear warm clothes
othersiwe
    It's a lovely day
    """

# Indetation matters in if statements.
# Code gets executed when the condition is true as long as its indented underneath the original condition
# if - the main condition usually the base case.
# elif - "else if / if not that, then this", another condition / secondary base case. used when you have more than 2 outcomes inbetween the if and else statements
# else - "otherwise", the negative of the if case. comes last in an if statement & can be omitted in some cases

is_hot = False
is_cold = False

if is_hot:
    print(
        "It's a hot day"
    )  # indented so it's executed. will only run if is_hot is true & is_cold is false
    print(
        "Drink plenty of water"
    )  # indented so it's executed. will only run if is_hot is true & is_cold is false
elif is_cold:
    print(
        "It's a cold day"
    )  # indented so it's executed. will only run if is_hot is false & is_cold is true
    print(
        "Wear warm clothes"
    )  # indented so it's executed. will only run if is_hot is false & is_cold is true
else:
    print(
        "It's a lovely day"
    )  # indented so it's executed. will only run if both is_cold & is_hot are false
print(
    "Enjoy your day"
)  # not indented so it's its execution is not dependent on when the condition is true

# Problem:
""" Price of a house is $1M
if a buyer has good credit
    down payment is 10%
otherwise
    down payment is 20%
    
print the down payment"""

has_good_credit = True
down_payment = 0
house_cost = 1000000
if has_good_credit:
    down_payment = house_cost * 10 / 100
else:
    down_payment = house_cost * 20 / 100

print(
    f"The buyer has a down payment of ${down_payment} on a house worth ${house_cost}"
)

# LOGICAL OPERATORS
'''
The three logical operators are:
AND, written as and
OR, written as or
NOT, writen as not
'''
# and - test if statements made on both sides of the operator have a truthy value.
# or - test if one of the two statements has a truthy value. This will be falsy only if both sides are falsy.
# not  - takes a single value to its right and returns the opposite value as a boolean.

# Example
# if an applicant has high income AND good credit
#   they are eligible for a loan

has_high_income = False
good_credit = True
bad_credit = True
has_record = False

if has_high_income and good_credit: # if one of these are false, we dont execute
    print("can get a loan")
if has_high_income or good_credit: # if both of these are false, we dont execute
    print("can get a loan")
if good_credit and not has_record: # the not changes record to true. two trues means statement prints
    print("get a loan")
    
# COMPARISON OPERATORS
# Comparison operators include ===, >, <. 
# These do not modify values, but rather test the relationship between them. 
# The test returns one of the two boolean values.

'''
if temp is greater than 30
    it's a hot day
otherwise if it's less than 10
    it's a cold day
otherwise
    it's neither a hot or cold day
'''

# === - Tests for Equality. Is "this" the same as "that"?
# !== - Tests for inequality. Is "this" different from that "that"?
# > - Greater than. 3 > 2 : Is 3 greater than 2 ?
# < - Less than. 3 < 2 : Is 3 less than 2 ?
# >= - Greater than or equal to.
# <= - Less than or equal to.
# != - Not equal to. 2 ! 3 : Is 2 not equal to 3?



import random
temp = random.randrange(0,100)
if temp >= 80:
    print(f"it's a hot day with a temp of {temp} degrees Fahrenheit")
elif temp <= 32:
    print(f"it's a cold day with a temp of {temp} degrees Fahrenheit")
else:
    print(f"it's an average day with a temp of {temp} degrees Fahrenheit")

#Problem
'''
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters
otherwise
    name looks good
'''
# take a input and return if the name meets the criteria
name = input("enter your name: ")

if len(name) < 3:
    print("name must be at least 3 characters long")
elif len(name) > 50:
    print("name can be a maximum of 50 characters long")
else:
    print("name looks good")