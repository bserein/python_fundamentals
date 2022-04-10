# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']


# Simple for loop - Loops through a list (or any sequence) / This is similar to For in in JS
for person in people:
    print(f'Current Person: {person}') # This will print out each person in the list


# Break - This will break out of the loop when the condition is met (i.e. when the current person is 'Sara')
for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}') # This will print out each person in the list until it reaches 'Sara' then stop the loop


# Continue - This will skip the current iteration of the loop and continue to the next iteration
for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}') # This will print out each person in the list until it reaches 'Sara' then continue to the next iteration and print out the next person in the list


# Range 
for i in range(5): # This will create a list of numbers from 0 to 4 (i.e. [0,1,2,3,4])
    print(i)

for i in range(len(people)): # This will create a list of names from the people list (i.e. John, Paul, Sara, Susan)
    print(people[i])

for i in range(0, 11): # This will create a list of numbers from 0 to 10 (i.e. [0,1,2,3,4,5,6,7,8,9,10])
    print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0 
while count <= 10:
    print(f'Count: {count}')
    count += 1 # This will add 1 to the count variable each time the loop runs