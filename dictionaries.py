# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# This is very similar to an Object Literal in JavaScript.

# Create dictionary
person = { 
    'first_name': 'Brian',
    'last_name': 'Serein', 
    'age': 24
        } # a dictionary is created with curly braces

# Use a constructor
# person2 = dict(first_name='Gilbert', last_name='Serein', age=29)

print(person, type(person)) #This will print the dictionary and the type of the dictionary
# print(person2, type(person2)) #This will print the dictionary and the type of the dictionary



# Get a value
print(person['first_name']) #This will print the value of the key 'first_name'/ unlike Javascript, instead of using (.) notation, we use [].

print(person.get('last_name')) #This will print the value of the key 'last_name'

#^you can do either way to get a value in Python


# Add Key/Value
person['phone'] = '555-555-5555' #This will add a new key/value pair to the dictionary

print(person) #This will print the dictionary with the new key/value pair


# Get dictionary keys
print(person.keys()) #This will print the keys of the dictionary such as 'first_name', 'last_name', 'age', etc.


# Get dictionary items
print(person.items()) #This will print the items of the dictionary such as ('first_name', 'Brian'), ('last_name', 'Serein'), etc.


#Get dictionary values
print(person.values()) #This will print the values of the dictionary such as 'Brian', 'Serein', etc.


# Copy a dictionary
person2 = person.copy() #This will copy the dictionary into a new dictionary
# This is similar to a spread operator in JavaScript

person2['city'] = 'San Francisco' #This will add a new key/value pair to the dictionary

print(person2) #This will print the copy of the dictionary with the new key/value pair


# Remove item
del person2['city'] #This will remove the key/value pair from the dictionary

#anther method to remove a key/value pair
person2.pop('phone') #This will remove the key/value pair from the dictionary

print(person2) 


# Clear dictionary
person2.clear() #This will clear the dictionary
print(person2)


# Get length
print(len(person)) #This will print the length of the dictionary

# List of dictionaries
people = [
    {'name': 'Brian', 'age': 24},
    {'name': 'Gilbert', 'age': 29}
   ] #This is a list of dictionaries

print(people) #This will print the list of dictionaries
print(people[1]['age']) #This will print the age of the second dictionary in the list