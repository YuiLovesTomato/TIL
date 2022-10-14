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

st_yt=0

for n in range(1, 10):

    temp = 1.0/n * np.sin(2*np.pi*n*x0)

    st_yt += temp

    

    if n==1:

        subplot_4th(temp, 2, 1)

        

    if n==2:

        subplot_4th(temp, 3, 2)

    

    if n==3:

        subplot_4th(temp, 4, 3)



    if n==9:

        subplot_4th(st_yt, 1, 9)
