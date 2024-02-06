# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# unchangeable
# same as a list but is unchangeable

fruits = ('apples', 'pears', 'berries')
# fruits2 = tuple(('apples', 'pears', 'berries'))

# single tuple value needs a trailing comma
fruits2 = ('apple',)
# print(fruits2, type(fruits2))

# delete a tuple
del fruits2
# print(fruits2)


# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruits_set = {'Apple', 'Oranges', 'Mango'}
print(fruits_set)

# check if in set
print('Mango' in fruits_set)

# Add to set
(fruits_set.add('Grape'))

# add duplicate
(fruits_set.add('Apple'))

print(fruits_set)

# remove from set
(fruits_set.remove('Grape'))
print(fruits_set)

