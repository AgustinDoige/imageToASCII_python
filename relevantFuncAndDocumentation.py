"""
PIL.Image.new(mode, size, color=0)[source]
Creates a new image with the given mode and size.

Parameters:	
mode – The mode to use for the new image. See: Modes.
size – A 2-tuple, containing (width, height) in pixels.
color – What color to use for the image. Default is black. If given, this should be a single integer or floating point value for single-band modes, and a tuple for multi-band modes (one value per band). When creating RGB images, you can also use color strings as supported by the ImageColor module. If the color is None, the image is not initialised.
Returns:	
An Image object."""


from PIL import Image
import numpy as np

def makeHalf(tpl):
	return (int(tpl[0]/2),int(tpl[1]/2),int(tpl[2]/2))

im = Image.open("test.png")
a = im.getdata()

b = list(a)
for i in range(len(b)):
	b[i] = makeHalf(b[i])

secIm = im.copy()
secIm.putdata(b)

secIm.show()