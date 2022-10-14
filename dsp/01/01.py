# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np



#setting table

t = np.linspace(-0.035, 0.05, 100)



#init t(x)

amplitude = 20

frequency = 40

shift = -0.4 * np.pi

radian_frequency = 2*np.pi*frequency



x = amplitude*np.cos(radian_frequency*t + shift)



plt.title("01")

plt.plot(t,x)

plt.show()
