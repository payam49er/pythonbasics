#open a file
file_path = '/Users/pshoghi/Desktop/sample_resource_RL.jsonl'
myFile = open('myfile.txt','w')
myFile.writelines('This is my test text one\n')
myFile.writelines('this is my test text two\n')
myFile.close()

#append to file
myFile = open('myfile.txt','a')
myFile.writelines('This is a third line\n')
myFile.close()

#read from a file
myFile = open(file_path,'r')
text = myFile.readlines(10)

for line in text:
    print(f'{line}\n')