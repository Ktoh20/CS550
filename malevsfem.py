import random
import matplotlib.pyplot as plt
names = ['fri', 'sat', 'sun', 'mon']
plt.figure(1,figsize=(15,3))
valuesm = [96.77777778,100.8888889,114.8888889,56.88888889]
valuesf = [73.11111111,70.88888889,122.8888889,56.11111111]
# values16 = [44.6,37.5,99.16,48.3]
# values17 = [68.6,72.2,154.4,39.6]
# values18 = [56,82.2,61.4,39.4]
plt.subplot(121)
plt.bar(names,valuesm , color=(.5,0.,.9,1.))
plt.subplot(122)
plt.bar(names,valuesf , color=(.75,.4,.6,.4))
# plt.subplot(153)
# plt.bar(names,values16 , color=(.65,.3,.2,1.), label='16 year olds')
# plt.subplot(154)
# plt.bar(names,values17 , color=(.55,.2,.3,1.), label='17 year olds')
# plt.subplot(155)
# plt.bar(names,values18 , color=(.45,.1,.4,1.), label='18 year olds')
plt.suptitle('male vs female')
#plt.legend()
plt.show()