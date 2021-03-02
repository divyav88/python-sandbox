# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
print('TUPLES')
 # Create tuple
fruits = ('Apples', 'Oranges', 'Grapes', 'Pears')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes', 'Pears'))
fruits2 = ('Apples')
print(fruits2, type(fruits2)) # type is string here

# Single value needs trailing comma
fruits2 = ('Apples',)
print(fruits2, type(fruits2)) # type is tuple here

# Get a value
print(fruits[1])

# Can't change value
#fruits[0] = 'Strawberries'

# Delete a tuple
del fruits2
#print(fruits2)

# Length of tuple
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

print('SETS')

# Create a Set
fruits_set = {'Apples', 'Oranges', 'Mangoes'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Add duplicate
fruits_set.add('Apples') # no error but will not add again

# Clear set
#fruits_set.clear()

# Delete set
#del fruits_set

print(fruits_set)