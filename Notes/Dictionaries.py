# DICTIONARIES
# A dictionary / object is a collection of key/value pairs. The pairs are also known as properties.
# It is identified by using curly braces {}

# keys in an object MUST be unique
customer = {
    "name": "Briahana",
    "age": 30,
    "is_verified": True,
}

# By keying into the object, the value at that key is returned. CASE SENSITIVE If key doesnt exist, throws error.
print(customer["name"])  # -> Briahana
# print(customer["Name"]) # -> KeyError
# print(customer["birthdate"]) # -> KeyError

# Update a property value at a given key
customer["name"] = "Bri"
# create a new property
customer["state"] = "NY"
print(customer)

# OBJECT METHODS
# obj[key] - bracket notation, the value at that key is returned. If key doesnt exist, throws error. CASE SENSITIVE
# .get(key) - returns the value at that key is returned. If key doesnt exist, returns 'none'

# Problem
# Create a program that take numbers as an input and prints out the number in written form

number_name = {
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
}
num_in_words = []
phone_number = input("Enter in your phone number: ")

for number in phone_number:
    num_in_words.append(number_name[number])
result = " ".join(num_in_words)
print(result)

