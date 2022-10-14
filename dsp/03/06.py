# -*- coding: utf-8 -*-



import numpy as np

import matplotlib.pylab as plt



min = 0

max = 32

gap = 3



x = np.arange(min, max, 1/gap)

y = np.arange(min, max, 1/gap)   #same

for i in range((max-min)*gap):

    y[i] = 3*np.cos(0.1*np.pi*i/gap + np.pi/2)



plt.figure(1)   # assign window 01

plt.stem(x, y, "blue"); plt.grid()     # graph, grid

plt.xlabel("n"); plt.ylabel("x(n)")     # labeling

plt.title("complex exp sequence")
