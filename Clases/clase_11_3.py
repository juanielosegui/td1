'''
Ejercicio 1A

def f (x:str) -> str:
    return ('T'+ x) * 3

r:str = f ('ini')
print (r)
'''

'''
Ejercicio 1B

def g (a:int , b:int) -> float :
    return a/b

a:int = 666
c:int = 222
r: float = g (a , c)                  #(a, c) reemplaza al argumento (a, b) en L14.
print (r)
'''

'''
Ejercicio 1C

def h (x:int , y:int) -> int :
     x = 10
     return x + y

b:int = 8
r:int = h (b , b)
print (r)
r = h(x , b)                        
print (r)
'''

'''
Ejercicio 2A

def f (x:int , y:int) -> float :
    return 1/x + 1/y                #Se suman las divisiones de 1 por x e y siempre y
                                     cuando x e y son distintos de cero.
'''

'''

Ejercicio 2B

 def g (x:int, y:int) -> float :
     a:int = x*y
     b:int = a*a
     return y/a + a*x/b             #La sumatoria entre 'y' y 'a' (siendo 'a' el producto entre
                                    #'x' e 'y') más el producto de 'a' y 'x' dividido por 'b'
                                    #(siendo 'b' el doble producto de 'a').
'''

def distancia (a:int, b:int, c:int, d:int) -> float:
    
    
