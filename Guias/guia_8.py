# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:55:12 2022

@author: juano
"""

from typing import Dict, Tuple, Set, List
import math

#2
#A): distancia al origen???

#B) Funciona
def suma_par_ordenado(puntoP:Tuple[float], puntoQ:Tuple[float]) -> Tuple:
    '''
    Requiere: nada
    Devuelve: la suma de los primeros elementos y los segundos elementos de ambas
    tuplas.
    '''
    x:float = puntoP[0] + puntoQ[0]
    y:float = puntoP[1] + puntoQ[1]
    suma:Tuple[float] = (x, y)
    
    return suma
    
puntoP:Tuple[float] = (2, 4)
puntoQ:Tuple[float] = (1, 5)

print('B:')
print(suma_par_ordenado(puntoP, puntoQ))

#C) Funciona

def suma_a_un_punto (punto:Tuple[float], sumando:Tuple[float]) -> Tuple:
    '''
    Requiere: nada
    Devuelve: la suma de un número a un par ordenado.
    '''
    x:float = punto[0] + sumando
    y:float = punto[1] + sumando
    resultado:Tuple[float] = (x,y)
    
    return resultado

punto:Tuple[float] = (14.5, 25.04)
sumando:float = 3.3

print('C:')
print(suma_a_un_punto(punto, sumando))

#D) Funciona
def mas_cercano(punto:Tuple) -> Tuple:
    '''
    Requiere: nada
    Devuelve: el punto entero más cercano.
    '''
    
    x:int = round(punto[0])
    y:int = round(punto[1])
    resultado:Tuple[int] = (x, y)
    
    return resultado
    
punto:Tuple[float] = (12.3, 5.8)

print('D:')
print(mas_cercano(punto))

#3 Pensar bien, sigo con otros

def buscar (elem:int, lista:List[int]) -> Tuple [bool, int]:
    '''
    Requiere: nada
    Devuelve: (True , p) si elem aparece en la lista por primera vez
    en la posición p; o bien (False, None) si no aparece nunca.
    '''

#5
def unicos (ls:List[str]) -> int:
    """
    Requiere: nada
    Devuelve: la cantidad de strings únicos en un ls.
    """
    filtro = set(ls)
    return len(filtro)
    
ls:List[str] = ['abc', 'd', 'ef', 'abc', 'ef', 'ef']

print('5:')
print(unicos(ls))

#6
"""
def es_pangrama (texto:str, letras:Set[str]) -> bool:
    '''
    Requiere: un texto sólo en minúscula
    Devuelve: true si todas las letras del abecedario están en ese texto.
    '''
    
    resultado:bool = True
    
    if letras in texto:
        return True
    
    return resultado

texto:str = 'extraño pan de col y kiwi se quemo bajo fugaz vaho'
letras:Set[str] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

print('6:')
print(es_pangrama(texto, letras))
"""

#8
#A
def jaccard (conjuntoA:Set, conjuntoB:Set) -> float:
    '''
    Requiere: nada
    Devuelve: el índice Jaccard entre dos conjuntos.
    '''
    indice:Set[float] = len(conjuntoA & conjuntoB)/len(conjuntoA | conjuntoB)
    
    return indice

conjuntoA:int = {1, 2, 3}
conjuntoB:int = {3, 4}

print('8:')
print('A:')
print(jaccard(conjuntoA, conjuntoB))


#B
"""
def kshingles (texto:str, caracteres:int) -> set:
    '''
    Requiere: nada
    Devuelve: el conjunto k-shingles de texto.
    '''
    
    resultado:Set[str] =
"""

#C

#9

def apariciones (s:str) -> Dict:
    '''
    Requiere: nada
    Devuelve: la cantidad de apariciones de cada letra en s.
    '''
    
    res:Dict = dict()
    
    for letras in s:
        res[letras] = 1
        
    return res

print('9:')
print(apariciones('agua'))

#10
"""
def deletreado (s:str) -> str:
    '''
    Requiere: nada
    Devuelve: cada letra del string deletreada
    '''
    res:Dict[str] = dict()
    
    pronunciacion:Dict[str, str] = dict()
    
    pronunciacion['a'] = 'a'
    pronunciacion['b'] = 'be'
    pronunciacion['c'] = 'ce'
    pronunciacion['d'] = 'de'
    pronunciacion['e'] = 'e'
    pronunciacion['f'] = 'efe'
    pronunciacion['g'] = 'ge'
    pronunciacion['h'] = 'hache'
    pronunciacion['i'] = 'i'
    pronunciacion['j'] = 'jota'
    pronunciacion['k'] = 'ka'
    pronunciacion['l'] = 'ele'
    pronunciacion['m'] = 'eme'
    pronunciacion['n'] = 'eñe'
    pronunciacion['o'] = 'o'
    pronunciacion['p'] = 'pe'
    pronunciacion['q'] = 'cu'
    pronunciacion['r'] = 'erre'
    pronunciacion['s'] = 'ese'
    pronunciacion['t'] = 'te'
    pronunciacion['u'] = 'u'
    pronunciacion['v'] = 've'
    pronunciacion['w'] = 'doble ve'
    pronunciacion['x'] = 'equis'
    pronunciacion['y'] = 'igriega'
    pronunciacion['z'] = 'zeta'
    
    for letra in s:
        if letra == pronunciacion[letra]:
 """

#11
#Devuelve un diccionario con un número como clave y su multiplicación por sí
#mismo como valor, se repite N veces.

#12 Preguntar