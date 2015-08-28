#!/usr/bin/python2.7
#coding=UTF-8
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

#分片赋值
numbers[0:3] = [3, 3, 3]
print(numbers)

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

#list()
strs = list("Hello World")
print(strs)
print("".join(strs))

#基本列表操作
#元素赋值
x = [1, 1, 1]
x[1] = 2
print(x)

#删除元素
names = ["Ethan", "Catelyn"]
del names[0]
print(names)

names = ["Ethan", "Catelyn", "Jack"]
del names[:]
print(names)

#元素添加
lst = [1, 2, 3]
lst.append(4)
print(lst)

#统计
lst = ["to", "be", "or", "not", "to", "be"]
print(lst.count("to"))

#合并
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

#查询
knights = ["We", "are", "the", "knights"]
print(knights.index("are"))

#插入
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers.insert(3, "four")
print(numbers)

#pop 
x = [1, 2, 3]
print(x.pop())

#remove
x = [1, 2, 3]
x.remove(1)
print(x)

#reverse
x = [1, 2, 3]
x.reverse()
print(x)

#sort
x = [4, 6, 1, 9, 5, 2]
print(sorted(x))
x.sort()
print(x)