# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object


# create class

class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    # creating mrethods
    def greeting(self):
        return f'I am {self.name} and i am {self.age}'
    
# extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        
    def setBalance(self, balance):
        self.balance = balance
        
    def greeting(self):
        return f'I am {self.name} and i am {self.age} amd balance is {self.balance}'
        
# init user objct
brad = User('Aaron Peter', 'oce@mail.com', 24)

# init customer object
jane = Customer('Jane Grace', 'JaneG@gmail.com', 24)

jane.setBalance(300)

print((brad.greeting()))