# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list (this is kind of like an array in JS)
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Pears', 'Apricots', 'Mangos']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5)) # This is the same as above, but like in JS you can say newArray = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

# Get a value
print(fruits[1]) 

# Get length
print(len(fruits)) 

# Append to list (adds to the end of the list)
fruits.append('Bananas') # This is the same as fruits.push('Bananas')

print(fruits)

# Remove from list (removes a value from the list)
fruits.remove('Pears') # This is the same as fruits.pop('Pears')

print(fruits)

# Insert into position
fruits.insert(2, 'DragonFruit') # Inserts at position 2

print(fruits)

# Change value
fruits[0] = 'Kiwi'

print(fruits)

# Remove from position
fruits.pop(2) # Removes from position 2 which is DragonFruit

print(fruits)

# Reverse list
fruits.reverse() # Reverses the list (does not mutate the list)

print(fruits)

# Sort list
fruits.sort() # Sorts in alphabetical order 

print(fruits)

# Reverse sort
fruits.sort(reverse=True) # Sorts in reverse alphabetical order

print(fruits)