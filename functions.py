# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function
def sayHello(name): #To create a default you would put (name = 'Brian')
    print(f"Hello {name}")


# sayHello('Brian Serein') #This will print 'Hello Brian Serein'


# Return a value
def getSum(num1, num2):
    total = num1 + num2
    return total #This will return the value of the total variable

num = getSum(4,7) 
# print(num) #This will print 11


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2 #This will create a lambda function that will return the sum of the two numbers
# the colon is like arrow function in JS

print(getSum(10,5)) #This will print 15