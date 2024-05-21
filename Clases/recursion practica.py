from typing import List

################
# EJERCICIO 1
################
def factorial(n:int) -> int:
    '''
    Requiere: n natural
    Devuelve: la productoria entre 1 y n
    '''
    if n == 1:  #Caso base
        return 1
    
    else:   #Caso recursivo
        return factorial(n-1) * n

print(factorial(3))
    
def suma_digitos(n:int) -> int:
    '''
    Requiere: n natural
    Devuelve: la suma de los digitos de n
    '''
    s:str = str(n)
    
    if len(s) == 1: #Caso base
        return int(s)
    
    else:   #Caso recursivo
        return int(s[0]) + suma_digitos(int(s[1:]))

print(suma_digitos(5234))

def suma_impares(n:int) -> int:
    '''
    Requiere: n natural
    Devuelve: la sumatoria de los primeros n-naturales impares siendo 1 el primer natural impar
    '''
    
    if n == 1:  #Caso base
      return 1
    
    else:
        return suma_impares(n-1) + 2*n-1
    

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

    if len(l) == 0: #ó if l == []
        return []
    
    else:
        return [l[0] + n] + sumar_n(l[1:], n)
        
print(sumar_n([13, 11, 31], 7))
    

################
# EJERCICIO 2b
################
def codificacion_inversa(xs:List[int]) -> str:
    '''
    Requiere: xs no vacia
    Devuelve: la concatenacion de los strings desde el ultimo en la lista hasta el primero.
    '''
    #completar
