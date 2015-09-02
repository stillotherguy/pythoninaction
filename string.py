#!/usr/bin/python2.7
#encoding=UTF-8
print(repr("I am Ethan"))
print(repr(10000000L))

print(`100000000000L`)

print(str("I am Ethan"))
print(str(100000000L))

print(r'\n\n\n\n\n\n\n')
print(u'Hello World')
print('''hahahahaha
	hahahahaha''')
print('hehehe\
	hehehe')
print(None)

#format
format = "Hello, %s %s enough for ya %%"
values = ("world", "hot")
print(format % values)

from math import pi
format = "PI with three decimals: % 10.3f"
print(format % pi)

from string import Template
s = Template("$x, glorious $x $$")
print(s.substitute(x='slum'))

s = Template("A $thing must never $action")
d = {"thing" : "gentleman", "action" : "show his socks"}
print(s.substitute(d))

from string import digits
from string import printable
from string import punctuation

print(digits)
print(printable)
print(punctuation)

#字符串方法
print("With a moo-moo here, and a moo-moo there".find("moo"))
print("With a moo-moo here, and a moo-moo there".find("moo", 18 , 28))

print(",".join(["a", "b", "c", "d"]))
print("ABCDEFG".lower())
print("BBBBBBBB".replace("B", "A"))
print("1,2,3,4".split(","))
print("*** SPAM * for * everyone!!! ***".strip(" *!"))

