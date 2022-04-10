# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# Sample JSON   
userJSON = '{"first_name": "Brian", "last_name": "Serein", "age": 24}'

# Parse to dictionary
user = json.loads(userJSON) # loads is a method of the json module that takes a string and converts it into a dictionary
print(user['first_name']) # print the first_name attribute of the user dictionary
print(user) # print the user dictionary


car = {'make': 'Tesla', 'model': '3', 'year': 2022}

carJSON = json.dumps(car) # dumps is a method of the json module and it takes a dictionary and converts it to JSON
print(carJSON)