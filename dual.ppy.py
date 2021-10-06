# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:54:35 2021

@author: JEASS
"""

from scipy.optimize import linprog

c = [1,3,2]                                   #ingreso funcion objetivo
A_ub=[[-10,-20,-40],[0,-3,1]]                 #ingreso funcion restricciones
b_ub=[-800,-10]
res = linprog(c, A_ub, b_ub, bounds=(0, None), method='simplex')  #muestra el resultado
print("Valor optimp: ", res.fun, "\nX: ", res.x)

from scipy.optimize import linprog

c = [2,4,3]                                       #ingreso funcion objetivo
A_ub=[[-30,-40,-60],[0,-3,1]]                      #ingreso funcion restricciones
b_ub=[-1000,-30]
res = linprog(c, A_ub, b_ub, bounds=(0, None), method='simplex') #ingreso funcion restricciones
print("Valor optimp: ", res.fun, "\nX: ", res.x)
