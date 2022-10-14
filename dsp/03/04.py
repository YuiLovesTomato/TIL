# -*- coding: utf-8 -*-



import numpy as np

import matplotlib.pylab as plt



def expseq(n0, n1, n2): # unit exp sequence

    N = n2-n1+1         # data amount    

    n = np.arange(N)    # order sequence

    xn = np.zeros(N)    # data array setting

    for i in range(N):      # generating

        if (i+n1)>=n0: xn[i]=np.power(0.7, i)

    return n, xn        # multi-return for stem



result = expseq(0, 0, 18)



plt.figure(1)   # assign window 01

plt.stem(result[0], result[1], "blue"); plt.grid()     # graph, grid

plt.xlabel("n"); plt.ylabel("x(n)")     # labeling

plt.title("unit exp sequence")
