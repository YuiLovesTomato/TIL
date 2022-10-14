# -*- coding: utf-8 -*-



import numpy as np

import matplotlib.pylab as plt



min = 0

max = 35

gap = 1



x = np.arange(min, max, 1/gap)

y = np.arange(min, max, 1/gap)   #same

for i in range((max-min)*gap):

    y[i] = i

    if i/7!=0:

        y[i] = i%7

    y[i]=y[i]+1



plt.figure(1)   # assign window 01

plt.stem(x, y, "blue"); plt.grid()     # graph, grid

plt.xlabel("n"); plt.ylabel("x(n)")     # labeling

plt.title("complex exp sequence")



