# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:09:47 2022

@author: juano
"""

#for VARIABLE in LISTA:
#   cuerpo

from typing import List

mundiales:List[str] = ['Corea-Japón', 'Alemania', 'Sudáfrica', 'Brasil', 'Rusia']

for m in mundiales:
#Asigna todos los elementos de mundiales a la variable m.
    print(m)
    
for numeros in range(20):
        if numeros % 2 == 0:
            print(numeros)
            
#Asigna todos los elementos del rango con la variable "numeros", entonces imprime
#todos los números que cumplan con el if.