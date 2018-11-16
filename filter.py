from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
import csv
import colorsys
import math

#from transforms import
#im1 = im.filter(ImageFilter.BLUR)
image = Image.open("grass.jpeg") 
imgx,imgy = image.size
px = image.load()
d = ImageDraw.Draw(image)
for x in range(imgx):
	for y in range(imgy):
		abc = px[(x,y)]
		#a+=1
		#b+=1
		#c+=1
		#print(abc)
		# a = 255
		# b = 25
		# c = 0
		d.text((500,500), "retliF", fill=(255,0,0))
	image.putpixel((x,y),(abc))
image.rotate(135).show()