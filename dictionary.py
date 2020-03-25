#simple dic
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age': 30
}

print(person)


#access value
print(person['first_name'])
print(person.get('last_name'))

#add key value
person['phone'] = '555-555-5555'
print(person.items())


print(len(person))