#!/usr/bin/python

def fun():
	x=int(raw_input("please input:"))
	y=int(raw_input("please input:"))

	if x>=90 and y >=90:
		return 1;
	else:
		return 0;

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
