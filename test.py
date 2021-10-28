#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:23:48 2021

@author: macromain
"""

import numpy as np
from scipy import signal
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
    


hauteurbio = 1*10**-3
zbio=viteau*1.02*10**3
vitessebio=viteau
alpha=np.pi/4

xb=
yb=

xe=0
ye=0

xr=0
yr=0


hypo=h/np.sin(alpha)
beta=np.arcsin((densiteEau*np.sin(alpha))/zbio)
hypobio=hauteurbio/np.cos(beta)
tempseau=(2*hypo)/viteau
tempsbio=(2*hypobio)/vitessebio
tempstotal=tempseau+tempsbio
distancerefraction=2*hypo+2*hypobio
    

    
fe=1e8;#echantillonnage f*100
t_max=1.5/1500;#le trajet le plus long pour un echo de retour est environ de 1.5m. Donc t_max = temps max de retour d'echo pr la simulation    
time=np.arange(0,t_max,1/fe)#vecteur temps
nbr_pulses=2
gate=(1+signal.square(2*np.pi*((1/t_max))*time,((nbr_pulses/f)/t_max)))/2#porte pour créer pûlse
sig=np.sin(2*np.pi*f*time)*gate#pulse signal

delay_bio=2*distance/viteau
delay_beton=tempstotal
refl_bio=np.sin(2*np.pi*f*(time-delay_bio))*(1+signal.square(2*np.pi*((1/t_max))*(time-delay_bio),((nbr_pulses/f)/t_max)))/2
refl_beton=np.sin(2*np.pi*f*(time-delay_beton))*(1+signal.square(2*np.pi*((1/t_max))*(time-delay_beton),((nbr_pulses/f)/t_max)))/2
# Initial=np.zeros(len(time))
# for i in range(len(time)):
#     Initial[i]=np.sin(2*np.pi*f*time[i])
# plt.plot(time,Initial)

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

