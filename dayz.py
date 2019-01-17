import random
import matplotlib.pyplot as plt
names = ['fri', 'sat', 'sun', 'mon']
plt.figure(1,figsize=(15,3))
values14 = [139,142,119.8,89.8]
values15 = [54.6,38,66.8,46]
values16 = [44.6,37.5,99.16,48.3]
values17 = [68.6,72.2,154.4,39.6]
values18 = [56,82.2,61.4,39.4]
plt.subplot(151)
plt.bar(names,values14 , color=(.5,0.,.5,1.), label='14 year olds')
plt.subplot(152)
plt.bar(names,values15 , color=(.75,.4,.6,1.), label='15 year olds')
plt.subplot(153)
plt.bar(names,values16 , color=(.65,.3,.2,1.), label='16 year olds')
plt.subplot(154)
plt.bar(names,values17 , color=(.55,.2,.3,1.), label='17 year olds')
plt.subplot(155)
plt.bar(names,values18 , color=(.45,.1,.4,1.), label='18 year olds')
plt.suptitle('Difference in age averages over 5 days')
plt.show()