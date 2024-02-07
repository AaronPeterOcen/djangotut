# If/ Else conditions are used to decide to do something based on something being true or false

a = 1
b = 8

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# simple if
if a == b:
    print(f'{a} == {b}')

# if else
# if a == b:
#     print(f'{a} == {b}')
# else:
#     print(f'{a} =/= {b}')
    
# elif
# if a == b:
#     print(f'{a} == {b}')
# elif a < b:
#     print(f'{a} > {b}')
# else:
#     print(f'{a} =/= {b}')

# nested if
# if a < b:
#     if a <= b:
#         print(f'{a} is greater than ')

# Logical operators (and, or, not) - Used to combine conditional statements

# and
# if a > 2 and b <= 10:
#     print(f'{a} is greater than 2 and less than 11')

# # or
# if a > 2 or b <= 10:
#     print(f'{a} is greater than 2 or is less than 11')

# # not
# if not a == b:
#     print(f'{a}  is not == to {b}')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

nums = [1,2,3,4,5,6]

# in
if a in nums:
    print(a in nums)
    
# not in
if b not in nums:
    print(a not in nums)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
