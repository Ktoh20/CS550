#day one 36 minutes
#day tw

import random
import matplotlib.pyplot as plt

datafri = [36,42,68,28,64,52,68,60,46,0,120]
datasat = [48,38,59,32,43,12,128,60,52,0,120]
datasun = [78,60,188,60,154,135,86,	60,108,0,120]
datamon = [33,11,46,18,124,44,72,60,60,0,120]
# data14 = []
# data15 = []
# data16 = []
# data17 = []
# data19 = []
# results = []
for j in range(1000):
	for i in range(10):
		rtime1 = len(datamon)-random.randint(0,10)
		rtime2 = len(datafri)-random.randint(0,10)
		rtime3 = len(datasat)-random.randint(0,10)
		rtime4 = len(datasun)-random.randint(0,10)
		results.append(rtime1*11//60)
		results.append(rtime2*11//60)
		results.append(rtime3*11//60)
		results.append(rtime4*11//60)


		 

#display = []
#for i in range(len(results)):
#	display[results]
results.sort()
x_axis = [x for x in range(44000)]
data2 = [y for y in range(0,4400)]

#plt.plot(x_axis, display, 'bs', data2, 'r^')
plt.plot(results, color=(.5,0.,.5,1.))
plt.ylabel("minutes")
plt.xlabel("amnt of times it hit")
plt.show()