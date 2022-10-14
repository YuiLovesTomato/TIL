# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np



#setting table

Fs = 100    #Sampling Frequency

Ts = 1/Fs   #Sampling T

Ns = 300    #Sampling 300



#time domain value

x0 = np.arange(0, Ns)*Ts    #np.arange(start=0, end, step size), returns array





def subplot_4th(var, index, n):

    plt.subplot(4,1,index); plt.plot(x0, var, 'b'); plt.ylim(-2,2); plt.grid();

    plt.ylabel('x(t)')

    plt.title('K=' + str(n))

    

    

#square wave and its sum loop

tr_yt=0

for n in range(1, 10, 2):

    temp = 1.0/np.power(n,2) * np.cos(2*np.pi*n*x0)

    tr_yt += temp

    

    if n==1:

        subplot_4th(temp, 2, 1)

        

    if n==3:

        subplot_4th(temp, 3, 3)

    

    if n==5:

        subplot_4th(temp, 4, 5)



    if n==7:

        subplot_4th(tr_yt, 1, 7)
