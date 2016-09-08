#!/usr/bin/python
#coding:utf8

import os
def dirList(path,allfile):
	filelist = os.listdir(path)
	fpath = os.getcwd()
	for filename in filelist:
		filepath=os.path.join(fpath,filename)
		allfile.append(filepath)
		if os.path.isdir(filepath):
			dirList(filepath,allfile)
		
	return allfile
allfile=[]
print dirList('/users/cheshire/documents/test-py/test/testdir',allfile)
print [x for x in os.walk('/users/cheshire/documents/test-py/test')]
