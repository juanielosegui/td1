# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 08:25:57 2022

@author: juano
"""

from typing import TextIO
from typing import List

#1)
#A) Funciona

file_handler:TextIO = open('agats.txt')
cancion:str = file_handler.read()
len(cancion)
    
print('agats.txt tiene ' + str(len(cancion)) + ' caracteres')

#B) Me borra el archivo agats.txt
'''
file_handler:TextIO = open('agats.txt', 'w')

i:int = 0

while i < len(cancion):
    file_handler.write(str(i) + "\n")
    i = i + 1

file_handler.close()
'''

#2) No sé cómo llamar a la función es_primo ni usar la n.
'''
son_primos:List[int] = [2, 3, 5, 7, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41]
f:TextIO = open('numeros_primos.txt', 'w')
n:int = 0

for primos in son_primos:
    f.write(str(primos) + '\n')
    
f.close()
'''

#3) Cómo sigo?
'''
f:TextIO = open ('fuente')
d:TextIO = open ('destino')
'''
#4)
#A

def imprimir_astericos (n:str) -> str:
    '''
    Requiere: un número mayor o igual a 0.
    Devuelve: imprime por pantalla una cantidad n de asteriscos.
    '''

    '*' * int(n)
    
#print(imprimir_astericos(input('Ingrese un número: ')))

#B)

def string_inverso (texto:str) -> str:
    '''
    Requiere: un string.
    Devuelve: el mismo string pero invertido.
    '''
    
    return texto[::-1]
    
print(string_inverso(input('Ingrese su string: ')))