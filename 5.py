
import re
s=r'abc'
print re.findall(s,"aaaabcaaaabcaabv")
s=r"t[oi]p"
st="top tip tap twp tep"
print re.findall(s,st)
s=r"t[^oi]p"
print re.findall(s,st)
r= r"^abc"
print re.findall(r,"^abc") #cant find
r= r"\^abc"
print re.findall(r,"^abc") #can find
bb=r"abc$"
print re.findall(bb,"abcab")
print re.findall(bb,"ababc")
print re.findall(bb,"abcabc")
bb=r"abc[$]"
print re.findall(bb,"abcabc")
print re.findall(bb,"abcabc$")
aa=r"[0-9a-zA-Z]"
print re.findall(aa,"abcd1234ABCD")
a=r"\d"   # 0-9   \D   \s null   \S  \w numalphabet \W
print re.findall(a,"abcd1234ABCD")
aaa=r"01*0"
print re.findall(aaa,"01111111111100111111000")
aaa=r"01+0"
print re.findall(aaa,"01111111111100111111000")
r=r"^010-\d\d\d\d\d\d\d\d$"
print re.findall(r,"010-78839294")
print re.findall(r,"010-2312321")
print re.findall(r,"011-32432352")

r=r"^010-\d{8}$"
print re.findall(r,"010-78839294")
print re.findall(r,"010-2312321")
print re.findall(r,"011-32432352")
r=r"^010-?\d{8}$"
print re.findall(r,"01078839294")
print re.findall(r,"0102312321")
print re.findall(r,"01132432352")
print re.findall(r,"010-23123211")
# + ? * {n}  \

aaa=r"ab+?"
print re.findall(aaa,"abbbbbbbbbbbbbbbbbbbbbbbbb")
aaa=r"ab*?"
print re.findall(aaa,"abbbbbbbbbbbbbbbbbbbbbbabbab")
#min match ?
print re.findall(r"a{1,3}","a")
print re.findall(r"a{1,3}","aa")
print re.findall(r"a{1,3}","aaa")
print re.findall(r"a{1,3}","aaaa")
print re.findall(r"a{1,3}","aaaaa")
#  {0,}==*  {1,}==+  (0,1)==?
print re.findall(r"a{1,3}","")
