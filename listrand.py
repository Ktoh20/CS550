import random
x = []
y = []
for i in range(0,10):
	if random.randint(0,101%3) == 0:
		x.append(random.randint(1,100))
	else:
		y.append(random.randint(1,100))
		 
	print(x)

