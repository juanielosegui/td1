# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 12:22:20 2022

@author: juano
"""

from typing import List

'''
def suma_en_pos_impares (ns:List[int], n:int) -> List[int]:
    """
    Requiere: nada .
    Devuelve: una lista con longitud igual a len(ns) tal que en
cada posición j entre 0 y len (ns) -1: si j es par
la lista tiene ns[j] y si j es impar , tiene ns[j]+n.
    """
    j = 0
    vr:List[int] = []
    
    while j < len(ns):
        if j%2==0:
            vr.append(ns[j]+n)
        
        elif j&2==1:
            vr.append(ns[j])
            
        j = j + 1

    return vr

ns:List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n:int = 100
print(suma_en_pos_impares(ns, n))
'''


def suma_en_pos_impares (ns:List[int], n:int) -> List[int]:
    """
    Requiere: nada .
    Devuelve: una lista con longitud igual a len(ns) tal que en
cada posición j entre 0 y len (ns) -1: si j es par
la lista tiene ns[j] y si j es impar , tiene ns[j]+n.
    """
    vr:List[int] = []
    
    for posicion in ns:
        if posicion % 2 == 0:
            vr.append(posicion + n)
            
        elif posicion % 2 == 1:
            vr.append(posicion)
        
        return vr

ns:List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n:int = 100
print(suma_en_pos_impares(ns, n))