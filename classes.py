# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
# With python you can do pretty much anything with classes. You can create your own classes, inherit from other classes, and create objects from those classes. You can also create your own functions that are associated with a class.
# You can do procedural or object oriented programming.

# Create Class
class User:
    # Constructor
    def __init__(self, name, email, age): # self is a reference to the object being created/ init is a method of the User class
        self.name = name # self.name is a reference to the name attribute of the object being created
        self.email = email # self.email is a reference to the email attribute of the object being created
        self.age = age # self.age is a reference to the age attribute of the object being created

     # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
        self._private = 1000 # Encapsulated variables are declares with '_' in the constructor. 

    def greeting(self): # greeting is a method of the User class
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

    #function for encap variable
    def print_encap(self): # print_encap is a method of the User class and it takes a dictionary and converts it to JSON 
        print(self._private) 

# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age): 
        User.__init__(self, name, email, age) #Called proper parent class constructor to make this as proper child inehriting all methods.
        self.name = name 
        self.email = email
        self.age = age
        self.balance = 0 

    def set_balance(self, balance): 
        self.balance = balance 

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}' 

# Init user object
brian = User('Brian Serein', 'brian@gmail.com', 24) 
brian.has_birthday() # call the has_birthday method on the brian object and this will increase the age by 1
print((brian.greeting())) 

# Init customer object
john = Customer('John Smith', 'Johnsmith@gmail.com', 30)
john.set_balance(500) # call the set_balance method on the john object and this will set the balance to 500
print(john.greeting())

#Encapsulation -->
brian.print_encap()
brian._private = 800 #Changing for brian
brian.print_encap()

# Method inherited from parent
john.print_encap() #Changing the variable for brad doesn't affect johns variable --> Encapsulation
john._private = 600
john.print_encap()

#Similary changing john's doesn't affect brian's variable.
brian.print_encap()