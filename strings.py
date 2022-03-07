# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'poopooplatter'
age = 9

# Concatenate - insert variable into a string
#print('Hello my name is '+name+' and I am '+str(age))

#########################################
# String Formatting

# Arguments by position
#print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
#print(f'Hello my name is {name} and I am {age}')

#########################################
# String Methods

s = 'hello world'

# Capitalization
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length (of any data type)
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count (the number of h's in the string)
sub = 'h'
print(s.count(sub))

# Starts with (boolean)
print(s.startswith('hello'))

# Ends with (boolean)
print(s.endswith('d'))

# Split into a list (creates and array of all the words)
print(s.split())

# Find position (index number of letter of first instance skipping spaces)
print(s.find('r'))

# Is all alphanumeric (boolean, False if contains a space)
print(s.isalnum())

# Is all alphabetic (boolean, False if contains a space)
print(s.isalpha())

# Is all numeric (boolean)
print(s.isnumeric())
