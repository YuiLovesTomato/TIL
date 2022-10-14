# -*- coding: utf-8 -*-



import numpy as np

import matplotlib.pylab as plt



n = [-3,-2,-1,0,1,2,3,4]    # index sequence

xn = [2,1,-1,0,1,4,3,7]     # order sequence



plt.figure(1)   # assign window 01

plt.stem(n, xn, "blue"); plt.grid()     # graph, grid

plt.xlabel("n"); plt.ylabel("x(n)")     # labeling

plt.title("Representation of a sequence x(n)")
