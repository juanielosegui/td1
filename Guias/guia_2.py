"""
Ejercicio 1A

def sumar1(x: int) : #PASO 3
	x = x + 1 #LA FUNCION HACE 10+1 Pero no se guarda en x porque no hace ningun return (El calculo queda en la nada)

x : int = 10 # PASO 1 Comienza el programa x vale 10

sumar1(x) #PASO 2 LLamamos a la funcion sumar1 con el valor 10 (Esto basicamente no hace nada porque no lo almacenamos en ningun lado, se ejecuta y se borra completamente, es como ignorarlo)
print (x) # PASO 4 Imprimimos x que todavia no se cambio por ningun valor (Recordemos que lo anterior fue ignorado al no tener return)
sumar1(x * x) #PASO 5 Nuevamente se llama a la funcion que queda en la nada (No se almacena en ningun lado y no se lo retorna)
print (x) #PASO 6 Volvemos a imprimir x que en ningun momento fue reemplazado.

'''

'''
Ejercicio 1B

def f(x: int) -> int: #Paso 3: recibe la variable 10.
    x = x + 1         #Paso 4: se reemplaza la x por la suma de 10+1.
    return x          #Paso 5: devuelve resultado 11.


x: int = 10           #Paso 1: x vale 10
x = f(x)              #Paso 2: se llama a la función f con la variable 10.
print(x)              #Paso 6: se imprime el nuevo valor de x (11).
print(x * x)          #Paso 7: se multiplica 11*11 que es 121.



'''

Ejercicio 1C

def f(x: int) -> int:       # Paso 5: la función f recibe al 10 entonces la x=10.
    x = x + 1               # Paso 6: se reemplaza la x por la suma de 10+1.
    return x                # Paso 7: devuelve resultado 11.


def g(y: int) -> int:       # Paso 3: la función g recibe el 10 entonces y vale 10.
    x: int = f(y)           # Paso 4: se llama a la función f(10) porque y=10.
    return f(x)             # Paso 8: reemplazo 11 en el paso 6 -> x=11+1 | Después devuelve resultado 12.


x: int = 10                 # Paso 1: x=10.
x = g(x)                    # Paso 2: se llama a la función g(10) y al final termina dando x=12.
print(x)                    # Paso 9: imprime 12.
x = g(x * x)                # Paso 10: se repite el paso 2 hasta el 8. x=146 sería el resultado de todos esos pasos.
print(x)                    # Paso 11: se imprime x=146.

'''

'''

def f2c (f: float) -> float:
    
    #Requiere: valor f de tipo float.
    #Devuelve: la conversión de grados fahrenheit a grafos celsius.
    
    celsius:float = (f - 32) * 5/9
    return celsius

print (f2c (80.0))
print (f2c (100.0))
print (f2c (200.0))
print (f2c (250.0))
print (f2c (150.0))

'''

'''
Ejercicio 3A

import math
def raiz (n: int) -> int:
    #Requiere: valor n que sea entero. Siempre que n sea mayor o igual a 0.
    #Devuelve: raíz de n.
    #Ejemplos. Si n=4, entonces la raíz de n (raíz de 4) iguala a 2.

    resultado:int = math.sqrt(n)
    return resultado

n:int = 121
print(raiz(n))

'''

'''

Ejercicio 3B

import math
def factorial (n: int) -> int:
    #Requiere: valor n que sea entero. Siempre que n ≥ 0.
    #Devuelve: factorial de n.
    #Ejemplos. Si n=5, entonces se hará 5 * 4 * 3 * 2 * 1.

    resultado:int = math.factorial(n)
    return resultado

n:int = 4
print(factorial(n))

'''

'''

Ejercicio 3C

import math


def combinatorio(n: int, k: int) -> int:
    # Requiere: valores de 'n' y 'k' enteros ≥ 0. k ≤ n.
    # Devuelve: resultado del combinatorio de n! sobre k!(n-k)!.

    resultado: int = math.factorial(n) / math.factorial(k) * math.factorial(n - k)
    return resultado


n: int = 3
k: int = 2

print(combinatorio(n, k))

'''

'''

EJERCICIO 3D

def carti(n:int, i: int) -> str:
    # Requiere: un valor de n ≥ 0
    # Devuelve: un string con valores de 'n' e 'i'
    # para todo 0 ≤ i ≤ n separados por comas.
    # Ejemplo: para n = 4, debe devolver "1,4,6,4,1"

'''

'''

EJERCICIO 3E

def asteriscos (n: int) -> str:
    # Requiere: un valor de n ≥ 0
    # Devuelve: línea de n cantidad de asteriscos
    # Ejemplo: si n = 3 -> ***
    
'''

'''

EJERCICIO 3F

def cuadrado_de_asteriscos (n: int) -> str:
    # Requiere: un valor de n ≥ 0.
    # Devuelve: cuadrado de asteriscos de lado n.
    # Ejemplo: si n = 3, entonces un lado del cuadrado va a tener 3 asteriscos de longitud.

'''

'''

EJERCICIO 3G

def inverso (s: str) -> str:
    # Requiere: un valor string.
    # Devuelve: los caracteres invertidos de ese valor string.
    # Ejemplo: si s = 'hola' -> 'aloh'

"""
# EJERCICIO 3H

def cantidad_a (s:str, a: str) -> int:
    """
    Requiere: un valor string s y un string a.
    Devuelve: la cantidad de veces que s está dentro de a
    """
    res:int = 0
    for letra in a:
        if letra == s:
            res = res + 1
        else:
            pass
        
        return res
s='a'
a='calabaza'
print(cantidad_a(s, a))