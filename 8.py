f0=open('test.txt','r')
print f0.read()
f0=open('test.txt','r')
print f0.readline()
f0=open('test.txt','r')
print f0.readlines()
f0=open('test.txt','r')
print f0.next()
print f0.next()
print f0.next()

f1=open('tes,txt','w+')

f1.write("abc")
print f1.read()
print f1.read()
f1.flush()
l= ['one\n','two\n','three\n']
f1.writelines(l)

print f1.read()
f1.seek(0,0)
print f1.read()
f0.close()
f1.close()
#seek(offset,opt)  opt:0 head    1 current  2 end   

