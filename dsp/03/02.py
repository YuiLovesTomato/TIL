# -*- coding: utf-8 -*-



import numpy as np

import matplotlib.pylab as plt



def impseq(n0, n1, n2): #unit sample sequence

    N = n2-n1+1         # data amount    

    n = np.arange(N)    # order sequence

    xn = np.zeros(N)    # data array setting

    for i in range(N):      # generating

        if (i+n1)==n0: xn[i]=1

    return n, xn        # multi-return for stem



result = impseq(0, 0, 20)



plt.figure(1)   # assign window 01

plt.stem(result[0], result[1], "blue"); plt.grid()     # graph, grid

plt.xlabel("n"); plt.ylabel("x(n)")     # labeling

plt.title("unit sample sequence")
