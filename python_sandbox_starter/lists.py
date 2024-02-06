# A List is a collection which is ordered and changeable. Allows duplicate members.
# similar to arrays

# creating a list
numbers = [1,2,3,4,5]
fruits = ['mango', 'apples', 'guava']

# use a constructor 
# numbers2 = list((1,2,3,4,5))

# get a value
print(numbers[2])

# change a value
fruits[0] = "sugarcane"
# append to list
fruits.append("pears")

# insert to a position
fruits.insert(2, "berries")

print(numbers)
print(fruits)