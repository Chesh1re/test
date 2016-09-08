import re
import urllib
def getHTML(url):
	page=urllib.urlopen(url)
	html = page.read()
	return html

def getIMG(html):
	reg=r'src="(http://.*?\.jpg)" pic_ext="jpeg"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x=0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg' % x)
		x+=1
	return imglist
html=getHTML("http://tieba.baidu.com/p/3885457501")

print getIMG(html)

