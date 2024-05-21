# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:53:03 2022

@author: juano
"""

# =============================================================================
# EJERCICIO 1
# =============================================================================
import math
from typing import List

class Punto:
    def __init__(self, lat:float, lon:float):
        self.x:float = lat
        self.y:float = lon
    
    def distancia_a(self, other) -> float:
        return math.sqrt(((self.x - other.x)**2)+((self.y - other.y)**2))
    
    def distancia_al_origen(self) -> bool:
        return math.sqrt(((self.x)**2)+(self.y)**2)
    
    def suma(self, other) -> bool:
        return (self.x + other.x, self.y + other.y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __repr__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
p1:Punto = Punto(9.12, 120.17)
p2:Punto = Punto(26.6, 17.2)


print(p1.distancia_a(p2))
print(p1.distancia_al_origen())
print(p1.suma(p2))
print(p1.__eq__(p2))
