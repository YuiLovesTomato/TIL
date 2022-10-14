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

    plt.subplot(4,1,index); plt.plot(x0, var, 'b'); plt.ylim(-1,1); plt.grid();

    plt.ylabel('x(t)')

    plt.title('K=' + str(n))

    

    

#square wave and its sum loop

sq_yt=0

for n in range(1, 50, 2):

    sq_yt += 1.0/n * np.sin(2*np.pi*n*x0)

    

    if n==1:

        subplot_4th(sq_yt, 1, 1)

        

    if n==5:

        subplot_4th(sq_yt, 2, 5)

    

    if n==11:

        subplot_4th(sq_yt, 3, 11)



    if n==49:

        subplot_4th(sq_yt, 4, 49)
