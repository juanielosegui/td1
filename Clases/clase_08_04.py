from typing import List

def nave_estelar_cercana(sensado:List[int], p:int) -> bool:
    
    #Requiere: p >= 0 and los elementos
    #          de la lista son >= 0.
    #Devuelve: True si hay una distamcia en sensado <= a p.
    #          False caso contrario.

    sensado:List = ['32638', '205', '258', '71115']
    i:int = 0
    resultado:bool = False

    while i < len(sensado):
        
        if sensado[i] <= p:
            resultado = True

        i = i + 1

    return resultado