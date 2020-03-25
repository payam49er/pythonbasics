names = ['Bob', 'Alice', 'Guido']

# foreach style in Python
for person in names:
    print(person)

for index, value in enumerate(names):
    print(f'{index} {value}')

for i in range(len(names)):
    print(f'{i} {names[i]}')

print("*********************")

count = 0
while count <= 10:
    print('count', count)
    count+=1


