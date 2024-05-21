from typing import List

################
# EJERCICIO 1
################
def factorial(n:int) -> int:
    '''
    Requiere: n natural
    Devuelve: la productoria entre 1 y n
    '''
    if n == 1:
        return 1
    
    else:
        return factorial(n-1) * n

print(factorial(3))
    
def suma_digitos(n:int) -> int:
    '''
    Requiere: n natural
    Devuelve: la suma de los digitos de n
    '''
    res:int = 0
    
    if len(str(n)) == 0:
        return 0
    
    else:
        return suma_digitos()

def suma_impares(n: int) -> int:
    '''
    Requiere: n natural
    Devuelve: la sumatoria de los primeros n-naturales impares siendo 1 el primer natural impar
    '''
        #completar
    

################
# EJERCICIO 2a
################

### OPCIÓN 1
def sumar_n(l:List[int], n:int) -> List[int]:
    '''
    Requiere: nada
    Devuelve: Sea L el valor de l modificada, len(L)==len(l), y en toda posición
          j entre 0 y len(l)-1:  L[j]==l[j] + n 
    '''
    #completar
    

################
# EJERCICIO 2b
################
def codificacion_inversa(xs:List[int]) -> str:
    '''
    Requiere: xs no vacia
    Devuelve: la concatenacion de los strings desde el ultimo en la lista hasta el primero.
    '''
    #completar
