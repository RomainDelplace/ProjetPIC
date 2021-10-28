#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:23:48 2021

@author: macromain
"""

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
#from scipy.signal import hilbert
#import pandas
#from scipy.fft import fft
viteau=1480#m.s^-1
densiteEau=1.48*10**6
f=1*10**6
#z = MasseVolumique * vitesse du milieu
#MasseVolumique bio = 1,02g/cm**3
d=0.4
h=0.4

distance= np.sqrt((d/2)**2+h**2)
    
t=2*distance/viteau
    


hauteurbio = 100*10**-3
zbio=viteau*1.02*10**3
vitessebio=viteau
alpha=np.pi/4

hypo=h/np.sin(alpha)
beta=np.arcsin((densiteEau*np.sin(alpha))/zbio)
hypobio=hauteurbio/np.cos(beta)
tempseau=(2*hypo)/viteau
tempsbio=(2*hypobio)/vitessebio
tempstotal=tempseau+tempsbio
distancerefraction=2*hypo+2*hypobio
    

    
fe=1e8;
t_max=1.5/1500;    
time=np.arange(0,t_max,1/fe)

sig=np.sin(2*np.pi*f*time)
porte=

Initial=np.zeros(len(time))
for i in range(len(time)):
    Initial[i]=np.sin(2*np.pi*f*time[i])
plt.plot(time,Initial)

reflexion=np.zeros(len(time))
j = 0
for i in range(len(time)):
    if i*10**-6<=t:
        reflexion[i]=0
    else:
       reflexion[i]=0.5*np.sin(2*np.pi*f*time[j])
       j=j+1

refraction=np.zeros(len(time))
k = 0
for i in range(len(time)):
    if i*10**-6<=tempstotal:
        refraction[i]=0
    else:
       refraction[i]=0.5*np.sin(2*np.pi*f*time[k])
       k=k+1
total=np.zeros(len(time))
for i in range(len(time)):
    total[i]=reflexion[i]+refraction[i]
plt.plot(time,total)

