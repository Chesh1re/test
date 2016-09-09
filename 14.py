import urllib
import re
def gethtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

def getGraph(html):
	ree=r'img src=".*?.jpg" style'
	list=re.findall('ree',html)
	x=0
	for i in list:
		urllib.urlretrieve(i,"%s.jpg" %x)
	return list


ll="http://tieba.baidu.com/p/1934517161#!/l/p1"
lst=getGraph(gethtml(ll))
print lst
