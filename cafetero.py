
def filtrar_solo_CAFE (texto: str) -> str:
    ''' Requiere: nada.
        Devuelve: dado un string s, devolver un 
        nuevo string formado por las letras C, A, F, o E 
        que aparezcan en s, en el mismo orden de 
        ocurrencia.
    '''
    res:str = ('')
    i:int=0
    #A. Empieza 
    while i < len(texto):
        #B
        if texto[i] == 'C' or texto[i] == 'A' or texto [i] == 'F' or texto[i] == 'E':
            res = res + texto [i]
    
        i = i + 1
        #C
    #D
    return res

#Funcion auxiliar filtrarCAFE_BD para es_cafetero:

def filtrarCAFE_BD (texto: str) -> str:
    ''' Requiere: nada.
        Devuelve: dado un string s, devolver un 
        nuevo string formado por las letras C, A, F, E, B, o D
        que aparezcan en s, en el mismo orden de 
        ocurrencia.
    '''
    res:str = ('')
    i:int=0
    #A
    while i < len(texto):
        #B
        if texto[i] == 'C' or texto[i] == 'A' or texto [i] == 'F' or texto[i] == 'E' or texto[i] == 'B' or texto[i] == 'D':
            res = res + texto[i]
    
        i = i + 1
        #C
    #D
    return res

def es_cafetero (n:int)->bool:
    '''Requiere:  n >= 0
    Devuelve: si n es cafetero (es decir, si y solo si su 
    representacion hexadecimal contiene exactamente una 
    ocurrencia de los símbolos C, A, F y E, en ese orden, 
    y no contiene ocurrencias de los símbolos B y D), True, 
    y si no lo es, False.
    '''
    n:str = filtrarCAFE_BD(str(hex(int(n)).upper()))
    return n == 'CAFE'

from typing import List

def n_esimo_cafetero (n:int) -> int:
    '''
    Requiere: n >= 1 (numeros ordinales)
    Devuelve: el n-ésimo número cafetero, considerando al 51966
    como el 1-ésimo número cafetero.
    ''' 
    num: int = 51966
    cafeteros: List[int] = []
    
    while len(cafeteros) <= n:
        if es_cafetero(num) == True:
            cafeteros.append(num)
        num = num + 1
    return cafeteros[n-1]

def cafeteros_entre (n:int, m:int) -> (int):
    '''
    Requiere: n >= 1, m >= n
    Devuelve: la lista de números cafeteros entre n y m, 
    inclusive en ambos casos (es decir, mayores o iguales a n,
    y menores o iguales a m), ordenada de menor a mayor.
    ''' 
    num: int = n
    cafeteros: List[int] = []
    
    while num <= m:
        if es_cafetero(num) == True:
            cafeteros.append(num)
        num = num + 1
    return cafeteros

