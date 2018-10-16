#Kyn Toh
#Red picture2
#code for picture one
from PIL import Image
import random

imgx = 512
imgy = 512

image = Image.new("RGB", (imgx,imgy))

for n in range(512):
	for m in range(512):
		#change m for horizontal patterns and change n for vertical patters, by using both i was able to create an infinite back and forth of checkerboards within checkerboards
		image.putpixel((n,m), (50+int(40*(-1)^m*(-1)^n),0,0))

image.save("picred3.png","PNG") 