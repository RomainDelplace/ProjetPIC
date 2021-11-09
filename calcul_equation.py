#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 08:20:56 2021

@author: OmbelineDo
"""

import sympy as sy
import matplotlib.pyplot as plt
import numpy as np

def resultat(Xb, Yb, Xr, Yr, Ys, c1, c2, h1, h2):
   Xs = sy.symbols('Xs')
   result = sy.solve(((Xs-Xb)*(Xs-Xb))/(c2*c2*(h1*h1))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)  
   #result = sy.solve(((Xs-Xb)*(Xs-Xb))/(c2*c2*((Xs-Xb)*(Xs-Xb)+(Ys-Yb)*(Ys-Yb)))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)  
   #result = sy.solveset(((Xs-Xb)*(Xs-Xb))/(c2*c2*((Xs-Xb)*(Xs-Xb)+(Ys-Yb)*(Ys-Yb)))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)
   result_root = sy.root(((Xs-Xb)*(Xs-Xb))/(c2*c2*((Xs-Xb)*(Xs-Xb)+(Ys-Yb)*(Ys-Yb)))-((Xr-Xs)*(Xr-Xs))/(c1*c1*((Xr-Xs)*(Xr-Xs)+(Yr-Ys)*(Yr-Ys))), Xs)  
   return result

Xb = 0.20
Yb = 0.50
Xr = 0.40
Yr = 0
Ys = 0.4
c1 = 1.48*10**6
c2 = 1.51*10**6
h1 = 0.1
h2 = 0
resultat_xs = resultat(Xb, Yb, Xr, Yr, Ys, c1, c2, h1, h2)
print(resultat_xs)