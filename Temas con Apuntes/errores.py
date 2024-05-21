'''

                                  !!  MAL HECHO !!

def ultimo_caracter (s: str) --> str:           #Arreglo flechita a un solo guion.
    """Requiere: len (s)>0
       Devuelve: el último caracter de s.
    """
    vr: int = s[len(s))]                        #Sobra un guion. Necesitamos un str en vez de un entero.
    return vr

texto: str = "hola mundo"
ult: str= ultimo_caracter(texto)

print(ult)
'''

'''
                                  !! BIEN HECHO !!

def ultimo_caracter (s: str) -> str:
    vr: str = s [len(s) - 1]
    return vr

texto: str = "hola mundo"
ult: str= ultimo_caracter(texto)

print(ult)

'''
