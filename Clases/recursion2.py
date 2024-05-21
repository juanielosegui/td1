# =============================================================================
# Clase 24.06.22 -> Usar pythontutor.com para visualizar los códigos
# =============================================================================

from typing import List

#a)
def pot_3 (n:int):
    '''
    Requiere: un n >= 0.
    Devuelve: la potencia de 3 a la n.
    '''
    
    
    if n == 0:
        return 1
    
    else:
        return 3 * pot_3(n-1)
    
print(pot_3(3))

#b)
def resto(n:int):
    '''
    Requiere: un n >= 0.
    Devuelve: el resto obtenido en la división de n por 5.
    '''
    
    if n < 5:
        return n
    
    else:
        return 
    
def es_capicua(xs:List[int]) -> bool:
    '''
    Requiere: nada
    Devuelve: un bool, que si es True es capicúa la lista y False de caso
    contrario
    '''
    if len(xs) == 0:
        return True
    
    else:
        return xs[0] == xs[-1] and es_capicua(xs[1:-1])
    
print(es_capicua([9, 8, 7, 8, 9]))
print(es_capicua([9]))