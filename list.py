#!/usr/bin/python2.7
ethan = ["Ethan", 27]
catelyn = ["Catelyn", 29]
database = [ethan, catelyn]
print(database)

#index
greeting = "Hello"
print(greeting[0])
print(greeting[-1])

#slice & copy
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
print(tag[32:-4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
print(numbers[-3:])
print(numbers[:3])
print(numbers[:])

#step length
print(numbers[0:10:1])
print(numbers[0:10:3])
print(numbers[8:3:-2])

#add
print([1, 2, 3] + [4, 5, 6])

#multi
print("python" * 5)
print([None] * 10)

#in
permissions = "rw"
print('r' in permissions)
print('w' in permissions)
print("rw" in permissions)

#len max min
print(len(numbers))
print(max(numbers))
print(min(numbers))