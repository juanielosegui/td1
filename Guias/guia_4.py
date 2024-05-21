'''
EJERCICIO 1A

def f2c(fahr: float) -> float:
    cel: float = (fahr - 32) * 5 // 9
    return cel

def tablaf2c() -> str:
    i:int = 0
    res: str = ''

    while i <= 120:
        res = res + str(i) + " F = " +str(f2c(i)) +" C\n" 
        i = i + 10
    return res

print(tablaf2c())


B)
La variable i oscila entre 0 y 120 inclusive.
La variable res es el resultado en tabla de la conversión f2c.


C)
El ciclo termina porque a la variable i se le agrega 10 hasta que llega
a 120, porque 0 <= i <= 120.
'''

'''
EJERCICIO 2

def es_palindromo (palabra: str) -> bool:
    #Requiere: un string de n caracteres.
    #Devuelve: true, si es palíndromo; false si no lo es.
    #Ejemplo: "Neuquén" es palíndromo, pero "Renault" no.

    i:int = 0

    while i < len(palabra):
        if not (palabra[i]==palabra[len(palabra)-1-i]):
            return False
        else:
            return True
    i = i + 1
print(es_palindromo(input('Poné una palabra capo:')))
'''

'''
EJERCICIO 3

def es_primo (numero:int) -> bool:
    #Requiere: un número int.
    #Devuelve: un bool; True si es primo, False si no lo es.
    #Ejemplo: 7 es primo porque se divide por sí mismo y por 1.

    i:int = 1
    divisores:int = 0
    
    while i <= numero and divisores < 3:
        if numero % i == 0:
            divisores = divisores + 1
        i = i + 1
    return divisores == 2
    
print(es_primo())
'''


