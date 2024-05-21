"""
#3)
#A)
 
from typing import List
'''
def max_elemento (lista:List[float]) -> float:
    
    #Requiere: una lista de valores tipo float.
    #Devuelve: el valor mayor de la lista.
    #Ejemplo: si lista = [0.5, 2.3] el mayor es 2.3.
    
    
    lista:List[float] = [6.7, 12.24, 4.3, 2.0, 0.204]
    i:int = 0
    res:float = 0

    while i < len(lista):
        if lista(i) > lista(i+1):
            i = i + 1
        
        else:
            res + lista (i)

    return res
'''

#B) Funciona

def concatenacion (series:List[str]) -> str:
    '''
    Requiere: una lista de strings.
    Devuelve: un string que son todos los elementos de la lista concatenados.
    '''
    
    series:List[str] = ['abc', 'defg', 'hijk']
    i:int = 0
    res:str = ''

    while i < len(series):
        
        res = res + series[i]
        i = i + 1

    return res

print(concatenacion(series=['abc', 'defg', 'hijk']))

#C)

def menor_a_mayor (lista_numeros:List[int]) -> bool:
    '''
    Requiere: una lista de enteros.
    Devuelve: un bool que determina si los enteros de la lista están
    ordenados (True), o no (False).
    '''
    
    lugar:int = 0
    
    if lista_numeros[0] > lista_numeros[1]:
        return False
    
    else:
        while lugar < len(lista_numeros)-1:
            if lista_numeros[lugar] < lista_numeros[lugar+1]:
                lugar = lugar + 1
        
            else:
                return False
            
        return True
            
print(menor_a_mayor(lista_numeros = [4, 3, 9]))
print(menor_a_mayor(lista_numeros = [2, 3, 1]))

#D) Preguntar

#E) Funciona

def suma_naturales (lista:List[int], numero:int) -> List:
    '''
    Requiere: una lista de enteros y un número natural.
    Devuelve: la suma de cada elemento de la lista con el
    número natural sumado.
    '''
    i:int = 0
    lista_sumada:List = []
    
    while i < len(lista):
        lista_sumada.append(lista[i] + numero)
        i = i + 1

    return lista_sumada

print(suma_naturales([9, 12, 18], 12))

#F) Funciona

def contar_caracteres (partes:List[str]) -> int:
    '''
    Requiere: una lista de strings.
    Devuelve: cuántos caracteres tiene luego de la concatenación
    de sus elementos.
    '''
    i:int = 0
    concatenacion:int = 0
    
    while i < len(partes):
        concatenacion = concatenacion + len(partes[i])
        i = i + 1
        
    return concatenacion

print(contar_caracteres(['tor', 'c', 'ua', 'to']))

#G) No funciona

def apariciones_a (lista:List[str]) -> int:
    
    '''
    Requiere: una lista de strings.
    Devuelve: la cantidad de veces que aparece la A en la
    concatenación de esos strings.
    '''
    pos_lista:int = 0
    pos_concatenacion:int = 0
    concatenacion:str = ''
    contador_a:int = 0
    
    while pos_lista < len(lista):
        concatenacion = concatenacion + lista[pos_lista]
        pos_lista = pos_lista + 1
        
    return concatenacion

    while pos_concatenacion < len(concatenacion):
        
        if concatenacion[pos_concatenacion] == 'a':
            contador_a + 1
            
        else:
            pos_concatenacion = pos_concatenacion + 1
            
    return contador_a

print(apariciones_a(['abba', 'acdc', 'bee gees', 'a-ha']))

#H) No funciona

def separacion (txt:str, sep:str) -> list:
    '''
    Requiere: un string con separaciones de caracteres.
    Devuelve: una lista con los strings separados.
    '''
    
    sep:str = ';'
    txt:str = 'a;bb;c;;ddd;'
    separacion:List = []
    
    txt.split(sep)

#4 No los entiendo
#A)

def meseta_mas_larga (lista:List[int]) -> List:
    '''
    Requiere: una lista de enteros.
    Devuelve: una lista con la meseta más larga.
    '''
    
    lista:List[int] = [1, 1, 2, 6, 6, 6, 3, 3]
    i = 0
    meseta:List[int] = []
    
    while i < len(lista):
        if i == i + 1:
            meseta.append(lista[i])
            i = i + 1
        else:
            i = i + 1
            
    return meseta

#B)

#C)

#8 La variable a reemplaza en todos los lugares donde aparezca
#  la variable ls? Por qué devuelven distintos valores si se usa la misma
#  variable? Por qué imprime 1 y no 

from typing import List

def suma_problematica (ls:List[int]) -> int:
    n:int=0
    i:int=0
    while i < len(ls):
        n=n+ls[i]
        i=i+1
        ls.clear()
    return n

a:List[int] = [1, 2, 3, 4]
print(suma_problematica(a))
print(suma_problematica(a))


#10)

from typing import List

def buscar_v1 (elem:int , ls:List [int]) -> bool :
    '''
    Requiere: nada.
    Devuelve: True si elem aparece al menos una vez en ls.
    '''
    r:bool = False
    i:int = 0
    while i < len(ls):
        r = r or (ls [i] == elem)
        i = i + 1
    return r

ls:List[int] = [1, 2, 4, 1, 5]
print(buscar_v1(1, ls))
"""

from typing import List

def buscar_v1 (elem:int, ls:List [int]) -> bool :
    '''
    Requiere: nada.
    Devuelve: True si elem aparece al menos una vez en ls.
    '''
    
    r:bool = False
    
    for items in ls:
        if elem == items:
            r = True
            break
        
        else:
            r = False
    
    return r

ls:List[int] = [1, 2, 4, 1, 5]
print(buscar_v1(1, ls))
print(buscar_v1(8, ls))

        