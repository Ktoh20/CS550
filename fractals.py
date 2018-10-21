#kyn toh
#fractals project
#draft one
#started october 18th 2018
#on my honor
import random
import math
from PIL import Image
p = random.randint(0,255)

imgx = 512
imgy = 512

#def outside(n,m):
#	if abs(n)>3:
#		image.putpixel((512-n),(512-m))
#	else:
#		image.putpixel(n,m)


def fractal(z,y):
	c = y
	#while True:
	#	try:
	for i in range(z):
		if abs(z) > 2:
			image.putpixel((z,y),(255,255,255))
			return z
		z = z*z + c
		image.putpixel((y,z),(90+p,90+p,90+p))
		#else:
		#	image.putpixel((z,y),(90+p,90+p,90+p))
		fractal()



image = Image.new("RGB",(imgx,imgy))

fractal()

image.save("fractals1.png","PNG") 


