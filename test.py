#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:23:48 2021

@author: macromain
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert
import pandas
from scipy.fft import fft
viteau=1500#m.s^-1
densiteEau=1,33

def TempsEmissionReflexion(d,h):
    distance= np.sqrt(d**2+h**2)
    
    t=distance/viteau
    
    return t

def TempsSignalRefraction(distance,hauteurbio,nbio,vitessebio,alpha,hauteuremeteur):
    hypo=hauteuremeteur/np.sin(alpha)
    beta=np.arcsin((densiteEau*np.sin(alpha))/nbio)
    hypobio=hauteurbio/np.cos(beta)
    tempseau=(2*hypo)/viteau
    tempsbio=(2*hypobio)/vitessebio
    tempstotal=tempseau+tempsbio
    return tempstotal
    
    
    

time=np.arange(0,6,0.01)
Initial=np.zeros(np.shape(time))
for i in range(len(time)):
    Initial[i]=np.sin(time[i])
plt.plot(Initial)
tref=TempsEmissionReflexion(0.4, 0.4)
reflexion=np.zeros(np.shape(time))
j = 0
for i in range(len(time)):
    if i*100<=tref:
        reflexion[i]=0
    else:
       reflexion[i]=0.5*np.sin(time[j])
       j=j+1
plt.plot(reflexion)
trac=TempsSignalRefraction(0,4,1*10**-6,  ,  ,  ,0,4)
refraction=np.zeros(np.shape(time))
k = 0
for i in range(len(time)):
    if i*100<=trac:
        refraction[i]=0
    else:
       refraction[i]=0.5*np.sin(time[k])
       k=k+1
plt.plot(refraction)
