# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# create func
def hello(name='ten'):
    print(f'Hello {name}')
    
# hello()

#Return values
def getSum(a, b):
    ttl = a + b
    return ttl

sum = getSum(1,4)
print(sum)

# A lambda function is a small anonymous function.
getSum = lambda a, b : a + b
print(getSum(11, 20))


# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

