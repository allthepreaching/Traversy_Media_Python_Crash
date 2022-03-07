# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list (PREFERRED)
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# Create list using a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(fruits[1])

# Get length of a list

print(len(fruits))

# Append (Add) to the end of a list
fruits.append('Mangos')

print(fruits)

# Remove from a list
fruits.remove('Grapes')

print(fruits)

# Insert into a specifc position into a list
fruits.insert(2, 'Strawberries')

print(fruits)

# Pop (remove) from specific position of a list
fruits.pop(2)

print(fruits)

# Reverse a list
fruits.reverse()

print(fruits)

# Sort a list alphabetically
fruits.sort()

print(fruits)

# Sort a list reverse alphabetically
fruits.sort(reverse=True)

print(fruits)

# Change value in specific position in a list
fruits[0] = 'Blueberries'

print(fruits)
