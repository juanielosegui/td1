from typing import List
def filtrar_solo_CAFE (texto: str) -> str:
    ''' Requiere: nada.
    Devuelve: dado un string s, devuelve un 
    nuevo string formado por las letras C, A, F, o E 
    que aparezcan en s, en el mismo orden de 
    ocurrencia.
    '''
    #creamos una variable de bucle llamada i y una variable llamada res en la cual se almacena el nuevo string que devolverá la función.
    res:str = ''
    i:int = 0
    
    while i < len(texto):
        #en cada repetición del ciclo analizamos la posición i en el string comparándola con las letras y concatenando la letra a res en el caso de que coincida con alguna y además incrementamos en 1 a i.      
        if texto[i] == 'C' or texto[i] == 'A' or texto[i] == 'F' or texto[i] == 'E':
           res = res + texto[i]
        
        i = i + 1
 
    return res

# flitarCAFE_BD es una funcion auxiliar para es_cafetero. Funciona igual que filtrar_solo_CAFE pero filtrando también B y D.
def filtrarCAFE_BD (texto:str) -> str:
    ''' Requiere: nada.
        Devuelve: dado un string s, devuelve un 
        nuevo string formado por las letras C, A, F, E, B, o D
        que aparezcan en s, en el mismo orden de 
        ocurrencia.
    '''
    res:str = ''
    i:int=0
    while i < len(texto):
        if texto[i] == 'C' or texto[i] == 'A' or texto[i] == 'F' or texto[i] == 'E' or texto[i] =='B'  or texto[i] == 'D':
            res = res + texto[i]
        
        i = i + 1

    return res

def es_cafetero (num: int)->bool:
    '''Requiere:  n >= 0
    Devuelve: True si n es cafetero (es decir, si y solo si su 
    representacion hexadecimal contiene exactamente una 
    ocurrencia de los símbolos C, A, F y E, en ese orden y sin repeticiones, 
    y no contiene ocurrencias de los símbolos B y D), 
    y si no lo es, False.
    ''' 
    #convertimos el número entero ingresado a un número hexadecimal y convertimos sus caracteras a mayúscula para luego convertirlo en string y poder ingresarlo como argumento en la función filtrarCAFE_BD para que nos devuelva un nuevo string que almacenaremos en la variable num.
    num:str = filtrarCAFE_BD(str(hex(num).upper()))
    #comparamos si el nuevo string num es igual a 'CAFE' para determinar si es un número cafetero. 
    return num == 'CAFE'

 
def n_esimo_cafetero (n:int) -> (int):
    '''
    Requiere: n >= 1
    Devuelve: el n-ésimo número que cumple con los requisitos para ser cafetero, considerando al 51966
    como el primer número cafetero.
    ''' 
    #creamos una variable llamada num que empieza por 51966 que es el primer número cafetero y creamos una variable de bucle llamada contador_cafetero, que empieza en 1, ya que el primer numero cafetero ya lo tenemos. Y esta irá incrementando en 1 cada vez que encuentre el siguiente número cafetero hasta llegar al n-ésimo número cafetero pedido.
    num: int = 51966
    contador_cafetero:int=1
    
    while (contador_cafetero < n): 
        #incrementamos en 1 a num y utilizamos la función es_cafetero para determinar si num lo es, en el caso de que lo sea incrementamos en 1 al contador y si no lo es no modificamos el contador.
        num = num + 1
        if es_cafetero(num):
            contador_cafetero = contador_cafetero + 1
           
    return num
 
def cafeteros_entre (n:int, m:int) -> (int):
    ''' 
    Requiere: n >= 1, m >= n
    Devuelve: la lista de números cafeteros entre n y m, 
    inclusive en ambos casos (es decir, mayores o iguales a n,
    y menores o iguales a m), ordenada de menor a mayor.
    ''' 
    #creamos una variable de bucle llamada num. Esta va a valer el numero que se le ingrese al parámetro n y creamos una lista llamada cafeteros que empieza vacía y en el caso de que haya numeros cafeteros entre n y m se almacenaran en esa lista.
    num: int = n
    cafeteros: List[int] = []
    
    while num <= m:
        #en cada repetición del ciclo aplicamos la función es_cafetero para verificar si num lo es, en el caso de que lo sea lo añadimos a la lista e incrementamos en 1 a num. Y si num no es cafetero no modificamos la lista e incrementamos en 1 a num.
        if es_cafetero(num):
            cafeteros.append(num)
        num = num + 1
    return cafeteros