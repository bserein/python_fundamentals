# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Oranges', 'Mangos', 'Strawberries')
# fruits2 = tuple(("Oranges", "Mangos", "Strawberries")) #This is with a constructor

# Single value needs trailing comma
fruits3 =("Oranges",) #This is a tuple with a single value because of the trailing comma (,) 
# without the trailing comma it would be a <str>

print(fruits, type(fruits3))


# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Apples' #This will not work because tuples are unchangeable



#Delete tuple
del fruits3 #This will delete the tuple

# print(fruits3) #This will print None because the tuple was deleted



# Get length
print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {"Apples", "Pears", "Blueberries"} # a set is created with curly braces

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("Grapes") #This will add the value to the set

print(fruits_set) #This will print the set with the new value



# add duplicate
fruits_set.add("Apples") #This will not add the value because it is a duplicate

print(fruits_set) #This will print the set without the duplicate value



# Remove from set
fruits_set.remove("Grapes") #This will remove the item from the set

print(fruits_set) #This will print the set without the "Grapes" value



# Clear set
fruits_set.clear() #This will clear the set

print(fruits_set) #This will print an empty set



# Delete set
del fruits_set #This will delete the set

print(fruits_set) #This will print None because the set was deleted