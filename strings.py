#concatinate

name = 'Payam'
age = 38
print('Hello, I am '+ name + ' '+ 'and I am'+' '+ str(age))

#arguments by position
print('{}, {}, {}'.format('a','b','c'))

#arguments with position
print('{1}, {2}, {0}'.format('a','b','c'))

#arguments by name
print('My name is {name} and I am {age}'.format(name=name,age=age))

#F-strings only Python 3.6+
print(f'My name is {name} and I am {age}')

#string methods
#Capitaize first letter
s = 'this is Payam'
print(s.capitalize())

#Make everything uppser case
print(s.upper())

#make all lower
print(s.lower())

#make swap case
print(s.swapcase())

#get the length of a string
print(len(s))

print(s.replace('this','Hello, this'))

#count how many 'i' exist in a string
print(s.count('i'))

#get methods for string
print(dir(str))