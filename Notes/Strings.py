# String variables are used to store textual data, characters and sequences of characters. 
# Can be specified by surrounding some text with single ' or double " quotes.
str_1 = "Hello World!"
str_2 = 'Hello World!!'
print(str_1)
print(str_2)

# If the string has an apostrophe, you should wrap the string in double qoutes so that it works properly
print("It's quite simple")
# If the string has qoute inside, you should wrap the string in single qoutes so that it works properly
print('that is "so" cool')

# If we have a piece of text with multiple lines, 
# then triple quotes (either ''' or """) can be used to surround the text.
str_3 = """
(CNN)AirAsia Flight QZ8501 climbed rapidly before it crashed,
a top Indonesian official said Tuesday, "according" to The Jakarta Post.

Then the plane stalled, Transportation Minister Ignasius Jonan said
at a parliamentary hearing, according to the AFP and Reuters news agencies.
"""
print(str_3)

str_4='''
(CNN)AirAsia Flight QZ8501 climbed rapidly before it crashed,
a top Indonesian official said Tuesday, 'according' to The Jakarta Post.

Then the plane stalled, Transportation Minister Ignasius Jonan said
at a parliamentary hearing, according to the AFP and Reuters news agencies.
'''
print(str_4)

# INDEXING

#if we want to get a specfic character in a string, we can key into it's index using square brackets
test_string=  'Python for Beginners'
# the index    0123456789......20
#*python only* -20...........-4-3-2-1      -1 is the index of the last character
print(test_string)
# Grab the first letter of the test string
print(test_string[0]) # P
print(test_string[-20]) # P

#grab a substring between two numbers not inclusive
print(test_string[7:10]) # for

# FORMATTED STRINGS 
# find more info about formatting here: https://colab.research.google.com/github/ipeirotis/introduction-to-python/blob/master/notes/D5-String_Formatting.ipynb#scrollTo=GDd-srjDkjSz
first_name = 'Briahana'
last_name = 'Maugé'

#print a message: Briahana [Mauge] is a coder
traditional_concat_message = first_name + ' [' + last_name + '] is a coder.'

print(traditional_concat_message)
#this works fine but can get confusing the more variables are used/longer the result

#lets try again with a formatted string instead to dynamically add variables to strings
formatted_message = f'{first_name} [{last_name}] is a coder.'
print(formatted_message)


# STRING FUNCTIONS
# len() - calculate the length of a string: general purpose and can be used on other data types
course = 'Python for Beginners'
print(len(course)) # -> 20


#  STRING METHODS
# .upper() - converts a str to uppercase letters. DOES NOT MODIFY ORIGINAL STRING
# .lower() - converts a str to loowercase letters. DOES NOT MODIFY ORIGINAL STRING
# .find(str) - returns the index when str is FIRST spotted. returns -1 when not found. CASE SENSATIVE
# .replace(old str, new str) - replaces the first argument with the second argument in all instances. CASE SENSATIVE
# .count('str') - counts the number of occurrences of one string in another.
# 'str' in string_variable - checks to see if str exsits in the string variable and returns a bool. CASE SENSATIVE
# .split(char in quotes) - splits the string into an array based on the character in the argument
# 'char in quotes'.join(string_variable) - joins an array into a string based on the character in quotes


print(course.upper()) # -> PYTHON FOR BEGINNERS
print(course.lower()) # -> python for beginners
print(course.find('e')) # -> 12 (the first e is found at index 12)
print(course.find('Y')) # -> -1 (not found)
print(course.find('Beginners')) # -> 11 the word starts at index 11
print(course.replace('Beginners', 'Absolute Beginners')) # -> Python for Absolute Beginners
print(course.replace('beginners', 'Absolute Beginners')) # -> Python for Beginners (beginners was not found so it didn't replace anything)
print(course.replace('n', 'm')) # -> Pythom for Begimmers
print(course.count('for')) # -> 1
print('Python' in course) # -> True
print('FOR' in course) # -> False
print(course.split(' ')) # -> ['Python', 'for', 'Beginners']
print(course.split('e')) # -> ['Python for B', 'ginn', 'rs']

course_arr = ['Python', 'for', 'Beginners']
course_arr2 = ['Python for B', 'ginn', 'rs']
print(''.join(course_arr)) # ->  'PythonforBeginners' (join with no space)
print(' '.join(course_arr)) # ->  'Python for Beginners' (join with a space)
print('e'.join(course_arr2)) # -> 'Python for Beginners' (join on the letter e)

