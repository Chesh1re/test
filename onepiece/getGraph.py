import urllib
import re
def gethtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html


def getGraph(html):
	reg=r'class="BDE_Image" src="(.*?\.jpg)" width'
	imreg=re.compile(reg)
	list=re.findall(imreg,html)
	print list
	x=0
	for i in list:
		urllib.urlretrieve(i,"%s.jpg" %x)
		x+=1
	return list

ll="http://tieba.baidu.com/p/2051538340"
lst=getGraph(gethtml(ll))
print lst
