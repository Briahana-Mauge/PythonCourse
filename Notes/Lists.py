# LISTS (arrays)
# A list provides a convenient way to store a collection of things / data. 
# Say we want to keep the numbers 2, 3, 5, 7, and 11 - all in one place. 
# Instead of creating five separate variables we can create a list to store all these values. 
# To create a list, we use the [ and ] square brackets, and in between put whatever values we need separated by commas.

# Lists (like strings) like strings can be accessed with indexes and have a length property.

names = ['Briahana', 'Krystal', 'Chynna', 'Nubia']
    #       0             1        2         3
    #      -4            -3       -2        -1
# print(names)
# print(names[0]) # -> Briahana: can index into a list and return the value at the specified index
# print(names[-1]) # -> Nubia: negative index start at the back of the list
# print(names[1:3]) # -> ['Krystal', 'Chynna'] returns a range of values within the index provided excluding the last number

# update the value of the first item in the list to include a last name
names[0] = 'Briahana Maugé' # -> mutates the original list setting a new value
# print(names) # -> ['Briahana Mauge', 'Krystal', 'Chynna', 'Nubia']

# Problem
# write a program to find the largest number in a list

random_numbers = [123, 5, 500,-432, .7, 77, 0,]
largest = random_numbers[0]
for number in random_numbers:
    if number > largest:
        largest = number
# print(f"The largest number in {random_numbers} is {largest}.") # -> 500

# MATRIX / 2D LISTS/ MULTIDIMENSIONAL LISTS

# Multidimensional lists are lists that contain lists as their elements. 
# If an list is filled with lists it is considered to be 2 dimensional (also often referred to as a matrix). 
# If those lists are also filled with lists it becomes a 3 dimensional list or multidimensional. 
# Typically it is BAD practice to go further than 2 dimensional lists.

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# print(matrix[0][1]) # -> 2: the 1st bracket is for the outer list, the 2nd bracket for the inner list

# update the value of the 2 item in the 1st list
matrix[0][1] = 20 # -> mutates the original list setting a new value
# print(matrix[0][1]) # -> 20

# Use a nested loop to print out every item present in the matrix
for row in matrix: # outer loop
    for item in row: # inner loop
        # print(item) # prints out value at matrix[row][item]
        print("")

# LIST FUNCTIONS
# len(list) - calculate the length of a list: general purpose and can be used on other data types

print(len(matrix)) # -> 3
# 
# 
# 

# LIST METHODS
# .append(element) - adds element to the end of a list
# .insert(index,element) - add an element to a list at a given index and shifts the elements after it to the next index up
# .remove(element) - removes the FIRST instance of an element passed as an arguent
# .index(element) - returns the index of the FIRST instance of an element passed as an argument. returns an error if not found
# .pop() - removes the last item from a list and returns it
# element in list_variable - checks to see if element exists in the list variable and returns a bool. CASE SENSATIVE
# .count(element) - counts the number of occurrences of an element in a list.
# .sort() - sorts the list in numerical and alphabetical ascending order.
# .reverse() - reverses the order of elements in a list.
# .copy() - make a copy of a list
# .clear() - removes all elements in a list


new_nums = [5,2,1,7,4,2,]

new_nums2 = new_nums.copy()
print(new_nums2) # -> [5,2,1,7,4,2,]
new_nums.append(20)
print(new_nums) # -> [5, 2, 1, 7, 4, 2, 20]
new_nums.insert(0,100)
print(new_nums) # -> [100, 5, 2, 1, 7, 4, 2, 20]
new_nums.insert(5,"half")
print(new_nums) # -> [100, 5, 2, 1, 7, 'half', 4, 2, 20]
new_nums.remove(2)
print(new_nums) # -> [100, 5, 1, 7, 'half', 4, 2, 20]
print(new_nums.index('half')) # -> 4
print(new_nums.pop()) # -> 20
print(new_nums) # -> [100, 5, 1, 7, 'half', 4, 2]
print(1 in new_nums) # -> True
new_nums.append(5) 
print(new_nums)# -> [100, 5, 1, 7, 'half', 4, 2, 5]
print(new_nums.count(5)) # -> 2
new_nums.remove('half')
print(new_nums) # -> [100, 5, 1, 7, 4, 2, 5]
new_nums.sort()
print(new_nums) # -> [1, 2, 4, 5, 5, 7, 100]
new_nums.reverse()
print(new_nums) # -> [100, 7, 5, 5, 4, 2, 1]

new_nums.clear()
print(new_nums) # -> []

letters = ['a','d','r','g','b','c']
print(letters) # -> ['a', 'd', 'r', 'g', 'b', 'c']
letters.sort()
print(letters) # -> ['a', 'b', 'c', 'd', 'g', 'r']
letters.reverse()
print(letters) # -> ['r', 'g', 'd', 'c', 'b', 'a']

# Problem
# Write a program that removes duplicates in a list
list = [2,2,4,6,3,4,6,1]
uniques = []

for number in list:
    if number not in uniques:
        uniques.append(number)
print(list)
print(uniques)

# TUPLES
# A touple is similar to a list except the can not be changed and are stored in parenthesis
# Touples are still 0-indexed so you can get values by using brackets

coordinates = (1,2,3)
print(coordinates[1]) # -> 2
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x,y,z) # -> 1,2,3

# Unpacking (used on touples and lists)
# shortens some code so there is less chance of repeating yourself
# below is a shortened version of code on lines 131-133
tester = ['this', 'works', 100]
a,b,c = coordinates # -> assigns the varible to the corresponding values in the touple
d,e,f = tester # -> assigns the varible to the corresponding values in the list
print(a,b,c) # -> 1,2,3
print(d,e,f) # -> this, works, 100