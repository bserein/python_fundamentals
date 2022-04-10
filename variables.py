# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1 # int
y = 2.5 # float
name = 'John' # string (can use single or double quotes)
is_cool = True # boolean (Needs to be Capitalized)

#Multiple Assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic Math
a = x + y

# print(type(x)) # Prints the data type of x

# Casting
x = str(x) # Converts x to a string
y = int(y) # Converts y to an integer
z = float(y) # Converts y to a float

# print(type(x), type(y), y, type(z), z) # Prints the data type of x, y, z
