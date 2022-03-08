# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON (like from an outside API)
userJSON = '{"first": "John", "last": "Doe", "age": 30}'

# Parse to dictionary
user = json.loads(userJSON)

print(user)
print(user['first'])

# Dictionary into JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1967}

carJSON = json.dumps(car)

print(carJSON)
