a = b = c = 1
b = 1L
b = 0xa
c = long(b)
print a,b,c
a = "abcdefg"
a = a[2:5]
print a
a = [1,2,3,4,5]
b = []
b[:] = a
b.append(0)
print a[1:-1]
print hex(12)
print int(12.0/5)
print -7//5

a = 1
b = c = 1
a = [1,2,3]
b = [1,2,3]
c = b
d = [1,2]
print d is b
d.append(3)
print d is b
print a is b
print b is c

a = 100
b = 'abc'
print "%d %c %s is dog"%(a,b[0],b)

class A:
    def __init__(self,a):
        self.a = a
    def __str__(self):
        return "%s says: fuck u"%self.a

x = A("Gao")
print x


import re

line = "Cats are smarter than dogs"

matchObj = re.match( r' (.*) are (.*?) (.*) ', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(0)
   print "matchObj.group(2) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
   print "matchObj.group(2) : ", matchObj.group(3)
   print "matchObj.group(2) : ", matchObj.group(4)
else:
   print "No match!!"



A = []
for i in A:
    i.append(1)
print A


a = set()
b = set()
a.add(1)
a.add(2)
a.add(3)
print a
print a
a = a- set([1])
print a


