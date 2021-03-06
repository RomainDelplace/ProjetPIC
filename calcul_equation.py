#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 08:20:56 2021

@author: Ombeline
"""

import sympy as sy
import matplotlib.pyplot as plt
import numpy as np

def resultat(Xb, Yb, Xr, Yr, Ys, c1, c2):
   Xs = sy.symbols('Xs')
   result = sy.solve((((Xs-Xb)**2)/(c2**2*((Xb-Xs)**2+(Yb-Ys)**2)))-(((Xr-Xs)**2)/(c1**2*((Xr-Xs)**2+(Yr-Ys)**2))), Xs) 
   return result

def resultat_prim(Xb, Yb, Xe, Ye, Ys, c1, c2):
   Xs = sy.symbols('Xs')
   result_prim = sy.solve((((Xs-Xe)**2)/(c1**2*((Xe-Xs)**2+(Ye-Ys)**2)))-(((Xb-Xs)**2)/(c2**2*((Xb-Xs)**2+(Yb-Ys)**2))), Xs) 
   return result_prim

Xb = -0.20
Yb = -0.5
Xe = 0
Ye = 0
Xr = -0.40
Yr = 0
Ys = -0.4
c1 = 1.48*10**3
c2 = 1.2*c1

def calculBR(Xb, Yb, Xr, Yr, Ys, c1, c2):
    resultat_xs = resultat(Xb, Yb, Xr, Yr, Ys, c1, c2)
    r_complex = []
    for i in range(len(resultat_xs)):
        res=complex(resultat_xs[i])
        resc=np.imag(res)
        res=np.real(res)
        if (resc < 1e-10):
            r_complex.append(res)
    
    for i in range(len(r_complex)):
        if (r_complex[i]>Xb and r_complex[i]<Xr):
            resultat_possible=r_complex[i]
    return resultat_possible

def calculEB(Xb, Yb, Xe, Ye, Ys, c1, c2):
    resultat_xs = resultat_prim(Xb, Yb, Xe, Ye, Ys, c1, c2)
    r_complex = []
    for i in range(len(resultat_xs)):
        res=complex(resultat_xs[i])
        resc=np.imag(res)
        res=np.real(res)
        r_complex.append(res)
        if (resc < 1e-10):
            r_complex.append(res)
            
    for i in range(len(r_complex)):
        if (r_complex[i]<Xb and r_complex[i]>Xe):
            resultat_possible=r_complex[i]
    return resultat_possible


def resultat2(Xb, Yb, Xr, Yr, Ys, c1, c2):
   Xs = sy.symbols('Xs')
   result = sy.solve(((3*(Xs)**2)+Xs+9), Xs)  
   first_result= result[0]
   second_result= result[1]
   #result = sy.solve(((Xs-Xb)*(Xs-Xb))/(c2*c2*((Xs-Xb)*(Xs-Xb)+(Ys-Yb)*(Ys-Yb)))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)  
   #result = sy.solveset(((Xs-Xb)*(Xs-Xb))/(c2*c2*((Xs-Xb)*(Xs-Xb)+(Ys-Yb)*(Ys-Yb)))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)
   #result_root = sy.root(((Xs-Xb)*(Xs-Xb))/(c2*c2*((Xs-Xb)*(Xs-Xb)+(Ys-Yb)*(Ys-Yb)))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)  
   return result











