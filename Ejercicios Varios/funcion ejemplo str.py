def suma_mas_diez (x: int) -> int:
    resultado:int = x + 10
    return resultado

x = 15
mensaje:str = str(suma_mas_diez(x))+ " es la suma entre "+str(x)+ " más 10"
print (mensaje)