#Learn how to handle errors
# anything other that exited with 0, means that the function/program crashed
# putting code in try except blocks can allow the program to run to end instead of crashing

try:
    age = int(input("Age: "))
    income = 2000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")