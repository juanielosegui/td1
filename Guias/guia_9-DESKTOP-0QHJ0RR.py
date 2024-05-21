# =============================================================================
# EJERCICIO 1
# =============================================================================
from importlib.util import module_for_loader
import math
from typing import List

class Punto:
    def __init__(self, lat:float, lon:float):
        self.x:float = lat
        self.y:float = lon
    
    def distancia_a(self, other) -> bool:
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

print('Clase de Puntos.')
print(p1.distancia_a(p2))
print(p1.distancia_al_origen())
print(p1.suma(p2))
print(p1.__eq__(p2))

class Auto:
    def __init__(self, m:str, mod:str, vm:int, km:int):
        self.marca = m
        self.modelo = mod
        self.velocidad_max = vm
        self.kilometraje = km

    def __repr__(self) -> str:
        return 'El '+ self.marca + ' ' + self.modelo + ' llega a ' + str(self.velocidad_max) + ' por hora y tiene ' + str(self.kilometraje) + ' viajados.'

a1:Auto = Auto('Ferrari', '458 Berlinetta', 341, 100.000)
a2:Auto = Auto('Toyota', 'Corolla', 200, 200.000)
a3:Auto = Auto('Suzuki', 'Vitara', 190, 250.000)

print('Clase de Autos .')
print(a1.__repr__())
print(a2.__repr__())
print(a3.__repr__())