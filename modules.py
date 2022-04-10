# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
import time

# You can also import specific functions from a module
from datetime import date # You won't have to use the datetime module to get today's date, you can just use date
from time import time # You won't have to use the time module to get the current time, you can just use time

# You can also import all functions from a module
from datetime import * # This will import all functions from the datetime module
from time import * # This will import all functions from the time module

# Pip modules

from camelcase import CamelCase # camelcase is a module that converts strings into camelcase/ make sure to install it using pip (pip3 install camelcase)

# Import a custom module
import validator # This is a custom module that you can create and import
from validator import validate_email # You can also import specific functions from a custom module


# today = datetime.date.today() # This will get today's date
today = date.today() # This will get the current date
print(today)


# timestamp = time.time() # This will get the current timestamp
timestamp = time() # This will get the current timestamp
print(timestamp)


c = CamelCase()
print(c.hump('hello there world')) # Makes everything lowercase and then capitalizes the first letter of each word 


# When you use pip to install a module, because it's a package, you can import all functions from the module
# it is also worth noting you should use pip3 to install modules, pip is for python 2
# to see all the modules you can install using pip, use the following command: pip3 list or pip3 freeze


email = 'test@test.com' 
if validate_email(email): # This will return true if the email is valid and false if it's not
    print('Email is valid ') 
else:
    print('Email is not valid')


