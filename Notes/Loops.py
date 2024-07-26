# LOOPS
# Loops are a solution for repetitive tasks.

# WHILE LOOP
# A while loop is similar to an if statement, in that we will check if some condition is true.
# Unlike an if statement, we will execute the code block following the while loop again and again as long as the condition is true.
# Whenever we reach the bottom of the code block, we go right back up and check the condition again.

i = 1
while i <= 4:
    print(i)  # indented so it runs inside the loop condition
    print("*" * i)  # how to repeat a string
    i += 1  # indented so it runs inside the loop condition

print("Loop is finished")


# FOR LOOPS
# A for loop is a condensed version of the while loop. Used to go throguh a collection of things
# With the for loop, each iteration the variable will hold a single character/index/thing at a time
# For loops can be used to iterate through
#       every character in a string
#       every item in a list (array)

for item in "Python":
    print(item)

prices = [10, 20, 30]
total = 0

for price in prices:
    total += price # add each price to the total variable
print(f"The total is ${total}.")

# NESTED LOOPS
# loops inside one another are called nested loops.

# Problem
# create coordinates to plot on a graph later
for x in range(4): # range(4) will not go iterate past 4 loops ex: 0,1,2,3
    for y in range(3):
        print(f"({x},{y})")

# Problem
# using nested loops create a loop to print out the letter 'f' made out of "x's" based on a given list
# output:
                                # xxxxx
                                # xx
                                # xxxxx
                                # xx
                                # xx
numbers = [5,2,5,2,2]

for x_count in numbers:
    word = ''
    for num in range(x_count):
        word += 'x'
    print(word) 

# using nested loops create a loop to print out the letter 'l' made out of "x's" based on a given list
# output:
                                # x
                                # x
                                # x
                                # x
                                # xxxxx
numbers2 = [1,1,1,1,5]
print(" ")
for x_count in numbers2:
    word = ''
    for num in range(x_count):
        word += 'x'
    print(word) 