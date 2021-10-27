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

def TempsEmissionReflexion(d,h):
    distance= np.sqrt(d**2+h**2)
    viteau=1500#m.s^-1
    t=distance/viteau
    
    return t


time=np.arange(0,0.001,0.000000001)
Initial=np.zeros(np.shape(time))
for i in range(len(time)):
    Initial[i]=np.sin(time[i])
plt.plot(Initial)
t=TempsEmissionReflexion(0.4, 0.4)
Premièresinus=np.zeros(np.shape(time))
j = 0
for i in range(len(time)):
    if i*100<=t:
        Premièresinus[i]=0
    else:
       Premièresinus[i]=np.sin(time[j])
       j=j+1
plt.plot(Premièresinus)
