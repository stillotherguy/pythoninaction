#!/usr/bin/python2.7
#encoding=UTF-8
class Person:
	__metaclass__ = type
	def __init__(self):
		self.name = "Ethan"
		self.age = 27

	def desc(self, *params):
		print self.name + "---" + repr(self.age)
		for param in params:
			print param
		return

p = Person()
p.desc("ahahah", "24123123")


def thread1():  
    for x in range(4):  
        yield  [x, x, x]  
           
   
def thread2():  
    for x in range(4,8):  
        yield  [x, x, x]  
           
   
threads=[]  
threads.append(thread1())  
threads.append(thread2())  
   
   
def run(threads):  
    for t in threads:  
        try:  
            print t.next()  
        except StopIteration:  
            pass 
        else:  
            threads.append(t)   
   
run(threads)

lst = [(x,y) for x in range(10) for y in range(20)]
print(lst)
print(dict(lst))
print(iter(lst))

generator = (x for x in range(10))
print(generator)
print(iter(generator))
print(generator.next())
print(generator.next())
print(generator.next())
print(generator.next())
import copy
if __name__ == "__main__":
	print(dir(copy))