#coding:utf8
import copy

a=[1,2,3,['a','b','c'],'d']
b=a
c=copy.copy(a)
print id(a)
print id(b)
print id(c)
a.append(4)
print a
print b
print c
print id(a)
print id(b)
print id(c)

a[3].append('d')
print id(a)
print id(b)
print id(c)
print a
print b
print c
print "########"
d=copy.deepcopy(a)
print a
print d
a[3].append('e')
print a
print c
print d
#copy 浅拷贝，对引用的拷贝，里面的元组变动也会跟着变  deepcopy 对对象的拷贝，全新无任何关系
