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
   first_result= result[0]
   second_result= result[1]
   #result = sy.solve(((Xs-Xb)*(Xs-Xb))/(c2*c2*((Xs-Xb)*(Xs-Xb)+(Ys-Yb)*(Ys-Yb)))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)  
   #result = sy.solveset(((Xs-Xb)*(Xs-Xb))/(c2*c2*((Xs-Xb)*(Xs-Xb)+(Ys-Yb)*(Ys-Yb)))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)
   #result_root = sy.root(((Xs-Xb)*(Xs-Xb))/(c2*c2*((Xs-Xb)*(Xs-Xb)+(Ys-Yb)*(Ys-Yb)))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)  
   return result

Xb = 0.20
Yb = 0.5
Xr = 0.40
Yr = 0
Ys = 0.4
c1 = 1.48*10**6
c2 = 1.51*10**6


resultat_xs = resultat(Xb, Yb, Xr, Yr, Ys, c1, c2)

#resultat_first_xs = resultat(Xb, Yb, Xr, Yr, Ys, c1, c2, h1, h2)[0]
#resultat_second_xs = resultat(Xb, Yb, Xr, Yr, Ys, c1, c2, h1, h2)[1]
