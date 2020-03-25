#create a class
class User:
    def __init__(self,name, email,age):
        self.name  = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name}'
    def has_birthday(self):
        self.age +=1



#initialize user object
payam = User('Payam Shoghi','payam49er@gmail.com',38)

#edit a property
payam.age = 38
payam.has_birthday()
print(payam.greeting())
print(payam.age)

#extending the user class, the customr class is inheriting from the User class
class Customer(User):
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self,balance):
        self.balance = balance
    def greeting(self):
        return f'My name is {self.name} and I have a balance of {self.balance}'


#init customer
john = Customer('John Doe','john@gmail.com',40)
print(john.name)

john.set_balance(500)
print(john.balance)

print(john.greeting())