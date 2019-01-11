#assuming that 4 blocks is the maximum he can walk, the longest walk he could take is an even number over twenty

#2. monte carlo simulations are simulations that are used to measure the possible outcomes of a situation that cannot usually be predicted because of outside factors. It is also used to understand the impact of risks
#problem 3
import matplotlib.pyplot as plt
import random
square = []
c = 0

for i in range(1001):
	x = random.randint(-1,1)
	y = random.randint(-1,1)
	if x*y>=1 or x*y<=-1:
		c+=1

print(c/100)
plt.Circle((0,0),1)
plt.show()

#problem 1&2
x = 0
y = 0
b = 0
grid = []
for i in range(11):
	d = random.randint(1,4)
	if d == 1:
		y+=1
		print(x,y)
		plt.plot([x],[y],'ro')
	if d == 2:
		x+=1
		print(x,y)
		plt.plot([x],[y],'ro')
	if d == 3:
		y-=1
		print(x,y)
		plt.plot([x],[y],'ro')
	if d == 4:
		x-=1
		print(x,y)
		plt.plot([x],[y],'ro')
#how far from home
print(x+y)
if x+y <= 4:
	print("you dont need to walk home")
else:
	b+=1
plt.show()

#for 100 simulations i get around 40% and the percentage then doesnt change for any number above and the equation i used represnted pi/2
