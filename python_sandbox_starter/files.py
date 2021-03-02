# Python has functions for creating, reading, updating, and deleting files.

# Open a file (it creates a file if not available)
myFile = open('myfile.txt', 'w')

# Get some info
print(f'Name: {myFile.name}')
print(f'Is Closed: {myFile.closed}')
print(f'Opening Mode: {myFile.mode}')

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like C#')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
