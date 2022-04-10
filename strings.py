### Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brian'
age = 24

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age)) #can only concatenate str (not "int") to str

### String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age)) #Unlike JS, Python doesn't need `${}` to access variables, however it does need to format the string.

# F-Strings (Only available in Python 3.6+) 
print(f'My name is {name} and I am {age}') #F-Strings are like template literals in JS, they allow you to use variables in a string.

### String Methods

s = 'hello world'

# Capitalize string
print(s.capitalize()) # Capitalizes the first letter of the string

# Make all uppercase
print(s.upper()) # Makes all letters uppercase

# Make all lower
print(s.lower()) # Makes all letters lowercase

# Swap case
print(s.swapcase()) # Swaps the case of all letters in the string

# Get length
print(len(s)) # Returns the length of the string

# Replace
print(s.replace('world', 'everyone')) # Replaces all instances of the first argument with the second argument

# Count
sub = 'o'
print(s.count(sub)) # Returns the number of times the substring occurs in the string

# Starts with
print(s.startswith('hello')) # Returns True if the string starts with the argument

# Ends with
print(s.endswith('d')) # Returns True if the string ends with the argument

# Split into a list
print(s.split()) # Splits the string into a/an list/array based on the argument

# Find position
print(s.find('r')) # Returns the position of the first instance of the argument

# Is all alphanumeric
print(s.isalnum()) # Returns True if the string contains only letters and numbers
# This method returned False because the string contained a space

# Is all alphabetic
print(s.isalpha()) # Returns True if the string contains only letters
# This method returned False because the string contained a space.

# Is all numeric
print(s.isnumeric()) # Returns True if the string contains only numbers
