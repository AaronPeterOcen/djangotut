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


print(perpe, type(perpe))
