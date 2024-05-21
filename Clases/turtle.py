import turtle as t #Alias del m√≥dulo turtle

t.shape("turtle")

def triangulo(d:float):
    '''Dibuja un tri√°ngulo equl√°tero de lado d'''
    t.forward(d)
    t.left(120)
    t.forward(d)
    t.left(120)
    t.forward(d)
    t.left(120)
    
def lineas_punteadas(n:int, d:float):
    '''Dibuja n l√≠neas punteadas de longitud d'''
    for i in range(n):
        t.pendown()
        t.forward(d)
        t.penup()
        t.forward(d)
        
#lineas_punteadas(5, 20)

# triangulo(100)
# triangulo(200)
# triangulo(300)

def cuadrado (d:float):
    t.speed(2)
    
    t.forward(d)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(d)

# cuadrado(100)

def montaÒa (d:float):
    t.speed(2)
    
    t.forward(d/3)
    t.left(60)
    t.forward(d/3)
    t.right(60)
    t.right(60)
    t.forward(d/3)
    t.left(60)
    t.forward(d/3)
    
# montaÒa(300)

def escalera(d:float, n:int):
    t.speed(2)
    
    if n == 0:
        pass #√≥ return
    
    else:    
        t.forward(d) 
        t.left(90)
        t.forward(d)
        t.right(90)
        t.forward(d)
        escalera(d, n-1)
        
# escalera(20, 10)


def escalera_v2(d:float, k:int):
    t.speed(2)
    if d <= 0:
        pass #Û return
    
    else:    
        t.forward(d) 
        t.left(90)
        t.forward(d)
        t.right(90)
        escalera_v2(d-k, k)
        
# escalera_v2(100, 25)

def cuadrado_espiral(d:float):
    t.speed(3)
    
    if d <= 0:
        pass
    else:
        t.forward(d)
        t.left(90)
        
        cuadrado_espiral(d-5)
        
cuadrado_espiral(300)
    
t.mainloop() #Se ejecuta y queda abierto
t.bye()      #Cierra bien el programa
    

# =============================================================================
# t.forward(100)
# t.left(90)      #Rotar una cantidad de grados a la derecha. 
# t.forward(150)  #Avanzar la distancia d.
# 
# t.mainloop()
# t.bye()
# =============================================================================