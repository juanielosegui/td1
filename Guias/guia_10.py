from typing import List
import turtle as t

# =============================================================================
# EJERCICIO 1
# =============================================================================

#a)
def pot2n(n:int) -> int:
    if n == 0:
        return 1
    
    else:
        return pot2n(n-1)*2
    
#print(pot2n(3))

#b)
def pot_a(a:int, n:int) -> int:
    if n == 0:
        return 1
    else:
        return pot_a(a, n-1)*a

#print(pot_a(3, 3))

#c)
def producto(n, m) -> int:
    if n == 0:
        return 0
    
    else:
        return producto(n-1, m) + m

# print(producto(3, 5))    

# ===========================================================================
# EJERCICIO 2
# ===========================================================================

#a)
def productoria(xs:List[int]) -> List:
    if len(xs) == 1:
        return xs[0]
    
    else:
        return xs[0] * productoria(xs[1:])

# print(productoria([2, 4, 6, 12]))

#b)
def cant_ocurrencias(xs:List[int], x:int) -> int:
    res:int = 0
    if len(xs) == 0:
        return 0

    elif xs[0] == x:
            res = res + 1
    return res+cant_ocurrencias(xs[1:], x)
        
xs = [1, 3, 5, 1, 6, 1, 7, 1]
x = 1

# print(cant_ocurrencias(xs, x))

#c)
def max_pos(xs:List[int]) -> int:
    if len(xs)==1:
        return 0
    else:
        res: int= max_pos(xs[1:])
        if xs[res+1]>xs[res]:
            res=res+1
        return res
    
# print(max_pos([1,9,7,2]))

#e)
def sumar_pos_pares(xs:List[int]) -> int:
    if len(xs) == 0:
        return 0

    else:
        xs[1] + sumar_pos_pares(xs[2:])

xs:List = [1, 2, 3, 4, 5, 6, 7]

print(sumar_pos_pares(xs))

# =============================================================================
# EJERCICIO 4
# =============================================================================

# t.shape("turtle")

# #a)
# def poligono(d:float, n:int):
#     t.speed(2)
#     if n == 1:
#         pass
    
#     else:
#         t.forward(d)
#         t.left(360/n)
#         poligono(d, n-1)
        
# poligono(100, 5)

# t.mainloop() #Se ejecuta y queda abierto
# t.bye()      #Cierra bien el programa