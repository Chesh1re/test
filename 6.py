import re
r1=r"^\d{3,4}-?\d{8}$"
p_tel=re.compile(r1)
p_tel.findall("010-12345678")
ll=re.compile(r'abcd',re.I)
print ll.findall('abcd')
print ll.findall('AbCd')

ll=re.compile(r'abcd',re.I)
print ll.findall('abc\\d')
print ll.findall('Ab\\Cd')

a=r'ab'
l=re.compile(a,re.I)
print l.match('aabcab')
print l.match('abcab').group()
print l.search('acab').group()

print l.match('abcab').start()
print l.match('abcab').end()
print l.match('abcab').span()
rs=r'c..t'
print re.sub(rs,'python','csvt caat cvvt cccc')

print re.subn(rs,'python','csvt caat cvvt cccc')
ip="1.2.3.4"
print ip.split(".")

s=r"123+345-789*000"
print re.split(r'[\+\-\*]',s)
email=r"\w{3}@\w+(\.com|\.cn)"
print re.match(email,'zzz@adf.com')
print re.match(email,'zzz@adf.cn')
print re.match(email,'zzz@adf.cm')
email=r"\w{3}@\w+(\.com|\.cn)"
print re.findall(email,'zzz@adf.com')
print re.findall(email,'zzz@adf.cn')
print re.findall(email,'zzz@adf.cm')
ss="""
ccb aa 
aa ccb
ccb cc
aa ccb
"""
print ss
sa=r"^ccb"
print re.findall(sa,ss,re.M)
