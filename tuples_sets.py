# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create a tuple (must use parentheses)
fruits = ('Apples', 'Oranges', 'Grapes')

# Create a tuple using a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# A tuple with ONE value MUST have a trailing comma or it will be seen as only a string (str)
fruits3 = ('Apples',)

print(fruits, fruits2, fruits3, type(fruits3))

# Get specific item from tuple
print(fruits[1])

# Delete tuple
del fruits2

# Get length of tuple
print(len(fruits))

####################################################################

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set (must use curly braces)
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if something is in a set (boolean)
print('Apples' in fruits_set)

# Add to a set
fruits_set.add('Grapes')

print(fruits_set)

# Remove from a set
fruits_set.remove('Grapes')

print(fruits_set)

# Clear a set (does not DELETE set but clears all the items)
fruits_set.clear()

print(fruits_set)

# Delete a set
del fruits_set
