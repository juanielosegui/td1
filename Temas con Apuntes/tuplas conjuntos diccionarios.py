from typing import Tuple, Set, Dict

#Tuplas, conjuntos y diccionarios. Son tipos de datos.

#TUPLA: almacenar muchos valores en una sola variable. Los valores van entre
#paréntesis, los elementos pueden ser de distintos tipos, y son inmutables.
#Permite hacer asignaciones simultáneas. Se puede pensar como un par ordenado
#o una terna ordenada.

punto:Tuple[float, float, float] = (1.7, -0.9, 0.4)
fecha:Tuple[int, str, int] = (25, 'mayo', 1810)
persona:Tuple[str, str, int] = ('Juani', 'Elosegui', 17)

#Operaciones:
    #Crear: (x, y, z)
    #len(t) devuelve la cantidad de elementos
    #t[i] devuelve el valor del i-ésimo componente
    #t == u: comparación componente a componente


#CONJUNTOS: formato Set[T]. Los elementos van entre llaves y separados por comas,
#siendo todos del mismo tipo. No hay elementos repetidos y no tienen orden. Son
#mutables

felinos:Set[str] = {'león', 'gato', 'tigre', 'guepardo'}

caninos:Set[str] = set()
caninos.add('perro')
caninos.add('lobo')
caninos.add('perro') #No se agrega un elemento ya presente en el conjunto.

#Si salta set() es un conjunto vacío.
#mi_conjunto:Set[str] = set()

#Operaciones:
    #set(): crea y devuelve un conjunto vacío.
    #{x, y, z}: crea y devuelve un conjunto con 3 elementos.
    #len(c): devuelve la cantidad de elementos de c.
    #x in c: evalúa la pertenencia.
    #c.add(x): agrega la x al conjunto c.
    #c.remove(x): quita la x del conjunto c.
    #c == d: evalúa si los conjuntos son iguales
    #c | d: nuevo conjunto con c y d unidos.
    #c & d: nuevo conjunto con la intersección de c y d.
    #c - d: nuevo conjunto con la diferencia entre c y d.
    #list(c): transforma a una lista con los elementos del conjunto c.
    #set(ls): conjunto nuevo con los elementos de la lista ls.

def caracteres (s:str) -> Set[str]:
    for caracteres in s:
        apariciones.add(caracteres)
        
    return apariciones
apariciones:Set[str] = set()
print(caracteres('bananas'))

def caracteres_en_comun(s:str, t:str) -> Set[str]:
    conjunto_s:Set[str] = set()
    conjunto_t:Set[str] = set()
    
    for caracteres_s in s:
        conjunto_s.add(caracteres_s)
        
    for caracteres_t in t:
        conjunto_t.add(caracteres_t)
        
    comunes:Set[str] = conjunto_t & conjunto_s
    
    return comunes

s:str = 'casablanca'
t:str = 'cablevision'
    
print(caracteres_en_comun(s, t))


#DICCIONARIOS: asocia valores a claves. Usando las variables d de tipo Dict[T1, T2]
#y las k de tipo T1 y tipo T2. Son mutables.

#Operaciones:
    #dict(): devuelve un diccionario nuevo y vacío.
    #{}: devuelve un diccionario nuevo y vacío.
    #len(d): devuelve la cantidad de claves del diccionario d.
    #k in d: evalúa si k está en d. Tipo bool.
    #d[k] = v: asocia el valor v a la clave k en el diccionario d.
    #d[k]: devuelve el valor asociado a la clave k en el diccionario d. Sólo k in d = True.
    #d.pop(k): borra la clave k y su valor asociado.
    #list(d): devuelve una lista con las claves del diccionario d.
    
peso_atomico:Dict[str, float] = dict()
peso_atomico['H'] = 1.00797
peso_atomico['He'] = 4.0026

def recitar(n:int) -> str:
    recitacion:Dict[int, str] = dict()
    recitacion[1] = 'uno'
    recitacion[2] = 'dos'
    recitacion[3] = 'tres'
    recitacion[4] = 'cuatro'
    recitacion[5] = 'cinco'
    recitacion[6] = 'seis'
    recitacion[7] = 'siete'
    recitacion[8] = 'ocho'
    recitacion[9] = 'nueve'
    recitacion[0] = 'cero'
    
    