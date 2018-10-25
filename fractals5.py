#kyn toh
#class code
#october 19th 2018-->october 25th 2018
#on my honor
#sources:none
#this will take at least 6 minutes to load
#this code creates 3 fractals and saves them as kyntohsfractalyeet123.png,KynTohMandelbrotCOol12345768.png, and KynTohMandelbrotCOol1234576.png
import colorsys
import csv
import random
from PIL import Image
#flipped y, x minus the image side so you start form zero to the bottom up
#change xmin and xmax ymin and ymax to zooooom
#colorsys
def kynuniquefractal1():
	#range and domain
	xmin, xmax = -0.5, 0.5
	ymin, ymax = -0.5, 0.5


	imgx, imgy = 2048, 2048

	image = Image.new("RGB", (imgx,imgy))

	maxIt = 256

	for y in range(imgy):
		cy = y * (ymax-ymin) / (imgy-1)+ymin
		for x in range(imgx):
			#x*xmax-xmin/(imgx-1)+xmin=equation for cx value
			cx = x * (xmax-xmin) / (imgx-1)+xmin
			c = complex(cx,cy)
			z = 0 
			for i in range(maxIt):
				#changes the amount of times before one point can escape the circle
				if abs(z) > 3.5:
					break
				z = z**3.5 + c*i
				#add i and change exponents to increase the ranges and reflections capable within the circle
				# if its even there will be at least four refelctive lines, if there are decimals then there is 1
				# and if odd then 2
	#keep i in the color to keep the mandelbrot shape
			r = (i*45)%256
			g = (i*22)%256
			b = 2324356//i

			image.putpixel((x,y),(r,g,b))
	image.save("kyntohsfractalyeet123.png","PNG")

def mand1():
	#more conversons between hsv to rgb
	test_color = colorsys.hsv_to_rgb(0.5, 0.8, 0.7)

	xmin, xmax = -0.1762990951538086, -0.17206764221191406
	ymin, ymax = 1.0685005187988281, 1.072731917407227

	imgx, imgy = 2048, 2048

	image = Image.new("RGB", (imgx,imgy))

	maxIt = 256

	for y in range(imgy):
		cy = y * (ymax-ymin) / (imgy-1)+ymin
		for x in range(imgx):
			#x*xmax-xmin/(imgx-1)+xmin=equation for cx value
			cx = x * (xmax-xmin) / (imgx-1)+xmin
			c = complex(cx,cy)
			z = 0 
			for i in range(maxIt):
				if abs(z) > 2.0:
					break
				z = z**2 + c
	#keep i in the color to keep thte mandelbrot shape
	#conversions from hsv->rgb->keeping i inside
			r = 255
			g = (i*25)%256
			b = 25//i

			image.putpixel((x,y),(r,g,b))
	image.save("KynTohMandelbrotCOol12345768.png","PNG")


def mand2():
	#using this to get colors for later
	test_color = colorsys.hsv_to_rgb(0.6, 0.8, 0.8)
	#range and domain of viewpoint
	xmin, xmax = -1.7878027943255592, -1.787694319790205
	ymin, ymax = -0.000053366055292158876, 0.00005510848006196056

	imgx, imgy = 2048, 2048

	image = Image.new("RGB", (imgx,imgy))

	maxIt = 256

	for y in range(imgy):
		cy = y * (ymax-ymin) / (imgy-1)+ymin
		for x in range(imgx):
			#x*xmax-xmin/(imgx-1)+xmin=equation for cx value
			cx = x * (xmax-xmin) / (imgx-1)+xmin
			c = complex(cx,cy)
			z = 0 
			for i in range(maxIt):
				if abs(z) > 2.0:
					break
				z = z**2 + c
	#keep i in the color adn youll keep thte mandelbrot shape
	#conversions from hsv->rgb->keeping i inside and i got these numbers:
			r = 128
			g = (i*192)%256
			b = 192//i

			image.putpixel((x,y),(r,g,b))
	image.save("KynTohMandelbrotCOol1234576.png","PNG")


kynfractal1()
mand1()
mand2()
