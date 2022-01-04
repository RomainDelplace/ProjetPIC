#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:02:30 2021

@author: ophelie
"""
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from tqdm import tqdm
import transonic

#_____________________________VARIABLES NUMPY_________________________________#
def cos(x):
    return np.cos(x)
def sin(x):
    return np.sin(x)
def tan(x):
    return np.tan(x)
def sqrt(x):
    return np.sqrt(x)
def acos(x):
    return np.arccos(x)
def asin(x):
    return np.arcsin(x)
def atan(x):
    return np.arctan(x)
def sinc(x):
    return np.sinc(x)
def bessel(x,y):
    return sc.special.jv(x,y)

pi=np.pi


# seulement 3D, attention aux indices
def matrice_replace(matrice,x,y,z,valeur):
    matrice[z][x][y]=valeur
    
def matrice_lecture(matrice,z):
    print(matrice[z])
#________________________________VARIABLES____________________________________#
x=np.linspace(-0.1,0.1,401)
y=np.linspace(-0.1,0.1,401)
z=np.linspace(-0.06,0.3,721)
a=20*10**-3

# Pour avoir 30° d'ouverture théorique, la largeur du piezo doit être égale à 2.5 mm
b=20*10**-3

d0=0.1
gamma=2.0944

# position capteur dans le repère
y12 = d0*cos(gamma-pi/2)
z12 = d0*sin(gamma-pi/2)
alpha = 25 * pi/180 # incidence de l'axe du récepteur sur celui de l'émetteur
r02 = -z12 + y12 / tan(alpha) # distance entre emetteur et point focal
r01 = sqrt((r02+z12)**2+y12**2) # distance entre recepteur et point focal

ell_center_y = y12/2
ell_center_z = z12/2
ang_ell = acos(y12/d0) # /!\ en math lab y12./d0 ??? traduction du point en python ??

# caracteristiques des transducteurs
lam =1480/10**6
k = 2*pi*10**6/1480
a0 = 0.01
ka=k*a0

### WAIT BAR
waitbar1=0
waitbar2=0

#_________________________________MATRICE_____________________________________#

beta2=np.array([[[0]*len(x)]*len(y)]*len(z),dtype=float)
betax=np.array([[[0]*len(x)]*len(y)]*len(z),dtype=float)
betay=np.array([[[0]*len(x)]*len(y)]*len(z),dtype=float)
beta1=np.array([[[0]*len(x)]*len(y)]*len(z),dtype=float)

print('creation des matrices faites')

#_______________________________REMPLISSAGE___________________________________#
# calcul des angles formés entre chaque point de l'espace et les axes
# emetteur (beta2) et recepteur (betax dans le plan 0yz et betay dans le plan Oxz)
for k in tqdm(range (0,len(z))):
    for i in range (0,len(x)):
        for j in range (0,len(y)):
            
            r1y = sqrt(x[i]**2+(z[k]+z12)**2)
            r2xyz = sqrt(x[i]**2+(y[j]-y12)**2+(z[k]+z12)**2)
            r2yz = sqrt(y12**2+(z12+r02)**2)
            pscal2 = -y12*(y[j]-y12)+(z[k]+z12)*(z12+r02)
            
            if (z[k]==0 and x[i] == 0 and y[j]==0):
                beta2[k][i][j]=acos(0.0)
            else :
                beta2[k][i][j]=acos(z[k]/sqrt(x[i]**2+y[j]**2+z[k]**2))
                betax[k][i][j]=acos((-y12 * (y[j]-y12) + (z[k]+z12) * (z12*r02))/(sqrt(y12**2 + (z12 + r02)**2 ) * sqrt((y[j]-y12)**2+(z[k]+z12)**2)))
            
            betay[k][i][j]=asin(x[i]/r1y)
            beta1[k][i][j]=acos(pscal2/(r2xyz*r2yz))
    waitbar2 += i

#_________________________________CALCULS_____________________________________#
# Directivité en reception ACVP
Db = sinc((b/lam)*sin(betax))
Da = sinc((a/lam)*sin(betay))
D1 = (Db*Da)**2


plt.imshow(10*np.log10(np.squeeze(D1[200,:,:])))
# resultat : carre avec  cone, en profil ligne de directivité cf photo

# Directivité en emission ACVP
D2 = (2*bessel(1,ka*sin(beta2))/(ka*sin(beta1)))**2

#  erreur ligne 96
# ValueError: cannot convert float NaN to integer

# erreur ligne 91 ( D1 ):
#     ufunc 'bitwise_xor' not supported for the input types, and the inputs
#     could not be safely coerced to any supported types according to the casting
#     rule ''safe''


