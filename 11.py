#coding:utf8
filename = raw_input('请输入你要操作的文件：')
try:
    f = open(filename)
    print hello
except IOError, msg:
    print "你指定的文件不存在"
except NameError, msg:
    print "内部变量调用错误"
finally:
    print "ok"
print "aaaa"

if filename == 'hello':
    raise TypeError("nothing!!!")

print "aa"
def aa():
	if 1==2:
		print "aaaa"


