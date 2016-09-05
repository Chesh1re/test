def ff(x,y):
	return x*y
l=range(1,10)
print reduce(ff,l)
def fff(x):
	if x>3:
		return True
print filter(fff,l)
print filter(lambda x:x>3,l)
a=[1,2,3]
b=[3,4,5]
print zip(a,b)
c=[8,9]
print zip(a,b,c)
print map(None,a,b)
print map(None,a,b,c)
print map(ff,a,b)
print [x*2 for x in l]
print [x*y for x in range(10) if x>3 if x%2 for y in range(5) if y%3]

print [x*y for x in range(10) if x>3 if x%2 for y in range(5) if not (y%3)]
