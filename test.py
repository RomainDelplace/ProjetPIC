#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:23:48 2021

@author: macromain
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import calcul_equation as ce
#from scipy.signal import hilbert
#import pandas
#from scipy.fft import fft
vitesse_eau=1480#m.s^-1
indice_eau=1.48*10**6
freq_emission=1*10**6
x_beton=20.0
y_beton=-50.0

x_emetteur=0.0
y_emetteur=-0.0

x_recepteur=40
y_recepteur=-0.0
#z = MasseVolumique * vitesse du milieu
#MasseVolumique bio = 1,02g/cm**3
distance_entre_capteur=0.4
distance_capteur_biofilm=0.49

distance_reflexion_speculaire= np.sqrt((distance_entre_capteur/2)**2+distance_capteur_biofilm**2)   
angle_injection_speculaire=np.arccos(distance_capteur_biofilm/distance_reflexion_speculaire)
t=2*distance_reflexion_speculaire/vitesse_eau

hauteur_biofilm = 1*10**-2
indice_biofilm=vitesse_eau*1.02*10**3
vitesse_biofilm=vitesse_eau



x_s=ce.calculBR(x_beton/100, y_beton/100, x_recepteur/100 , y_recepteur/100,-distance_capteur_biofilm,indice_eau,indice_biofilm)*100

angle_injection_secondaire_eau=np.arctan(np.sqrt((x_recepteur-x_s)**2)/np.sqrt((y_recepteur-distance_capteur_biofilm)**2))

hypothenus_secondaire_eau=distance_capteur_biofilm/np.sin(angle_injection_secondaire_eau)
angle_injection_secondaire_biofilm=np.arcsin((indice_eau*np.sin(angle_injection_secondaire_eau))/indice_biofilm)
hypothenus_secondaire_biofilm=hauteur_biofilm/np.cos(angle_injection_secondaire_biofilm)
temps_speculaire_eau=(2*hypothenus_secondaire_eau)/vitesse_eau
temps_speculaire_biofilm=(2*hypothenus_secondaire_biofilm)/vitesse_biofilm
temps_total_speculaire=temps_speculaire_eau+temps_speculaire_biofilm
distance_refraction_speculaire=2*hypothenus_secondaire_eau+2*hypothenus_secondaire_biofilm
    




freq_echantillonnage=1e8;#echantillonnage f*100
temp_max_echo=2/1500;#le trajet le plus long pour un echo de retour est environ de 1.5m. Donc t_max = temps max de retour d'echo pr la simulation    
vecteur_temps=np.arange(0,temp_max_echo,1/freq_echantillonnage)#vecteur temps
nbr_pulses=2
porte=(1+signal.square(2*np.pi*((1/temp_max_echo))*vecteur_temps,((nbr_pulses/freq_emission)/temp_max_echo)))/2#porte pour créer pûlse
signal_pulse=np.sin(2*np.pi*freq_emission*vecteur_temps)*porte#pulse signal
plt.plot(vecteur_temps,signal_pulse)


retard_dans_biofilm=2*distance_reflexion_speculaire/vitesse_eau
retard_paroi=temps_total_speculaire
reflexion_dans_biofilm=np.sin(2*np.pi*freq_emission*(vecteur_temps-retard_dans_biofilm))*(1+signal.square(2*np.pi*((1/temp_max_echo))*(vecteur_temps-retard_dans_biofilm),((nbr_pulses/freq_emission)/temp_max_echo)))/2

reflexion_dans_beton=np.sin(2*np.pi*freq_emission*(vecteur_temps-retard_paroi))*(1+signal.square(2*np.pi*((1/temp_max_echo))*(vecteur_temps-retard_paroi),((nbr_pulses/freq_emission)/temp_max_echo)))/2
signal_recu=reflexion_dans_biofilm+reflexion_dans_beton
plt.plot(vecteur_temps,signal_recu)



echo=0
pas=0.1
vitesse_eau=1480#m.s^-1
for i in np.arange(0,x_recepteur,0.1):
    Xi=x_emetteur+i
    Yi=-distance_capteur_biofilm*100
    distanceGauche=np.sqrt((x_emetteur-Xi)**2+(y_emetteur-Yi)**2)
    distanceDroite=np.sqrt((x_recepteur-Xi)**2+(y_recepteur-Yi)**2)
    distanceEcho=(distanceDroite+distanceGauche)/100
    tempsEcho=distanceEcho/vitesse_eau
    echoSignal=np.sin(2*np.pi*freq_emission*(vecteur_temps-tempsEcho))*(1+signal.square(2*np.pi*((1/temp_max_echo))*(vecteur_temps-tempsEcho),((nbr_pulses/freq_emission)/temp_max_echo)))/2
    echo=echo+echoSignal
plt.plot(vecteur_temps,echo)
