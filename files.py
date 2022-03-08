# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myFile.txt', 'w')

# Get file info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to a file
myFile.write('I love python')
myFile.write(' and javascript.')
myFile.close()

# Append to a file
myFile = open('myFile.txt', 'a')
myFile.write(' I love php as well.')
myFile.close()

# Read from a file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
