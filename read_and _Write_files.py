file = open('test.txt')
#read the content of the file
print(file.read())
#i want to read first 2 charecter in evry data
print(file.read(2))

# i want ot get the data line wise
print(file.readline())

# when we try to r=use readline when read already used the pointer must at the 2 character. so . it'll read from the after two charecters

# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()