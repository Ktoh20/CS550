import random
import matplotlib.pyplot as plt

results = []
for j in range(1000):
	total = 0
	for i in range(10):
		flip = random.randint(0,1)
		total += flip
	results.append(total)

display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]]+=1

x_axis = [x for x in range(11)]
data2 = [y for y in range(6,16)]

#plt.plot(x_axis, display, data2)
plt.bar(x_axis, display, color=(.5,0.,.5,1.))
plt.ylabel("commonality")
plt.xlabel("hours per 5 days")
plt.show()