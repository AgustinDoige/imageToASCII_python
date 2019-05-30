from PIL import Image
import numpy as np

def writeImage(im,fileName):
	data = list(im.getdata())
	x = im.getbbox()[2]
	y = im.getbbox()[3]
	c = 0
	with open(fileName,'w') as f:
		for i1 in range(x):
			for i2 in range(y):
				f.write(getASCII(data[c]))
				c+=1
			f.write("\n")

def getASCII(tpl):
	val = int(sum(tpl)/3)
	if (val<51):
		return ' '
	if (val<101):
		return ':'
	if (val<151):
		return '+'
	if (val<201):
		return 'G'
	return '*'

def makeHalf(tpl):
	return (int(tpl[0]/2),int(tpl[1]/2),int(tpl[2]/2))

def normalize(tpl): # Used in greyScale(im)
	val = int((tpl[0]+tpl[1]+tpl[2])/3)
	return (val,val,val)

def greyScale(im): #Returns a copy of im with in black and white
	ImLis = list(im.getdata())
	for i in range(len(ImLis)):
		ImLis[i] = normalize(ImLis[i])
	Im2 = im.copy()
	Im2.putdata(ImLis)
	return Im2

def getImage(fileString,width):  #Returns an Image Object correctly resized.
	im = Image.open(fileString)
	x = im.getbbox()[2]
	y = im.getbbox()[3]
	size = (width,int(y*width/x))
	return greyScale(im.copy().resize(size))

outputWidth = 150
# b = getImage("test.png",outputWidth)
fileN = "test2.jpg"
b = getImage(fileN,outputWidth)
writeImage(b,"example.txt")
# writeImage(Image.open("test.png"),"example.txt")


"""
for i in range(len(b)):
	b[i] = makeHalf(b[i])

secIm = im.copy()
secIm.putdata(b)
secIm.resize()
secIm.show()
"""