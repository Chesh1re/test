#!/usr/bin/python
#coding:utf8

import os
def dirList(path):
	filelist = os.listdir(path)
	fpath = os.getcwd()
	allfile = []
	for filename in filelist:
		filepath=os.path.join(fpath,filename)
		if os.path.isdir(filepath):
			dirList(filepath)
		allfile.append(filepath)
	return allfile
print dirList('/users/cheshire/documents/test-py/test/testdir')
