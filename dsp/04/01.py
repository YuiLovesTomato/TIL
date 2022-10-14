# -*- coding: utf-8 -*-



import numpy as np

import matplotlib.pylab as plt



def sigadd(n1, x1, n2, x2):

    #sequence axis

    nk = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2))+1)

    N = len(nk) #length of sequence

    y1 = np.zeros(N)

    y2 = np.zeros(N)

    aa=abs(min(min(n1),min(n2)))

    n1 = n1+aa

    n2 = n2+aa

    y1[int(min(n1)):int(max(n1)+1)]=x1

    y2[int(min(n1)):int(max(n1)+1)]=x2

    y = y1+y2

    return nk, y, y1, y2



n1 = np.arange(0,15,1)

x1=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1])

n2 = np.arange(-5,8,1)

x2 = np.array([1,2,3,4,5,6,7,6,5,4,3,2,1])



n, y, zx1, zx2 = sigadd(n1, x1, n2, x2);

print("y(n)=",y)

print("x1(n)=",zx1)

print("x2(n)=",zx2)

print("n=",n)

plt.figure(1)

plt.subplot(3,1,1)

plt.stem(n,zx1,"blue"); plt.grid()

plt.subplot(3,1,2)

plt.stem(n,zx2,"blue"); plt.grid()

plt.subplot(3,1,3); plt.stem(n,y,"blue");plt.grid()
