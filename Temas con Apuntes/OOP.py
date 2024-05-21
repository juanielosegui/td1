from typing import Set

VER:str = 'verano'
OTO:str = 'otoño'
PRI:str = 'primavera'
INV:str = 'invierno'

class Fruta:
    def __init__(self, n:str, p:float, es:Set[str]):
    #Inicializa una fruta con nombre n, precio p y estaciones es.
        self.nombre:str = n
        self.precio:float = p
        self.estaciones:Set[str] = es
        #Self se refiere al objeto en cuestión
    
    def mostrar_como_string(self) -> str:
        #Devuelve una representación de tipo str de la fruta
        return self.nombre + ' ($' +str(self.precio) + '/kg)'

    def __repr__(self) -> str:
        #Devuelve una representación de tipo str de f.
        return self.nombre + ' ($' +str(self.precio) + '/kg)'
    
    def disponible_en(self, est:str) -> bool:
        #True si esta fruta está en es.
        return (est in self.estaciones)
    
    def __lt__ (self, other) -> bool:
        #Comparación entre frutas.
        return (self.precio < other.precio)
    
b:Fruta = Fruta('Banana de Ecuador', 150.0, {PRI, OTO, INV})
u:Fruta = Fruta('Uva verde', 60.0, {VER})
p:Fruta = Fruta('Pera Williams', 70.0, {VER})

#lista_de_frutas:List[Fruta] = [b, u, p]
print(u.mostrar_como_string())
print(u) #Repr: transforma un objeto como string

if b.disponible_en(VER):
    print('Si')
else:
    print('No')
    
"""
b:Tuple[str, float, Set[str]] = ('Banana de Ecuador', 150.0, {PRI, OTO, INV})

u:Tuple[str, float, Set[str]] = ('Uva verde', 60.0, {VER})
p:Tuple[str, float, Set[str]] = ('Pera Williams', 70.0, {VER})

lista_de_frutas:List[Tuple[str, float, Set[str]]] = [b, u, p]
print(lista_de_frutas)
"""