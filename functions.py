def sayHello(name):
    """
    Prints Hello and then name.
    """
    print(f'Hello {name}')

sayHello("Payam")


def addNumbers(a,b):
    return a+b


print(addNumbers(4,5))


#lambda function is a small anonymous function. It is the same as arrow functions
#it can get as many parameters, but it can have only one expression

getSum = lambda num1,num2 : num1 + num2

print(getSum(9,2))

add = (lambda x: x+1) (2)
print(add)