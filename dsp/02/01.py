# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np



#setting table

Fs = 100    #Sampling Frequency

Ts = 1/Fs   #Sampling T

Ns = 300    #Sampling 300



#time domain value

x0 = np.arange(0, Ns)*Ts    #np.arange(start=0, end, step size), returns array



#amplitude domain value

y1t = 1.0 * np.sin(2*np.pi*1*x0)

n=3; y2t = 1.0/n * np.sin(2*np.pi*n*x0)     #decreasing by 1/2n-1

n=5; y3t = 1.0/n * np.sin(2*np.pi*n*x0)



#insert some loop here

y0t = y1t +y2t + y3t









#expression



plt.subplot(4,1,1); plt.plot(x0, y0t, 'b'); plt.ylim(-1,1); plt.grid();

plt.ylabel('x(t)')

plt.title('A periodic rectngular signal x(t)=x1(t)+x2(t)+x3(t)')



plt.subplot(4,1,2); plt.plot(x0, y1t, 'b'); plt.ylim(-1,1); plt.grid();

plt.ylabel('x(t)')

plt.title('x1(t)')



plt.subplot(4,1,3); plt.plot(x0, y2t, 'b'); plt.ylim(-1,1); plt.grid();

plt.ylabel('x(t)')

plt.title('x2(t)')



plt.subplot(4,1,4); plt.plot(x0, y3t, 'b'); plt.ylim(-1,1); plt.grid();

plt.ylabel('x(t)')

plt.title('x3(t)')
