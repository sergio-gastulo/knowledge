# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:37:00 2023

@author: sgast
"""

import numpy as np 
import random as rnd 
import matplotlib.pyplot as plt

#%%

x = [0.2,0.6,0.8,0.1]
y = [2,4,1,10]
plt.plot(x,y)
plt.show()

#%%

def makelist(n,a,b):
    outputlist = list()
    for i in range(n):
        outputlist.append(rnd.randint(a,b))
    return outputlist

x = makelist(200,6,66)
y = makelist(200,6,66)
plt.scatter(x,y)
plt.show()

#%%
x2 = np.linspace(0,2, num= 200)
y2 = np.exp(np.sqrt(x2))
z2 = y2-1
plt.plot(x2,y2,"k+",x2,z2,"b")
plt.title("ASD")
plt.show()

#%%

Dom = np.linspace(0,20,200)
Im = np.exp(np.sin(Dom)**2)
noise = np.random.normal(0.1,0.98,200)
iruido = Im+noise

plt.figure(num = 1)
plt.plot(Dom,Im,'or')
plt.title("Señal limpia")

plt.figure(num=2)
plt.plot(Dom,iruido)
plt.title('Señal sucia')
plt.axhline(y = np.mean(Im),
            xmin = 0,
            xmax = 15,
            ls = '--',
            color = 'red')

plt.axvline(x = 12, color = 'green')

plt.show()


#%%
Dom = np.linspace(0,20,200)
Im = np.exp(np.sin(Dom)**2)
noise = np.random.normal(0.1,0.98,200)*1e-1
iruido = Im+noise

plt.plot(Dom,iruido,color = 'green')
plt.xlabel('independent variable')
plt.ylabel('dependent variable')
plt.title('señal+ruido $x^2$')
plt.axhline(y = np.mean(iruido),
           xmin = 0, xmax = 10,
           ls = 'dashdot',
           color = 'red')

#sombreando un area alrededor de la media de la variable dependiente
mediaY = np.mean(iruido)

#sombreado:plt axshpan horizontal
plt.axhspan(ymin = mediaY-0.25,
            ymax = mediaY+0.25,
            color = 'black', 
            alpha = 0.5)






