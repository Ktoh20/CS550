import random
import matplotlib.pyplot as plt
names = ['fri', 'sat', 'sun', 'mon']
plt.figure(1,figsize=(15,3))
values14 = [139,142,119.8,89.8]
values15 = [54.6,38,66.8,46]
values16 = [44.6,37.5,99.16,48.3]
values17 = [68.6,72.2,154.4,39.6]
values18 = [56,82.2,61.4,39.4]
#plt.subplot(151)
plt.plot(names,values14 , 'r--', label='14 year olds')
#plt.subplot(152)
plt.plot(names,values15 , 'g-', label='15 year olds')
#plt.subplot(153)
plt.plot(names,values16 , color=(.65,.3,.2,1.), label='16 year olds')
#plt.subplot(154)
plt.plot(names,values17 , 'b--', label='17 year olds')
#plt.subplot(155)
plt.plot(names,values18 , color=(.45,.1,.4,.5), label='18 year olds')
#plt.suptitle('Difference in age averages over 5 days')
plt.legend()
plt.show()