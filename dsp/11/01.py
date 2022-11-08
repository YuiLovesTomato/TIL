# -*- coding: utf-8 -*-

import numpy as np

### Convolution Summing

##init variables

# given x[n], h[n] and thier index arr
xn = [3,11,7,0,-1,4,2]; n1=[-3,-2,-1,0,1,2,3]
hn = [2,3,0,-5,2,1]; n2=[-1,0,1,2,3,4]

# min: -3 + (-1)
nmin = min(n1) + min(n2)

# max: 3 + 4
nmax = max(n1) + max(n2)

# n for yn
n=np.arange(nmin, nmax+1)

#N for whole table length, yn for output
N = len(n)
yn = np.zeros(N)



## summing loop

# range n: -4 to 7 in a single sweep (whole row in table)
for n in range(nmin, nmax+1):
    sum = 0

    #range k: -3 to 4 (each row in table)
    for k in range(min(n1), max(n1)+1):

    #does n-k exists? and is it included in this step
        if ((n-k)>=min(n2) and (n-k)<=max(n2)):

            #convolution sum
            #why abs?
            sum=sum+xn[k+abs(min(n1))]*hn[n-k+abs(min(n2))]
            
            #save
            yn[n+abs(nmin)] = sum


##printing results

print("x(n): ", xn)
print("h(n): ", hn)
print("y(n): ", yn)
