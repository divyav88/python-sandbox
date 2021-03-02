# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Divya'
age = 26

# Concatename
#print('Hello, my name is '+ name + ' and I am '+ str(age))

# String Formatting

# Arguments by position
#print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
#print(f'Hello, My name is {name} and I am {age}')

# String Methods
s = 'hello world'

# Capitalize string
print(f'Capitalize string = {s.capitalize()}')

# Upper case
print(f'Upper case = {s.upper()}')

# Lower case
print(f'Lower case = {s.lower()}')

# Swap case
print(f'Swap case = {s.swapcase()}')

# Get length
print(f'Get length = {len(s)}')

# Replace
print(f"Replace = {s.replace('world','everyone')}")

# Count
sub = 'h'
print(f'Count = {s.count(sub)}') # it is case sensitive

# Starts with
print(f"Starts with = {s.startswith('hello')}")

# Ends with
print(f"Ends with = {s.endswith('d')}")

# Split into a list
print(f'Split into a list = {s.split()}')

# Find position
print(f"Find position = {s.find('r')}")

# Is all alphanumeric
print(f'Is all alphanumeric = {s.isalnum()}')

# Is all alphabetic
print(f'Is all alphabetic = {s.isalpha()}')

# Is all numeric
print(f'Is all numeric = {s.isnumeric()}')