# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dictionary
person = {
    'first': 'John',
    'last': 'Doe',
    'age': 30
}

print(person, type(person))

# Create dictionary using constructor
person2 = dict(first='Sara', last='Jones')

print(person2, type(person2))

# Access a single value from a dictionary
print(person['first'])
print(person.get('last'))

# Add key/value pair to a dictionary
person['phone'] = '555-666-8877'

print(person)

# Get dictionary keys
print(person.keys())

# Get dictionary items
print(person.items())

# Copy a dictionary
person3 = person.copy()
person3['city'] = 'Bosstown'

print(person3)

# Remove a key/value pair from a dictionary
del(person['age'])
person.pop('phone')

print(person)

# Clear a dictionary
person.clear()

print(person)

# Get the length of a dictionary (number of key/value pairs)
print(len(person3))

# Get a list of dictionaries
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 35}
]

print(people)

# Get a specific value from a list of dictionaries
print(people[1]['name'])
