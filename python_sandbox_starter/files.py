# Python has functions for creating, reading, updating, and deleting files.

# Open file

file1 = open('file1.txt', 'w')

# get info on file
print('Name:', file1.name)
print('Closes:', file1.closed)

# write to file
file1.write('python oye')
file1.write('python is the best')
file1.close()

# append to file

# read from file
# use r+ as mode