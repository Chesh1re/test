import re
import urllib
def getHTML(url):
	page=urllib.urlopen(url)
	html = page.read()
	return html

def getIMG(html):
	reg=r'img src="(http://.*?\.jpg)" alt'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x=41
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg' % x)
		x+=1
	return imglist
html=getHTML("http://www.justinmaller.com/project/mythic/")

print getIMG(html)

