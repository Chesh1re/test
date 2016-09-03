#!/usr/bin/python
#coding:utf8

def fun():
	x=int(raw_input("please input:"))
	y=int(raw_input("please input:"))

	if x>=90 and y >=90:
		return 1
	else:
		return 0

if fun():
	print "pass!"
else:
	print "Dead!"

for i in range(1,10,2):
	print i,"good"
num=0
for n in range(1,101):
	num += n
print num
d = {1:'aaa',2:'bbb',3:'ccc',4:'ddd'}
dd=['aa','bb','cc','dd','ee']
for n in range(len(dd)):
	print dd[n]

for k,v in d.items():
	print k
	print v
	if k == 3:
		break
	if k == 2:
		print "#"*10
		continue
		print "test continue"
else:
	print "ending..."
while i!='e':
	print 2333333
	i=raw_input("input next key:")
	
	if not i:
		break
else:
	print "ending..."
def isE(x,y):
	if x==y:
		print x,'=',y
	else:
		print x,'!=',y
a=raw_input("give a:")
b=raw_input("give b:")

isE(a,b)

def mashine(x=3,y="呵呵"):
	print "生成一个",x,"型",y,"类的螺丝"
mashine()
mashine(y="噗")
mashine(4)
x="i am a global var"
def prr():
	global y
	y = 200

	global x
	x = 100

print x
prr()
print x
print y
