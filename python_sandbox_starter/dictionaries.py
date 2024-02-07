# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# key value pair

# create dict
perpe = {
    'name1' : 'ocen',
    'name2' : 'aaron',
}

# use a constructor
# person2 = dict(name1='peter', name2="micke")

# get value
print(perpe['name1'])

# add value
perpe['address'] = '2034.2324.20434'

# get dict keys
print(perpe.keys())

# copy dict
perpe2 = perpe.copy()
perpe2['city'] = 'Boston'

# get len
print(len(perpe2))

# list of dict
pepple = [
    {'name': 'Cathy', 'age':23},
    {'name': 'Martha', 'age': 22}
]

print(pepple[1]['name'])


print(perpe2, type(perpe2))
