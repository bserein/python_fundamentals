# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w') # w is for write, r is for read, a is for append, w+ is for write and read (overwrite)

# Get info
print('Name: ', myFile.name) # MyFile is basically an object that has properties and methods associated with it
print('Is Closed: ', myFile.closed) # True if the file is closed, False if it is open
print('Opening Mode: ', myFile.mode) # Mode is the way the file is opened

# Write to file
myFile.write('I love Python') # Write to the file
myFile.write(' and Javascript') # Write to the file
myFile.close() # Close the file

# Append to file
myFile = open('myfile.txt', 'a') # a is for append
myFile.write(', I also like C#')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+') # r+ is for read and write
text = myFile.read(100) # Read 100 characters from the file
print(text)