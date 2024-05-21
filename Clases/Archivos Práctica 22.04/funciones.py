from typing import List

################
# EJERCICIO 1
################
def suma_en_posiciones_impares(l:List[int], n:int) -> List[int]:
    '''Suma n a los números que están en posiciones impares de l.
    Requiere: nada
    Devuelve: len(vr)==len(l), y en toda posición j entre 0 y len(l)-1:
          vr[j]==l[j] si j es par, o bien vr[j]==l[j]+n si j es impar.
    '''
    vr: List[int] = []
    i:int = 0
    #A
    while i < len(l):
    #B
        if i%2 == 0:            
           vr.append(l[i]) 
            
        elif i%2 == 1:
            vr.append(l[i] + n)
            
        i = i + 1
      #C  
    
    return vr

l:List = [3, 8, 4, 7, 5]
n:int = 10
print(suma_en_posiciones_impares(l, n))




################
# EJERCICIO 2
################
def suma_en_posiciones_impares_v2(l: List[int], n: int):
    '''Modifica l sumando n a los números que están en posiciones impares
    Requiere: nada
    Devuelve: Sea L el valor de l modificada, len(L)==len(l), y en toda posición
          j entre 0 y len(l)-1:  L[j]==l[j] si j es par, o bien L[j]==l[j]+n si j es impar.
    '''
    i: int = 0
    while i < len(l):
            if i % 2 == 1:
                l[i] = l[i] + n
            
    i = i + 1

l:List = [3, 8, 4, 7, 5]
n:int = 10
print(suma_en_posiciones_impares(l, n))



################
# EJERCICIO 3
################
#def suma_en_posiciones_impares_v3(l: List[int], n: int) -> List[int]:
    '''Suma n a los números que están en posiciones impares de l.
    Requiere: nada
    Devuelve: Sea L el valor de l modificada, len(L)==len(l), y en toda posición
          j entre 0 y len(l)-1:  L[j]==l[j] si j es par, o bien L[j]==l[j]+n si j es impar.
    '''
    vr: List[int] = []
    i: int
    for ...:
        # completar!
    return vr


def suma_en_posiciones_impares_v4(l: List[int], n: int):
    '''Modifica l sumando n a los números que están en posiciones impares
    Requiere: nada
    Devuelve: Sea L el valor de l modificada, len(L)==len(l), y en toda posición
          j entre 0 y len(l)-1:  L[j]==l[j] si j es par, o bien L[j]==l[j]+n si j es impar.
    '''
    i: int
    for ...:
        # completar!
    return vr