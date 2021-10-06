# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:54:35 2021

@author: JEASS
"""

#El desarrollo de tres estrategias de un proceso administrativo 
#de fondos de inversión a largo plazo causa costos de 1, 3 y 2 millones 
#de pesos por año de procesamiento, respectivamente. Cada estrategia genera 
#10, 20 y 40 millones en beneficios por año, en el mismo orden, y se requiere un nivel mínimo 
#de  800 millones en beneficios para que el negocio sea conveniente a los inversionistas.  
#Por último se sabe que la diferencia entre el triple de la duración de la estrategia con costo de 
#3 millones menos la duración de la estrategia de 2 millones debe ser de por lo menos 10 años. 
#¿Cuál es la duración óptima de cada estrategia que garantiza los beneficios esperados y minimiza los costos de administración?

from scipy.optimize import linprog

c = [1,3,2]                                   #ingreso funcion objetivo
A_ub=[[-10,-20,-40],[0,-3,1]]                 #ingreso funcion restricciones
b_ub=[-800,-10]
res = linprog(c, A_ub, b_ub, bounds=(0, None), method='simplex')  #muestra el resultado
print("Valor optimp: ", res.fun, "\nX: ", res.x)


#En una compañía se implementaron tres estrategias para medir el rendimiento a largo plazo 
#de sus empleados, estas estrategias causan costos de 2, 4 y 3 horas de preparación por mes, 
#respectivamente. Cada estrategia genera 30, 40 y 60 horas en beneficios por mes, en el mismo orden,
#y se requiere un nivel mínimo de  1000 horas en beneficios para que las estrategias sean 
#convenientes a la compañía.  Por último se sabe que la diferencia entre el triple de la duración de la 
#estrategia con costo de 4 horas menos la duración de la estrategia de 3 horas debe ser de por lo menos 30 meses.
#¿Cuál es la duración óptima de cada estrategia que garantiza los beneficios esperados y minimiza los costos?

from scipy.optimize import linprog

c = [2,4,3]                                       #ingreso funcion objetivo
A_ub=[[-30,-40,-60],[0,-3,1]]                      #ingreso funcion restricciones
b_ub=[-1000,-30]
res = linprog(c, A_ub, b_ub, bounds=(0, None), method='simplex') #ingreso funcion restricciones
print("Valor optimp: ", res.fun, "\nX: ", res.x)
