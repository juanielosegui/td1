"""
import math

def volumen_cilindro (r: float, h:float) -> float: #Encabezado

    #Requiere: valores r>0; h>0
    #Devuelve: el volumen de un cilindro de radio r y altura h, calculado
    #aprox. pi*r (al cuadrado) * h, donde pi ~ 3.1415927.

    volumen:float = math.pi * r * r * h
    return volumen

mi_radio:float = 1.0
mi_altura: float = 1.0
print(volumen_cilindro(mi_radio, mi_altura))
print(volumen_cilindro(10.0, 10.0))
print(volumen_cilindro(12.345, 6.789))
print(volumen_cilindro(0.1, 0.1))
"""

"""
def cant_vocales(texto: str) -> int: #Encabezado
    
    #Requiere: texto formado por caracteres, sus mayúsculas y espacios en blanco.
    #Devuelve: cantidad de apariciones de a,e,i,o,u y á,é,í,ó,ú. Sus mayúsculas también.
    Ejemplos: ' '=0 ; 'aeiOU'=5 ; 'eeeee'=5
"""

