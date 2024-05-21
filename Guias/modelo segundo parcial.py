from typing import List

# Ejercicio 1A)

def lista_ordenada_ascendente(xs:List[int]) -> bool:
    '''
    Requiere: nada
    Devuelve: True, si xs está ordenada en forma ascendente, False en caso contrario.
    '''
    if len(xs) == 0: #Si la lista está vacía devuelve True
        return True

    else:
        return xs[0] < lista_ordenada_ascendente(xs[1:])


# print(lista_ordenada_ascendente([]))
# print(lista_ordenada_ascendente([2, 2]))
# print(lista_ordenada_ascendente([0, 1, 2, 3, 4, 3]))
# print(lista_ordenada_ascendente([-3, -2]))
# print(lista_ordenada_ascendente([-3, -2]))
# print(lista_ordenada_ascendente([4, 3, 2, 1]))

# EJERCICIO 1B)

def f(b:str) -> int:
    '''
    Requiere: b es un string de 0's y 1's
    '''
    if len(b) == 0:
        return 0

    else:
        aux:int = f(b[:-1])
        return aux * 2 + int(b[:-1])


# EJERCICIO 2

def procesar(xs: List[int]) -> int:
    vr:int = 0                          #O(1)
    i:int = 0                           #O(1)   
    j:int = len(xs) - 1                 #O(1)
    while i < j :                       #O(N)
        if f (xs, i) == f (xs, j) :     #O()
            vr = vr + 1                 #O(1)
        i = i + 1                       #O(1)
        j = j - 1                       #O(1)
    return vr                           #O(1)

# O(1)+O(1)+O(1)+O(N*1*1*(max(1, 1)))
# O(1)+O(N*1*1*1)
# O(1)+O(N)
# O(N)

# EJERCICIO 3

from typing import Set , Tuple , Dict

def incrementar_tupla (t:Tuple [int ,int]) :
    t = (t[0]+1, t[1]+1)

def agregar (t:Tuple[int, int] , d:Dict [int, Set[int]]) :
    k:int = t[0]
    v:int = t[1]
    
    if not k in d :
        d[k] = set()
    d[k].add(v)

tup_1:Tuple [int, int] = (0 ,0)
tup_2:Tuple [int, int] = tup_1

print (tup_1, tup_2)
incrementar_tupla(tup_1)
print(tup_1, tup_2)

dic_1:Dict[int, Set[int]] = dict ()
dic_2:Dict[int, Set[int]] = dic_1
print(dic_1)
print(dic_2)

agregar(tup_1, dic_1)
print(dic_1 )
print(dic_2)

agregar((0, 1), dic_1)
print(len(dic_1))
print(len(dic_1[0]))

# EJERCICIO 4

class Fruta:
    def __init__(self, n :str, p:float, es:Set[str]) :
        ''' Inicializa una fruta con nombre n, precio p, estaciones es. '''
        self.nombre:str = n
        self.precio:float = p
        self.estaciones : Set [str] = es

    def disponible_en(self, estacion:str) -> bool:
        ''' Requiere: estacion es 'primavera', 'verano', 'otoño' o 'invierno'.
            Devuelve: True si estacion está en las estaciones de la fruta.
        '''
        estacion in self.estaciones

def fruta_mas_cara(lis:List[Fruta], est:str) -> Fruta:
        '''Requiere: En lis hay al menos una Fruta disponible en est.
        Devuelve: La Fruta con precio máximo en lis que está disponible en
        la estación est.
        '''
        fruta_cara = lis[0]
        precio_maximo = lis[0].precio
        for fruta in lis:
            if fruta.disponible_en(est) and fruta.precio > precio_maximo:
                fruta_cara = fruta
                precio_maximo = fruta.precio
        return fruta_cara