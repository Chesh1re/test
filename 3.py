#!/usr/bin/python
#coding:utf8

from __future__ import division

def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def div(x,y):
	return x/y
def mul(x,y):
	return x*y

def cal(x,o,y):
	if o == '+':
		return add(x,y)
	elif o== '-':
		return sub(x,y)
	elif o=='*':
		return mul(x,y)
	elif o=='/':
		return div(x,y)
	else:
		pass
print cal(2,'+',3)
print cal(5,'-',1)
print cal(1,'*',3)
print cal(4,'/',2)

operator = {"+":add,"-":sub,"*":mul,"/":div}
print operator["+"](3,2)
def f(x,o,y):
	return operator.get(o)(x,y)
print add(2,3)
print f(3,"+",2)
def pp():
	print "this is pp"
