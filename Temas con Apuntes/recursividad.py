# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:05:16 2022

@author: chipi
"""

# =============================================================================
# RECURSIÓN: llamarse a sí mismo
# =============================================================================

import time
from typing import List

def saludar(n:int):
    if n==0:        #Caso Base
        print('DESPEGUE!')
    else:           #Caso recursivo
        print('hola', n)
        time.sleep(0.4)
        saludar(n-1)
    
#saludar(0)

#Manera de iterar sin usar ningún for ni while.
#Caso base (línea 16/17) pone un caso en específico que corte la recursión.

def sumar_lista(xs:List[int]) -> int:
    if len(xs) == 0:
        return 0
    else:
        xs[0] + sumar_lista(xs[1:])