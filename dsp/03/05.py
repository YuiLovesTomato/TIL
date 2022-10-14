# -*- coding: utf-8 -*-



import numpy as np

import matplotlib.pylab as plt



x = np.arange(0, 10, 0.1) #fill 0 to 10, 100 points

y = np.arange(0, 10, 0.1)   #same

for i in range(100):    #for 100 each points

    y[i] = np.exp((2+3j)*(i/10))  #y[i] is e^0.1, e^0.2... so i/10



plt.figure(1)   # assign window 01

plt.stem(x, y, "blue"); plt.grid()     # graph, grid

plt.xlabel("n"); plt.ylabel("x(n)")     # labeling

plt.title("complex exp sequence")
