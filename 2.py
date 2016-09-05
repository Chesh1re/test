#!/usr/bin/python
#coding:utf8

def fun(n):
	if n>0:
		return n*fun(n-1)	
	else:
		return 1

a=fun(5)
print a
l=range(1,6)
print reduce(lambda x,y:x-y,l)
sum=reduce(lambda x,y:x+y,l)
print sum
import master
import master as cc
cc.master()
from master import master 
master()


