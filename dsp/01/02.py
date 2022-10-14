# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np



#setting table

t = np.linspace(-0.01, 0.02, 100)



#init t(x)

amplitude = 5

frequency = 100

shift = 0

radian_frequency = 2*np.pi*frequency



x = amplitude*np.cos(radian_frequency*t + shift)



plt.title("02-100Hz")

plt.plot(t,x)

plt.show()
