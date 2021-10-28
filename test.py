#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:23:48 2021

@author: macromain
"""

import numpy as np
import matplotlib.pyplot as plt
#from scipy.signal import hilbert
#import pandas
#from scipy.fft import fft
viteau=1500#m.s^-1
densiteEau=1.48*10**6
#z = MasseVolumique * vitesse du milieu
#MasseVolumique bio = 1,02g/cm**3
def TempsEmissionReflexion(d,h):
    distance= np.sqrt(d**2+h**2)
    
    t=2*distance/viteau
    
    return t

def TempsSignalRefraction(distance,hauteurbio,zbio,vitessebio,alpha,hauteuremeteur):
    hypo=hauteuremeteur/np.sin(alpha)
    beta=np.arcsin((densiteEau*np.sin(alpha))/zbio)
    hypobio=hauteurbio/np.cos(beta)
    tempseau=(2*hypo)/viteau
    tempsbio=(2*hypobio)/vitessebio
    tempstotal=tempseau+tempsbio
    return tempstotal
    
    
    

time=np.arange(0,0.001,0.000001)
Initial=np.zeros(len(time))
for i in range(len(time)):
    Initial[i]=np.sin(time[i])
plt.plot(time,Initial)
tref=TempsEmissionReflexion(0.4, 0.4)
reflexion=np.zeros(len(time))
j = 0
for i in range(len(time)):
    if i*10**-6<=tref:
        reflexion[i]=0
    else:
       reflexion[i]=0.5*np.sin(time[j])
       j=j+1

trac=TempsSignalRefraction(0.4,100*10**-3,viteau*1.02*10**3,viteau,np.pi/4,0.4)
refraction=np.zeros(len(time))
k = 0
for i in range(len(time)):
    if i*10**-6<=trac:
        refraction[i]=0
    else:
       refraction[i]=0.5*np.sin(time[k])
       k=k+1
total=np.zeros(len(time))
for i in range(len(time)):
    total[i]=reflexion[i]+refraction[i]
plt.plot(time,total)

